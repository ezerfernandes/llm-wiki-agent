---
title: "Semantic Kernel"
type: entity
tags: [framework, microsoft, agents, sdk, open-source, agentic-design-patterns]
sources: [agentic-design-patterns-appendices-bg]
last_updated: 2026-06-07
---

# Semantic Kernel

**Semantic Kernel** is an SDK from [[microsoft|Microsoft]] that integrates large language models with conventional programming code. Per [[agentic-design-patterns-appendices-bg|*Agentic Design Patterns* Appendix C]] (Gulli), it works through a system of **"plugins"** and **"planners"**, allowing an LLM to invoke native functions and orchestrate workflows — effectively treating the model as a **reasoning engine within a larger software application**.

## In Agentic Design Patterns (Gulli)
- **Primary strength**: seamless integration with existing **enterprise codebases**, particularly in **.NET and Python** environments.
- **Trade-off**: the conceptual overhead of its plugin/planner architecture can present a steeper learning curve than more straightforward agent frameworks.
- Named among the appendix's "Other agent development frameworks" alongside [[autogen|AutoGen]], [[LlamaIndex]], [[Haystack]], MetaGPT, SuperAGI, and AWS [[awsstrands|Strands Agents]].

## Connections
- [[agentic-design-patterns-appendices-bg]] — source (Appendix C).
- [[microsoft]] — developer.
- [[autogen]] — Microsoft's conversation-driven multi-agent framework (peer).
- [[ToolUse]] / [[FunctionCalling]] — "plugins" are the native-function-calling mechanism.
- [[Planning]] — "planners" map to the planning pattern.
