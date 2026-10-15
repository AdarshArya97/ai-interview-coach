
import json
import math
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from app.integrations.llm.base import LLMProvider
from app.modules.interview.prompts import (
    GRADER_SYSTEM_PROMPT,
    GRADER_USER_PROMPT,
)


class GradingResult(BaseModel):
    """Validated result returned by the AI answer grader."""

    model_config = ConfigDict(extra="forbid")

    score: float = Field(ge=0)
    label: Literal["correct", "partially_correct", "incorrect"]
    strengths: list[str]
    missing_concepts: list[str]
    feedback: str


async def grade_answer(
    provider: LLMProvider,
    question: str,
    answer: str,
    reference_answer: str,
    max_score: float = 5,
) -> GradingResult:
    """Grade an interview answer using an LLM and validate its output."""

    if not question.strip():
        raise ValueError("Question cannot be empty.")

    if not answer.strip():
        answer = "[No answer provided]"

    if not math.isfinite(max_score) or max_score <= 0:
        raise ValueError("max_score must be a positive, finite number.")

    prompt = GRADER_USER_PROMPT.format(
        question=question,
        answer=answer,
        reference_answer=reference_answer or "No reference answer provided.",
        max_score=max_score,
    )

    raw_response = await provider.generate(
        prompt=prompt,
        system=GRADER_SYSTEM_PROMPT,
        json_mode=True,
    )

    try:
        data = json.loads(raw_response)
        result = GradingResult.model_validate(data)
    except (json.JSONDecodeError, ValidationError) as exc:
        raise ValueError(
            f"The LLM returned an invalid grading response: {exc}"
        ) from exc

    if not math.isfinite(result.score) or result.score > max_score:
        raise ValueError(
            f"Grader score must be between 0 and {max_score}."
        )

    # Round only after validating the original score.
    result.score = round(result.score, 2)

    return result
