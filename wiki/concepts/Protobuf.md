---
title: "Protobuf (Protocol Buffers)"
type: concept
tags: [api, serialization, formats]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
**Protocol Buffers (Protobuf)** is Google's binary, schema-defined serialization format that pairs with [[gRPC]] for high-performance RPC. Developers describe data structures in `.proto` files, and `protoc` generates strongly-typed client + server stubs in every supported language.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] cites Protobuf as the schema/serialization layer that makes [[gRPC]] faster than [[REST]] + [[JSON]] for inter-service ML communication. The chapter recommends gRPC + Protobuf for internal microservice traffic (e.g., business microservice → LLM microservice) and reserves JSON for the public-facing API where client compatibility dominates.

## Key details
- Binary on the wire — much smaller and faster to (de)serialize than JSON.
- Schemas in `.proto` files; the same schema generates client + server stubs in many languages.
- Backwards/forwards compatibility via numbered fields and optional / repeated modifiers.
- Strongly typed: serialization errors surface at compile time, not at runtime.
- Schema coupling: any change requires regenerating and redeploying stubs in every consumer.

## Connections
- [[gRPC]] — the RPC framework Protobuf is paired with.
- [[JSON]] — the text-based alternative.
- [[REST]] / [[RESTAPI]] — the protocol JSON serves; Protobuf is the gRPC alternative.
- [[MicroservicesArchitecture]] — the deployment topology where Protobuf is most valuable.
- [[ModelServing]] — the broader practice.
