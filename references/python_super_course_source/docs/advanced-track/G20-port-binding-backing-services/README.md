# G20 Port Binding & Backing Services [Core]

Duration: 3–4h
P: C8, C9

## Goal
Treat databases, caches, and brokers as attached resources configured by URL.

## Topics
- Service URLs/DSNs; connection pooling
- Local dev via docker-compose; secret management integration
- Retries/backoff for transient failures

## Before you start (preflight)
- Chosen backing service (DB/cache/queue) available locally

## Outcomes
- Attach/detach a backing service without code changes
- Configure service via env DSN; secrets not in code
- Handle transient failures gracefully

## Build (hands-on)
- Wire a database (SQLite→Postgres path acceptable)
- Configure DSN via env; use pooling
- Add retry/backoff to initial connection logic

## Acceptance (CI-verifiable)
- Integration tests pass using DSN from env
- No secrets in repository; checks in CI
- Connection handling robust to intermittent failures

## Quick win
Start with SQLite locally, then switch to Postgres just by changing DSN.

## Common pitfalls
- Embedding credentials in config files
- Ignoring connection pooling leading to exhaustion

## Reflection
What made swapping services trivial in your codebase?

## References
- DSN conventions; Postgres pooling docs
