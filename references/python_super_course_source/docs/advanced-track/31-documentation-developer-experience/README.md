# 31 Documentation & Developer Experience [Core]

Duration: 2–3h
P: C7, 24

## Goal
Make the project easy to consume, maintain, and contribute to.

## Topics
- MkDocs/Sphinx; mkdocstrings; docstring conventions
- Changelog automation (Keep a Changelog); ADRs
- Contribution guidelines; CLI help UX

## Before you start (preflight)
- Docs tool chosen (MkDocs recommended)
- Project has docstrings in key modules

## Outcomes
- Publish a browsable docs site in CI
- Provide contribution guidance and changelog
- Improve CLI and API help surfaces

## Build (hands-on)
- Set up MkDocs with mkdocstrings for API reference
- Add CONTRIBUTING.md and a CHANGELOG with an initial release
- Improve CLI help and inline usage examples

## Acceptance (CI-verifiable)
- Docs build job passes and publishes site artifact
- Lint check ensures no broken internal links
- CONTRIBUTING and CHANGELOG present and referenced in README

## Quick win
Generate API reference pages automatically from docstrings.

## Common pitfalls
- Stale docs drifting from code; keep docs in CI
- Overlong pages—prefer concise, task-oriented docs

## Reflection
What piece of documentation will most help a new contributor?

## References
- MkDocs + mkdocstrings docs; Keep a Changelog
