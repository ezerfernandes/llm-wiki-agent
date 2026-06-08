---
title: "AutoGen"
type: concept
tags: [framework, agents, multi-agent, open-source, microsoft, agentic-design-patterns]
sources: [agentic-design-patterns-appendices-bg]
last_updated: 2026-06-07
---

# AutoGen

**AutoGen** is a [[microsoft|Microsoft]] open-source framework for **orchestrating multiple agents that solve tasks through conversation**. As described in [[agentic-design-patterns-appendices-bg|*Agentic Design Patterns* Appendix C]] (Gulli), its architecture enables agents with distinct capabilities to interact, allowing for complex problem decomposition and collaborative resolution.

## In Agentic Design Patterns (Gulli)
- **Primary advantage**: a flexible, **conversation-driven** approach that supports dynamic and complex multi-agent interactions.
- **Trade-off**: this conversational paradigm can lead to **less predictable execution paths** and may require sophisticated prompt engineering to ensure tasks converge efficiently.
- It is listed in the appendix's "Other agent development frameworks" alongside [[LlamaIndex]], [[Haystack]], MetaGPT, SuperAGI, Microsoft [[SemanticKernel|Semantic Kernel]], and AWS [[awsstrands|Strands Agents]] — distinct from the more granular [[LangChain]]/[[langgraph|LangGraph]] and the higher-level [[GoogleADK|ADK]]/[[crewai|CrewAI]] orchestrators.

## Why it matters in agentic systems
AutoGen represents the **conversation-centric** school of [[MultiAgentCollaboration|multi-agent collaboration]]: instead of wiring an explicit state graph (LangGraph) or defining roles/tasks/process (CrewAI), agents converge on a solution by talking to one another. This maximizes flexibility at the cost of determinism.

## Connections
- [[agentic-design-patterns-appendices-bg]] — source (Appendix C).
- [[microsoft]] — developer of AutoGen.
- [[MultiAgentCollaboration]] — the pattern it implements.
- [[langgraph]] / [[crewai]] / [[GoogleADK]] — peer multi-agent frameworks.
- [[SemanticKernel]] — Microsoft's other LLM-orchestration framework.
