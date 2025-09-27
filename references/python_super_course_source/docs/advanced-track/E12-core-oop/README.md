# E12 Core OOP in Python (composition‑first) [Core]

Duration: 3–4h
P: A2

## Goal
Use OOP idiomatically in Python without overengineering.

## Topics
- Classes/instances; dataclasses and value objects
- Dunder methods; rich comparisons; immutability where helpful
- Composition over inheritance; ABCs; protocols; DI basics

## Before you start (preflight)
- Tests green; ready to refactor a small feature

## Outcomes
- Model a problem with clean boundaries and testable objects
- Prefer composition and small interfaces
- Use dataclasses and protocols effectively

## Build (hands-on)
- Refactor a feature:
  - Introduce value objects (dataclasses) and a small service layer
  - Define protocols for dependencies; inject implementations in tests
  - Keep constructors light; enforce invariants

## Acceptance (CI-verifiable)
- Tests pass; public behavior preserved (or versioned)
- No global state; explicit dependencies via constructor or provider
- Docstrings explain responsibilities and boundaries

## Quick win
Turn a loose dict into a typed dataclass with validation at construction.

## Common pitfalls
- Deep inheritance hierarchies; prefer composition
- Constructors doing heavy work or I/O

## Reflection
Which object boundary made unit testing easier?

## References
- dataclasses; abc & typing.Protocol
