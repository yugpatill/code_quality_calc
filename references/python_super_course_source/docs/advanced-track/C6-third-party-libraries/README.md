# C6 Working with Third‑Party Libraries [Core]

Duration: 2–3h
P: A2

## Goal
Discover, evaluate, and integrate libraries responsibly.

## Topics
- Reading docs, semantic versioning, constraints/markers
- Minimal APIs; avoid tight coupling; adapter pattern
- Deprecation handling; basic security scanning

## Before you start (preflight)
- A feature that could benefit from a library (HTTP client, CLI, formatting)

## Outcomes
- Select and justify a library choice
- Wrap it behind an internal interface with contract tests
- Pin constraints to keep upgrades predictable

## Build (hands-on)
- Integrate a library (e.g., httpx or typer) behind an adapter
- Add contract tests for your interface; avoid leaking library types
- Add constraints and a short upgrade policy in README/ADR

## Acceptance (CI-verifiable)
- Tests pass using the adapter interface only
- Constraints/lock present; security scan added (pip‑audit)
- No direct imports of the library in core domains

## Quick win
Introduce an adapter so calling code is independent from the library API.

## Common pitfalls
- Re‑exporting library types across internal APIs
- Accepting wide version ranges without testing

## Reflection
What interface boundary did you create, and how will it ease future swaps?

## References
- SemVer; Adapter pattern references; pip‑audit
