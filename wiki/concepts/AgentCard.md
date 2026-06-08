---
title: "Agent Card"
type: concept
tags: [agents, a2a, inter-agent-communication, capability-discovery, agent-card, protocol, agentic-design-patterns]
sources: [agentic-design-patterns-ch15-a2a]
last_updated: 2026-06-07
---

# Agent Card

An **Agent Card** is an agent's **digital identity** in the [[A2AProtocol|A2A protocol]] — usually a **JSON file** that declares the key information other agents need to discover, understand, and interact with it. It is the unit of **automatic capability discovery** in [[InterAgentCommunication|Inter-Agent Communication]] ([[AntonioGulli|Gulli]], [[AgenticDesignPatterns|*Agentic Design Patterns*]] Ch 15): a client reads a remote agent's card to learn what it can do and how to reach it, without needing to understand the remote agent's internal operation (the remote agent is "opaque").

## What it declares
- **Identity** — the agent's `name` and `description`.
- **Endpoint** — the `url` where the A2A server is reachable.
- **`version`** — the agent/interface version.
- **`capabilities`** — feature flags such as `streaming`, `pushNotifications`, and `stateTransitionHistory`.
- **`authentication`** — supported auth `schemes` (e.g. `apiKey`, OAuth 2.0).
- **`defaultInputModes` / `defaultOutputModes`** — e.g. `["text"]` (A2A is modality-agnostic, so audio/video are possible).
- **`skills`** — a list, each with `id`, `name`, `description`, `inputModes`/`outputModes`, `examples`, and `tags` (e.g. a `get_current_weather` skill, or a `check_availability` skill).

```json
{
  "name": "WeatherBot",
  "description": "Provides accurate weather forecasts and historical data.",
  "url": "http://weather-service.example.com/a2a",
  "version": "1.0.0",
  "capabilities": { "streaming": true, "pushNotifications": false, "stateTransitionHistory": true },
  "authentication": { "schemes": ["apiKey"] },
  "defaultInputModes": ["text"],
  "defaultOutputModes": ["text"],
  "skills": [ { "id": "get_current_weather", "name": "Get Current Weather", "...": "..." } ]
}
```

## Discovery & security
Clients find Agent Cards via three strategies:
- **Well-Known URI** — hosted at a standardized path (e.g. `/.well-known/agent.json`); broad, automated, public/domain-specific access.
- **Curated Registries** — a centralized, queryable catalog; suited to enterprises needing centralized management and access control.
- **Direct Configuration** — embedded or privately shared; for closely-coupled/private systems where dynamic discovery isn't crucial.

Regardless of method, card endpoints should be secured (access control, mutual TLS, network restrictions). The card also **declares authentication requirements explicitly**, centralizing and simplifying auth management — though the card holds only non-secret information (actual credentials travel in HTTP headers).

## Why it matters
The Agent Card is what makes A2A's **dynamic discovery** possible: it lets agents advertise their skills and lets clients consume those skills at runtime rather than hard-coding integrations. It is the agent↔agent analog of an OpenAPI/service descriptor, and the structural counterpart to [[ModelContextProtocol|MCP's]] server capability manifest (MCP's `list_tools` discovery) — but for whole agents rather than individual tools.

## Connections
- [[InterAgentCommunication]] — the pattern the Agent Card belongs to.
- [[A2AProtocol]] — the protocol that defines the Agent Card.
- [[ModelContextProtocol|MCP]] — the agent↔tool analog; MCP's tool manifest plays a similar discovery role one layer down.
- [[GoogleADK|Google ADK]] — the hands-on example builds an `AgentCard(...)` for a Calendar Agent.
- [[agentic-design-patterns-ch15-a2a]] — source page.
