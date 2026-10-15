import asyncio

from app.core.config import settings
from app.integrations.llm.base import LLMError
from app.modules.knowledge.embeddings import embed_texts

TEXTS = [
    "Overfitting happens when a model memorises its training data.",
    "A model that scores well on training data but badly on new data is overfitting.",
    "Docker containers package an application together with its dependencies.",
]


async def main():
    print("Embedding model:", settings.embedding_model)
    try:
        vecs = await embed_texts(TEXTS)
    except LLMError as e:
        print("FAILED:", e)
        return
    dot = lambda a, b: sum(x * y for x, y in zip(a, b))
    print("Dimensions:", len(vecs[0]))
    print("Related pair similarity:  ", round(dot(vecs[0], vecs[1]), 3))
    print("Unrelated pair similarity:", round(dot(vecs[0], vecs[2]), 3))


asyncio.run(main())