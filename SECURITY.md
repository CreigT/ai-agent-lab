# Security Policy

AI Agent Lab is a defensive cybersecurity research project. Safety controls apply to code, data, prompts, tools, and external integrations.

## Rules

- Never commit real API keys, passwords, tokens, private logs, or customer data.
- Keep secrets in environment variables; `.env.example` must contain placeholders only.
- Use the minimum permissions required for every tool or integration.
- Keep potentially impactful actions behind explicit human approval.
- Validate tool inputs and constrain tools to their documented defensive purpose.
- Do not silently expand an agent's permissions or accessible resources.
- Sanitize example logs and reports before committing them.
- Treat model output as untrusted input when it influences tools or security decisions.

## Defensive Scope

This repository is intended for authorized defensive research, education, triage assistance, and security automation. Testing should be performed only against systems and data the operator is authorized to use.

## Reporting

Do not disclose secrets, private data, or actionable exploit details in public issues. Report sensitive concerns privately to the project owner.

---

**Sponsored by CREIGNIFICENT LLC.**
