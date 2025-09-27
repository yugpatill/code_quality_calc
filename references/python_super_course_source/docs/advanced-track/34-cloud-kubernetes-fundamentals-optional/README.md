# 34 Cloud & Kubernetes Fundamentals (Optional)

Duration: 4–6h
P: G18–G21

## Goal
Operate your service on a modern platform with basic Kubernetes knowledge.

## Topics
- Container registries and image promotion
- Kubernetes: Deployments, Services, Ingress, Secrets/ConfigMaps
- IaC basics (Terraform); GitOps; progressive delivery (blue/green, canary)

## Before you start (preflight)
- Container image build working; local K8s (minikube/k3d/kind) available

## Outcomes
- Deploy the service to a local K8s cluster
- Manage config via Secrets/ConfigMaps (env injection)
- Expose via Ingress and smoke test

## Build (hands-on)
- Write minimal manifests (or Kustomize) for Deployment/Service/Ingress
- Inject env via Secrets/ConfigMaps; avoid hardcoding secrets
- Deploy to minikube/k3d; run a smoke test against the endpoint

## Acceptance (CI-verifiable)
- Manifests validate (kubeval/kubeconform) in CI
- A simple e2e smoke test runs against a local cluster job (optional)
- No secrets committed; checks enforce this

## Quick win
Use Kustomize overlays for dev/stage/prod to keep env-specific tweaks clean.

## Common pitfalls
- Missing readiness probes causing rolling update issues
- Baking secrets into images or manifests

## Reflection
What did your overlay structure look like, and how will it scale with environments?

## References
- Kubernetes docs; Kustomize; GitOps (Argo CD/Flux) overviews
