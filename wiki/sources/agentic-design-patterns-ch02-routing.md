---
title: "Chapter 2 — Routing (Agentic Design Patterns)"
type: source
tags: [agentic-design-patterns, agents, routing, control-flow, conditional-logic, intent-classification, delegation]
date: 2025-06-01
source_file: raw/books/agentic-design-patterns.pdf
sources: [agentic-design-patterns]
---

## Summary
Chapter 2 of [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] establishes **[[Routing|routing]]** as the second of the 21 patterns: the mechanism that injects **conditional logic** into an agent so it can dynamically evaluate criteria and select among multiple downstream actions, tools, or sub-agents — the adaptive, branching counterpart to the linear [[PromptChaining|prompt chaining]] pattern. It enumerates four ways to implement the router (LLM-based, embedding/semantic, rule-based, and ML-model-based) and shows where routing fits in the agent cycle. It closes with two hands-on examples of a coordinator delegating to specialist sub-agents — one in [[LangChain]]/[[LangGraph]] (`RunnableBranch`) and one in [[GoogleADK|Google ADK]] (Auto-Flow `sub_agents`). (Agentic Design Patterns, PDF pp 36–49.)

## Key Claims
- Routing introduces **conditional logic** into an agent's framework, shifting it from a fixed execution path to dynamic evaluation of criteria to select the next action — enabling flexible, context-aware behavior. It is the conditional counterpart to sequential [[PromptChaining|prompt chaining]].
- The core component is an **evaluation-and-dispatch mechanism**, implementable four ways: **LLM-based routing** (prompt the model to emit a route identifier), **embedding-based / semantic routing** (route to the most similar capability embedding), **rule-based routing** (if-else / switch / keyword matching — faster and more deterministic but less flexible), and **ML model-based routing** (a fine-tuned discriminative classifier whose routing logic lives in learned weights, not a runtime prompt).
- ML-model routing is **distinct from LLM-based routing**: the decision component is not a generative model executing a prompt at inference; LLMs may only pre-generate synthetic training data.
- Routing can be applied at **multiple junctures**: at the outset to classify a primary task, at intermediate points in a chain, or inside a subroutine to select a tool.
- **Practical applications** span human-computer interaction (intent interpretation, escalation, curriculum selection), automated data/document pipelines (routing emails/tickets/payloads as a classification-and-distribution function), and complex multi-tool/multi-agent systems (routing as a high-level dispatcher).
- Frameworks [[LangChain]], [[LangGraph]], and [[GoogleADK|Google ADK]] (also [[CrewAI]]) provide explicit constructs for routing; **LangGraph's state-based graph** is especially suited to routing contingent on accumulated system state, expressed as conditional transitions between nodes.
- Both hands-on examples implement a **coordinator → specialist-sub-agent delegation pattern** ([[AgentHandoff|agent handoff]]): LangChain via a `RunnableBranch` on a router chain's `'booker'/'info'/'unclear'` decision; ADK via a `Coordinator` agent whose `sub_agents` trigger LLM-driven Auto-Flow delegation.
- **Rule of thumb**: use routing when an agent must decide between multiple distinct workflows, tools, or sub-agents based on input or state — essential for triage/classification (e.g., a support bot distinguishing sales, technical support, and account questions).

## Key Quotes
> "This capacity for dynamic decision-making, which governs the flow of control to different specialized functions, tools, or sub-processes, is achieved through a mechanism known as routing." — Routing Pattern Overview, p 36

> "Routing introduces conditional logic into an agent's operational framework, enabling a shift from a fixed execution path to a model where the agent dynamically evaluates specific criteria to select from a set of possible subsequent actions." — p 36

> "This technique is distinct from LLM-based routing because the decision-making component is not a generative model executing a prompt at inference time. Instead, the routing logic is encoded within the fine-tuned model's learned weights." — Machine Learning Model-Based Routing, p 37

> "With its state-based graph architecture, LangGraph is particularly well-suited for complex routing scenarios where decisions are contingent upon the accumulated state of the entire system." — p 37

> "It transforms an agent from a static executor of pre-defined sequences into a dynamic system that can make decisions about the most effective method for accomplishing a task under changing conditions." — Practical Applications & Use Cases, p 38

## Connections
- [[Routing]] — the chapter's named pattern (primary concept; created from this chapter).
- [[AgenticDesignPatterns]] — book hub; this is Chapter 2 of the 21 patterns.
- [[AntonioGulli]] — author (code examples credited to Marco Fago, MIT-licensed).
- [[PromptChaining]] — Ch 1's pattern; routing is its conditional/branching counterpart.
- [[AgentHandoff]] — the coordinator→sub-agent delegation pattern both code examples implement.
- [[Parallelization]] — adjacent control-flow pattern (Ch 3).
- [[ModelRouter]] / [[IntentClassifier]] — the production-architecture instantiation of LLM-based routing (augmented with this chapter's taxonomy).
- [[QueryRouting]] — embedding/source-selection routing in RAG (the chapter cross-refs RAG, Ch 14).
- [[Classification]] — the ML-model-based routing mechanism.
- [[RoutingBasedAgenticAI]] — the theoretical sample-efficiency view of routing to specialists.
- [[Embedding]] / [[SemanticSimilarity]] — embedding-based routing primitives.
- [[LangChain]] / [[LangGraph]] / [[GoogleADK]] / [[CrewAI]] — frameworks in the hands-on examples (LangGraph/ADK augmented).
- [[gemini|Gemini]] — `gemini-2.5-flash` (LangChain example) / `gemini-2.0-flash` (ADK example) is the model driven; [[openai|OpenAI]] and [[Anthropic]] named as alternative providers.
- [[ToolUse]] — ADK routes via `FunctionTool`-wrapped capabilities.

## Contradictions
- None found. The chapter's router taxonomy refines and extends the existing [[ModelRouter]] / [[IntentClassifier]] framing (*AI Engineering* Ch 10) rather than conflicting with it; it complements [[PromptChaining]] as the conditional sibling pattern.
