"""Load knowledge_base/*.md files into the chunks table, with embeddings.

Run:  docker compose exec backend python -m scripts.ingest_knowledge
Safe to run repeatedly: chunks already in the database are skipped.
"""
import asyncio
import hashlib
from pathlib import Path

from sqlalchemy import select

from app.db.models.chunk import Chunk
from app.db.session import SessionLocal
from app.integrations.llm.base import LLMError
from app.modules.knowledge.embeddings import embed_texts

KB = Path("/app/knowledge_base")
REQUIRED = ["topic", "subtopic", "difficulty", "source_name", "source_url", "license"]


def parse(path: Path):
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---"):
        raise ValueError("missing front matter")
    _, fm, body = raw.split("---", 2)
    meta = {}
    for line in fm.strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    missing = [k for k in REQUIRED if not meta.get(k)]
    if missing:
        raise ValueError(f"missing fields {missing}")
    body = body.strip()
    if len(body) < 100:
        raise ValueError("body too short (under 100 characters)")
    meta.setdefault("role", "ml_engineer")
    return meta, body


async def main():
    found, errors, items = 0, 0, []
    for path in sorted(KB.rglob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        found += 1
        try:
            meta, body = parse(path)
        except ValueError as e:
            errors += 1
            print(f"SKIPPED {path.relative_to(KB)}: {e}")
            continue
        digest = hashlib.sha256(
            f"{meta['role']}|{meta['topic']}|{body}".encode()
        ).hexdigest()
        items.append((digest, meta, body))

    with SessionLocal() as db:
        existing = set(db.scalars(select(Chunk.content_hash)))
        new = [it for it in items if it[0] not in existing]
        if new:
            texts = [f"{m['subtopic']}: {b}" for _, m, b in new]
            try:
                vectors = await embed_texts(texts, task_type="RETRIEVAL_DOCUMENT")
            except LLMError as e:
                print("FAILED while embedding:", e)
                return
            for (digest, m, b), vec in zip(new, vectors):
                db.add(
                    Chunk(
                        topic=m["topic"], subtopic=m["subtopic"],
                        difficulty=m["difficulty"], role=m["role"], content=b,
                        source_name=m["source_name"], source_url=m["source_url"],
                        license=m["license"], content_hash=digest, embedding=vec,
                    )
                )
            db.commit()

    print(f"Files found: {found} | skipped with errors: {errors} | "
          f"already in database: {len(items) - len(new)} | inserted: {len(new)}")


asyncio.run(main())