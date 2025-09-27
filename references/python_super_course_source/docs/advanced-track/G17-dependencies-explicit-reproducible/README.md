# G17 Dependencies: Explicit & Reproducible [Core]

Duration: 2–3h
P: C7

## Goal
Ensure explicit, isolatable dependencies and reproducible installs.

## Topics
- pyproject constraints; version pins and markers
- Lockfiles and hashes (e.g., pip-tools/uv/poetry); SBOM basics
- Minimal dependency surface; pre-commit for hygiene

## Before you start (preflight)
- pyproject.toml present; CI builds artifact

## Outcomes
- Produce a locked, hashed dependency set
- Rebuild the environment cleanly in CI and locally
- Document dependency policy and update cadence

## Build (hands-on)
- Add or generate a lockfile with hashes (tool of choice)
- Add pre-commit hooks (format, lint, security scan)
- Document rebuild steps and verify in CI job logs

## Acceptance (CI-verifiable)
- Lockfile present and used in CI
- Security scan passes (pip-audit or similar)
- Rebuild logs show deterministic versions

## Quick win
Pin transitive dependencies for critical libs to avoid surprise breaks.

## Common pitfalls
- Wide version ranges that mask incompatibilities
- Unpinned dev tools causing flaky CI

## Reflection
What’s your policy for dependency updates and why?

## References
- PyPA packaging guides; pip-tools/uv/poetry docs
