# CyberSecEval Crew

This CrewAI project evaluates open-source LLMs using Meta's CyberSecEval framework.  
It processes JSON test reports from 7 evaluation types and generates a final recommendation report.

## How it works

- Each assessment (MITRE, FRR, etc.) is handled by a dedicated agent.
- Reports are analyzed using a chunked JSON reader.
- A final agent synthesizes findings into a readable Markdown (and optionally PDF) report.

<!-- ## Usage

```bash
poetry install
poetry run python src/cybersec_eval/main.py -->
