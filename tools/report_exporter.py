"""Report export utilities for markdown and JSON outputs."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path


@dataclass(slots=True)
class ResearchReport:
    query: str
    response: str
    safe: bool
    blocked_reason: str | None = None



def export_report(report: ResearchReport, output_dir: str) -> tuple[Path, Path]:
    """Export a research report as both Markdown and JSON."""
    reports_path = Path(output_dir)
    reports_path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    base_name = f"research_report_{timestamp}"

    md_path = reports_path / f"{base_name}.md"
    json_path = reports_path / f"{base_name}.json"

    md_content = (
        f"# Defensive Cybersecurity Research Report\n\n"
        f"- **Generated (UTC):** {timestamp}\n"
        f"- **Safe Request:** {report.safe}\n\n"
        f"## Query\n\n{report.query}\n\n"
        f"## Response\n\n{report.response}\n\n"
    )

    if report.blocked_reason:
        md_content += f"## Blocked Reason\n\n{report.blocked_reason}\n"

    md_path.write_text(md_content, encoding="utf-8")
    json_path.write_text(json.dumps(asdict(report), indent=2), encoding="utf-8")

    return md_path, json_path
