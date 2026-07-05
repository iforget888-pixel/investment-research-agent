# Local Backend

**Status**: Draft  
**Last updated**: 2026-07-05

## Stack

The MVP backend starts with a local Docker stack:

- FastAPI API service
- PostgreSQL with pgvector
- Redis
- MinIO object storage

## Run

```bash
cp .env.example .env
docker compose up --build
```

## Endpoints

```text
GET    /health
GET    /watchlist
POST   /watchlist
GET    /watchlist/{item_id}
PATCH  /watchlist/{item_id}
GET    /raw-materials
POST   /raw-materials
GET    /raw-materials/{material_id}
PATCH  /raw-materials/{material_id}
```

## Design Notes

The API layer deliberately avoids agent logic. It stores the research state and raw inputs. Agent workers will later consume raw materials, produce evidence, update thesis impact, and generate weekly briefs.

The current schema is created automatically on API startup. That is acceptable for the first scaffold; once tables stabilize, migrations should move to Alembic.
