from fastapi import FastAPI

app = FastAPI(title="AI Interview Coach")


@app.get("/health")
def health():
    return {"status": "ok"}
