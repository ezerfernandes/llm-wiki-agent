---
title: "JSON-RPC 2.0"
type: concept
tags: [protocols, networking, api, rpc, json, a2a, agents]
sources: [agentic-design-patterns-ch15-a2a]
last_updated: 2026-06-07
---

# JSON-RPC 2.0

**JSON-RPC 2.0** is a lightweight, stateless **remote procedure call (RPC) protocol** encoded in JSON. A client sends a request object naming a `method`, supplying `params`, and carrying an `id` for correlating the eventual response; the server returns a result (or error) tagged with the same `id`. It is transport-agnostic but most commonly carried over HTTP(S).

## Role in A2A
JSON-RPC 2.0 is the **payload format for [[A2AProtocol|Google's A2A protocol]]**: per [[AntonioGulli|Gulli]] ([[AgenticDesignPatterns|*Agentic Design Patterns*]] Ch 15), *"All communication within the A2A framework is conducted over HTTP(S) using the JSON-RPC 2.0 protocol for payloads."* The chapter's two canonical A2A methods are JSON-RPC calls:

- **`sendTask`** (a.k.a. `tasks/send`) — the **synchronous** method; the client asks for and expects a single, complete answer.
- **`sendTaskSubscribe`** (a.k.a. `tasks/sendSubscribe`) — the **streaming** method; it establishes a persistent connection (over [[ServerSentEvents|SSE]]) so the agent can send back multiple incremental updates / partial results over time.

Example synchronous request (abbreviated from the chapter):

```json
{
  "jsonrpc": "2.0",
  "id": "1",
  "method": "sendTask",
  "params": {
    "id": "task-001",
    "sessionId": "session-001",
    "message": { "role": "user", "parts": [ { "type": "text", "text": "What is the exchange rate from USD to EUR?" } ] },
    "acceptedOutputModes": ["text/plain"],
    "historyLength": 5
  }
}
```

## Why it matters
JSON-RPC's simplicity (named methods, structured params, request/response correlation by `id`) makes it a natural fit for the [[InterAgentCommunication|agent↔agent]] messaging A2A standardizes. It is also the wire style used by [[ModelContextProtocol|MCP]] (JSON-RPC-style `tools/call` over stdio or streamable HTTP) — so both of the book's interoperability protocols, agent↔agent and agent↔tool, share a JSON-RPC lineage.

## Connections
- [[A2AProtocol]] — uses JSON-RPC 2.0 over HTTP(S) for all payloads.
- [[InterAgentCommunication]] — the A2A pattern these RPC methods implement.
- [[ServerSentEvents|SSE]] — the streaming transport `sendTaskSubscribe` rides on.
- [[ModelContextProtocol|MCP]] — also JSON-RPC-style (`tools/call`); the agent↔tool counterpart.
- [[agentic-design-patterns-ch15-a2a]] — source page.
