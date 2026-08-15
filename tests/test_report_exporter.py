import json
import tempfile
import unittest
from pathlib import Path

from tools.report_exporter import ResearchReport, export_report


class ReportExporterTests(unittest.TestCase):
    def test_exports_markdown_and_json(self):
        report = ResearchReport(
            query="Summarize defensive guidance",
            response="Use least privilege.",
            safe=True,
        )
        with tempfile.TemporaryDirectory() as directory:
            md_path, json_path = export_report(report, directory)
            self.assertTrue(md_path.exists())
            self.assertTrue(json_path.exists())
            self.assertIn("Defensive Cybersecurity Research Report", md_path.read_text(encoding="utf-8"))
            payload = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["query"], report.query)
            self.assertTrue(payload["safe"])

    def test_exports_block_reason(self):
        report = ResearchReport(
            query="blocked request",
            response="",
            safe=False,
            blocked_reason="Safety guardrail",
        )
        with tempfile.TemporaryDirectory() as directory:
            md_path, _ = export_report(report, directory)
            text = Path(md_path).read_text(encoding="utf-8")
            self.assertIn("Blocked Reason", text)
            self.assertIn("Safety guardrail", text)


if __name__ == "__main__":
    unittest.main()
