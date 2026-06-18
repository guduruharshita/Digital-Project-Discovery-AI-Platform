from fastapi import APIRouter

from app.models.schemas import ArtifactType, GenerateRequest, GenerateResponse
from app.services.ai_service import generate_artifacts

router = APIRouter(prefix="/api", tags=["generate"])


@router.get("/artifact-types")
def list_artifact_types():
    return {"types": [t.value for t in ArtifactType]}


@router.post("/generate", response_model=GenerateResponse)
async def generate(request: GenerateRequest) -> GenerateResponse:
    return await generate_artifacts(request.description, request.artifact_type)
