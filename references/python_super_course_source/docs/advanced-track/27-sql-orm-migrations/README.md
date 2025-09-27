# 27 SQL & ORMs with Migrations [Core]

Duration: 3–4h
P: G20

## Goal
Model data with correctness and performance.

## Topics
- SQLAlchemy/SQLModel basics; relationships; indexing
- Alembic migrations; transactions; connection pooling
- N+1 detection; testing with temporary DBs

## Before you start (preflight)
- Database service available (SQLite/Postgres); DSN via env var
- Alembic configured (or will be during the module)

## Outcomes
- Model and migrate a schema safely
- Avoid common performance pitfalls (N+1)
- Write reliable integration tests

## Build (hands-on)
- Introduce a relational backing service (Postgres or SQLite first)
- Create models, migrations, and a repository layer
- Add integration tests using a temporary database

## Acceptance (CI-verifiable)
- Migrations run up/down cleanly
- Integration tests pass; no N+1 on a representative query
- DSN provided via environment; no credentials in code

## Quick win
Add appropriate indexes and measure the improvement.

## Common pitfalls
- Tight coupling between models and route handlers
- Long-lived sessions without proper cleanup

## Reflection
Which query did you optimize and how did you prove it?

## References
- SQLAlchemy/SQLModel docs; Alembic docs
