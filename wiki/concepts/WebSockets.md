---
title: "WebSockets"
type: concept
tags: [api, protocols, networking, streaming]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
**WebSockets** is a bidirectional, full-duplex communication protocol that runs over a single long-lived TCP connection (initiated via HTTP upgrade). It is the canonical transport for real-time, interactive applications — chat, multiplayer games, live trading — and one of the protocols LLM providers use to stream tokens.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] cites WebSockets as the protocol that products like ChatGPT and Claude use for token streaming: "LLM-style services such as **ChatGPT** and **Claude** often use **WebSockets** to stream individual tokens (Server-Sent Events / SSE), improving perceived responsiveness in real-time inference." The chapter contrasts WebSockets (bidirectional) with [[ServerSentEvents]] (one-way server-to-client) — both improve perceived latency over plain REST request/response by surfacing tokens as they generate, but only WebSockets supports interactive bidirectional flows.

## Key details
- Bidirectional: both client and server can push messages at any time.
- Long-lived TCP connection avoids per-request HTTP overhead.
- Initiated via HTTP/1.1 `Upgrade: websocket` handshake.
- Common alternative for one-way streaming: [[ServerSentEvents]] (simpler, HTTP-friendly).
- Trade-off: more complex than HTTP polling; firewalls / proxies sometimes block long-lived upgrades.

## Connections
- [[ServerSentEvents]] — the one-way streaming alternative.
- [[REST]] / [[RESTAPI]] — the stateless request/response baseline.
- [[gRPC]] — the schema-typed alternative with built-in bidirectional streaming.
- [[OnlineRealTimeInference]] — the archetype WebSockets serves for streaming LLM UX.
- [[ModelServing]] — the broader practice.
- [[ChatGPT]] / [[anthropic]] — products that use WebSockets for token streaming.
