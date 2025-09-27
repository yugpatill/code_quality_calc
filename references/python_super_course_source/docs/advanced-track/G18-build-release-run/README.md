# G18 Build/Release/Run Lifecycle [Core]

Duration: 3–4h
P: C7, C9

## Goal
Separate build artifacts from configuration; promote immutable builds.

## Topics
- Build artifacts (wheels, containers); release metadata
- Environment injection at deploy; feature flags; semantic versioning
- Provenance and artifact storage

## Before you start (preflight)
- CI can build artifacts; environment variables managed via CI

## Outcomes
- Produce immutable artifacts and promote them across environments
- Inject config at runtime without rebuilds
- Track releases with metadata and changelog entries

## Build (hands-on)
- Add CI jobs to build and store artifact/image
- Inject environment at run time; verify behavior differs by env
- Tag release with version and changelog

## Acceptance (CI-verifiable)
- Build job produces and stores artifact
- Deploy/run job uses the artifact without rebuilding
- Release notes generated/updated automatically

## Quick win
Add a version endpoint that reads from build metadata.

## Common pitfalls
- Rebuilding per environment; keep builds identical
- Hardcoding config into images/artifacts

## Reflection
How did you verify the same artifact runs across environments?

## References
- CI/CD provider docs; SemVer; release metadata patterns
