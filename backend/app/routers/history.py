from fastapi import APIRouter, Query

from app.database import GenerationRecord, get_recent

router = APIRouter(prefix="/api", tags=["history"])


@router.get("/history", response_model=list[GenerationRecord])
def get_history(limit: int = Query(default=20, ge=1, le=100)):
    return get_recent(limit=limit)
