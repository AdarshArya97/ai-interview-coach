import math

import httpx

from app.core.config import settings
from app.integrations.llm.base import LLMError, RateLimitError

BASE = "https://generativelanguage.googleapis.com/v1beta/models"


def _normalize(v: list[float]) -> list[float]:
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


async def embed_texts(
    texts: list[str], task_type: str = "RETRIEVAL_DOCUMENT"
) -> list[list[float]]:
    """Embed texts. Use RETRIEVAL_DOCUMENT for chunks, RETRIEVAL_QUERY for questions."""
    if not settings.gemini_api_key:
        raise LLMError("GEMINI_API_KEY is not set")

    model = settings.embedding_model
    url = f"{BASE}/{model}:batchEmbedContents"
    headers = {"x-goog-api-key": settings.gemini_api_key}
    out: list[list[float]] = []

    async with httpx.AsyncClient(timeout=settings.llm_timeout_seconds) as client:
        for i in range(0, len(texts), 50):
            batch = texts[i : i + 50]
            body = {
                "requests": [
                    {
                        "model": f"models/{model}",
                        "content": {"parts": [{"text": t}]},
                        "taskType": task_type,
                        "outputDimensionality": settings.embedding_dimensions,
                    }
                    for t in batch
                ]
            }
            try:
                r = await client.post(url, json=body, headers=headers)
            except httpx.HTTPError as e:
                raise LLMError(f"Network problem during embedding: {e}") from e

            if r.status_code == 429:
                raise RateLimitError("Embedding rate limit or quota reached")
            if r.status_code != 200:
                raise LLMError(f"Embedding returned {r.status_code}: {r.text[:300]}")
            try:
                out.extend(_normalize(e["values"]) for e in r.json()["embeddings"])
            except (KeyError, ValueError) as e:
                raise LLMError("Unexpected embedding response shape") from e
    return out