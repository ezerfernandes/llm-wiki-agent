---
title: "AWS Strands Agents"
type: entity
tags: [framework, aws, agents, sdk, open-source, model-agnostic, agentic-design-patterns]
sources: [agentic-design-patterns-appendices-bg]
last_updated: 2026-06-07
---

# AWS Strands Agents

**Strands Agents** is an [[Amazon|AWS]] lightweight, flexible **SDK** that uses a **model-driven approach** for building and running AI agents. Per [[agentic-design-patterns-appendices-bg|*Agentic Design Patterns* Appendix C]] (Gulli), it is designed to be simple and scalable, supporting everything from basic conversational assistants to complex multi-agent autonomous systems.

## In Agentic Design Patterns (Gulli)
- **Model-agnostic** — broad support for various LLM providers.
- **Native [[ModelContextProtocol|MCP]] integration** for easy access to external tools.
- **Core advantage**: simplicity and flexibility, with a customizable **agent loop** that is easy to get started with.
- **Trade-off**: its lightweight design means developers may need to build out more surrounding operational infrastructure (advanced monitoring, lifecycle management) that heavier frameworks provide out of the box.
- Named among the appendix's "Other agent development frameworks" alongside [[autogen|AutoGen]], [[LlamaIndex]], [[Haystack]], MetaGPT, SuperAGI, and Microsoft [[SemanticKernel|Semantic Kernel]].

## Connections
- [[agentic-design-patterns-appendices-bg]] — source (Appendix C).
- [[Amazon]] / AWS — vendor.
- [[ModelContextProtocol|MCP]] — natively integrated for external tooling.
- [[GoogleADK]] / [[crewai]] / [[langgraph]] — peer agent frameworks.

*(This page resolves both `[[AWSStrands]]` and `[[awsstrands]]` wikilinks.)*
