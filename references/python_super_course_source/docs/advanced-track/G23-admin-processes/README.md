# G23 Admin Processes [Core]

Duration: 2–3h
P: C7, C8

## Goal
Run one-off admin tasks in the same environment and codebase as the app.

## Topics
- Management commands (Click/argparse)
- Migrations, batch jobs, operational runbooks
- Safety checks and dry-run modes

## Before you start (preflight)
- App can be invoked as a module; CLI tooling available

## Outcomes
- Add and run admin commands safely alongside the app
- Document and test one-off operational tasks
- Provide dry-run safeguards

## Build (hands-on)
- Add a manage CLI with subcommands for migrations/seed tasks
- Implement a dry-run flag and safety prompts
- Write tests for at least one admin task

## Acceptance (CI-verifiable)
- CLI help lists commands with clear descriptions
- Tests pass for the admin task
- Docs include a short operational runbook

## Quick win
Add a seed command to generate realistic dev data.

## Common pitfalls
- Running destructive tasks without confirmation or backups
- Environment-specific hacks that break in CI

## Reflection
Which safety check would have prevented a real incident?

## References
- Click/argparse docs; operational runbook templates
