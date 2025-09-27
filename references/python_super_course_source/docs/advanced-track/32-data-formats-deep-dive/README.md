# 32 Data Formats Deep Dive [Recommended]

Duration: 3–4h
P: D10

## Goal
Choose the right data formats for scale and longevity, and manage schema evolution.

## Topics
- Columnar formats: Arrow/Parquet; compression (gzip, zstd)
- Binary schemas: Avro/Protobuf; forward/backward compatibility
- Schema evolution strategies; contracts and validation (pandera or Pydantic)
- Streaming large files safely; pickling risks and portability

## Before you start (preflight)
- Sample dataset (CSV/JSON) ready; optional: pyarrow, fastparquet, protobuf/avro libs installed

## Outcomes
- Convert a CSV pipeline to Parquet with compression
- Define and validate a schema; handle schema evolution
- Demonstrate a Protobuf/Avro message for a critical path

## Build (hands-on)
- Convert CSV → Parquet with compression and partitioning if relevant
- Add schema validation with pandera (or Pydantic models)
- Define a Protobuf/Avro schema; serialize/deserialize a sample record
- Document schema evolution policy and test backward compatibility

## Acceptance (CI-verifiable)
- Tests validate schema and round-trip for Parquet and Protobuf/Avro
- Performance guard: Parquet path faster/smaller than CSV on sample
- No pickled artifacts committed; lint checks forbid pickle usage in critical paths

## Quick win
Switch intermediate CSV artifacts to Parquet to cut disk and I/O dramatically.

## Common pitfalls
- Ignoring schema versioning; breaking consumers silently
- Using pickle for long-term storage or interop

## Reflection
What schema evolution rule did you set, and how will you enforce it?

## References
- Apache Arrow/Parquet; Protobuf/Avro docs; pandera
