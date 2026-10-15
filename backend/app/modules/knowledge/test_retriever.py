
from app.db.session import SessionLocal
from app.modules.knowledge.retriever import retrieve_chunks


def main():
    db = SessionLocal()

    try:
        results = retrieve_chunks(
            db=db,
            query="What is overfitting and how can regularization help?",
            top_k=5,
            topic="machine_learning",
        )

        for rank, chunk in enumerate(results, start=1):
            print(f"\nRank: {rank}")
            print(f"ID: {chunk.id}")
            print(f"Topic: {chunk.topic}")
            print(f"Subtopic: {chunk.subtopic}")
            print(f"Content: {chunk.content[:300]}")

    finally:
        db.close()


if __name__ == "__main__":
    main()
