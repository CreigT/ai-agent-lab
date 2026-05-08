"""Core defensive cybersecurity research agent."""

from __future__ import annotations

import logging
from dataclasses import dataclass

from openai import OpenAI

from agents.guardrails import evaluate_prompt


logger = logging.getLogger(__name__)


SYSTEM_PROMPT = """You are a defensive cybersecurity research assistant.

Allowed behavior:
- Explain cybersecurity concepts safely and clearly.
- Summarize CVEs at a high level.
- Provide defensive recommendations, detections, mitigations, and patching guidance.

Do not provide:
- Malware creation guidance
- Exploit development steps
- Phishing or credential theft guidance
- Offensive automation workflows
- Any instructions that facilitate unauthorized access

If a request is unsafe, refuse briefly and redirect to defensive best practices.
"""


@dataclass(slots=True)
class AgentResult:
    safe: bool
    response_text: str
    blocked_reason: str | None = None


class CyberResearchAgent:
    """Minimal OpenAI-backed assistant with safety-first behavior."""

    def __init__(self, api_key: str, model: str) -> None:
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def run(self, user_query: str) -> AgentResult:
        """Process a user query with guardrails and LLM assistance."""
        guardrail = evaluate_prompt(user_query)
        if not guardrail.allowed:
            logger.warning("Prompt blocked by guardrails", extra={"reason": guardrail.reason})
            return AgentResult(
                safe=False,
                response_text=(
                    "I can’t help with offensive or harmful cybersecurity requests. "
                    "I can help with defensive analysis, hardening, detection, and incident response best practices."
                ),
                blocked_reason=guardrail.reason,
            )

        logger.info("Running defensive cybersecurity query")
        response = self.client.responses.create(
            model=self.model,
            input=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_query},
            ],
        )

        text = response.output_text.strip() if response.output_text else "No response generated."
        return AgentResult(safe=True, response_text=text)
