# B5 Regular Expressions and Text Processing [Recommended]

Duration: 2–3h
P: A1

## Goal
Parse and transform text safely and efficiently.

## Topics
- `re` module: patterns, groups, named groups, flags
- Compile vs inline; pre‑compilation for hot paths
- Validation vs extraction; escaping safely (raw strings)
- Performance pitfalls and catastrophic backtracking awareness
- When to prefer structured parsers over regex

## Before you start (preflight)
- Sample log/CSV/text fixtures available

## Outcomes
- Write maintainable regex for validation and extraction
- Avoid performance traps and ambiguous patterns
- Provide clear errors when parsing fails

## Build (hands-on)
- Implement a log parser or input validator:
  - Compile patterns; use named groups
  - Cover tricky cases and invalid inputs with tests
  - Measure runtime on a larger sample (sanity perf guard)

## Acceptance (CI-verifiable)
- Tests pass for typical, edge, and invalid cases
- No catastrophic patterns (document safeguards)
- Parser returns structured, typed outputs or clear errors

## Quick win
Use named groups to make match group access self‑documenting.

## Common pitfalls
- Forgetting to escape user input
- Overusing regex where a proper CSV/JSON parser is safer

## Reflection
Where did regex help—and where did you deliberately avoid it?

## References
- Python `re` docs; Regular‑Expressions.info (concepts)
