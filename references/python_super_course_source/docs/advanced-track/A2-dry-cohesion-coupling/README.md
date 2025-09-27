# A2 DRY, Cohesion & Coupling, Clean Structure [Core]

Duration: 3–4h
P: A1

## Goal
Refactor for clarity and reuse using DRY while maintaining high cohesion and low coupling.

## Topics
- DRY vs premature abstraction; single responsibility
- Module boundaries; function extraction; naming; docstrings
- Dependency seams; adapters; small interfaces; internal APIs

## Before you start (preflight)
- Tests green from A1
- IDE ready with rename symbol and refactor tools

## Outcomes
- Identify duplication and refactor safely
- Explain design trade-offs between reuse and simplicity
- Improve cohesion and reduce coupling across modules

## Build (hands-on)
- Select a feature with duplication and:
  - Extract functions/classes; introduce a small internal API
  - Add an adapter for an external dependency
  - Update docstrings and module-level docs
- Keep tests passing at each step; commit small, focused changes

## Acceptance (CI-verifiable)
- Tests pass; no coverage regression
- Duplication reduced (document before/after in PR description)
- Public API remains stable (or changes are versioned)

## Quick win
Extract a parameter object to clarify a long parameter list.

## Common pitfalls
- Abstracting too early; prefer duplication until you see the pattern
- Cross-module imports that increase coupling

## Reflection
Where did you draw the line between helpful abstraction and overengineering?

## References
- Refactoring catalogs (extract function/class, introduce parameter object)
