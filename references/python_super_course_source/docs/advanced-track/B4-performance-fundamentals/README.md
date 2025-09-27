# B4 Python Performance Fundamentals [Core]

Duration: 3–4h
P: B3

## Goal
Measure, don’t guess—profile and optimize where it matters.

## Topics
- Algorithmic complexity and data structure choices
- CPU profiling (cProfile), wall‑clock timing (`time.perf_counter`)
- Line profiling (line_profiler) and memory profiling (optional)
- Vectorization basics and set/dict membership trade‑offs
- Warm‑ups, variance, and microbenchmark pitfalls

## Before you start (preflight)
- cProfile available; optional: line_profiler, memory_profiler
- A function or endpoint suspected to be slow

## Outcomes
- Profile to identify hotspots, not assumptions
- Apply targeted optimizations and demonstrate measured gains
- Document performance budgets and results

## Build (hands-on)
- Profile a slow routine or endpoint; capture top hotspots
- Implement two optimizations (e.g., data structure change, algorithmic improvement)
- Re‑measure and record before/after metrics with a simple benchmark harness

## Acceptance (CI-verifiable)
- Include a benchmark script; CI captures and stores summary numbers (non‑gating)
- Document ≥ 20% improvement in the selected hotspot (or justify limitations)
- All tests green; no regressions in correctness

## Quick win
Replace `list` membership checks with `set` for O(1) average lookup.

## Common pitfalls
- Overfitting to microbenchmarks that don’t reflect real workloads
- Trading readability for negligible speedups

## Reflection
Which optimization delivered the most value per line changed?

## References
- Python docs: time; cProfile; line_profiler
