# 25 Observability: Metrics & Traces [Core]

Duration: 3–4h
P: C8, G22

## Goal
See what the system does in real time with metrics and traces.

## Topics
- Prometheus metrics: counters, gauges, histograms
- OpenTelemetry traces: spans, context propagation
- RED/USE signals; linking logs, metrics, and traces

## Before you start (preflight)
- docker-compose for Prometheus + Tempo/Jaeger (or similar) available
- App exposes /metrics (or ready to add)

## Outcomes
- Instrument endpoints with metrics and traces
- Validate signals locally and in tests
- Correlate requests across logs/metrics/traces

## Build (hands-on)
- Add metrics to key endpoints (latency, error rate)
- Instrument traces with spans and attributes
- Compose stack to scrape/export locally and verify dashboards

## Acceptance (CI-verifiable)
- Unit/integration tests assert metric presence/shape
- Tracing headers round-trip through at least one path
- Linting ensures no PII in telemetry attributes

## Quick win
Add request latency histograms and a simple alert threshold.

## Common pitfalls
- High-cardinality labels exploding metrics storage
- Tracing without propagating context

## Reflection
Which metric best reflects user experience for your service?

## References
- Prometheus docs; OpenTelemetry Python docs
