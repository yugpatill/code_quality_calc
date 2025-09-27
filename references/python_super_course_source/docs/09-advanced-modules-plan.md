# Advanced Python Modules Plan

This plan proposes the next set of units to take students from solid fundamentals to professional-level software engineering with Python. It’s organized into coherent tracks with clear prerequisites, learning outcomes, and hands-on deliverables. Each module is scoped as a 2–6 hour unit, suitable for class sessions or self-paced study.

Legend
- P: Prerequisites (module numbers)
- Outcomes: Concrete skills students can demonstrate at the end
- Build: Suggested hands-on artifact or micro-project that compounds across modules

### Guiding frameworks

- Refactoring perspective: We frame refactoring and patterns using broadly known pattern families (creational, structural, behavioral) and a practical catalog of safe refactorings (extract function, extract class, introduce parameter object, replace conditional with polymorphism, etc.). This informs modules E12/E13 and new G15–G16.
- Twelve-Factor App: We intentionally cover all twelve factors across existing and new modules (notably C7, C8, C9 and G17–G23). See the crosswalk below to map factors to modules and deliverables.

## Track A — Software Craftsmanship & Robustness

1) Defensive Programming, Errors, and Contracts (EAFP vs LBYL)
- Goal: Write resilient code that fails fast, communicates intent, and recovers gracefully.
- Topics: EAFP vs LBYL; invariants; assertions; guard clauses; exceptions hierarchy; custom exceptions; error boundaries; fail-fast; design by contract (pre-/post-conditions); sentinel values vs exceptions; logging basics.
- P: Prior testing foundations (earlier units)
- Outcomes: Students can choose EAFP or LBYL appropriately and implement clear error handling with actionable messages.
- Build: Harden an existing module (e.g., calculator ops, config loader) with contracts, explicit exceptions, and tests for error paths.

2) DRY, Cohesion & Coupling, and Clean Python Structure
- Goal: Refactor for clarity and reuse using DRY while maintaining high cohesion and low coupling.
- Topics: DRY vs premature abstraction; single responsibility; module boundaries; function extraction; naming; docstrings; dependency seams; adapters; small interfaces; internal APIs.
- P: (1)
- Outcomes: Students can identify duplication, refactor safely, and explain design trade-offs.
- Build: Refactor a feature into reusable modules with updated tests and internal docs.

## Track B — Language Internals & Performance

3) Iterators, Generators, and Lazy Evaluation
- Goal: Use Python’s iterator protocol for memory-efficient, composable pipelines.
- Topics: iterator protocol; yield; generator functions/expressions; itertools; context managers; lazy evaluation; backpressure; common pitfalls.
- P: (1)
- Outcomes: Students can replace eager loops with generators and reason about memory/performance.
- Build: Streaming data pipeline (e.g., read large CSV lazily, filter/transform, write out).

4) Python Performance Fundamentals
- Goal: Measure, not guess—profile and optimize where it matters.
- Topics: algorithmic complexity; cProfile; time/perf counters; line_profiler; memory profiling; data structures; vectorization (NumPy optional); GIL model; concurrency choices (threads vs processes vs asyncio) at a high level.
- P: (3)
- Outcomes: Students can profile a program, identify hotspots, and apply targeted fixes with measured gains.
- Build: Profile a slow routine; implement two optimizations; show before/after metrics.

5) Regular Expressions and Text Processing
- Goal: Parse and transform text safely and efficiently.
- Topics: Python re module; common patterns; groups; flags; compiled regex; performance and catastrophic backtracking; when to prefer parsers over regex; escaping; validation vs extraction.
- P: (1)
- Outcomes: Students can write maintainable regex and know when not to use it.
- Build: Log parser or data validator with tests and performance guardrails.

## Track C — Packaging, Libraries, and Services

