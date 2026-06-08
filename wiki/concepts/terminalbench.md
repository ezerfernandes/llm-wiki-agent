---
title: "Terminal-Bench"
type: concept
tags: [benchmark, agents, cli-agents, evaluation, agentic-design-patterns]
sources: [agentic-design-patterns-appendices-bg]
last_updated: 2026-06-07
---

# Terminal-Bench

**Terminal-Bench** is an evaluation framework for measuring the proficiency of AI agents at executing complex tasks within a **command-line interface**. As described in [[agentic-design-patterns-appendices-bg|*Agentic Design Patterns* Appendix E]] (Gulli), the terminal is identified as an optimal environment for AI-agent operation because it is **text-based and sandboxed**.

## Key facts (Appendix E)
- Initial release **Terminal-Bench-Core-v0** comprises **80 manually curated tasks** spanning domains such as scientific workflows and data analysis.
- **Terminus** is a minimalistic reference agent developed to serve as a standardized testbed for equitable comparison across language models.
- The framework is designed for **extensibility** — integrating diverse agents via containerization or direct connections.
- Future directions: enabling **massively parallel evaluations**, incorporating established benchmarks, and encouraging open-source community contributions for task expansion.

## Why it matters in agentic systems
Because many CLI coding-agent use cases overlap, the differentiator between tools ([[claudecode|Claude Code]], [[GeminiCLI|Gemini CLI]], [[Aider]], [[copilotcli|GitHub Copilot CLI]]) is the **quality, efficiency, and nuance** of results — exactly what Terminal-Bench is built to quantify. (Reference: https://www.tbench.ai/)

## Connections
- [[agentic-design-patterns-appendices-bg]] — source (Appendix E).
- [[codingagents]] / [[CodingAgent]] — the agents it evaluates.
- [[claudecode]] / [[GeminiCLI]] / [[Aider]] / [[copilotcli]] — CLI agents under test.
- [[Benchmarking]] — general evaluation context.
