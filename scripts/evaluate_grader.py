
"""Evaluate the real Gemini answer grader against labeled examples."""

import asyncio
import json
import sys
from pathlib import Path
from statistics import mean

# Resolve paths from the project root, regardless of the working directory.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
BACKEND_DIR = PROJECT_ROOT / "backend"
EVAL_FILE = PROJECT_ROOT / "eval_data" / "graded_answers.json"
RESULTS_FILE = (
    PROJECT_ROOT / "eval_data" / "results" / "grader_metrics.json"
)

# Allow imports from backend/app when running this script from the project root.
sys.path.insert(0, str(BACKEND_DIR))

from app.integrations.llm.gemini import GeminiProvider
from app.modules.interview.grader import grade_answer


# Temporary reference answers for the current six-example dataset.
# For a larger dataset, store reference_answer in each JSON sample instead.
REFERENCE_ANSWERS = {
    "What is overfitting?": (
        "Overfitting occurs when a model learns the training data too "
        "closely, including noise, and performs poorly on unseen data."
    ),
    "What is regularization in machine learning?": (
        "Regularization adds a penalty or constraint to discourage "
        "excessive model complexity and help reduce overfitting."
    ),
}


def calculate_mae(
    expected_scores: list[float],
    predicted_scores: list[float],
) -> float:
    """Mean Absolute Error: lower is better."""
    if not expected_scores:
        return 0.0

    return mean(
        abs(expected - predicted)
        for expected, predicted in zip(expected_scores, predicted_scores)
    )


def calculate_accuracy(
    expected: list[str],
    predicted: list[str],
) -> float:
    """Classification accuracy for answer labels."""
    if not expected:
        return 0.0

    return sum(
        actual == predicted_label
        for actual, predicted_label in zip(expected, predicted)
    ) / len(expected)


async def evaluate():
    if not EVAL_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {EVAL_FILE}")

    with EVAL_FILE.open("r", encoding="utf-8") as file:
        samples = json.load(file)

    if not samples:
        raise ValueError("Evaluation dataset is empty")

    provider = GeminiProvider()

    expected_scores = []
    predicted_scores = []
    expected_labels = []
    predicted_labels = []
    details = []

    for index, sample in enumerate(samples, start=1):
        sample_id = sample["id"]
        question = sample["question"]
        answer = sample["answer"]
        expected_score = float(sample["expected_score"])
        max_score = float(sample["max_score"])
        expected_label = sample["expected_label"]

        if max_score <= 0:
            raise ValueError(f"Invalid max_score for sample {sample_id}")

        if not 0 <= expected_score <= max_score:
            raise ValueError(
                f"Invalid expected_score for sample {sample_id}"
            )

        reference_answer = sample.get(
            "reference_answer",
            REFERENCE_ANSWERS.get(question),
        )

        if not reference_answer:
            raise ValueError(
                f"No reference answer provided for sample {sample_id}. "
                "Add reference_answer to the dataset."
            )

        print(f"[{index}/{len(samples)}] Grading {sample_id}: {question}")

        try:
            result = await grade_answer(
                provider=provider,
                question=question,
                answer=answer,
                reference_answer=reference_answer,
                max_score=max_score,
            )
        except Exception as exc:
            # Record failures rather than silently counting them as predictions.
            details.append({
                "id": sample_id,
                "error": str(exc),
            })
            print(f"  FAILED: {exc}")
            continue

        expected_scores.append(expected_score)
        predicted_scores.append(result.score)
        expected_labels.append(expected_label)
        predicted_labels.append(result.label)

        details.append({
            "id": sample_id,
            "question": question,
            "answer": answer,
            "expected_score": expected_score,
            "predicted_score": result.score,
            "score_error": round(
                abs(expected_score - result.score), 2
            ),
            "max_score": max_score,
            "expected_label": expected_label,
            "predicted_label": result.label,
            "label_correct": result.label == expected_label,
            "strengths": result.strengths,
            "missing_concepts": result.missing_concepts,
            "feedback": result.feedback,
        })

        print(
            f"  Expected: {expected_score}/{max_score} ({expected_label})"
        )
        print(
            f"  Predicted: {result.score}/{max_score} ({result.label})"
        )

    successful = len(expected_scores)
    failed = len(samples) - successful

    report = {
        "evaluation_type": "real_gemini_grader",
        "model": provider.name,
        "sample_count": len(samples),
        "successful_count": successful,
        "failed_count": failed,
        "mae": (
            round(calculate_mae(expected_scores, predicted_scores), 4)
            if successful else None
        ),
        "label_accuracy": (
            round(
                calculate_accuracy(expected_labels, predicted_labels), 4
            )
            if successful else None
        ),
        "note": (
            "Metrics are calculated only on successful predictions. "
            "Results from this small dataset are an initial evaluation, "
            "not proof of production-level reliability."
        ),
        "results": details,
    }

    RESULTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_FILE.write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print("\n--- Real Gemini Grader Evaluation ---")
    print(f"Total samples: {len(samples)}")
    print(f"Successful predictions: {successful}")
    print(f"Failed predictions: {failed}")

    if successful:
        print(f"MAE: {report['mae']:.4f}")
        print(f"Label accuracy: {report['label_accuracy']:.2%}")
    else:
        print("No successful predictions; metrics unavailable.")

    print(f"Results saved to: {RESULTS_FILE}")


if __name__ == "__main__":
    asyncio.run(evaluate())
