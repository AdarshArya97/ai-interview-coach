
"""Orchestrates resume parsing, skill matching, and AI feedback."""

import json
import logging

from pydantic import ValidationError

from app.integrations.llm.base import LLMError
from app.integrations.llm.gemini import GeminiProvider
from app.modules.resume.parser import extract_resume_text
from app.modules.resume.prompts import (
    RESUME_ANALYSIS_SYSTEM_PROMPT,
    build_resume_analysis_prompt,
)
from app.modules.resume.schemas import (
    ResumeAnalysisRequest,
    ResumeAnalysisResult,
)
from app.modules.resume.scoring import calculate_match


logger = logging.getLogger(__name__)


class ResumeAnalysisError(Exception):
    """Raised when resume analysis cannot be completed."""


class ResumeAnalysisService:
    def __init__(self, llm=None):
        self.llm = llm if llm is not None else GeminiProvider()

    async def analyze(
        self,
        pdf_bytes: bytes,
        request: ResumeAnalysisRequest,
    ) -> ResumeAnalysisResult:
        # 1. Extract text from the uploaded PDF.
        try:
            resume_text = extract_resume_text(pdf_bytes)
        except ValueError as exc:
            raise ResumeAnalysisError(str(exc)) from exc

        # 2. Calculate deterministic skill coverage.
        job_text = request.job_description or request.job_role
        match = calculate_match(resume_text, job_text)

        # 3. Build the prompt and request AI feedback.
        prompt = build_resume_analysis_prompt(
            resume_text=resume_text,
            job_role=request.job_role,
            job_description=request.job_description,
        )

        try:
            raw_response = await self.llm.generate(
                prompt=prompt,
                system=RESUME_ANALYSIS_SYSTEM_PROMPT,
                json_mode=True,
            )
        except LLMError as exc:
            # Log the underlying provider error for debugging.
            logger.error(
                "Gemini resume analysis failed: %s",
                exc,
            )
            raise ResumeAnalysisError(
                "The AI provider could not complete resume analysis."
            ) from exc

        # 4. Parse and validate Gemini's JSON response.
        try:
            feedback = json.loads(raw_response)

            if not isinstance(feedback, dict):
                raise ValueError("Expected a JSON object.")

            result_data = {
                "job_role": request.job_role,
                "resume_skills": match["resume_skills"],
                "matched_skills": match["matched_skills"],
                "missing_skills": match["missing_skills"],
                "match_score": match["match_score"],
                "strengths": feedback["strengths"],
                "improvement_suggestions": feedback[
                    "improvement_suggestions"
                ],
                "likely_interview_questions": feedback[
                    "likely_interview_questions"
                ],
            }

            return ResumeAnalysisResult.model_validate(result_data)

        except (
            json.JSONDecodeError,
            KeyError,
            TypeError,
            ValueError,
            ValidationError,
        ) as exc:
            logger.error(
                "Invalid resume analysis response: %s",
                exc,
            )
            raise ResumeAnalysisError(
                "The AI returned an invalid resume analysis. Please retry."
            ) from exc
