"""Application configuration helpers."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(slots=True)
class AppConfig:
    """Runtime configuration for the cybersecurity research assistant."""

    openai_api_key: str
    openai_model: str = "gpt-4.1-mini"
    log_level: str = "INFO"
    reports_dir: str = "reports"



def load_config() -> AppConfig:
    """Load configuration from environment variables.

    Raises:
        ValueError: If required settings are missing.
    """
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise ValueError("OPENAI_API_KEY is required. Set it in your environment or .env file.")

    return AppConfig(
        openai_api_key=api_key,
        openai_model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini").strip() or "gpt-4.1-mini",
        log_level=os.getenv("LOG_LEVEL", "INFO").strip().upper() or "INFO",
        reports_dir=os.getenv("REPORTS_DIR", "reports").strip() or "reports",
    )
