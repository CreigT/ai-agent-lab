# ai-agent-lab

A beginner-friendly Python 3.11+ starter project for a **defensive cybersecurity research assistant**.

> This project is intentionally scoped to safe, defensive use cases such as education, CVE summarization, and hardening recommendations.

## Features (v1)

- Modular architecture for easy extension
- Structured logging
- OpenAI API integration
- Guardrails to block unsafe/offensive requests
- Defensive cybersecurity concept explanations
- CVE summarization workflow
- Report exporting to:
  - Markdown (`.md`)
  - JSON (`.json`)

## Project structure

```text
ai-agent-lab/
├── app/
│   ├── config.py
│   └── logging_config.py
├── agents/
│   ├── guardrails.py
│   └── cyber_research_agent.py
├── tools/
│   └── report_exporter.py
├── prompts/
├── reports/
├── tests/
├── scripts/
│   └── run_research.py
├── .env.example
├── AGENTS.md
├── README.md
└── requirements.txt
```

## Safety scope

Allowed:
- Cybersecurity concept explanation
- CVE summarization
- Defensive recommendations
- Security awareness and hardening guidance

Blocked:
- Malware generation
- Exploit automation
- Phishing kit creation
- Credential theft
- Offensive tooling
- Shell execution instructions for attacks
- Autonomous attack workflows

## Quickstart

1. Use Python 3.11+.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy environment template:

```bash
cp .env.example .env
```

4. Add your OpenAI API key to `.env`:

```env
OPENAI_API_KEY=your_key_here
```

5. Run the research script:

```bash
python scripts/run_research.py --query "Summarize CVE-2024-3094 and provide defensive mitigations"
```

## Notes

- This is **Version 1** and intentionally simple.
- The tool avoids offensive output by design.
- Add tests in `tests/` as you expand behavior.
