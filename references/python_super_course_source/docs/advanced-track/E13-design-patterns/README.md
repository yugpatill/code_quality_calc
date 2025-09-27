# E13 Design Patterns, Pythonically [Recommended]

Duration: 3–4h
P: E12

## Goal
Apply common patterns with simple, readable Python.

## Topics
- Strategy, Factory, Adapter, Observer, Template Method, Command
- Dependency injection in Python; avoiding global state
- Anti‑patterns and when not to use a pattern

## Before you start (preflight)
- A feature with branching or interchangeable behaviors

## Outcomes
- Recognize forces and choose patterns intentionally
- Keep implementations small, composable, and testable
- Explain the trade‑off behind your choice

## Build (hands-on)
- Implement 2–3 patterns in a cohesive mini‑feature:
  - Replace a long if/elif chain with Strategy
  - Introduce a Factory for object creation concerns
  - Use Adapter to isolate a third‑party dependency

## Acceptance (CI-verifiable)
- Tests verify behavior across multiple strategies
- Clear boundaries; no pattern‑for‑pattern’s‑sake complexity
- Brief ADR explaining forces and outcome

## Quick win
Replace conditional branching with a strategy registry (dict of callables).

## Common pitfalls
- Over‑abstracting simple code
- Hidden coupling via singletons or module globals

## Reflection
Which pattern provided the highest clarity per line of code?

## References
- Refactoring/Patterns references; Python Cookbook patterns
