# AI Interview Coach

Resume analyzer and adaptive AI mock interviews with RAG-grounded questions.

## Quick start

1. Copy the environment file: `cp .env.example .env` (Windows: `copy .env.example .env`)
2. Fill in at least one LLM key in `.env`
3. Start everything: `docker compose up --build`
4. Backend health check: http://localhost:8000/health
5. Frontend: http://localhost:5173

## Structure

- `frontend/` React + TypeScript app
- `backend/` FastAPI app (modular monolith: auth, resume, interview, knowledge, reports)
- `knowledge_base/` source material for grounded questions
- `eval_data/` labeled data for retrieval and grader evaluation
- `scripts/` offline ingestion and evaluation scripts
- `docs/` architecture and design notes

## Status

Skeleton only. Build order: knowledge base and retrieval, interview loop, grader evaluation,
resume analyzer, frontend, hardening, strict mode.
