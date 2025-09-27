# 29 Types & Static Analysis at Scale [Core]

Duration: 2–3h
P: A2, E12 (beneficial)

## Goal
Use modern typing to enable safe refactoring and reliability.

## Topics
- typing.Annotated, Protocols, TypedDict; generics
- mypy/pyright configuration and strictness levels
- Interplay with pydantic v2; runtime vs static validation boundaries

## Before you start (preflight)
- mypy/pyright available in the environment
- Tests green

## Outcomes
- Add types to a module and enable strict checks in CI
- Use Protocols to decouple implementations
- Balance runtime validation with static typing

## Build (hands-on)
- Add typing to a core module (or API layer):
  - Introduce Protocols for dependencies
  - Add TypedDict/Annotated where helpful
  - Configure mypy/pyright in CI; fix findings

## Acceptance (CI-verifiable)
- mypy/pyright passes (document chosen strictness)
- Tests still green
- Coverage unchanged or improved

## Quick win
Turn a duck-typed dependency into a Protocol and watch refactors get easier.

## Common pitfalls
- Over-constraining types where flexibility is needed
- Forgetting to type public interfaces first

## Reflection
What refactor became safer thanks to types? Cite the Protocol that enabled it.

## References
- typing and mypy docs; pyright docs
