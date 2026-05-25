---
title: "REST API"
type: concept
tags: [api, protocols, system-design, deployment]
sources: [leh-ch01-understanding-llm-twin-concept, leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
A **REST API** (Representational State Transfer Application Programming Interface) is an HTTP-based interface in which resources are exposed at URLs and manipulated with standard HTTP verbs (GET, POST, PUT, DELETE), typically exchanging [[JSON]] payloads. It is the dominant protocol for public-facing ML inference endpoints because of its ubiquity and ease of integration.

## In LLM Engineer's Handbook
[[leh-ch01-understanding-llm-twin-concept]] establishes the REST API as the client-facing protocol for the LLM Twin's inference pipeline. [[leh-ch10-inference-pipeline-deployment]] makes the trade-offs explicit: **REST is more accessible but slower** (JSON serialization overhead), while **[[gRPC]] with [[Protobuf]]** is faster on the wire and preferred for internal services within the same ML system. The chapter implements the LLM Twin's business microservice as a [[FastAPI]] application exposing `POST /rag` with [[Pydantic]] request/response schemas, and notes that LLM-style services such as ChatGPT and Claude often layer [[WebSockets]] or [[ServerSentEvents|Server-Sent Events]] on top for token streaming.

## Key details
- HTTP-based; resources at URLs; verbs GET/POST/PUT/DELETE/PATCH.
- Wire format typically [[JSON]] (text), making it human-readable but slower than binary alternatives.
- Public-facing client compatibility is the primary reason to choose REST over [[gRPC]].
- For streaming use cases (tokens, partial answers), REST is often augmented with SSE or WebSockets.
- FastAPI is the canonical Python framework the book uses to expose REST endpoints.

## Connections
- [[REST]] — the architectural style REST APIs implement.
- [[gRPC]] — the binary, schema-typed alternative for internal services.
- [[JSON]] — the dominant REST payload format.
- [[Protobuf]] — the gRPC schema format contrasted with JSON.
- [[WebSockets]] — alternative streaming protocol used by ChatGPT/Claude.
- [[ServerSentEvents]] — one-way streaming protocol used by TGI for token streaming.
- [[FastAPI]] — Python framework used for the LLM Twin's business microservice.
- [[ModelServing]] — the broader practice REST APIs enable.
- [[OnlineRealTimeInference]] — the deployment archetype REST APIs most often serve.
