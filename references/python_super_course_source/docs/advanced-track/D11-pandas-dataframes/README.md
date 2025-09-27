# D11 Productive DataFrames with pandas [Recommended]

Duration: 3–4h
P: D10

## Goal
Apply vectorized patterns for analytics and ETL.

## Topics
- Series/DataFrame basics; indexing; filtering
- Joins/merge; groupby/agg; time series; IO
- Performance pitfalls; method chaining; testing pandas code

## Before you start (preflight)
- pandas installed; small CSV fixture present

## Outcomes
- Implement a small analysis/ETL pipeline with tests
- Avoid common performance and correctness pitfalls
- Keep transformations readable and reproducible

## Build (hands-on)
- Ingest CSV → transform → aggregate → export
- Use method chaining; avoid loops over rows
- Write tests for key transformations using small fixtures

## Acceptance (CI-verifiable)
- Tests assert expected aggregations and schema
- No chained assignment warnings; no row‑by‑row loops
- Simple perf check (pipeline runs under X seconds on sample)

## Quick win
Replace a Python loop with vectorized pandas operations.

## Common pitfalls
- Mutating views unintentionally (chained assignment)
- Mixed dtypes causing unexpected behaviors

## Reflection
Which transformation became drastically simpler with method chaining?

## References
- pandas user guide; testing pandas code best practices
