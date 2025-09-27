# G22 Logs as Event Streams [Core]

Duration: 2–3h
P: C8

## Goal
Emit structured logs to stdout/stderr for aggregation.

## Topics
- Structured logging; correlation IDs; log levels/policies
- OpenTelemetry logging and exporters
- Exporting to aggregators; sampling basics

## Before you start (preflight)
- Logging framework selected (structlog or stdlib logging with JSON formatter)

## Outcomes
- Replace ad hoc prints with structured, stream-friendly logs
- Propagate correlation IDs through request flows
- Avoid PII in logs; apply policies consistently

## Build (hands-on)
- Add structured logging with JSON formatter
- Inject/propagate correlation IDs across one request path
- Add log sampling where appropriate

## Acceptance (CI-verifiable)
- Tests assert presence of correlation IDs and structured fields
- Lint or CI check for PII/secret patterns in logs
- Logs go to stdout/stderr (no files) and are parseable

## Quick win
Attach a correlation ID to each request and include it in all logs.

## Common pitfalls
- Logging sensitive data
- Overusing debug logs in performance-critical paths

## Reflection
What log field most improved your ability to diagnose issues?

## References
- structlog; stdlib logging cookbook; OTel logging
