# C8 Web APIs with FastAPI & Pydantic [Core]

Duration: 4–5h
P: C6, C7

## Goal
Design robust APIs with validation and great developer experience.

## Topics
- FastAPI routing; dependency injection
- Request/response models; Pydantic validation/serialization
- Error handlers; OpenAPI; testing with pytest; async basics

## Before you start (preflight)
- FastAPI and pydantic installed; uvicorn available
- Test framework ready (pytest) and sample tests run

## Outcomes
- Implement a small REST API with validated I/O and tests
- Provide a clean developer experience via OpenAPI
- Structure code for easier refactoring

## Build (hands-on)
- Implement CRUD for a simple resource with:
  - Pydantic models (request/response)
  - Dependency-injected service layer
  - Error handler returning Problem+JSON style responses
  - Tests (happy path + error cases)

## Acceptance (CI-verifiable)
- pytest passes; coverage >= 80%
- OpenAPI schema validates and documents all routes
- Error responses conform to your error envelope

## Quick win
Add a validation rule to a Pydantic model and watch FastAPI enforce it automatically.

## Common pitfalls
- Returning internal exceptions directly (leakage)
- Mixing data access in route handlers (skip the service seam)

## Reflection
What boundary did you create to keep route handlers simple?

## References
- FastAPI docs, Pydantic v2 docs
