from datetime import datetime

from pgvector.sqlalchemy import Vector
from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

# Must match settings.embedding_dimensions. Changing it later needs a new migration.
EMBEDDING_DIM = 768


class Chunk(Base):
    __tablename__ = "chunks"

    id: Mapped[int] = mapped_column(primary_key=True)
    topic: Mapped[str] = mapped_column(String(64), index=True)
    subtopic: Mapped[str | None] = mapped_column(String(128))
    difficulty: Mapped[str] = mapped_column(String(16), default="medium")
    role: Mapped[str] = mapped_column(String(32), default="ml_engineer", index=True)
    content: Mapped[str] = mapped_column(Text)
    source_name: Mapped[str] = mapped_column(String(128))
    source_url: Mapped[str] = mapped_column(String(512))
    license: Mapped[str] = mapped_column(String(64))
    content_hash: Mapped[str] = mapped_column(String(64), unique=True)
    embedding = mapped_column(Vector(EMBEDDING_DIM))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )