# G15 Refactoring Fundamentals & Code Smells [Core]

Duration: 3–4h
P: A1, A2

## Goal
Make changes safe and incremental with tests as a guardrail.

## Topics
- Code smells: duplication, long function, long parameter list, feature envy
- Small-step refactorings: extract function/class, inline, rename, introduce parameter object, move method/field
- Characterization tests; approval tests; strangler fig pattern for legacy

## Before you start (preflight)
- Identify a module needing cleanup; tests exist (or write characterization tests)

## Outcomes
- Plan and execute a series of small, safe refactors
- Keep behavior constant while improving design
- Communicate refactor intent through commits and PRs

## Build (hands-on)
- Create an issue listing target smells and chosen refactorings
- Apply refactorings in small commits; keep tests green
- Write a brief PR description detailing before/after and trade-offs

## Acceptance (CI-verifiable)
- All tests pass across the refactor series
- Public API unchanged (or changes are versioned and documented)
- PR documents the smells addressed and refactor steps

## Quick win
Extract a block into a well-named function; readability jumps immediately.

## Common pitfalls
- Large, mixed-purpose refactor commits that hide regressions
- Unintended behavior changes due to insufficient tests

## Reflection
Which refactoring provided the most clarity per line changed?

## References
- Refactoring catalogs (classic) and code smell guides
