# C7 Creating & Publishing Packages (pyproject) [Core]

Duration: 3–4h
P: C6

## Goal
Ship reusable, versioned libraries with CI quality gates.

## Topics
- pyproject.toml metadata; build backends
- Entry points/CLIs; versioning strategy; wheels vs sdists
- Test matrix; publishing workflows (TestPyPI)

## Before you start (preflight)
- Project organized as a package; tests green

## Outcomes
- Build sdist and wheel; install locally and in CI
- Publish to TestPyPI; verify install and CLI
- Document versioning and release checklist

## Build (hands-on)
- Author pyproject.toml; add console_scripts for CLI if applicable
- Configure build in CI; produce artifacts
- Publish to TestPyPI; add install smoke test job

## Acceptance (CI-verifiable)
- Build job produces sdist + wheel artifacts
- TestPyPI publish job succeeds; install smoke test passes
- Version bump + changelog entry present for release

## Quick win
Add a CLI entry point via console_scripts for instant usability.

## Common pitfalls
- Implicit namespace packages with accidental imports
- Missing runtime dependencies in project metadata

## Reflection
How does your chosen versioning strategy map to your release cadence?

## References
- PyPA packaging guides; setuptools/pondered backend docs
