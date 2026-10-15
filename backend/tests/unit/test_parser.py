"""Unit tests for resume PDF parsing."""

from io import BytesIO

import pytest
from pypdf import PdfWriter

from app.modules.resume.parser import (
    ResumeParseError,
    extract_resume_text,
)


def create_text_pdf(text: str) -> bytes:
    """Create a small PDF containing extractable text."""
    from reportlab.pdfgen import canvas

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.drawString(72, 750, text)
    pdf.save()
    return buffer.getvalue()


def test_empty_pdf_bytes_are_rejected():
    with pytest.raises(ResumeParseError, match="uploaded PDF is empty"):
        extract_resume_text(b"")


def test_invalid_pdf_bytes_are_rejected():
    with pytest.raises(ResumeParseError, match="could not be read"):
        extract_resume_text(b"This is not a PDF")


def test_text_pdf_extracts_content():
    pdf_bytes = create_text_pdf(
        "Python developer with machine learning experience"
    )

    result = extract_resume_text(pdf_bytes)

    assert "Python developer" in result
    assert "machine learning" in result


def test_pdf_without_readable_text_is_rejected():
    writer = PdfWriter()
    writer.add_blank_page(width=612, height=792)

    buffer = BytesIO()
    writer.write(buffer)

    with pytest.raises(ResumeParseError, match="No readable text found"):
        extract_resume_text(buffer.getvalue())


def test_encrypted_pdf_is_rejected():
    writer = PdfWriter()
    writer.add_blank_page(width=612, height=792)
    writer.encrypt("test-password")

    buffer = BytesIO()
    writer.write(buffer)

    with pytest.raises(
        ResumeParseError,
        match="Password-protected PDFs are not supported",
    ):
        extract_resume_text(buffer.getvalue())