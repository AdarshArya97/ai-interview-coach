
import asyncio
from io import BytesIO

from reportlab.pdfgen import canvas

from app.modules.resume.schemas import ResumeAnalysisRequest
from app.modules.resume.service import ResumeAnalysisService


class FakeLLM:
    async def generate(self, prompt, system=None, json_mode=False):
        assert json_mode is True
        assert "Machine Learning Engineer" in prompt

        return """
        {
          "strengths": ["Resume demonstrates Python experience."],
          "improvement_suggestions": [
            "Add measurable results to project descriptions."
          ],
          "likely_interview_questions": [
            "Explain a machine learning project you built."
          ]
        }
        """


def make_pdf(text: str) -> bytes:
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.drawString(72, 750, text)
    pdf.save()
    return buffer.getvalue()


async def main():
    service = ResumeAnalysisService(llm=FakeLLM())

    pdf_bytes = make_pdf(
        "Python developer with machine learning experience."
    )

    request = ResumeAnalysisRequest(
        job_role="Machine Learning Engineer",
        job_description="We require Python and machine learning skills.",
    )

    result = await service.analyze(pdf_bytes, request)

    print(result.model_dump())

    assert result.job_role == "Machine Learning Engineer"
    assert "python" in result.resume_skills
    assert result.match_score == 100.0
    assert len(result.strengths) > 0
    assert len(result.likely_interview_questions) > 0

    print("Resume service tests passed.")


if __name__ == "__main__":
    asyncio.run(main())
