# G16 Pattern Families Deep Dive [Recommended]

Duration: 3–4h
P: E12 (pairs with E13)

## Goal
Apply patterns as vocabulary for communicating design trade-offs—not as ceremony.

## Topics
- Creational: Factory, Builder
- Structural: Adapter, Facade, Decorator, Proxy
- Behavioral: Strategy, Observer, Template Method, Command
- Composition-first; DI in Python; anti-patterns

## Before you start (preflight)
- Feature with multiple viable designs

## Outcomes
- Recognize forces and choose patterns judiciously
- Keep implementations small and Pythonic
- Compare designs for readability and performance

## Build (hands-on)
- Implement two alternative designs for the same requirement using different patterns
- Benchmark lightly and compare readability and testability
- Document the decision with a short ADR

## Acceptance (CI-verifiable)
- Tests pass for both designs
- Benchmark summary included in PR
- ADR explains chosen pattern and rejected alternatives

## Quick win
Replace a deep import chain with a Facade to simplify call sites.

## Common pitfalls
- Pattern-for-pattern’s-sake; avoid over-engineering
- Hidden globals that defeat DI and test seams

## Reflection
Which forces (variability, isolation, lifecycle) drove your pattern choice?

## References
- Pattern references (concise), Pythonic implementations
