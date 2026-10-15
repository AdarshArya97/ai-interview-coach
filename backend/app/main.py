
from fastapi import FastAPI

from app.modules.resume.router import router as resume_router

app = FastAPI(title="AI Interview Coach")

app.include_router(resume_router)


@app.get("/health")
def health():
    return {"status": "ok"}
