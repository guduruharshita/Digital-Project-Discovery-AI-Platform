from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import os, json
from dotenv import load_dotenv
import openai

load_dotenv()
app = FastAPI(title="DiscoveryAI API", version="0.2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ProjectInput(BaseModel):
    description: str
    artifact_type: str = "srs"

class Requirement(BaseModel):
    id: int
    type: str
    description: str

class GenerationOutput(BaseModel):
    title: str
    requirements: List[Requirement]
    summary: str

PROMPTS = {
    "srs": "You are a software requirements analyst. Extract functional (FR) and non-functional (NFR) requirements from the product description. Return JSON: {title, summary, requirements:[{id,type,description}]}",
    "user_stories": "You are an agile product manager. Generate user stories as JSON: {title, summary, requirements:[{id,type,description}]} where description follows: As a [persona], I want [action] so that [benefit].",
    "boilerplate": "You are a senior engineer. Identify key modules and return scaffolding descriptions as JSON: {title, summary, requirements:[{id,type,description}]}",
}

@app.get("/")
def health_check():
    return {"status": "ok", "service": "DiscoveryAI API"}

@app.get("/artifact-types")
def artifact_types():
    return {"types": list(PROMPTS.keys())}

@app.post("/generate", response_model=GenerationOutput)
async def generate(input_data: ProjectInput):
    if not input_data.description.strip():
        raise HTTPException(status_code=400, detail="Description cannot be empty")
    prompt = PROMPTS.get(input_data.artifact_type, PROMPTS["srs"])
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": input_data.description},
            ],
            response_format={"type": "json_object"},
            temperature=0.3,
        )
        parsed = json.loads(response.choices[0].message.content)
        return GenerationOutput(**parsed)
    except openai.OpenAIError as e:
        raise HTTPException(status_code=502, detail=f"OpenAI error: {str(e)}")
