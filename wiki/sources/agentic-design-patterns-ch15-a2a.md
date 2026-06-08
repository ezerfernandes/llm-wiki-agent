---
title: "Chapter 15 — Inter-Agent Communication / A2A (Agentic Design Patterns)"
type: source
tags: [agentic-design-patterns, agents, a2a, inter-agent-communication, multi-agent, protocol, interoperability, agent-card]
date: 2025-06-01
source_file: raw/books/agentic-design-patterns.pdf
sources: [agentic-design-patterns]
---

## Summary
Chapter 15 of [[AntonioGulli|Gulli's]] [[AgenticDesignPatterns|*Agentic Design Patterns*]] (PDF pp 231–245) presents **Inter-Agent Communication (A2A)** as the 15th of the book's 21 patterns: the discipline of letting diverse AI agents — potentially built on different frameworks ([[langgraph|LangGraph]], [[crewai|CrewAI]], [[GoogleADK|Google ADK]]) — collaborate via a common open standard. The chapter centers on **Google's Agent2Agent (A2A) protocol**, an open, HTTP(S)-based, [[JSONRPC|JSON-RPC 2.0]] standard, walking through its core actors (User / Client Agent / Remote Agent), the **[[AgentCard|Agent Card]]** digital-identity / capability-discovery file, asynchronous **tasks / messages / artifacts**, three interaction mechanisms (synchronous request-response, asynchronous polling, SSE streaming, plus webhook push notifications), and security (mTLS, audit logs, OAuth 2.0 / API-key credentials). It explicitly contrasts A2A (agent↔agent, *horizontal*) with [[ModelContextProtocol|MCP]] (agent↔tool, *vertical*), framing them as complementary layers, and ends with a runnable [[GoogleADK|ADK]]-based A2A "Calendar Agent" server.

## Key Claims
- **A2A is an open standard for agent interoperability.** It lets AI agents developed with different technologies (LangGraph, CrewAI, Google ADK) work together regardless of origin or framework, via seamless coordination, task delegation, and information exchange.
- **Industry backing is broad.** A2A is supported by Atlassian, Box, [[LangChain]], [[MongoDB]], [[Salesforce]], SAP, and ServiceNow; [[microsoft|Microsoft]] plans to integrate it into Azure AI Foundry and Copilot Studio; Auth0 and SAP are adding A2A support. (Historically the protocol was open-sourced by [[google|Google]] and later donated to the Linux Foundation.)
- **Three core actors.** *User* initiates requests; *A2A Client (Client Agent)* acts on the user's behalf; *A2A Server (Remote Agent)* exposes an HTTP endpoint, operating as an **"opaque" system** — the client need not understand its internal details.
- **The Agent Card is the unit of discovery.** A JSON file declaring identity, endpoint URL, version, capabilities (streaming, push notifications, state-transition history), skills (id/name/description/examples/tags), default input/output modes, and authentication requirements.
- **Discovery has three strategies.** Well-Known URI (`/.well-known/agent.json`), Curated Registries (centralized enterprise catalog), and Direct Configuration (embedded/private). Agent Card endpoints should be secured (access control, mTLS, network restrictions).
- **Communication is structured around asynchronous tasks.** Each task has a unique id and moves through states (submitted → working → completed/failed), supporting parallel processing of long-running work. Agents exchange **Messages** (attributes = key-value metadata + one or more **parts** carrying text/files/structured JSON); agent outputs are **artifacts** (also composed of parts, streamable incrementally). A server-generated **contextId** groups related tasks to preserve continuity.
- **All A2A traffic is HTTP(S) with JSON-RPC 2.0 payloads.** `sendTask` (a.k.a. `tasks/send`) is the synchronous single-answer method; `sendTaskSubscribe` (a.k.a. `tasks/sendSubscribe`) opens a persistent connection for incremental/streaming updates.
- **Four interaction mechanisms.** Synchronous request/response; asynchronous polling (server acks "working" + task id, client polls until completed/failed); SSE streaming updates (persistent one-way server→client push); webhook push notifications (server POSTs to a client-registered URL on significant status change). A2A is **modality-agnostic** — not just text but audio/video for rich multimodal apps.
- **A2A complements MCP.** MCP structures an agent's interaction with external data/tools (agent↔tool); A2A coordinates communication among agents (agent↔agent). The two are complementary, not competing.
- **Security is built in.** Mutual TLS (mTLS) for encrypted/authenticated connections, comprehensive audit logs, Agent Card authentication declarations, and credential handling via OAuth 2.0 tokens or API keys passed in HTTP headers (never URLs/bodies).
- **Rule of thumb.** Use A2A to orchestrate collaboration between two or more agents — especially across different frameworks — and when an agent must dynamically discover and consume another agent's capabilities.

## Key Quotes
> "The Agent2Agent (A2A) protocol is an open standard designed to enable communication and collaboration between different AI agent frameworks." — chapter overview
> "The remote agent operates as an 'opaque' system, meaning the client does not need to understand its internal operational details." — Core Actors (A2A Server)
> "An agent's digital identity is defined by its Agent Card, usually a JSON file." — Agent Card
> "All communication within the A2A framework is conducted over HTTP(S) using the JSON-RPC 2.0 protocol for payloads." — Communications and Tasks
> "While MCP focuses on structuring context for agents and their interaction with external data and tools, A2A facilitates coordination and communication among agents, enabling task delegation and collaboration." — A2A vs. MCP
> "A2A is modality-agnostic, meaning it can facilitate these interaction patterns not just for text, but also for other data types like audio and video." — Interaction Mechanisms

## Connections
- [[InterAgentCommunication]] — the pattern this chapter defines (created from this source; resolves long-standing forward-links).
- [[A2AProtocol]] — Google's Agent2Agent protocol, the concrete standard the chapter teaches.
- [[AgentCard]] — the capability-discovery / digital-identity sub-concept.
- [[AgenticDesignPatterns]] / [[AntonioGulli]] — book hub (pattern #15 of 21) and author.
- [[AgenticDesignPattern]] — the meta-concept catalog.
- [[MultiAgentCollaboration]] / [[multiagentsystems|Multi-Agent Systems]] — A2A is the communication substrate these patterns depend on (Ch 7).
- [[AgentCommunication]] — the agent characteristic A2A operationalizes.
- [[ModelContextProtocol]] — the complementary agent↔tool protocol (Ch 10); explicit MCP-vs-A2A contrast.
- [[JSONRPC]] — the wire protocol for A2A payloads.
- [[ServerSentEvents]] — the SSE streaming transport.
- [[GoogleADK|Google ADK]] / [[gemini|Gemini]] — framework + model of the hands-on Calendar Agent server.
- [[google|Google]] — author of the A2A protocol.
- [[microsoft|Microsoft]] / [[LangChain]] / [[MongoDB]] / [[Salesforce]] — named industry backers.
- [[AgentHandoff]] / [[TaskDecomposition]] — delegation mechanics A2A carries.

## Contradictions
- None found. The chapter's MCP-vs-A2A boundary agrees with the boundary note already on [[ModelContextProtocol]] (agent↔tool vs agent↔agent are complementary layers).
