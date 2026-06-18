import json
import time

import openai
from fastapi import HTTPException

from app.config import get_settings
from app.models.schemas import ArtifactType, GenerateResponse

_SYSTEM_PROMPTS: dict[ArtifactType, str] = {
    ArtifactType.SRS: (
        "You are a software requirements analyst. Given the product description, "
        "generate a structured SRS with numbered functional (FR) and non-functional (NFR) requirements. "
        'Return strictly valid JSON: {"title": str, "summary": str, '
        '"requirements": [{"id": int, "type": str, "description": str}]}'
    ),
    ArtifactType.USER_STORIES: (
        "You are an agile product manager. Generate user stories as: "
        "'As a [persona], I want [action] so that [benefit]'. "
        'Return strictly valid JSON: {"title": str, "summary": str, '
        '"requirements": [{"id": int, "type": "Story", "description": str}]}'
    ),
    ArtifactType.BOILERPLATE: (
        "You are a senior software engineer. Identify key modules and generate "
        "boilerplate descriptions for each. "
        'Return strictly valid JSON: {"title": str, "summary": str, '
        '"requirements": [{"id": int, "type": "Module", "description": str}]}'
    ),
}


async def generate_artifacts(description: str, artifact_type: ArtifactType) -> GenerateResponse:
    settings = get_settings()
    client = openai.AsyncOpenAI(api_key=settings.openai_api_key)
    t0 = time.monotonic()

    try:
        response = await client.chat.completions.create(
            model=settings.openai_model,
            messages=[
                {"role": "system", "content": _SYSTEM_PROMPTS[artifact_type]},
                {"role": "user", "content": description},
            ],
            response_format={"type": "json_object"},
            temperature=0.3,
        )
        raw = response.choices[0].message.content
        parsed = json.loads(raw)
        result = GenerateResponse(**parsed, artifact_type=artifact_type)
    except openai.AuthenticationError:
        raise HTTPException(status_code=401, detail="Invalid OpenAI API key.")
    except openai.RateLimitError:
        raise HTTPException(status_code=429, detail="OpenAI rate limit reached. Try again later.")
    except openai.OpenAIError as exc:
        raise HTTPException(status_code=502, detail=f"AI service error: {exc}")
    except (json.JSONDecodeError, ValueError) as exc:
        raise HTTPException(status_code=500, detail=f"Failed to parse AI response: {exc}")

    from app.database import GenerationRecord, save_record
    save_record(GenerationRecord(
        description=description,
        artifact_type=artifact_type.value,
        title=result.title,
        summary=result.summary,
        requirements_count=len(result.requirements),
        duration_ms=int((time.monotonic() - t0) * 1000),
    ))

    return result
