---
title: "Composio"
type: entity
tags: [agent-framework, tools, enterprise]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Composio

**Composio** is an agent framework that **focuses on enterprise-API integrations**. Cited in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] as the contrast to [[AutoGPT]] in framework specialization:

> *"Different frameworks might focus on different categories of tools. For example, AutoGPT focuses on social media APIs (Reddit, X, and Wikipedia), whereas Composio focuses on enterprise APIs (Google Apps, GitHub, and Slack)."*

## What it covers

Composio's tool inventory targets the enterprise productivity surface:

- **[[google|Google]] Apps** — Gmail, Calendar, Drive, Sheets.
- **[[GitHub]]** — repos, issues, PRs.
- **[[Slack]]** — messages, channels, users.

The framework provides authentication, rate-limiting, and schema-typed API surfaces that an LLM can call via [[FunctionCalling|function calling]].

## Position in the agent-framework landscape

| Framework | Focus |
|---|---|
| [[AutoGPT]] | Social-media APIs |
| **Composio** | Enterprise APIs |
| [[LangChain]] | General-purpose |
| [[langgraph|LangGraph]] | Stateful agent orchestration |

## Connections

- [[Agent]] / [[ToolInventory]] — the abstractions Composio populates.
- [[AutoGPT]] — peer framework with different specialization.
- [[FunctionCalling]] — the API protocol Composio exposes.
- [[google|Google Apps]] / [[GitHub]] / [[Slack]] — Composio's primary tool targets.
- [[ai-engineering-ch06-rag-agents]] — primary source.
