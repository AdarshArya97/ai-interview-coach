
"""Unit tests for resume skill extraction and matching."""

import pytest

from app.modules.resume.scoring import (
    calculate_match,
    calculate_match_against_skills,
    extract_skills,
    load_role_skills,
)


@pytest.fixture
def taxonomy():
    return {
        "python": ["python", "python3"],
        "machine learning": [
            "machine learning",
            "ml",
            "machine-learning",
        ],
        "docker": ["docker", "containers", "containerization"],
    }


def test_extract_skills(taxonomy):
    text = "Experienced in Python3, ML, and Docker."
    assert extract_skills(text, taxonomy) == [
        "docker",
        "machine learning",
        "python",
    ]


def test_extract_skills_avoids_partial_word_matches(taxonomy):
    assert extract_skills("I enjoy pythonista tools.", taxonomy) == []


def test_calculate_match_all_skills_match(taxonomy):
    result = calculate_match(
        "Python, machine learning, Docker",
        "Python, ML, Docker",
        taxonomy,
    )
    assert result["match_score"] == 100.0
    assert result["missing_skills"] == []


def test_calculate_match_one_skill_missing(taxonomy):
    result = calculate_match(
        "Python and machine learning",
        "Python, machine learning, Docker",
        taxonomy,
    )
    assert result["match_score"] == 66.67
    assert result["missing_skills"] == ["docker"]


def test_calculate_match_no_matching_skills(taxonomy):
    result = calculate_match(
        "I have communication skills",
        "Python and Docker",
        taxonomy,
    )
    assert result["match_score"] == 0.0
    assert result["matched_skills"] == []


def test_empty_job_description_has_zero_score(taxonomy):
    result = calculate_match("Python experience", "", taxonomy)
    assert result["match_score"] == 0.0


def test_match_against_explicit_required_skills(taxonomy):
    result = calculate_match_against_skills(
        "Python and ML experience",
        ["python", "machine learning", "docker"],
        taxonomy,
    )
    assert result["match_score"] == 66.67
    assert result["matched_skills"] == ["machine learning", "python"]
    assert result["missing_skills"] == ["docker"]


def test_unknown_required_skill_is_rejected(taxonomy):
    with pytest.raises(ValueError, match="Unknown canonical skills"):
        calculate_match_against_skills(
            "Python experience",
            ["java"],
            taxonomy,
        )


def test_role_configuration_loads():
    roles = load_role_skills()
    assert "machine learning engineer" in roles
    assert "python developer" in roles
