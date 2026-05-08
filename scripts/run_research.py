"""CLI entrypoint for the defensive cybersecurity research assistant."""

from __future__ import annotations

import argparse
import logging

from agents.cyber_research_agent import CyberResearchAgent
from app.config import load_config
from app.logging_config import configure_logging
from tools.report_exporter import ResearchReport, export_report


logger = logging.getLogger(__name__)



def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run a defensive cybersecurity research query.")
    parser.add_argument("--query", required=True, help="User query for defensive cybersecurity research")
    return parser



def main() -> int:
    args = build_parser().parse_args()
    config = load_config()
    configure_logging(config.log_level)

    agent = CyberResearchAgent(api_key=config.openai_api_key, model=config.openai_model)
    result = agent.run(args.query)

    report = ResearchReport(
        query=args.query,
        response=result.response_text,
        safe=result.safe,
        blocked_reason=result.blocked_reason,
    )
    md_path, json_path = export_report(report, config.reports_dir)

    logger.info("Research completed", extra={"markdown_report": str(md_path), "json_report": str(json_path)})
    print("=== Assistant Response ===")
    print(result.response_text)
    print(f"\nMarkdown report: {md_path}")
    print(f"JSON report: {json_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
