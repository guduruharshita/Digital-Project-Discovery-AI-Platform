from fastapi import APIRouter

from app.config import get_settings

router = APIRouter(tags=["health"])


@router.get("/health")
def health():
    settings = get_settings()
    return {"status": "ok", "environment": settings.environment, "version": "2.0.0"}
