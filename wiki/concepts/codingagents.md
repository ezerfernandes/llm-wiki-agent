---
title: "Coding Agents"
type: concept
tags: [agents, coding-agents, software-development, cli-agents, agentic-design-patterns]
sources: [agentic-design-patterns-appendices-bg]
last_updated: 2026-06-07
---

# Coding Agents

**Coding agents** are specialized AI agents that participate in the software-development lifecycle — writing, testing, documenting, refactoring, and reviewing code. [[agentic-design-patterns-appendices-bg|*Agentic Design Patterns* Appendices E and G]] (Gulli) cover them from two angles:

- **As CLIs (Appendix E)** — AI Agent Command-Line Interfaces that turn the terminal into an intelligent collaborative workspace: [[claudecode|Claude Code (Claude CLI)]], [[GeminiCLI|Gemini CLI]], [[Aider]], and [[copilotcli|GitHub Copilot CLI]], benchmarked by [[terminalbench|Terminal-Bench]].
- **As a team pattern (Appendix G)** — the [[CodingAgent|Coding Agent]] framework, where a human orchestrator leads specialist agent personas (Scaffolder, Test Engineer, Documenter, Optimizer, Process Supervisor) via a context staging area and version-controlled invocation prompts.

See [[CodingAgent]] for the full pattern and [[VibeCoding]] for the ideation phase that precedes it.

## Connections
- [[CodingAgent]] — the detailed human-led team pattern.
- [[agentic-design-patterns-appendices-bg]] — source (Appendices E & G).
- [[claudecode]] / [[GeminiCLI]] / [[Aider]] / [[copilotcli]] — CLI coding agents.
- [[terminalbench]] — CLI-agent benchmark.
- [[VibeCoding]] — related entry-point paradigm.
