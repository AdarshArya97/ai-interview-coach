
"""Skill extraction and deterministic resume-to-job matching."""

import json
from pathlib import Path


TAXONOMY_PATH = Path(__file__).with_name("skills_taxonomy.json")


def load_skill_taxonomy() -> dict[str, list[str]]:
    with TAXONOMY_PATH.open("r", encoding="utf-8") as file:
        taxonomy = json.load(file)

    return {
        canonical.lower(): [
            canonical.lower(),
            *(alias.lower() for alias in aliases),
        ]
        for canonical, aliases in taxonomy.items()
    }


def extract_skills(
    text: str,
    taxonomy: dict[str, list[str]] | None = None,
) -> list[str]:
    """Return canonical skills found in text using whole-word matching."""
    import re

    if taxonomy is None:
        taxonomy = load_skill_taxonomy()

    normalized_text = text.lower()
    found = []

    for canonical, aliases in taxonomy.items():
        for alias in aliases:
            pattern = rf"(?<!\w){re.escape(alias.lower())}(?!\w)"
            if re.search(pattern, normalized_text):
                found.append(canonical)
                break

    return sorted(set(found))


def calculate_match(
    resume_text: str,
    job_text: str,
    taxonomy: dict[str, list[str]] | None = None,
) -> dict:
    """Compare detected skills and calculate a transparent match score."""
    resume_skills = set(extract_skills(resume_text, taxonomy))
    required_skills = set(extract_skills(job_text, taxonomy))

    matched = sorted(resume_skills & required_skills)
    missing = sorted(required_skills - resume_skills)

    score = (
        round(len(matched) / len(required_skills) * 100, 2)
        if required_skills
        else 0.0
    )

    return {
        "resume_skills": sorted(resume_skills),
        "required_skills": sorted(required_skills),
        "matched_skills": matched,
        "missing_skills": missing,
        "match_score": score,
    }
