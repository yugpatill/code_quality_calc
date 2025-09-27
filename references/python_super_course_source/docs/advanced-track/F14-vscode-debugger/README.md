# F14 VS Code Debugger: Stepping & Watches [Core]

Duration: 2–3h
P: A1

## Goal
Debug confidently in local and test scenarios.

## Topics
- launch.json configurations; program vs module; env vars
- Breakpoints: standard, conditional, hit count, logpoints
- Step in/over/out; call stack; variables; watches
- Debugging tests; attaching to a running process; async/subprocess debugging

## Before you start (preflight)
- VS Code with Python extension installed
- A failing test or repro case identified

## Outcomes
- Create a launch.json suited to your project
- Use conditional breakpoints and watches to isolate issues
- Debug tests and async code paths

## Build (hands-on)
- Add a launch.json with two configs: run app, debug tests
- Set a conditional breakpoint and a logpoint on a failing path
- Use watches to observe a variable across frames; fix the issue

## Acceptance (CI-verifiable)
- Documented debug steps in module README (screenshots optional)
- A reproducible failing test is fixed via debugging
- launch.json checked in and referenced from root README/docs

## Quick win
Use a logpoint to print state without pausing execution.

## Common pitfalls
- Breakpoints not hit due to misaligned working directory
- Launching a module incorrectly; prefer `${workspaceFolder}` and module mode when needed

## Reflection
What signal (watch/logpoint/stack) led you to the root cause?

## References
- VS Code Python debugging docs
