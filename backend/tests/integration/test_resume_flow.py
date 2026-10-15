
"""Tests for the resume analysis service flow."""

import json
from unittest.mock import AsyncMock, patch

import anyio
import pytest

from app.modules.resume.schemas import (
    ResumeAnalysisRequest,
    ResumeAnalysisResult,
)
from app.modules.resume.service import (
    ResumeAnalysisError,
    ResumeAnalysisService,
)


VALID_FEEDBACK = {
    "strengths": ["Strong Python fundamentals"],
    "improvement_suggestions": [
        "Add more ML project details"
    ],
    "likely_interview_questions": [
        "Explain a machine learning project you built."
    ],
}


def create_mock_llm(response=None):
    """Create a mock LLM without making real API calls."""
    llm = AsyncMock()
    llm.generate.return_value = (
        json.dumps(VALID_FEEDBACK)
        if response is None
        else response
    )
    return llm


def test_role_defaults_are_used_when_description_is_missing():
    async def scenario():
        mock_llm = create_mock_llm()
        request = ResumeAnalysisRequest(
            job_role="Machine Learning Engineer",
        )
        service = ResumeAnalysisService(llm=mock_llm)

        with (
            patch(
                "app.modules.resume.service.extract_resume_text",
                return_value="Python and machine learning experience",
            ),
            patch(
                "app.modules.resume.service.load_role_skills",
                return_value={
                    "machine learning engineer": [
                        "python",
                        "machine learning",
                        "docker",
                    ]
                },
            ),
        ):
            result = await service.analyze(b"%PDF-test", request)

        assert isinstance(result, ResumeAnalysisResult)
        assert result.match_score == pytest.approx(66.67)
        assert result.matched_skills == [
            "machine learning",
            "python",
        ]
        assert result.missing_skills == ["docker"]
        mock_llm.generate.assert_awaited_once()

    anyio.run(scenario)


def test_job_description_takes_priority():
    async def scenario():
        mock_llm = create_mock_llm()
        request = ResumeAnalysisRequest(
            job_role="Machine Learning Engineer",
            job_description="Python and Docker experience required",
        )
        service = ResumeAnalysisService(llm=mock_llm)

        with (
            patch(
                "app.modules.resume.service.extract_resume_text",
                return_value="Python experience",
            ),
            patch(
                "app.modules.resume.service.load_role_skills",
            ) as mock_load_roles,
        ):
            result = await service.analyze(b"%PDF-test", request)

        assert result.match_score == pytest.approx(50.0)
        assert result.matched_skills == ["python"]
        assert result.missing_skills == ["docker"]
        mock_load_roles.assert_not_called()
        mock_llm.generate.assert_awaited_once()

    anyio.run(scenario)


def test_unknown_role_without_description_raises_error():
    async def scenario():
        mock_llm = create_mock_llm()
        request = ResumeAnalysisRequest(
            job_role="Quantum Engineer",
        )
        service = ResumeAnalysisService(llm=mock_llm)

        with (
            patch(
                "app.modules.resume.service.extract_resume_text",
                return_value="Python experience",
            ),
            patch(
                "app.modules.resume.service.load_role_skills",
                return_value={
                    "python developer": ["python"],
                },
            ),
        ):
            with pytest.raises(
                ResumeAnalysisError,
                match="no default skill profile",
            ):
                await service.analyze(b"%PDF-test", request)

        mock_llm.generate.assert_not_awaited()

    anyio.run(scenario)


def test_invalid_gemini_json_raises_analysis_error():
    async def scenario():
        mock_llm = create_mock_llm("not valid JSON")
        request = ResumeAnalysisRequest(
            job_role="Machine Learning Engineer",
        )
        service = ResumeAnalysisService(llm=mock_llm)

        with (
            patch(
                "app.modules.resume.service.extract_resume_text",
                return_value="Python and machine learning",
            ),
            patch(
                "app.modules.resume.service.load_role_skills",
                return_value={
                    "machine learning engineer": [
                        "python",
                        "machine learning",
                    ]
                },
            ),
        ):
            with pytest.raises(
                ResumeAnalysisError,
                match="invalid resume analysis",
            ):
                await service.analyze(b"%PDF-test", request)

        mock_llm.generate.assert_awaited_once()

    anyio.run(scenario)
