
from io import BytesIO

from reportlab.pdfgen import canvas

from app.modules.resume.parser import (
    ResumeParseError,
    extract_resume_text,
)


def create_test_pdf(text: str) -> bytes:
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.drawString(72, 750, text)
    pdf.save()
    return buffer.getvalue()


def main():
    pdf_bytes = create_test_pdf(
        "Python developer with machine learning experience"
    )

    text = extract_resume_text(pdf_bytes)

    print("Extracted text:", text)
    assert "Python" in text
    assert "machine learning" in text.lower()

    try:
        extract_resume_text(b"")
    except ResumeParseError:
        print("Empty-file validation passed.")
    else:
        raise AssertionError("Empty PDF bytes should be rejected.")

    print("Parser tests passed.")


if __name__ == "__main__":
    main()
