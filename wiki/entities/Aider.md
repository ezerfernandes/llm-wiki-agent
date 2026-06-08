---
title: "Aider"
type: entity
tags: [product, open-source, cli-agent, coding-agent, git, model-agnostic, agentic-design-patterns]
sources: [agentic-design-patterns-appendices-bg]
last_updated: 2026-06-07
---

# Aider

**Aider** is an **open-source, model-agnostic** AI coding assistant that acts as a true pair programmer by working directly on your files and **committing changes to Git**. Profiled in [[agentic-design-patterns-appendices-bg|*Agentic Design Patterns* Appendix E]] (Gulli) as one of four leading CLI coding agents.

## Strengths (Appendix E)
- **Directness** — it applies edits, **runs tests to validate them, and automatically commits every successful change** to Git.
- **Model-agnostic** — gives users complete control over cost and capabilities (bring your own model).
- A **git-centric workflow** makes it ideal for developers who value efficiency, control, and a transparent, auditable trail of all code modifications.

## Example use cases
- **Test-Driven Development (TDD)** — "Create a failing test for a function that calculates the factorial of a number," then "Now, write the code to make the test pass" (Aider implements and re-runs the test to confirm).
- **Precise bug squashing** — "The `calculate_total` function in `billing.py` fails on leap years. Add the file to the context, fix the bug, and verify your fix against the existing test suite."
- **Dependency updates** — update an outdated `requests` library across all Python files, fixing deprecated calls and updating `requirements.txt`.

## Connections
- [[agentic-design-patterns-appendices-bg]] — source (Appendix E).
- [[codingagents]] / [[CodingAgent]] — the broader pattern.
- [[claudecode]] / [[GeminiCLI]] / [[copilotcli]] — peer CLI coding agents.
- [[terminalbench|Terminal-Bench]] — CLI-agent benchmark.
- Reference: https://aider.chat/
