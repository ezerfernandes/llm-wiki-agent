---
title: "GitHub Copilot CLI"
type: entity
tags: [product, github, microsoft, cli-agent, coding-agent, agentic-design-patterns]
sources: [agentic-design-patterns-appendices-bg]
last_updated: 2026-06-07
---

# GitHub Copilot CLI

**GitHub Copilot CLI** extends the popular [[GitHubCopilot|GitHub Copilot]] AI pair programmer into the **terminal**. Profiled in [[agentic-design-patterns-appendices-bg|*Agentic Design Patterns* Appendix E]] (Gulli) as one of four leading CLI coding agents.

## Strengths (Appendix E)
- **Native, deep integration with the GitHub ecosystem** — it understands the context of a project *within GitHub*.
- **Agentic capabilities** — it can be assigned a **GitHub issue**, work on a fix, and **submit a pull request** for human review.

## Example use cases
- **Automated issue resolution** — a manager assigns a bug ticket (e.g. "Issue #123: Fix off-by-one error in pagination"); the agent checks out a new branch, writes the code, and submits a PR referencing the issue, without manual developer intervention.
- **Repository-aware Q&A** — "Where in this repository is the database connection logic defined, and what environment variables does it require?" (Copilot uses whole-repo awareness to answer with file paths).
- **Shell-command helper** — `gh? find all files larger than 50MB, compress them, and place them in an archive folder` → Copilot generates the exact shell command.

## Connections
- [[agentic-design-patterns-appendices-bg]] — source (Appendix E).
- [[GitHubCopilot]] — the parent pair-programmer product.
- [[microsoft]] — GitHub's parent company.
- [[codingagents]] / [[CodingAgent]] — the broader pattern.
- [[claudecode]] / [[GeminiCLI]] / [[Aider]] — peer CLI coding agents.
- [[terminalbench|Terminal-Bench]] — CLI-agent benchmark.
- Reference: https://docs.github.com/en/copilot/github-copilot-enterprise/copilot-cli

*(This page resolves both `[[copilotcli]]` and `[[CopilotCLI]]` wikilinks.)*