6) Working with Third-Party Libraries
- Goal: Discover, evaluate, and integrate libraries responsibly.
- Topics: reading docs; semantic versioning; constraints; virtual environments; minimal APIs; avoiding tight coupling; adapter pattern for libraries; handling deprecations; basic security scanning.
- P: (2)
- Outcomes: Students can select a library, wrap it behind an internal interface, and write contract tests.
- Build: Integrate a library (e.g., requests/httpx or rich/typer) behind an adapter with tests.

7) Creating and Publishing Python Packages (Modern pyproject)
- Goal: Ship reusable, versioned libraries with CI-quality gates.
- Topics: pyproject.toml; build backends; project metadata; entry points/CLIs; versioning strategy; README/docs; test matrix; wheels vs sdists; publishing workflows.
- P: (2, 6)
- Outcomes: Students can package and publish to a private index or TestPyPI with automation.
- Build: Factor a core module into a package; publish to TestPyPI with release notes.

8) Building Web APIs with FastAPI and Pydantic
- Goal: Design robust APIs with validation and great DX.
- Topics: FastAPI routing; dependency injection; request/response models; Pydantic validation and serialization; error handlers; OpenAPI; testing with pytest; async basics.
- P: (1, 3, 5), ideally (7)
- Outcomes: Students can implement a small REST API with validated I/O and tests.
- Build: CRUD-style microservice with one or two resources and CI tests.

9) Configuration and Environment Variables (12-Factor)
- Goal: Externalize configuration cleanly and securely.
- Topics: env vars; .env and dotenv; config precedence; pydantic BaseSettings; secrets handling; environment-specific configs; safe defaults; feature flags.
- P: (1), pairs well with (8)
- Outcomes: Students can design a configuration layer that’s testable and environment-aware.
- Build: Central config module for app/service with tests and docs.

## Track D — Data Workflows & Formats

10) Data Formats: CSV, JSON, YAML, and Serialization
- Goal: Read, validate, transform, and persist common data formats.
- Topics: csv/json/yaml stdlib and safe loaders; schema with Pydantic; datetime/timezone handling; encoding; streaming I/O; error reporting.
- P: (3, 5)
- Outcomes: Students can build robust import/export paths with validation and clear errors.
- Build: Data import/export toolkit supporting CSV and JSON with schema validation.

11) Productive DataFrames with pandas
- Goal: Apply vectorized patterns for analytics and ETL.
- Topics: Series/DataFrame basics; indexing; joins/merge; groupby/agg; time series; IO; performance pitfalls; method chaining; testing pandas code.
- P: (10)
- Outcomes: Students can implement a small analysis/ETL pipeline with tests and performance checks.
- Build: Mini ETL: ingest CSV->transform->aggregate->export, with performance budget.

## Track E — Object-Oriented Design & Patterns

12) Core OOP in Python (Composition-first)
- Goal: Use OOP idiomatically in Python without overengineering.
- Topics: classes/instances; dataclasses; dunder methods; composition vs inheritance; ABCs; protocols; dependency injection basics; test seams; value vs entity objects.
- P: (2)
- Outcomes: Students can model a problem with clean boundaries and testable objects.
- Build: Refactor a feature to use value objects and a small service layer.

13) Design Patterns, Pythonically
- Goal: Apply common patterns with simple, readable Python.
- Topics: Strategy, Factory, Adapter, Observer, Template Method; dependency injection; anti-patterns; choosing patterns based on forces.
- P: (12)
- Outcomes: Students can recognize forces, choose patterns intentionally, and refactor to them.
- Build: Implement 2–3 patterns in a cohesive mini feature with tests.

## Track F — Tooling & Debugging Mastery

14) VS Code Debugger: Stepping, Watches, and Beyond
- Goal: Debug confidently in local and test scenarios.
- Topics: launch configurations; breakpoints (conditional, logpoints); step in/over/out; watches; call stack; debugging tests; attach to running process; async and subprocess debugging; remote debugging basics.
- P: (1)
- Outcomes: Students can create a launch.json, debug failing tests, and use watches to isolate issues.
- Build: Add debug configs to the project and record a short debugging walkthrough.

