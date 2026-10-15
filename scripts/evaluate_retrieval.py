
"""Evaluate retrieval quality using labeled subtopics."""

import json
from pathlib import Path

from app.db.session import SessionLocal
from app.modules.knowledge.retriever import retrieve_chunks

EVAL_FILE = Path("/app/eval_data/retrieval_queries.json")
RESULTS_FILE = Path("/app/eval_data/results/retrieval_metrics.json")


def recall_at_k(
    relevant_subtopics: set[str],
    retrieved_subtopics: list[str],
    k: int,
) -> float:
    """Fraction of expected relevant subtopics retrieved in top k."""
    if not relevant_subtopics:
        return 0.0

    found = set(retrieved_subtopics[:k])
    return len(relevant_subtopics & found) / len(relevant_subtopics)


def main():
    if not EVAL_FILE.exists():
        raise FileNotFoundError(
            f"Evaluation dataset not found: {EVAL_FILE}"
        )

    with EVAL_FILE.open("r", encoding="utf-8") as file:
        queries = json.load(file)

    if not queries:
        raise ValueError("Evaluation dataset is empty")

    db = SessionLocal()
    results = []

    try:
        for item in queries:
            query = item["query"]
            expected = set(item["relevant_subtopics"])

            chunks = retrieve_chunks(
                db=db,
                query=query,
                top_k=5,
                role="ml_engineer",
            )

            retrieved = [chunk.subtopic for chunk in chunks if chunk.subtopic]

            r3 = recall_at_k(expected, retrieved, 3)
            r5 = recall_at_k(expected, retrieved, 5)

            result = {
                "query": query,
                "expected_subtopics": sorted(expected),
                "retrieved_subtopics": retrieved,
                "retrieved_chunk_ids": [chunk.id for chunk in chunks],
                "recall_at_3": round(r3, 4),
                "recall_at_5": round(r5, 4),
            }
            results.append(result)

            print(f"\nQuery: {query}")
            print(f"Expected: {sorted(expected)}")
            print(f"Retrieved: {retrieved}")
            print(f"Recall@3: {r3:.2f} | Recall@5: {r5:.2f}")

    finally:
        db.close()

    avg_r3 = sum(r["recall_at_3"] for r in results) / len(results)
    avg_r5 = sum(r["recall_at_5"] for r in results) / len(results)

    report = {
        "query_count": len(results),
        "recall_at_3": round(avg_r3, 4),
        "recall_at_5": round(avg_r5, 4),
        "query_results": results,
    }

    RESULTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_FILE.write_text(
        json.dumps(report, indent=2),
        encoding="utf-8",
    )

    print("\n--- Retrieval Evaluation Summary ---")
    print(f"Queries evaluated: {len(results)}")
    print(f"Mean Recall@3: {avg_r3:.2%}")
    print(f"Mean Recall@5: {avg_r5:.2%}")
    print(f"Results saved to: {RESULTS_FILE}")


if __name__ == "__main__":
    main()
