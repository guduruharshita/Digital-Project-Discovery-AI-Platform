from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import os, json
import openai
from dotenv import load_dotenv

load_dotenv()
router = APIRouter(prefix="/api", tags=["generation"])
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
    "srs": "Extract functional (FR) and non-functional (NFR) requirements. Return JSON: {title, summary, requirements:[{id,type,description}]}",
    "user_stories": "Generate user stories. Return JSON: {title, summary, requirements:[{id,type,description}]}",
    "boilerplate": "Generate module scaffolding. Return JSON: {title, summary, requirements:[{id,type,description}]}",
}

@router.post("/generate", response_model=GenerationOutput)
async def generate(input_data: ProjectInput):
    if not input_data.description.strip():
        raise HTTPException(status_code=400, detail="Description cannot be empty")
    prompt = PROMPTS.get(input_data.artifact_type, PROMPTS["srs"])
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": prompt},
                      {"role": "user", "content": input_data.description}],
            response_format={"type": "json_object"},
            temperature=0.3,
        )
        return GenerationOutput(**json.loads(response.choices[0].message.content))
    except openai.OpenAIError as e:
        raise HTTPException(status_code=502, detail=str(e))
