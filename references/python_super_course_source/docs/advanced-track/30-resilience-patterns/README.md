# 30 Resilience Patterns [Core]

Duration: 3–4h
P: G19, G20

## Goal
Survive failures gracefully.

## Topics
- Retries with exponential backoff + jitter (tenacity)
- Circuit breaker, timeouts, bulkheads
- Fallback strategies; chaos probes

## Before you start (preflight)
- One route depends on a backing service
- Tests exist for the happy path

## Outcomes
- Design failure modes deliberately
- Verify behavior under partial failure via tests
- Document and justify backoff/circuit thresholds

## Build (hands-on)
- Add tenacity-based retry with jitter to a flaky outbound call
- Implement circuit breaker and timeout policy
- Add tests covering transient failure and open-circuit behavior

## Acceptance (CI-verifiable)
- Tests pass for retries, timeouts, and open-circuit scenarios
- Backoff policy documented and observable in logs/metrics
- No unbounded retries; no blocking the event loop

## Quick win
Guard a single outbound call with a timeout and see error surfaces improve.

## Common pitfalls
- Retrying non-idempotent operations
- Too-aggressive retries amplifying incidents

## Reflection
How did you ensure idempotency for the retried operation?

## References
- tenacity; Polly patterns (conceptually)
