
import asyncio

from app.integrations.llm.gemini import GeminiProvider
from app.modules.interview.grader import grade_answer


async def main():
    provider = GeminiProvider()

    result = await grade_answer(
        provider=provider,
        question="What is overfitting?",
        answer=(
            "A model learns the training data too closely "
            "and performs poorly on unseen data."
        ),
        reference_answer=(
            "Overfitting occurs when a model learns patterns "
            "and noise in training data, resulting in poor "
            "generalization to unseen data."
        ),
        max_score=5,
    )

    print("\n--- Gemini Grading Result ---")
    print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    asyncio.run(main())
