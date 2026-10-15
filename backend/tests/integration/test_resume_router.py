"""HTTP endpoint tests for resume upload validation."""

from unittest.mock import AsyncMock

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.modules.resume.router import service
from app.modules.resume.schemas import ResumeAnalysisResult


client = TestClient(app)


@pytest.fixture
def mock_analysis(monkeypatch):
    """Mock the analysis service to avoid real LLM/API calls."""
    result = ResumeAnalysisResult(
        job_role="Machine Learning Engineer",
        resume_skills=["python"],
        matched_skills=["python"],
        missing_skills=[],
        match_score=100.0,
        strengths=["Python experience is demonstrated."],
        improvement_suggestions=[],
        likely_interview_questions=[],
    )

    mock = AsyncMock(return_value=result)
    monkeypatch.setattr(service, "analyze", mock)
    return mock


def test_rejects_non_pdf_content_type():
    response = client.post(
        "/resume/analyze",
        files={"file": ("resume.txt", b"hello", "text/plain")},
        data={"job_role": "Machine Learning Engineer"},
    )

    assert response.status_code == 415
    assert response.json()["detail"] == "Please upload a PDF file."


def test_rejects_invalid_pdf_signature(mock_analysis):
    response = client.post(
        "/resume/analyze",
        files={
            "file": (
                "resume.pdf",
                b"This is not a PDF file",
                "application/pdf",
            )
        },
        data={"job_role": "Machine Learning Engineer"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "The uploaded file is not a valid PDF."
    )
    mock_analysis.assert_not_awaited()


def test_rejects_oversized_pdf(mock_analysis):
    oversized_content = b"%PDF-1.4\n" + (
        b"A" * (10 * 1024 * 1024)
    )

    response = client.post(
        "/resume/analyze",
        files={
            "file": (
                "large.pdf",
                oversized_content,
                "application/pdf",
            )
        },
        data={"job_role": "Machine Learning Engineer"},
    )

    assert response.status_code == 413
    assert response.json()["detail"] == (
        "Resume PDF must be 10 MB or smaller."
    )
    mock_analysis.assert_not_awaited()


def test_valid_pdf_reaches_analysis_service(mock_analysis):
    pdf_content = b"%PDF-1.4\nMock PDF content"

    response = client.post(
        "/resume/analyze",
        files={
            "file": (
                "resume.pdf",
                pdf_content,
                "application/pdf",
            )
        },
        data={"job_role": "Machine Learning Engineer"},
    )

    assert response.status_code == 200
    assert response.json()["job_role"] == "Machine Learning Engineer"
    assert response.json()["match_score"] == 100.0
    mock_analysis.assert_awaited_once()