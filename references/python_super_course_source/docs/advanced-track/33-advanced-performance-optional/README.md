# 33 Advanced Performance (Optional)

Duration: 3–4h
P: B4

## Goal
Apply advanced techniques (caching/compiled code) when profiling shows a true hotspot.

## Topics
- Caching: functools.lru_cache, Redis caching patterns
- Numba/Cython to speed numeric hotspots; PyPy trade-offs
- Microbenchmark caveats; perf budgets; correctness vs speed

## Before you start (preflight)
- A profiled hotspot identified; correctness tests in place

## Outcomes
- Apply one advanced technique to a hotspot
- Measure improvement and validate correctness remains
- Document trade-offs and maintenance impact

## Build (hands-on)
- Add an lru_cache or Redis-backed cache to a hot function
- Or compile a numeric routine with Numba/Cython
- Re-run benchmarks and record before/after metrics

## Acceptance (CI-verifiable)
- Benchmark summary artifact stored (non-gating)
- Tests ensure cached/compiled paths match baseline behavior
- Rollback plan documented if perf gain is marginal

## Quick win
Use lru_cache for deterministic pure functions to save repeated work.

## Common pitfalls
- Caching functions with side effects or non-hashable inputs
- Premature optimization adding complexity without payoff

## Reflection
What was the improvement (time/allocations), and was it worth the complexity?

## References
- functools.lru_cache; Numba/Cython docs; Redis client docs
