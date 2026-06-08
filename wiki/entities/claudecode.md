---
title: "Claude Code"
type: entity
tags: [product, anthropic, coding-agent, cli-agent, agentic-design-patterns]
sources: [2605.03808-agentic-imodels, 2605.02396-heavyskill, agentic-design-patterns-appendices-bg]
last_updated: 2026-06-07
---

# Claude Code

Anthropic's CLI-based coding agent. Used as the autoresearch driver in AGENTIC-IMODELS and as one of four ADS systems benchmarked on BLADE; gains up to 73% from agent-interpretable evolved models. Also referenced in HEAVYSKILL as an example agentic harness.

## In Agentic Design Patterns (Gulli) — Appendix E
[[agentic-design-patterns-appendices-bg|Appendix E]] profiles **Claude CLI (Claude Code)** as one of four leading AI coding CLIs. It frames it as a high-level coding agent with **deep, holistic understanding of a project's architecture**, whose core strength is its "agentic" nature — building a mental model of the whole repository for complex, multi-step tasks. The interaction is conversational (pair-programming style: it explains its plans before executing), making it ideal for **large-scale refactoring** and broad architectural features.

- **Built-in tools**: file ingestion, code-structure analysis, edit generation; **deep Git integration** (branch + commit management).
- **Extensibility via [[ModelContextProtocol|MCP]]** (the appendix's "Multi-tool Control Protocol") — users define and integrate custom tools (private APIs, DB queries, project scripts), positioning the developer as arbiter of the agent's functional scope and **Claude as a reasoning engine augmented by user-defined tooling**.
- Example use cases named: large-scale refactoring (e.g. session-cookie auth → stateless JWTs across the codebase), API integration from an OpenAPI spec, and documentation generation (TSDoc comments). Reference: https://docs.anthropic.com/en/docs/claude-code/cli-reference

## Connections
- [[anthropic|Anthropic]]
- [[agentic-design-patterns-appendices-bg]] — Appendix E (CLI coding agents).
- [[codingagents]] / [[CodingAgent]] — the broader coding-agent pattern.
- [[GeminiCLI]] / [[Aider]] / [[copilotcli|GitHub Copilot CLI]] — peer CLI coding agents.
- [[terminalbench|Terminal-Bench]] — CLI-agent benchmark.
- [[ModelContextProtocol|MCP]] — custom-tool extensibility.
- [[2605.03808-agentic-imodels]]
- [[autoresearch|Autoresearch]]
- [[agenticharness|AgenticHarness]]
