---
title: "Agent Handoff (Delegation)"
type: concept
tags: [agentic-design-patterns, agents, routing, delegation, multi-agent, coordinator]
sources: [agentic-design-patterns-ch02-routing, agentic-design-patterns-ch07-multi-agent]
last_updated: 2026-06-07
---

# Agent Handoff (Delegation)

**Agent handoff** (a.k.a. **delegation**) is the pattern where a central **coordinator** agent analyzes an incoming request and hands it off to one of several **specialized sub-agents** to actually do the work, rather than answering directly. It is the concrete realization of [[Routing|routing]] when the routing targets are *agents* (not just tools or functions), and it is the structural entry point into [[MultiAgentCollaboration|multi-agent collaboration]].

In [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] Ch 2 ([[agentic-design-patterns-ch02-routing|Routing]]), both hands-on code examples *"simulate a basic delegation pattern often seen in multi-agent architectures"* — a coordinator that routes user requests to specialist handlers based on classified intent.

## How it works

A **coordinator/router** sits in front of N specialist sub-agents. The flow:

1. The coordinator classifies the request's intent (via [[Routing|LLM-, rule-, or embedding-based routing]]).
2. It selects the matching specialist and **passes the original request** to it (the *handoff*).
3. The specialist executes (often using its own [[ToolUse|tools]]) and returns a result.
4. A fallback/"unclear" handler catches requests that can't be confidently delegated.

The coordinator's instruction is explicitly *"do not try to answer the user directly"* — its only job is to analyze and delegate.

## Two framework realizations (Ch 2)

- **[[LangChain]] / [[LangGraph]]** — explicit, manual wiring. A `coordinator_router_chain` emits a decision string (`'booker' / 'info' / 'unclear'`); a **`RunnableBranch`** then routes the original request to the matching handler function. Delegation logic is visible and developer-controlled.
- **[[GoogleADK|Google ADK]]** — implicit, framework-managed. Defining a `Coordinator` `Agent` with `sub_agents=[booking_agent, info_agent]` enables **Auto-Flow**: ADK's internal logic performs LLM-driven delegation to the appropriate sub-agent automatically. Each sub-agent is equipped with `FunctionTool`-wrapped capabilities.

The contrast captures a broader architectural axis: **explicit computational-graph delegation** (LangGraph) vs **declarative capability-based delegation** (ADK Auto-Flow).

## Why it matters

Handoff/delegation is how agentic systems achieve **separation of concerns** at the agent level — each specialist is simpler, more reliable, and independently improvable, while the coordinator stays thin. It is the bridge from single-agent [[Routing|routing]] to full [[MultiAgentCollaboration|multi-agent systems]], and the mechanism behind dispatcher-style architectures (research systems routing among search/summarize/analyze agents, etc.).

## Connections

- [[agentic-design-patterns-ch02-routing]] — primary source.
- [[agentic-design-patterns-ch07-multi-agent]] — Ch 7 names **Sequential Handoffs** as a core *form* of [[MultiAgentCollaboration|multi-agent collaboration]] (one agent's output → the next, like a pipeline across distinct agents).
- [[Routing]] — handoff is routing where the targets are agents.
- [[MultiAgentCollaboration]] — the broader pattern handoff is the entry point to.
- [[AgenticDesignPatterns]] — book hub.
- [[GoogleADK]] — Auto-Flow declarative delegation via `sub_agents`.
- [[LangChain]] / [[LangGraph]] — explicit `RunnableBranch` / conditional-edge delegation.
- [[ToolUse]] — specialists act through tools.
- [[Orchestrator]] — analogous coordination role at the pipeline level.
- [[Agent]] / [[AgenticAI]] — the system context.
