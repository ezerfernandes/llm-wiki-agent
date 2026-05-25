---
title: "REST (Representational State Transfer)"
type: concept
tags: [api, protocols, architecture]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
**REST** (Representational State Transfer) is an architectural style for distributed systems in which clients manipulate server-side resources by exchanging representations (commonly [[JSON]]) over a stateless HTTP protocol, using standardized verbs and URLs. REST is the dominant style for public-facing web and ML APIs.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] contrasts REST with [[gRPC]] when discussing protocol choice for LLM serving: "REST is more accessible but slower" (JSON serialization overhead), while gRPC with [[Protobuf]] is faster on the wire and preferred for internal services within the same ML system at the cost of schema coupling. The chapter argues REST remains the right default for the client-facing surface of the LLM Twin's business microservice ([[FastAPI]] + `POST /rag`).

## Key details
- Architectural style (not a protocol per se), typically realized over HTTP/1.1 or HTTP/2.
- Stateless: every request must carry the information needed to fulfill it.
- Uniform interface: resources at URLs, manipulated with verbs.
- Wire format usually JSON; XML and other formats also valid but rare in modern APIs.
- Trade-off: maximal interoperability, lower wire performance than binary alternatives.

## Connections
- [[RESTAPI]] — concrete API style implementing REST.
- [[gRPC]] — binary, schema-typed alternative.
- [[JSON]] — dominant payload format.
- [[Protobuf]] — gRPC's binary schema format.
- [[ModelServing]] — the broader serving discipline REST supports.
- [[FastAPI]] — Python framework used to expose REST APIs in the book.
