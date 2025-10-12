from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="DiscoveryAI API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ProjectInput(BaseModel):
    description: str

@app.get("/")
def health_check():
    return {"status": "ok", "service": "DiscoveryAI API"}

@app.post("/generate")
async def generate(input_data: ProjectInput):
    return {"title": "Draft", "requirements": [], "summary": ""}
