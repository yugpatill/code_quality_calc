# D10 Data Formats: CSV, JSON, YAML, Serialization [Core]

Duration: 2–3h
P: B3, B5

## Goal
Read, validate, transform, and persist common data formats.

## Topics
- csv/json/yaml stdlib; safe YAML loaders
- Schema with Pydantic; datetime/timezone handling; encoding
- Streaming I/O; error reporting and user‑friendly messages

## Before you start (preflight)
- Sample CSV/JSON fixtures available

## Outcomes
- Build robust import/export with validation and clear errors
- Handle timezones and encodings correctly
- Stream large data safely

## Build (hands-on)
- Implement a data import/export toolkit:
  - Parse CSV/JSON into typed models (Pydantic)
  - Validate and report helpful errors
  - Export transformed data; support streaming for large files

## Acceptance (CI-verifiable)
- Round‑trip tests (import → transform → export)
- Invalid input yields actionable error messages
- Streaming path covered by a smoke test

## Quick win
Use `csv.DictReader` and model validation to avoid index‑based errors.

## Common pitfalls
- Naive datetime handling; always be explicit about timezones
- Loading entire files when a stream will do

## Reflection
What validation saved the most debugging time for bad inputs?

## References
- csv/json/yaml docs; Pydantic schema validation
