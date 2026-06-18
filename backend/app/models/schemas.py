from enum import Enum

from pydantic import BaseModel, Field


class ArtifactType(str, Enum):
    SRS = "srs"
    USER_STORIES = "user_stories"
    BOILERPLATE = "boilerplate"


class GenerateRequest(BaseModel):
    description: str = Field(..., min_length=10, max_length=2000)
    artifact_type: ArtifactType = ArtifactType.SRS


class Requirement(BaseModel):
    id: int
    type: str
    description: str


class GenerateResponse(BaseModel):
    title: str
    summary: str
    requirements: list[Requirement]
    artifact_type: ArtifactType
