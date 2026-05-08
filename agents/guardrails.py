"""Safety guardrails for defensive-only cybersecurity interactions."""

from __future__ import annotations

from dataclasses import dataclass


BLOCKLIST_KEYWORDS = {
    "malware",
    "ransomware",
    "botnet",
    "phishing kit",
    "credential theft",
    "steal password",
    "keylogger",
    "exploit automation",
    "weaponize",
    "zero-day exploit code",
    "reverse shell",
    "c2 server",
    "autonomous attack",
}


@dataclass(slots=True)
class GuardrailResult:
    allowed: bool
    reason: str



def evaluate_prompt(prompt: str) -> GuardrailResult:
    """Decide whether a prompt is safe to process.

    This v1 implementation uses keyword checks for clarity.
    """
    normalized = prompt.lower()
    for term in BLOCKLIST_KEYWORDS:
        if term in normalized:
            return GuardrailResult(
                allowed=False,
                reason=(
                    "Request blocked by safety guardrails. "
                    "This assistant supports defensive cybersecurity research only."
                ),
            )

    return GuardrailResult(allowed=True, reason="Prompt is allowed.")
