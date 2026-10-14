import asyncio
import time

from app.core.config import settings
from app.integrations.llm.base import LLMError
from app.integrations.llm.gemini import GeminiProvider


async def main():
    print("Model:", settings.gemini_model)
    start = time.time()
    try:
        out = await GeminiProvider().generate("Reply with the single word: ready")
    except LLMError as e:
        print("FAILED:", e)
        return
    print("Response:", out.strip())
    print(f"Latency: {time.time() - start:.1f}s")


asyncio.run(main())