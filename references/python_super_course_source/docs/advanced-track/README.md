# Advanced Track (Temporary Workspace)

This workspace hosts fully outlined modules for the advanced curriculum. Use this as a learner-facing index and a staging area while we integrate modules into the main docs and assignments.

Purpose
- Give learners a clear path with consistent module structure
- Provide hands-on builds and acceptance criteria per module
- Keep tracks modular so cohorts can choose Service or Data focus

Legend
- Tags: [Core] = essential, [Recommended] = high value, [Optional] = nice-to-have/advanced
- Duration: approximate focused effort per module
- P: Prerequisites by module code (e.g., A1)

How to use
- Start with the sequence below (or pick a track)
- Open each module folder’s README and follow the plan
- Commit your build artifacts to the same repo to form a cumulative capstone

## Suggested sequence (condensed)
A1 → A2 → 29 → B3 → B4 → B5 → C6 → C7 → C8 → 24 → 25 → 26 → C9 → G17 → G18 → G19 → G20 → 27 → G21 → G22 → G23 → D10 → 32 → D11 → E12 → E13 → 28 → 30 → 31 → F14 → [33, 34 optional]

## Tracks and modules

Track A — Software Craftsmanship & Robustness
- A1 Defensive Programming, Errors, and Contracts [Core]
- A2 DRY, Cohesion & Coupling, Clean Structure [Core]

Track B — Language Internals & Performance
- B3 Iterators, Generators, Lazy Evaluation [Core]
- B4 Python Performance Fundamentals [Core]
- B5 Regular Expressions and Text Processing [Recommended]

Track C — Packaging, Libraries, and Services
- C6 Working with Third-Party Libraries [Core]
- C7 Creating & Publishing Packages (pyproject) [Core]
- C8 Web APIs with FastAPI & Pydantic [Core]
- C9 Configuration & Env Vars (12-Factor) [Core]

Track D — Data Workflows & Formats
- D10 CSV, JSON, YAML, Serialization [Core]
- D11 Productive DataFrames with pandas [Recommended]

Track E — Object-Oriented Design & Patterns
- E12 Core OOP in Python (composition-first) [Core]
- E13 Design Patterns, Pythonically [Recommended]

Track F — Tooling & Debugging Mastery
- F14 VS Code Debugger: Stepping & Watches [Core]

Track G — Refactoring & Cloud-Native (12-Factor)
- G15 Refactoring Fundamentals & Code Smells [Core]
- G16 Pattern Families Deep Dive [Recommended]
- G17 Dependencies: explicit & reproducible [Core]
- G18 Build/Release/Run lifecycle [Core]
- G19 Processes, Concurrency, Disposability [Core]
- G20 Port Binding & Backing Services [Core]
- G21 Dev/Prod Parity [Core]
- G22 Logs as Event Streams [Core]
- G23 Admin Processes [Core]

Additional Advanced Modules
- 24 API Design & Governance [Core]
- 25 Observability: Metrics & Traces [Core]
- 26 Security for Python APIs [Core]
- 27 SQL & ORMs with Migrations [Core]
- 28 Async & Background Jobs [Recommended]
- 29 Types & Static Analysis at Scale [Core]
- 30 Resilience Patterns [Core]
- 31 Documentation & Developer Experience [Core]
- 32 Data Formats Deep Dive [Recommended]
- 33 Advanced Performance [Optional]
- 34 Cloud & Kubernetes Fundamentals [Optional]

Notes
- This folder is temporary; once vetted, modules will be folded into the main docs and assignments.
- Keep commits small. Use a short ADR (Architecture Decision Record) for notable design choices.
