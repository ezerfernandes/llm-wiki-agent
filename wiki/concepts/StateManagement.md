---
title: "State Management (Agentic Systems)"
type: concept
tags: [agents, state, session, context, agentic-design-patterns]
sources: [agentic-design-patterns-ch01-prompt-chaining, agentic-design-patterns-ch08-memory-management]
last_updated: 2026-06-07
---

# State Management (Agentic Systems)

**State management** is the practice of tracking, persisting, and updating an agent's working information — the conversation history, intermediate results, task progress, and scratchpad variables — across the steps of a single run and (optionally) across sessions. It is the substrate that turns a [[StatelessLLM|stateless LLM]] call into a coherent, multi-step [[AgenticAI|agentic]] workflow.

In [[AgenticDesignPatterns|Gulli's *Agentic Design Patterns*]], state is one of the layers that [[ContextEngineering|context engineering]] assembles before each generation, and it is the short-term complement to long-term [[MemoryManagement|memory management]]: short-term/working state lives in the [[ContextWindow|context window]] and the run's scratchpad, while long-term knowledge is externalized to stores.

## How it works in frameworks

- **[[langgraph|LangGraph]]** models state explicitly: a typed `State` object flows through a graph of nodes, each node reads and returns partial state updates, and a **checkpointer** persists state so threads are resumable.
- **[[GoogleADK|Google ADK]]** exposes a `Session` whose `events` log + `state` key-value dictionary hold the active conversation; state must be mutated through the event pipeline (`output_key` or `EventActions.state_delta`), with `user:` / `app:` / `temp:` prefixes scoping persistence.
- **[[crewai|CrewAI]]** threads task outputs between agents as the crew progresses.

## Why it matters

Without managed state an agent cannot do [[SequentialDecomposition|multi-step decomposition]], [[Planning|planning]], [[Reflection|reflection]] loops, or [[ExceptionHandlingAndRecovery|recovery]] (which depends on a restorable prior state). It underpins nearly every other pattern.

## Related

- [[MemoryManagement]] — long-term/persistent counterpart to short-term state.
- [[ContextEngineering]] — state is one input layer it curates.
- [[PromptChaining]] — passes state between chained LLM calls.
- [[ContextHandoff]] / [[StructuredOutputs]] — structured state hand-off between steps.
