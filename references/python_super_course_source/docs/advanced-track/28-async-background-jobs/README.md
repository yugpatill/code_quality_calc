# 28 Async & Background Jobs [Recommended]

Duration: 3–4h
P: B4, C8

## Goal
Run async I/O correctly in your service and offload work safely to background jobs.

## Topics
- asyncio fundamentals; async/await patterns in FastAPI
- Background tasks in FastAPI; worker queues (Celery/RQ/Arq)
- Scheduled jobs (APScheduler); retries with backoff; idempotency
- Backpressure and rate limiting; graceful shutdown of workers

## Before you start (preflight)
- App runs locally; one route suitable for async I/O
- Optional: Redis or RabbitMQ available for queueing (docker-compose)

## Outcomes
- Implement at least one async endpoint and one background job
- Schedule a recurring job safely with logging/metrics
- Ensure idempotency and timeouts to avoid duplication/hangs

## Build (hands-on)
- Convert a blocking endpoint to async where appropriate (e.g., HTTP or DB I/O)
- Add a background task triggered by an API call (queue worker)
- Add one scheduled job (e.g., cleanup) with APScheduler or equivalent
- Implement retry with jitter and idempotency keys for the background task

## Acceptance (CI-verifiable)
- Tests cover async endpoint and worker logic (use pytest-asyncio)
- Timeouts and retries verified; idempotent behavior proven by tests
- Worker shutdown handled gracefully (no orphan tasks)

## Quick win
Move a slow email/send call to a background job to reduce request latency.

## Common pitfalls
- Doing CPU-bound work in async tasks (use a process pool instead)
- Forgetting to await async calls or mixing sync/async DB libraries

## Reflection
How did you enforce idempotency to avoid duplicate side effects?

## References
- FastAPI background tasks; Celery/RQ/Arq docs; APScheduler
