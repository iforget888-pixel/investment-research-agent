# Investment Research Agent

Personal investment research agent workspace.

This repository intentionally starts from a light skeleton migrated from the prior research-weekly project:

- Vite + React frontend shell
- shared UI primitives
- PDF / vision / LLM browser utilities
- fresh product documentation

It does not carry over the old AI-weekly taxonomy, Appwrite client, source list, or weekly-agent business logic.

## Current Documents

- `docs/PRD.md` - product definition draft
- `docs/architecture-options.md` - backend and storage options
- `agent/README.md` - planned agent pipeline boundary

## Local Development

```bash
pnpm install
pnpm run dev
```

Backend selection is intentionally open. The current recommendation is a Docker-based local stack rather than Appwrite.

## Local Backend

The first backend scaffold uses Docker Desktop:

```bash
cp .env.example .env
docker compose up --build
```

Services:

- API: http://localhost:8000
- API health: http://localhost:8000/health
- Postgres: localhost:5432
- Redis: localhost:6379
- MinIO: http://localhost:9001
