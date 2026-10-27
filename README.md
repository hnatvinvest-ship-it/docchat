# docchat

Chat with your documents, with source citations (RAG). Upload a PDF or markdown file, ask a question, and get a streamed answer together with citations from the document fragments it was based on.

## Status

Work in progress. The backend skeleton is done: health endpoint, typed settings read from `.env`, tests and linting. Document ingestion, retrieval, chat streaming and the frontend are planned (see the roadmap).

## Tech stack

- **Backend:** Python 3.12, FastAPI, Pydantic Settings
- **Database:** PostgreSQL with the pgvector extension (vector similarity search)
- **LLM:** OpenAI API (chat model and embeddings)
- **Frontend (planned):** Vite, React, TypeScript
- **Tooling:** uv, ruff, pytest, Docker Compose

## Project structure

```
backend/             FastAPI app, tests, pyproject.toml
  app/main.py        application and GET /health
  app/config.py      settings loaded from environment and .env
  tests/             pytest tests
frontend/            React app (planned)
docker-compose.yml   PostgreSQL + pgvector
.env.example         template for local configuration
```

## Getting started

Prerequisites: Docker Desktop, [uv](https://docs.astral.sh/uv/) and an OpenAI API key.

1. Create your local config and add your key. `.env` is git-ignored and must never be committed:

   ```bash
   cp .env.example .env
   ```

2. Start the database:

   ```bash
   docker compose up -d
   ```

3. Run the backend:

   ```bash
   cd backend
   uv sync
   uv run uvicorn app.main:app --reload
   ```

   Health check: http://localhost:8000/health. Interactive API docs: http://localhost:8000/docs.

## Tests and linting

```bash
cd backend
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

## Roadmap

- [x] Repository, Docker Compose with pgvector
- [x] FastAPI skeleton, `GET /health`, settings, tests, linting
- [ ] Database migrations, `documents` and `chunks` tables
- [ ] Document upload, text extraction, chunking, embeddings
- [ ] Retrieval and streamed chat (SSE) with source citations
- [ ] Frontend: upload, streaming chat, citations panel
- [ ] Answer quality evaluation and results table