---

## Track G — Refactoring & Cloud-Native (12-Factor)

15) Refactoring Fundamentals & Code Smells (inspired by classic catalogs)
- Goal: Make changes safe and incremental with tests as a guardrail.
- Topics: spotting duplication and smells; small-step refactorings (extract function/class, inline, rename, introduce parameter object, move method); characterization tests; approval tests; strangler fig for legacy code; refactor vs rewrite.
- P: (A1, A2)
- Outcomes: Students can plan and execute safe refactors with passing tests throughout.
- Build: Refactor a non-trivial module behind tests; show a sequence of small, documented refactoring commits.

16) Pattern Families Deep Dive (Creational, Structural, Behavioral)
- Goal: Apply patterns as vocabulary for communicating design trade-offs—not as ceremony.
- Topics: Strategy, Factory, Builder, Adapter, Facade, Decorator, Proxy, Observer, Template Method, Command; composition-first mindset; anti-patterns (e.g., global state); test seams; dependency injection in Python.
- P: (E12), pairs with (E13)
- Outcomes: Students can recognize forces, choose patterns judiciously, and keep implementations Pythonic and small.
- Build: Implement two alternative designs for the same requirement using different patterns, benchmark/readability compare, and test.

17) Explicit Dependencies & Reproducible Environments (12-Factor: Dependencies)
- Goal: Ensure explicit, isolatable dependencies and reproducible installs.
- Topics: pyproject constraints; lockfiles; hashes; virtual environments; platform markers; minimal viable dependency surface; SBOM basics; pre-commit hooks for hygiene.
- P: (C7)
- Outcomes: Students can create reproducible envs across dev/CI and document the dependency policy.
- Build: Produce a locked, hashed dependency set; demonstrate clean rebuild locally and in CI.

18) Build, Release, Run Lifecycle (12-Factor: Build/Release/Run, Codebase)
- Goal: Separate build artifacts from configuration; promote immutable builds.
- Topics: build artifacts (wheels, containers); release metadata; environment injection at deploy; feature flags; semantic versioning; provenance.
- P: (C7, C9)
- Outcomes: Students can produce immutable artifacts and promote them across environments without rebuilds.
- Build: CI workflow that builds once, stores an artifact/image, and injects env at deploy time.

19) Processes, Concurrency, and Disposability (12-Factor: Processes, Concurrency, Disposability)
- Goal: Design stateless, disposable processes with graceful startup/shutdown.
- Topics: stateless app processes; concurrency models (threads/processes/asyncio) trade-offs; readiness/liveness probes; timeouts; signal handling; idempotency for retries.
- P: (B4), pairs with (C8)
- Outcomes: Students can implement graceful shutdown and horizontal concurrency safely.
- Build: Add health endpoints and signal-safe shutdown to the service; demonstrate scale-out.

20) Port Binding & Backing Services (12-Factor: Port Binding, Backing Services)
- Goal: Treat databases, caches, and brokers as attached resources configured by URL.
- Topics: service URLs/DSNs; FastAPI port binding; connection pooling; local dev via docker-compose; secret management integration; retries/backoff.
- P: (C8, C9)
- Outcomes: Students can attach/detach services without code changes.
- Build: Wire a Postgres (or SQLite->Postgres) backing service via env DSN with migrations.

21) Dev/Prod Parity (12-Factor: Dev/Prod Parity)
- Goal: Keep dev/test/stage/prod as similar as practical to reduce drift.
- Topics: containerized dev env; devcontainers; compose profiles; seed vs fixture data; migration strategies; timezones/localization parity.
- P: (17, 18, 20)
- Outcomes: Students can run near-identical workflows locally and in CI.
- Build: Devcontainer or compose-based dev setup mirroring production service graph.

