# Architecture Options

**Status**: Draft  
**Last updated**: 2026-07-05

## Recommendation

Use a local Docker-based backend for this personal project.

Recommended first stack:

- Frontend: Vite + React
- API: FastAPI or Node API
- Database: PostgreSQL
- Vector search: pgvector
- Queue / cache: Redis
- Workers: Python agent workers
- Object storage: MinIO
- Scheduler: worker cron or Temporal later
- Search: PostgreSQL full text first, OpenSearch later only if needed

This gives more control than Appwrite for investment research, especially for relational data, audit trails, financial time series, vector search, background jobs, and local ownership.

## Why Not Default To Appwrite

Appwrite was a good fit for the previous company frontend project because it provided a quick hosted database, auth, storage, and direct browser access.

For this personal investment agent, the tradeoffs are different:

- financial data is relational and time-series heavy
- evidence needs strong provenance and queryability
- agent jobs need background execution and retries
- vector search will likely matter
- local privacy may matter for interviews and notes
- Docker is available, so the backend can be owned end to end

Appwrite can still be considered later if speed of CRUD UI becomes more important than backend control.

## Option A: Lightweight Local Backend

```text
Vite frontend
  -> FastAPI / Node API
  -> PostgreSQL + pgvector
  -> local filesystem or MinIO
  -> Python workers
```

Pros:

- simple to understand
- easy local development
- good enough for MVP
- avoids premature infrastructure complexity

Cons:

- workers and scheduling need some setup
- auth and permissions are manual if needed later

## Option B: Heavier Research Platform

```text
Vite frontend
  -> API service
  -> PostgreSQL + pgvector
  -> Redis
  -> MinIO
  -> Temporal / workflow engine
  -> OpenSearch
```

Pros:

- robust pipeline orchestration
- strong observability and retries
- better for many automated jobs

Cons:

- too heavy before the core research loop is proven
- more local operations burden

## Option C: Appwrite

Pros:

- fast CRUD
- built-in auth and storage
- familiar from the previous project

Cons:

- less natural for investment research data modeling
- less control over background agent workflows
- weaker fit for vector retrieval and audit-heavy pipelines
- would carry company-project assumptions into a personal project

## Proposed Decision

Start with Option A:

```text
PostgreSQL + pgvector + MinIO + Redis + API + Python workers
```

Do not implement the backend until the PRD research loop is agreed. The first schema should be derived from product objects, not from the old Appwrite tables.
