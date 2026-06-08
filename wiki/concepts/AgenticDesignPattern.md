---
title: "Agentic Design Pattern"
type: concept
tags: [agents, design-patterns, software-engineering, agentic-design-patterns]
sources: [agentic-design-patterns-00-frontmatter, agentic-design-patterns-ch14-rag, agentic-design-patterns-appendices-bg]
last_updated: 2026-06-07
---

# Agentic Design Pattern

An **agentic design pattern** is a reusable, battle-tested template or blueprint that offers a proven approach to a recurring problem in designing and implementing agent behavior. The concept is the direct transposition of the classic software-engineering idea of *design patterns* (and architectural patterns for buildings) into the domain of LLM-driven autonomous agents. It is formalized as a meta-concept in [[AntonioGulli|Antonio Gulli's]] book [[AgenticDesignPatterns|*Agentic Design Patterns*]] — this page is the **concept**, distinct from the book hub entity.

## Why patterns matter for agents
Realizing the defining characteristics of an [[AgenticAI|agentic system]] — [[Autonomy]], [[Proactiveness]], [[Reactiveness]], [[GoalOriented|goal-orientation]], [[ToolUse|tool use]], [[MemoryManagement|memory]], and [[AgentCommunication|communication]] — introduces significant complexity: how does the agent maintain state across steps, decide *when* and *how* to use a tool, coordinate with other agents, and recover from errors? Patterns answer these recurring questions by providing:

- A **common language and structure** that makes an agent's logic clearer and easier to maintain.
- **Reusable solutions** so engineers avoid reinventing fundamentals (conversational flow, external-capability integration, multi-agent coordination, error handling, state management).
- Improved **structure, maintainability, reliability, and efficiency**, accelerating development by letting builders focus on the unique aspects of their application rather than foundational mechanics.

> "They are not rigid rules, but rather battle-tested templates or blueprints that offer proven approaches to standard design and implementation challenges in the agentic domain."

## The 21 patterns of the book
The book extracts 21 fundamental patterns: [[PromptChaining]], [[Routing]], [[Parallelization]], [[Reflection]], [[ToolUse]], [[Planning]], [[MultiAgentCollaboration]], [[MemoryManagement]], [[LearningAndAdaptation]], [[ModelContextProtocol]], [[GoalSettingAndMonitoring]], [[ExceptionHandlingAndRecovery]], [[HumanInTheLoop]], [[RAG]], [[InterAgentCommunication]], [[ResourceAwareOptimization]], [[ReasoningTechniques]], [[Guardrails]], [[EvaluationAndMonitoring]], [[Prioritization]], [[ExplorationAndDiscovery]].

## Capstone synthesis — the book's Conclusion (four foundational categories)
The book's [[agentic-design-patterns-appendices-bg|Conclusion]] groups the 21 patterns into four categories that mirror the core competencies of an intelligent agent:
1. **Core Execution and Task Decomposition** — [[PromptChaining]] (linear decomposition), [[Routing]] (conditional path/tool selection), [[Parallelization]] (concurrent independent sub-tasks), [[Planning]] (multi-step plans toward a high-level objective).
2. **Interaction with the External Environment** — [[ToolUse]] / [[FunctionCalling]] (grounding in real-world APIs/databases) and [[rag|Knowledge Retrieval (RAG)]] (querying knowledge bases for context).
3. **State, Learning, and Self-Improvement** — [[MemoryManagement]] (short- and long-term context), [[Reflection]] and **Self-Correction** (critique and iteratively refine own output), and [[LearningAndAdaptation]] (evolve behavior from feedback/experience).
4. **Collaboration and Communication** — [[MultiAgentCollaboration]] (specialized agents with distinct roles), standardized by [[InterAgentCommunication|Inter-Agent Communication (A2A)]] and [[ModelContextProtocol|Model Context Protocol (MCP)]].

**Combining patterns**: the Conclusion stresses that real power comes from *composition* — its worked example (an autonomous AI research assistant) weaves ≥5 patterns (Planning → Tool Use → Multi-Agent Collaboration → Reflection/Self-Correction → Memory Management). **Looking forward**, it forecasts a shift from human-in-the-loop "co-pilot" to **human-on-the-loop** oversight, the rise of agentic ecosystems/marketplaces standardized by MCP + A2A, and a sharpened focus on **safety, alignment, and robustness** ("safety patterns"). Final framing: patterns are "the grammar of a new language of creation."

## Connections
- [[AgenticDesignPatterns]] — the book (entity) that catalogs these patterns.
- [[AgenticAI]] — the system class patterns help build.
- [[AgentComplexitySpectrum]] — patterns map onto the Level 0–3 progression.
- [[agentic-design-patterns-00-frontmatter]] — source page.
