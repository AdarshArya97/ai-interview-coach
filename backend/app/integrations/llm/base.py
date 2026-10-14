from abc import ABC, abstractmethod


class LLMError(Exception):
    """Any failure talking to an LLM provider."""


class RateLimitError(LLMError):
    """Provider said we hit a quota or rate limit (HTTP 429)."""


class LLMProvider(ABC):
    name: str

    @abstractmethod
    async def generate(
        self, prompt: str, system: str | None = None, json_mode: bool = False
    ) -> str:
        ...