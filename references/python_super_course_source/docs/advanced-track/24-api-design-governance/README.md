# 24 API Design & Governance [Core]

Duration: 3–4h
P: C8

## Goal
Deliver consistent, evolvable APIs with excellent DX.

## Topics
- Versioning (semantic vs URI/header-based)
- Pagination, filtering, sorting
- Error envelopes (Problem+JSON) and idempotency keys
- OpenAPI style guide; linting (Spectral)
- Client SDK generation and deprecation policies

## Before you start (preflight)
- FastAPI project running locally; OpenAPI generated
- Spectral (or similar) installed for spec linting

## Outcomes
- Design an API spec adhering to a style guide
- Enforce conventions via spec linting in CI
- Generate a client SDK and validate a smoke test

## Build (hands-on)
- Write/adjust OpenAPI to match conventions
- Add spectral ruleset and CI job for linting
- Generate a client SDK (e.g., openapi-generator) and write a smoke test

## Acceptance (CI-verifiable)
- Spec lint passes; errors/warnings addressed
- Client SDK compiles (or installs) and smoke test runs
- Versioning strategy documented (README/ADR)

## Quick win
Adopt Problem+JSON and ensure every error path returns a consistent shape.

## Common pitfalls
- Inconsistent pagination parameters across endpoints
- Drifting from the spec as code evolves (keep CI as guardrail)

## Reflection
What trade-off did you choose for versioning and why?

## References
- OpenAPI specification; Problem+JSON RFC7807
