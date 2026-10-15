"""FastAPI endpoints for resume analysis."""

from fastapi import APIRouter, File, Form, HTTPException, UploadFile, status

from app.modules.resume.schemas import (
    ResumeAnalysisRequest,
    ResumeAnalysisResult,
)
from app.modules.resume.service import (
    ResumeAnalysisError,
    ResumeAnalysisService,
)

router = APIRouter(prefix="/resume", tags=["Resume"])
service = ResumeAnalysisService()

MAX_PDF_SIZE = 10 * 1024 * 1024  # 10 MB


@router.post(
    "/analyze",
    response_model=ResumeAnalysisResult,
    status_code=status.HTTP_200_OK,
)
async def analyze_resume(
    file: UploadFile = File(...),
    job_role: str = Form(..., min_length=2, max_length=150),
    job_description: str | None = Form(
        default=None,
        max_length=15000,
    ),
):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=415,
            detail="Please upload a PDF file.",
        )

    try:
        pdf_bytes = await file.read(MAX_PDF_SIZE + 1)

        if len(pdf_bytes) > MAX_PDF_SIZE:
            raise HTTPException(
                status_code=413,
                detail="Resume PDF must be 10 MB or smaller.",
            )

        # Check for a PDF header near the beginning of the file.
        if b"%PDF-" not in pdf_bytes[:1024]:
            raise HTTPException(
                status_code=400,
                detail="The uploaded file is not a valid PDF.",
            )

        request = ResumeAnalysisRequest(
            job_role=job_role,
            job_description=job_description,
        )

        return await service.analyze(pdf_bytes, request)

    except ResumeAnalysisError as exc:
        raise HTTPException(
            status_code=422,
            detail=str(exc),
        ) from exc

    finally:
        await file.close()
