
import asyncio
import json

from app.integrations.llm.base import LLMProvider
from app.modules.interview.grader import grade_answer


class FakeLLMProvider(LLMProvider):
    """Test provider that avoids real API calls."""

    name = "fake"

    async def generate(self, prompt, system=None, json_mode=False):
        assert json_mode is True

        return json.dumps({
            "score": 4,
            "label": "correct",
            "strengths": [
                "Correctly identifies poor generalization."
            ],
            "missing_concepts": [
                "Could mention learning noise in training data."
            ],
            "feedback": (
                "Good explanation. Add how overfitting affects "
                "performance on unseen data."
            ),
        })


async def main():
    result = await grade_answer(
        provider=FakeLLMProvider(),
        question="What is overfitting?",
        answer=(
            "A model performs well on training data but poorly "
            "on unseen data."
        ),
        reference_answer=(
            "Overfitting occurs when a model learns training data "
            "too closely, including noise, and generalizes poorly."
        ),
        max_score=5,
    )

    print(result.model_dump_json(indent=2))
    assert result.score == 4
    assert result.label == "correct"


if __name__ == "__main__":
    asyncio.run(main())