22) Logs as Event Streams (12-Factor: Logs)
- Goal: Emit structured logs to stdout/stderr for aggregation.
- Topics: structured logging; correlation IDs; sampling; log levels/policies; OpenTelemetry basics; exporting to aggregators.
- P: (C8)
- Outcomes: Students can switch from arbitrary prints to structured, stream-friendly logs.
- Build: Add structured logs with correlation through one request path; verify in tests.

23) Admin Processes (12-Factor: Admin Processes)
- Goal: Run one-off admin tasks in the same environment and codebase as the app.
- Topics: management commands; Click/argparse CLIs; migrations; batch jobs; operational runbooks.
- P: (C7, C8)
- Outcomes: Students can add and run administrative commands safely alongside the app.
- Build: Add a manage CLI for data migrations/seed tasks with tests and docs.

## Twelve-Factor App Crosswalk

- I. Codebase → (C7, 18): Single codebase; versioned releases; immutable builds
- II. Dependencies → (17, C7): Explicit, isolated dependencies; reproducible installs
- III. Config → (C9): Config in environment, not in code
- IV. Backing services → (20): Treat services as attached resources via URLs/DSNs
- V. Build, release, run → (18): Strict separation; promote artifacts across envs
- VI. Processes → (19): Stateless processes, share-nothing design
- VII. Port binding → (20, C8): Export services via port binding
- VIII. Concurrency → (19, B4): Scale out via process model; choose concurrency model intentionally
- IX. Disposability → (19): Fast startup/shutdown; graceful signal handling
- X. Dev/prod parity → (21): Keep gaps small across time, personnel, and environment
- XI. Logs → (22): Treat logs as event streams
- XII. Admin processes → (23): One-off admin tasks run as processes in the same environment

## Suggested Sequencing (with Dependencies)
- A1 → A2 → B3 → B4 → B5 → C6 → C7 → C8 → C9 → G17 → G18 → G19 → G20 → G21 → G22 → G23 → D10 → D11 → E12 → E13 → F14
- Flexible swaps:
  - B5 (Regex) can precede B4 (Performance) if the course prefers text-first focus.
  - C8 (FastAPI) can precede C7 (Packaging) for a service-first track; packaging then formalizes reuse.
  - G17–G23 (12-Factor) can be interleaved while building the service in C8/C9.
  - D11 (pandas) can be moved earlier for a data-focused cohort after D10.

---

## Additional Advanced Modules (Professional Depth)

24) API Design & Governance (beyond code)
- Goal: Deliver consistent, evolvable APIs with excellent DX.
- Topics: versioning (semantic vs URI/header-based); pagination and filtering; error envelopes and problem+json; idempotency keys; OpenAPI style guides; client SDK generation; deprecation policies.
- P: (C8)
- Outcomes: Students design and validate an API spec, then enforce conventions in tests.
- Build: Governance checklist + spectral/lint rules on OpenAPI; example SDK generation.

25) Observability: Metrics & Traces
- Goal: See what the system does in production in real time.
- Topics: Prometheus metrics (counters, gauges, histograms); OpenTelemetry traces; spans and context propagation; RED/USE signals; linking logs, metrics, traces.
- P: (G22), pairs with (C8)
- Outcomes: Students instrument endpoints with metrics/traces and validate in tests.
- Build: Add metrics/traces to service; export locally (Prometheus/Tempo/Jaeger) via docker-compose.

26) Security for Python APIs
- Goal: Build secure-by-default services.
- Topics: OAuth2/OIDC flows; JWT validation; CSRF vs CORS; security headers; rate limiting; SSRF and SQL injection mitigations; dependency scanning (pip-audit); SAST/DAST pipeline; secret rotation.
- P: (C8, C9, G17)
- Outcomes: Students add authn/z, safe defaults, and security checks to CI.
- Build: Secure a couple endpoints; add pip-audit/CodeQL jobs and rate limiting.

27) SQL & ORMs with Migrations
- Goal: Model data with correctness and performance in mind.
- Topics: SQLAlchemy/SQLModel basics; Alembic migrations; transactions; indexing; connection pooling; N+1 detection; testing with temporary databases.
- P: (G20)
- Outcomes: Students model and migrate a schema, avoiding common pitfalls.
- Build: Introduce a relational backing service with migrations and integration tests.

