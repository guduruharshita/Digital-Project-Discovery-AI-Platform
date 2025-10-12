from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
import openai

load_dotenv()

app = FastAPI(title="DiscoveryAI API", version="1.0.0")

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
    artifact_type: str = "srs"  # srs | user_stories | boilerplate

class Requirement(BaseModel):
    id: int
    type: str
    description: str

class GenerationOutput(BaseModel):
    title: str
    requirements: List[Requirement]
    summary: str

PROMPTS = {
    "srs": """You are a software requirements analyst. Given this product description, generate a structured SRS with numbered functional and non-functional requirements. Format each as: [FR/NFR-N] Description. Return JSON with keys: title, summary, requirements (list of {id, type, description}).""",
    "user_stories": """You are an agile product manager. Given this product description, generate user stories in the format 'As a [persona], I want [action] so that [benefit]'. Return JSON with keys: title, summary, requirements (list of {id, type, description}).""",
    "boilerplate": """You are a senior software engineer. Given this product description, identify the key modules and generate boilerplate code structure descriptions. Return JSON with keys: title, summary, requirements (list of {id, type, description}).""",
}

@app.get("/")
def health_check():
    return {"status": "ok", "service": "DiscoveryAI API"}

@app.post("/generate", response_model=GenerationOutput)
async def generate_artifacts(input_data: ProjectInput):
    if not input_data.description.strip():
        raise HTTPException(status_code=400, detail="Description cannot be empty")

    system_prompt = PROMPTS.get(input_data.artifact_type, PROMPTS["srs"])

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": input_data.description},
            ],
            response_format={"type": "json_object"},
            temperature=0.3,
        )
        result = response.choices[0].message.content
        import json
        parsed = json.loads(result)
        return GenerationOutput(**parsed)
    except openai.OpenAIError as e:
        raise HTTPException(status_code=502, detail=f"OpenAI error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/artifact-types")
def list_artifact_types():
    return {"types": list(PROMPTS.keys())}
