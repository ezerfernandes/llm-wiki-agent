---
title: "gRPC"
type: concept
tags: [api, protocols, networking, deployment]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
**gRPC** is Google's open-source high-performance RPC framework that uses HTTP/2 as transport and [[Protobuf]] (Protocol Buffers) for schema-typed binary serialization. Compared to [[REST]] + [[JSON]], gRPC is faster on the wire and statically typed, at the cost of schema coupling between client and server.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] contrasts gRPC with REST when discussing inter-service communication: "REST is more accessible but slower (JSON serialization); gRPC with protobuf is faster on the wire and preferred for internal services within the same ML system, at the cost of schema-coupling between client and server." The chapter notes that the LLM Twin's business microservice exposes REST (for client compatibility) but recommends gRPC for the lower-level internal call between the business microservice and the LLM microservice when latency budgets are tight.

## Key details
- Transport: HTTP/2 (multiplexed, persistent connections).
- Serialization: Protobuf (binary, schema-defined `.proto` files).
- Code generation: client + server stubs are generated from `.proto` schemas in every supported language.
- Streaming: built-in support for unary, server-streaming, client-streaming, and bidirectional streaming.
- Trade-off: schema coupling means client and server must agree on the `.proto` files; updates need versioning.

## Connections
- [[REST]] / [[RESTAPI]] — the text-based alternative.
- [[Protobuf]] — the schema/serialization format.
- [[JSON]] — REST's wire format, contrasted.
- [[WebSockets]] — alternative for bidirectional streaming use cases.
- [[ServerSentEvents]] — one-way streaming alternative.
- [[MicroservicesArchitecture]] — typical deployment topology where gRPC is used.
- [[ModelServing]] — the broader practice.