28) Async & Background Jobs
- Goal: Run async I/O correctly and offload work safely.
- Topics: asyncio fundamentals; async FastAPI patterns; queues (Celery/RQ/Arq) and retries with idempotency; scheduled jobs (APScheduler); backpressure.
- P: (B4, C8)
- Outcomes: Students implement background tasks and scheduled jobs with safe retries.
- Build: One async endpoint + one queued job + one scheduled job with tests.

29) Types & Static Analysis at Scale
- Goal: Use types to enable refactoring and reliability.
- Topics: typing.Annotated, Protocols, TypedDict; mypy/pyright config; pydantic v2 type interplay; runtime vs static validation boundaries.
- P: (E12)
- Outcomes: Students add typing to a module and turn on strict checks in CI.
- Build: Raise type coverage; adopt protocols to decouple implementations.

30) Resilience Patterns
- Goal: Survive failures gracefully.
- Topics: retries with exponential backoff and jitter (tenacity); circuit breaker; timeouts; bulkheads; fallback strategies; chaos probes.
- P: (G19, G20)
- Outcomes: Students design failure modes and verify via tests.
- Build: Add retry/circuit-breaker around a flaky backing service and test it.

31) Documentation & Developer Experience
- Goal: Make the project easy to consume, maintain, and contribute to.
- Topics: Sphinx/MkDocs; mkdocstrings; docstring conventions; changelog automation (Keep a Changelog); ADRs; contribution guidelines; CLI help UX.
- P: (C7, 24)
- Outcomes: Students produce a browsable docs site and contribution workflow.
- Build: MkDocs site with API reference, tutorials, and ADRs; publish in CI.

32) Data Formats Deep Dive
- Goal: Handle large and evolving data safely.
- Topics: Arrow/Parquet; Avro/Protobuf; schema evolution; compression; streaming large files; pickling risks.
- P: (D10)
- Outcomes: Students choose proper formats and manage schema evolution.
- Build: Convert CSV pipeline to Parquet with schema validation.

33) Advanced Performance (optional)
- Goal: Go beyond profiling basics when needed.
- Topics: caching (functools/Redis); Numba/Cython; PyPy trade-offs; microbenchmark pitfalls; perf budgets.
- P: (B4)
- Outcomes: Students apply one advanced technique and measure impact.
- Build: Add a cache layer or compiled hot path with before/after benchmarks.

34) Cloud & Kubernetes Fundamentals (optional)
- Goal: Operate services on a modern platform.
- Topics: container registries; IaC (Terraform basics); Kubernetes Deployments/Services/Ingress; Secrets; GitOps; progressive delivery.
- P: (G18–G21)
- Outcomes: Students deploy a service to a local or managed Kubernetes cluster.
- Build: Minimal k8s manifests + GitOps-style rollout.

### Extended Sequencing (including 24–34)
- … C8 → C9 → G17 → G18 → G19 → G20 → G21 → G22 → G23 → 24 → 25 → 26 → 27 → 28 → 29 → 30 → 31 → 32 → D11 → E12 → E13 → F14 → [33, 34 optional]

## Capstone Direction (Optional)
- Service Track: Turn the calculator into a FastAPI microservice with Pydantic models, config layer, profiling, and packaging.
- Data Track: Build an ETL + analytics pipeline using generators, regex parsing, CSV/JSON, and pandas, with profiling and packaging.

## Assessment & Excellence Criteria
- Each module includes:
  - Tests for happy paths and edge/error cases
  - Measured performance baselines where relevant
  - Clear documentation (docstrings/README) and internal API boundaries
  - Idiomatic, maintainable Python with DRY and high cohesion
  - Thoughtful use of exceptions, validation, and configuration

This plan is designed to be modular: adopt tracks wholesale or insert individual modules into your existing progression. Ready for feedback and iteration.