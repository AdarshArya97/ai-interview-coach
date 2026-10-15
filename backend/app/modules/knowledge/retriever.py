
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.chunk import Chunk
from app.modules.knowledge.embeddings import embed_texts


async def _embed_query(query: str) -> list[float]:
    embeddings = await embed_texts(
        [query],
        task_type="RETRIEVAL_QUERY",
    )
    return embeddings[0]


def retrieve_chunks(
    db: Session,
    query: str,
    top_k: int = 5,
    topic: str | None = None,
    role: str | None = None,
) -> list[Chunk]:
    """Retrieve the top-k chunks most similar to a question."""

    query = query.strip()

    if not query:
        raise ValueError("Query cannot be empty")
    if top_k < 1:
        raise ValueError("top_k must be at least 1")

    # Run the async embedding function from this synchronous function.
    import asyncio

    query_embedding = asyncio.run(_embed_query(query))

    stmt = select(Chunk)

    if topic:
        stmt = stmt.where(Chunk.topic == topic)

    if role:
        stmt = stmt.where(Chunk.role == role)

    stmt = (
        stmt
        .order_by(Chunk.embedding.cosine_distance(query_embedding))
        .limit(top_k)
    )

    return list(db.scalars(stmt).all())
