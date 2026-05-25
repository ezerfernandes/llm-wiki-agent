---
title: "AutoGPT"
type: entity
tags: [tool, open-source, agent, llm-orchestration]
sources: [ai-engineering-ch01-intro, ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# AutoGPT

Open-source autonomous AI-agent framework launched in 2023, one of the early high-visibility implementations of the "agent that plans and uses tools" pattern. Cited in [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]] as one of four open-source AI-engineering tools that within two years of launch **garnered more GitHub stars than Bitcoin** — on track to surpass React and Vue. The set: **AutoGPT, [[StableDiffusion]] Web UI, [[LangChain]], [[Ollama]]**. AutoGPT also surfaced as an early example of *"AIs that can plan and use tools"* — Huyen's working definition of an [[Agent|agent]].

Also cited for **extracting structured data from web pages and PDFs**, in the coding-tool subsection of Ch 1's [[FoundationModelUseCases|use case]] taxonomy (listed as AgentGPT in the cited list).

## Connections

- [[AIEngineering]] — discipline AutoGPT serves.
- [[LangChain]] / [[Ollama]] / [[StableDiffusion]] — peer tools in the four-OSS-tool cohort.
- [[WorkflowAutomation]] / [[llmagents]] / [[AgenticAI]] — Ch 1's agent framing.
- [[ai-engineering-ch01-intro]] — primary source.

## From [[ai-engineering-ch06-rag-agents|AI Engineering Ch 6]]

Ch 6 re-engages AutoGPT as the canonical **social-media-API-focused** agent framework, contrasted with [[Composio]]:

> *"Different frameworks might focus on different categories of tools. For example, AutoGPT focuses on social media APIs (Reddit, X, and Wikipedia), whereas Composio focuses on enterprise APIs (Google Apps, GitHub, and Slack)."*

This is the **specialization** observation in Ch 6's tool-selection guidance — there is no general agent framework, only agent frameworks specialized to particular tool-API surfaces. Choosing between AutoGPT, [[Composio]], [[LangChain]], etc. is a function of *which tool surface your agent needs to act on*, not just framework quality.
