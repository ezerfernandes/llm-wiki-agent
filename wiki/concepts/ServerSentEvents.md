---
title: "Server-Sent Events (SSE)"
type: concept
tags: [api, protocols, networking, streaming]
sources: [leh-ch10-inference-pipeline-deployment, dspy-deployment-tutorial, agentic-design-patterns-ch15-a2a]
last_updated: 2026-06-07
---

## Definition
**Server-Sent Events (SSE)** is a one-way streaming protocol that lets a server push a continuous stream of text events to a client over a single HTTP connection. It is the dominant protocol for LLM token streaming because it is simpler than [[WebSockets]] (one-way only, plain HTTP) and works through standard proxies and load balancers without special handling.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] cites SSE as the protocol used by [[TextGenerationInference|TGI]] (Hugging Face's serving engine) to stream tokens to clients in the LLM Twin's SageMaker deployment: "safetensors fast loading, and SSE token streaming." The chapter notes that SSE is the natural pair for LLM completion APIs because the use case is unidirectional (server → client, token by token) and the simpler protocol matches the deployment topology.

## In DSPy
[[dspy-deployment-tutorial|The DSPy Deployment tutorial]] specifies SSE as the canonical web-layer transport for [[DSPyStreaming|`dspy.streamify`]]-wrapped programs. Pattern: `dspy.utils.streaming.streaming_response(stream)` converts the DSPy chunk union (`StreamResponse | StatusMessage | Prediction`) into properly framed SSE text, wrapped in [[FastAPI]]'s `StreamingResponse(..., media_type="text/event-stream")`. Closes [[DSPyStreaming|the Streaming concept page's]] forward reference to *"natural transports for the streaming generator at the web layer."*

## In A2A (Agentic Design Patterns, Gulli — Ch 15)
SSE is one of [[A2AProtocol|A2A]]'s four interaction mechanisms — the **Streaming Updates** mode. The [[JSONRPC|JSON-RPC]] `sendTaskSubscribe` (`tasks/sendSubscribe`) method opens a persistent, one-way server→client SSE connection so a remote agent can continuously push status changes or partial results without the client making repeated requests — the same unidirectional-push fit SSE has for LLM token streaming, applied to [[InterAgentCommunication|agent↔agent]] task updates. SSE support is advertised by an agent's [[AgentCard|Agent Card]] (`capabilities.streaming`). The contrast partner in A2A is webhook **push notifications** (server POSTs to a client-registered URL) for very long-running tasks.

## Key details
- One-way: server-to-client only.
- Standard HTTP — works through CDNs, proxies, load balancers, and corporate firewalls.
- MIME type `text/event-stream`; messages framed by `data:` lines and double-newlines.
- Built-in automatic reconnect by the EventSource browser API.
- Simpler than WebSockets when you only need server-push.
- Used by OpenAI's, Anthropic's, and TGI's streaming endpoints.

## Connections
- [[WebSockets]] — the bidirectional streaming alternative.
- [[REST]] / [[RESTAPI]] — the request/response baseline SSE extends.
- [[TextGenerationInference]] — the HuggingFace serving engine using SSE.
- [[OnlineRealTimeInference]] — the archetype SSE serves for streaming UX.
- [[ContinuousBatching]] — the server-side optimization that pairs with SSE to stream from a busy inference engine.
- [[TTFT]] / [[TPOT]] — the latency metrics SSE makes observable to the client.
- [[ModelServing]] — the broader practice.
- [[A2AProtocol]] / [[InterAgentCommunication]] — A2A uses SSE for its streaming `sendTaskSubscribe` mode.
- [[JSONRPC]] — the RPC layer whose `sendTaskSubscribe` rides on SSE.
