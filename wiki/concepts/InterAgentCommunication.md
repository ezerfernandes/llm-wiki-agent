---
title: "Inter-Agent Communication (A2A)"
type: concept
tags: [agentic-design-patterns, agents, a2a, inter-agent-communication, multi-agent, protocol, interoperability, agent-card, pattern]
sources: [agentic-design-patterns-ch15-a2a]
last_updated: 2026-06-07
---

# Inter-Agent Communication (A2A)

**Inter-Agent Communication (A2A)** is the **15th [[AgenticDesignPatterns|agentic design pattern]]** ([[AntonioGulli|Gulli]], Ch 15): the discipline of letting **diverse AI agents — potentially built on different frameworks — collaborate through a common, open, standardized protocol**. Where a single agent hits limits on complex, multi-faceted problems, A2A enables seamless coordination, **task delegation**, and information exchange across agents regardless of their underlying technology. This concept page is the wiki's canonical anchor for the pattern; many pages ([[MultiAgentCollaboration]], [[multiagentsystems|Multi-Agent Systems]], [[AgentCommunication]], [[ModelContextProtocol|MCP]], [[AgenticDesignPattern]], the [[AgenticDesignPatterns|book hub]]) forward-link `[[InterAgentCommunication]]`; this page resolves those references.

The chapter centers on **[[A2AProtocol|Google's Agent2Agent (A2A) protocol]]** as the concrete realization — an open standard letting agents developed with [[langgraph|LangGraph]], [[crewai|CrewAI]], or [[GoogleADK|Google ADK]] interoperate.

## The problem it solves
Individual AI agents struggle with complex, multi-faceted problems on their own, and the core obstacle to combining them is **the lack of a common language or protocol**. Without a standard, integrating disparate agents is costly and time-consuming, blocking the creation of sophisticated systems where specialized agents combine their unique skills. A2A supplies that universal standard, fostering a **modular, scalable ecosystem** for multi-agent systems.

This is the explicit dependency [[MultiAgentCollaboration|Multi-Agent Collaboration]] (Ch 7) names: multi-agent efficacy "is not merely due to the division of labor but is **critically dependent on the mechanisms for inter-agent communication**," requiring a standardized communication protocol and a shared ontology. A2A is the pattern that supplies that protocol.

## Core concepts of A2A
The protocol provides a structured approach for agent interactions built on several foundational pillars: **Core Actors, Agent Card, Agent Discovery, Communication & Tasks, Interaction Mechanisms, and Security.**

### Core actors
A2A involves three main entities:
1. **User** — initiates requests for agent assistance.
2. **A2A Client (Client Agent)** — an application or AI agent acting on the user's behalf to request actions or information.
3. **A2A Server (Remote Agent)** — an AI agent/system exposing an HTTP endpoint that processes client requests and returns results. The remote agent is an **"opaque" system**: the client does not need to understand its internal operational details — only its declared interface.

### Agent Card (capability discovery)
An agent's digital identity is defined by its **[[AgentCard|Agent Card]]**, usually a JSON file declaring identity, endpoint **URL**, **version**, supported **capabilities** (`streaming`, `pushNotifications`, `stateTransitionHistory`), **authentication** schemes, default input/output **modes**, and a list of **skills** (each with id, name, description, examples, tags). It is the unit of automatic **discovery** and interaction — other agents read an Agent Card to learn what a remote agent can do and how to reach it.

**Discovery strategies:**
- **Well-Known URI** — host the card at a standardized path (e.g. `/.well-known/agent.json`); broad, automated accessibility for public/domain-specific use.
- **Curated Registries** — a centralized catalog of cards queryable by criteria; suited to enterprises needing centralized management and access control.
- **Direct Configuration** — card info embedded or privately shared; for closely-coupled/private systems where dynamic discovery isn't crucial.

Card endpoints should be secured (access control, mTLS, network restrictions) even though the card itself holds non-secret information.

### Communication & tasks
Communication is structured around **asynchronous tasks** — the fundamental units of work for long-running processes. Each task has a unique identifier and moves through states (**submitted → working → completed / failed**), enabling parallel processing in complex operations. Agents communicate via a **Message**, which carries **attributes** (key-value metadata such as priority or creation time) and one or more **parts** (the actual content — plain text, files, or structured JSON). The tangible outputs an agent generates during a task are **artifacts** (distinct from the MLOps [[Artifact]] concept); artifacts are likewise composed of parts and can be **streamed incrementally** as results become available. A server-generated **`contextId`** groups related tasks to preserve continuity across multiple interactions.

All A2A communication runs over **HTTP(S)** with **[[JSONRPC|JSON-RPC 2.0]]** payloads. The synchronous `sendTask` (`tasks/send`) method asks for a single complete answer; `sendTaskSubscribe` (`tasks/sendSubscribe`) establishes a persistent connection for incremental/streaming updates.

### Interaction mechanisms
A2A offers multiple interaction methods, each with a distinct mechanism:
- **Synchronous Request/Response** — for quick, immediate operations; the client sends a request and waits for a complete response in one exchange.
- **Asynchronous Polling** — for longer tasks; the server immediately acks with a "working" status + task id, and the client periodically polls until the task is "completed" or "failed."
- **Streaming Updates ([[ServerSentEvents|Server-Sent Events / SSE]])** — a persistent one-way server→client connection lets the remote agent continuously push status changes or partial results without repeated client requests.
- **Push Notifications (Webhooks)** — for very long-running/resource-intensive tasks; the client registers a webhook URL and the server POSTs an async "push" on significant status changes (e.g., completion).

A2A is **modality-agnostic** — it facilitates these patterns not just for text but for audio and video, enabling rich multimodal applications. The Agent Card declares whether an agent supports streaming and/or push notifications.

### Security
- **Mutual TLS (mTLS)** — encrypted, authenticated connections preventing unauthorized access and interception.
- **Comprehensive Audit Logs** — all inter-agent communications recorded (information flow, agents, actions) for accountability, troubleshooting, and security analysis.
- **Agent Card Declaration** — authentication requirements declared explicitly in the card, centralizing auth management.
- **Credential Handling** — agents authenticate with OAuth 2.0 tokens or API keys passed via **HTTP headers** (never URLs or message bodies), preventing credential exposure.

## A2A vs. MCP
A2A **complements** [[ModelContextProtocol|Anthropic's Model Context Protocol (MCP)]] rather than competing with it. The book draws the line cleanly:

| Axis | A2A (Ch 15) | MCP (Ch 10) |
|---|---|---|
| **Direction** | **Agent ↔ Agent** (horizontal) | **Agent ↔ Tool / Data** (vertical) |
| **Purpose** | Coordination, task delegation, collaboration *among agents* | Structuring an agent's context + access to external data and tools |
| **Topology** | Source Agent ↔ A2A protocol ↔ Target Agent(s) | Source Agent ↔ MCP ↔ Tools (browser, filesystem, vector DB, APIs) |
| **Layer** | High-level task/workflow protocol between agents | Standardized interface for an LLM to reach external resources |

The two are complementary layers: MCP standardizes how an agent reaches its tools; A2A standardizes how agents coordinate with each other. (See the matching boundary note on [[ModelContextProtocol]].)

## Practical applications
- **Multi-Framework Collaboration** — the primary use case: independent agents (ADK, LangGraph, CrewAI) communicate and collaborate regardless of framework, each specializing in a different aspect of a problem.
- **Automated Workflow Orchestration** — in enterprises, agents delegate and coordinate tasks (e.g., data-collection agent → analysis agent → report-generation agent), all over A2A.
- **Dynamic Information Retrieval** — a primary agent requests live data from a specialized "data fetching agent" that uses external APIs and returns the result.

## Hands-on (Google ADK)
The chapter builds an A2A-compliant **Calendar Agent** server on [[GoogleADK|Google ADK]]: an `LlmAgent` (`gemini-2.0-flash-001`) with a `CalendarToolset` (Google Calendar API) is described by an `AgentCard` (name, description, `url`, `version`, default input/output modes, `AgentCapabilities(streaming=True)`, and a `check_availability` `AgentSkill`). A `Runner` wires in-memory artifact/session/memory services; an `ADKAgentExecutor` + `DefaultRequestHandler` feed an `A2AStarletteApplication`, which is mounted on a Starlette app (with an OAuth `/authenticate` route) and served via [[Uvicorn|uvicorn]]. Reference samples live at the Google A2A GitHub repo (Java, Go, Python; LangGraph, CrewAI, Azure AI Foundry, AG2 examples), Apache-2.0 licensed.

## Rule of thumb
Use Inter-Agent Communication when you need to **orchestrate collaboration between two or more agents** — especially across different frameworks (Google ADK, LangGraph, CrewAI) — and when an agent must **dynamically discover and consume the capabilities of other agents** to complete a task.

## Connections
- [[A2AProtocol]] — Google's Agent2Agent protocol; the concrete open standard this pattern teaches.
- [[AgentCard]] — the capability-discovery / digital-identity file at the center of A2A.
- [[AgenticDesignPatterns]] / [[AntonioGulli]] — book hub (pattern #15 of 21) and author.
- [[AgenticDesignPattern]] — the meta-concept catalog of reusable agent patterns.
- [[MultiAgentCollaboration]] / [[multiagentsystems|Multi-Agent Systems]] — what A2A makes possible; the pattern that names inter-agent communication as a hard dependency.
- [[AgentCommunication]] — the agent *characteristic* A2A operationalizes into a concrete protocol.
- [[ModelContextProtocol|MCP]] — the complementary agent↔tool protocol (Ch 10).
- [[JSONRPC]] — the JSON-RPC 2.0 wire protocol for A2A payloads.
- [[ServerSentEvents|SSE]] — the streaming-updates transport.
- [[AgentHandoff]] / [[TaskDecomposition]] — delegation mechanics A2A carries between agents.
- [[GoogleADK|Google ADK]] / [[gemini|Gemini]] — framework + model of the hands-on Calendar Agent.
- [[google|Google]] — author of the A2A protocol.
- [[Artifact]] — disambiguation: A2A "artifacts" (task outputs made of parts) are distinct from the MLOps artifact concept.
- [[agentic-design-patterns-ch15-a2a]] — source page (Ch 15, pp 231–245).
