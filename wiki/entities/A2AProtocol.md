---
title: "A2A Protocol (Agent2Agent)"
type: entity
tags: [protocol, agents, a2a, inter-agent-communication, open-standard, google, linux-foundation, interoperability, agentic-design-patterns]
sources: [agentic-design-patterns-ch15-a2a]
last_updated: 2026-06-07
---

# A2A Protocol (Agent2Agent)

**A2A (Agent2Agent)** is an **open standard, originally authored by [[google|Google]]**, designed to enable communication and collaboration between different AI agent frameworks. It ensures **interoperability**, allowing AI agents developed with technologies like [[langgraph|LangGraph]], [[crewai|CrewAI]], or [[GoogleADK|Google ADK]] to work together regardless of their origin or framework differences. A2A is the concrete realization of the [[InterAgentCommunication|Inter-Agent Communication]] pattern taught in [[AntonioGulli|Gulli's]] [[AgenticDesignPatterns|*Agentic Design Patterns*]], Chapter 15.

## What it is
A2A is an **HTTP(S)-based protocol using [[JSONRPC|JSON-RPC 2.0]]** for payloads. Its foundational pillars: three **Core Actors** (User / A2A Client / A2A Server), the **[[AgentCard|Agent Card]]** digital-identity & discovery file, **Agent Discovery** (Well-Known URI / Curated Registry / Direct Configuration), **Communication & Tasks** (asynchronous tasks with state machines; Messages with parts; streamable artifacts; a server-generated `contextId`), **Interaction Mechanisms** (synchronous request/response via `sendTask`, asynchronous polling, [[ServerSentEvents|SSE]] streaming via `sendTaskSubscribe`, webhook push notifications), and **Security** (mTLS, audit logs, OAuth 2.0 / API-key credentials in HTTP headers). It is **modality-agnostic** (text, audio, video). Full protocol mechanics live on the [[InterAgentCommunication]] concept page.

## Governance & adoption
- **Open-source**, welcoming community contributions to drive its evolution. (Google later donated the A2A project to the **Linux Foundation** to vendor-neutralize its governance.)
- Backed by a broad set of technology companies and service providers: **Atlassian, Box, [[LangChain]], [[MongoDB]], [[Salesforce]], SAP, ServiceNow**.
- [[microsoft|Microsoft]] plans to integrate A2A into **Azure AI Foundry** and **Copilot Studio**; **Auth0** and **SAP** are integrating A2A into their platforms/agents.
- Reference implementations: the **Google A2A GitHub repository** (`github.com/google-a2a/A2A` and `a2a-samples`) — examples in Java, Go, and Python showing LangGraph, CrewAI, Azure AI Foundry, and AG2 ([[autogen|AutoGen]]) agents communicating; Apache-2.0 licensed. The protocol spec is published at `a2a-protocol.org`.

## Relationship to MCP
A2A **complements** [[ModelContextProtocol|Anthropic's MCP]]: A2A is the **agent ↔ agent** (horizontal) coordination layer; MCP is the **agent ↔ tool/data** (vertical) access layer. They are designed to coexist.

## Connections
- [[InterAgentCommunication]] — the design pattern A2A realizes; full mechanics.
- [[AgentCard]] — A2A's capability-discovery file.
- [[ModelContextProtocol]] — the complementary agent↔tool protocol.
- [[JSONRPC]] / [[ServerSentEvents]] — A2A's wire protocol and streaming transport.
- [[google|Google]] — protocol author; [[GoogleADK|Google ADK]] — Google's agent framework that hosts A2A servers.
- [[AgenticDesignPatterns]] / [[AntonioGulli]] — book hub and author.
- [[agentic-design-patterns-ch15-a2a]] — source page.
