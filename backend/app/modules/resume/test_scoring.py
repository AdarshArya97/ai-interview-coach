
from app.modules.resume.scoring import calculate_match, extract_skills


def main():
    resume = """
    Python developer with experience in ML and Docker containers.
    """

    job = """
    Required skills: Python, machine learning, Docker.
    """

    result = calculate_match(resume, job)

    print(result)

    assert result["matched_skills"] == [
        "docker",
        "machine learning",
        "python",
    ]
    assert result["missing_skills"] == []
    assert result["match_score"] == 100.0

    # Check that Python is not detected inside a larger word.
    assert "python" not in extract_skills(
        "I enjoy pythonic programming."
    )

    print("Scoring tests passed.")


if __name__ == "__main__":
    main()
