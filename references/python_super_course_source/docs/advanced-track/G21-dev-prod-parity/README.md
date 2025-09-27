# G21 Dev/Prod Parity [Core]

Duration: 2–3h
P: G17–G20

## Goal
Keep dev/test/stage/prod as similar as practical to reduce drift.

## Topics
- Containerized dev env; devcontainers; compose profiles
- Seed vs fixture data; migration strategies
- Timezone and locale parity

## Before you start (preflight)
- Containerized dev workflow acceptable in your environment

## Outcomes
- Run near-identical workflows locally and in CI
- Keep configuration and services consistent across envs
- Manage realistic data in non-prod safely

## Build (hands-on)
- Add a devcontainer or compose profile mirroring production services
- Seed data strategy documented and implemented for non-prod
- Verify parity by running the same commands locally and in CI

## Acceptance (CI-verifiable)
- CI and local use the same entry commands
- Parity checklist added to the repo and referenced in PR template
- Timezone/locale explicitly configured and tested

## Quick win
Use a single `make` or task runner entrypoint for all environments.

## Common pitfalls
- Hidden differences in env vars or service versions
- Drift in seed data leading to irreproducible bugs

## Reflection
Which parity improvement reduced a class of “works on my machine” issues?

## References
- devcontainers; docker-compose profiles; parity checklists
