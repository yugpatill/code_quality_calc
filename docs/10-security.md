# 10) Security and dependency health

## Bandit (static security analysis)
- Run: `bandit -q -r src -x tests`
- In Makefile target `security` and CI job.

## pip‑audit (dependency vulnerabilities)
- Run: `pip-audit -r requirements.txt || true`
- Included in `make security` and CI.

## Dependabot (automated updates)
- Config: `.github/dependabot.yml`
- Opens weekly PRs for pip and GitHub Actions updates (minor/patch grouped).

---

Next: [Everyday workflows](./11-workflows.md)
