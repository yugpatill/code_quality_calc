# G19 Processes, Concurrency, Disposability [Core]

Duration: 3–4h
P: B4, pairs with C8

## Goal
Design stateless, disposable processes with graceful startup/shutdown.

## Topics
- Stateless process model; horizontal concurrency
- Readiness/liveness probes; idempotency for retries
- Signal handling; timeouts; graceful shutdown

## Before you start (preflight)
- One endpoint or worker can be interrupted safely

## Outcomes
- Implement graceful shutdown and readiness checks
- Scale out safely with stateless design
- Ensure idempotent operations for retries

## Build (hands-on)
- Add signal handlers for SIGTERM/SIGINT
- Implement readiness/liveness endpoints
- Make one operation idempotent; verify with tests

## Acceptance (CI-verifiable)
- Tests cover shutdown behavior and idempotency
- Readiness/liveness endpoints behave per contract
- No stateful in-process caches that break restarts

## Quick win
Add a timeout to external calls to avoid hanging shutdowns.

## Common pitfalls
- Shared mutable state across workers without coordination
- Non-idempotent operations retried blindly

## Reflection
What change made the biggest difference in shutdown reliability?

## References
- Twelve-Factor: Processes, Disposability; OS signal docs
