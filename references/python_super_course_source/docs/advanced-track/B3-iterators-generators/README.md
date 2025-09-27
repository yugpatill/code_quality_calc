# B3 Iterators, Generators, Lazy Evaluation [Core]

Duration: 2–3h
P: A1

## Goal
Use Python’s iterator protocol for memory‑efficient, composable pipelines.

## Topics
- Iterator protocol (`__iter__`, `__next__`), iteration contexts
- `yield`, generator functions/expressions, generator delegation (`yield from`)
- `itertools` (chain, islice, tee, groupby, accumulate)
- Context managers for streaming I/O; lazy evaluation patterns
- Common pitfalls (exhaustion, one‑shot iterators)

## Before you start (preflight)
- Tests run locally; Python ≥ 3.10; venv active

## Outcomes
- Replace eager loops and temporary lists with generators
- Compose transformations using `itertools` safely
- Reason about memory and backpressure for large inputs

## Build (hands-on)
- Create a streaming pipeline:
  - Read a large CSV lazily (line by line)
  - Filter and transform records with generator functions
  - Write the transformed output without loading everything into memory
- Add tests for correctness on a small fixture and a lightweight scale smoke test

## Acceptance (CI-verifiable)
- Unit tests pass for happy path and an empty input case
- Pipeline does not materialize the entire dataset (no OOM in a synthetic large test)
- File handles closed via context managers

## Quick win
Swap a list comprehension used only for iteration with a generator expression.

## Common pitfalls
- Reusing an exhausted iterator unintentionally
- Copying iterators that cannot be duplicated (understand `tee` semantics)

## Reflection
Where did laziness most reduce memory footprint in your pipeline?

## References
- Python docs: Iterators, Generators; itertools how‑to
