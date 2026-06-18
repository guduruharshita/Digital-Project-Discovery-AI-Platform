from typing import Optional
import uuid
from datetime import datetime, timezone

from sqlmodel import Field, Session, SQLModel, create_engine, select

from app.config import get_settings

_engine = None


def _init_engine():
    global _engine
    if _engine is not None:
        return _engine
    settings = get_settings()
    if not settings.database_url:
        return None
    _engine = create_engine(settings.database_url, echo=False, pool_pre_ping=True)
    SQLModel.metadata.create_all(_engine)
    return _engine


class GenerationRecord(SQLModel, table=True):
    __tablename__ = "generation_history"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    description: str = Field(max_length=2000)
    artifact_type: str = Field(max_length=30)
    title: Optional[str] = None
    summary: Optional[str] = None
    requirements_count: int = 0
    duration_ms: Optional[int] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


def save_record(record: GenerationRecord) -> None:
    engine = _init_engine()
    if engine is None:
        return
    with Session(engine) as session:
        session.add(record)
        session.commit()


def get_recent(limit: int = 20) -> list[GenerationRecord]:
    engine = _init_engine()
    if engine is None:
        return []
    with Session(engine) as session:
        return list(
            session.exec(
                select(GenerationRecord)
                .order_by(GenerationRecord.created_at.desc())
                .limit(limit)
            ).all()
        )
