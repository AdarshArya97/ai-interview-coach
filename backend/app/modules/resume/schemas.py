
from pydantic import BaseModel, Field


class ResumeAnalysisRequest(BaseModel):
    job_role: str = Field(
        min_length=2,
        max_length=150,
        description="Target job role, e.g. Machine Learning Engineer",
    )
    job_description: str | None = Field(
        default=None,
        max_length=15000,
        description="Optional job description for more precise matching",
    )


class ResumeAnalysisResult(BaseModel):
    job_role: str
    resume_skills: list[str]
    matched_skills: list[str]
    missing_skills: list[str]
    match_score: float = Field(ge=0, le=100)
    strengths: list[str]
    improvement_suggestions: list[str]
    likely_interview_questions: list[str]
