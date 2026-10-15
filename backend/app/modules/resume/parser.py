
"""PDF text extraction for the Resume module."""

from io import BytesIO
from pypdf import PdfReader


class ResumeParseError(ValueError):
    """Raised when a resume cannot be read or contains no usable text."""


def extract_resume_text(pdf_bytes: bytes) -> str:
    if not pdf_bytes:
        raise ResumeParseError("The uploaded PDF is empty.")

    try:
        reader = PdfReader(BytesIO(pdf_bytes), strict=False)

        if reader.is_encrypted:
            raise ResumeParseError(
                "Password-protected PDFs are not supported."
            )

        pages = []

        for page in reader.pages:
            text = page.extract_text() or ""
            if text.strip():
                pages.append(text.strip())

        extracted_text = "\n\n".join(pages).strip()

    except ResumeParseError:
        raise
    except Exception as exc:
        raise ResumeParseError(
            "The PDF could not be read. Please upload a valid PDF."
        ) from exc

    if not extracted_text:
        raise ResumeParseError(
            "No readable text found. The PDF may be scanned; "
            "OCR support is not implemented yet."
        )

    return extracted_text
