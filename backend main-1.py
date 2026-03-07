from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequirementInput(BaseModel):
    text: str

class RequirementOutput(BaseModel):
    requirements: List[str]

@app.post("/generate-requirements", response_model=RequirementOutput)
async def generate_requirements(input_data: RequirementInput):
    return RequirementOutput(requirements=[
        "The system shall allow users to sign up.",
        "The system shall allow users to log in.",
        "The system shall generate requirements using AI.",
        "The system shall export SRS and design documents."
    ])
@app.get("/")
def home():
    return {"message": "Backend running. Go to /docs"}
