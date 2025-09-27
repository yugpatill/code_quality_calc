# 26 Security for Python APIs [Core]

Duration: 4–5h
P: C8, C9, G17

## Goal
Build secure-by-default services.

## Topics
- OAuth2/OIDC, JWT validation
- CORS, security headers, CSRF context
- Rate limiting and input validation depth
- SSRF/SQLi protections; dependency scanning (pip-audit)
- SAST/DAST pipelines; secret rotation basics

## Before you start (preflight)
- OpenAPI available; auth flows identified
- pip-audit (or safety) available; CodeQL (if on GitHub)

## Outcomes
- Add authn/z to selected endpoints with safe defaults
- Add security scans to CI; address findings
- Document threat model assumptions and mitigations

## Build (hands-on)
- Implement OAuth2/JWT auth (or API key pattern for simplicity)
- Add CORS and security headers middleware
- Add pip-audit and (optionally) CodeQL to CI; fix vulnerabilities

## Acceptance (CI-verifiable)
- Security tests pass (authorized vs unauthorized)
- Scanners report no high/critical vulnerabilities
- Headers present (CSP optional), CORS rules tested

## Quick win
Add rate limiting with sensible defaults to prevent abuse.

## Common pitfalls
- Leaking secrets in logs or error messages
- Overly permissive CORS rules in production

## Reflection
What was the highest-impact security improvement you made?

## References
- OWASP API Top 10; FastAPI security docs; pip-audit
