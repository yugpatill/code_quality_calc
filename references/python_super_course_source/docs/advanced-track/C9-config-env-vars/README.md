# C9 Configuration & Environment Variables (12‑Factor) [Core]

Duration: 2–3h
P: C8 (recommended), A1

## Goal
Externalize configuration cleanly and securely.

## Topics
- Environment variables; .env and python‑dotenv
- Pydantic BaseSettings; precedence and safe defaults
- Secrets handling and environment‑specific configs

## Before you start (preflight)
- Identify config values used by your app (DSNs, secrets, toggles)

## Outcomes
- Central configuration module that’s testable and environment‑aware
- No secrets in code or repo; clear precedence rules
- Helpful errors when config is missing or invalid

## Build (hands-on)
- Implement a BaseSettings config with env var overrides
- Add .env for dev and document loading in local runs only
- Write tests verifying precedence, defaults, and validation

## Acceptance (CI-verifiable)
- Tests pass; no secrets detected in repo (basic grep or pre‑commit hook)
- Config values loaded via env; missing/invalid config fails early with clear errors

## Quick win
Adopt .env for local dev while keeping CI and prod purely env‑driven.

## Common pitfalls
- Hiding missing config with broad defaults
- Loading .env in production by mistake

## Reflection
Which config did you validate up front to prevent a runtime surprise?

## References
- Pydantic BaseSettings; Twelve‑Factor Config
