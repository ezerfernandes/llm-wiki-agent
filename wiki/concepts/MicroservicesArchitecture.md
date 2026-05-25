---
title: "Microservices Architecture"
type: concept
tags: [architecture, system-design, deployment]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
**Microservices architecture** decomposes an application into a collection of small, independently deployable services that communicate over the network (REST, gRPC, message queues). Each service owns its data, runs in its own process, and can be scaled and updated independently — at the cost of operational complexity and network-hop latency.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] is the canonical chapter for ML-serving microservices. The LLM Twin is split into two microservices: a **FastAPI business service** that handles [[rag|RAG]] retrieval and prompt augmentation, and an **[[AWSSageMakerInferenceEndpoint|AWS SageMaker]] LLM microservice** that runs the fine-tuned model inside a Hugging Face DLC powered by [[TextGenerationInference|TGI]]. The split is justified by the GPU/CPU asymmetry: the LLM microservice is GPU-bound and expensive (A100/V100/A10G), while the business logic is CPU/I-O-bound and cheap; coupling them in a [[MonolithicArchitecture|monolith]] wastes GPU time during business-logic execution. The chapter argues a pragmatic migration path: **start monolithic, design for modularity (separate Python modules or packages), then split into services later** — failing to design modularly forces a rewrite during the transition.

## Key details
- Each service can use a heterogeneous tech stack — LLM in Rust/C++/ONNX/TensorRT, business logic in Python.
- Decouples GPU (model) from CPU (business) scaling.
- Network hops add latency; the savings from independent scaling typically dominate.
- Communication patterns: REST (public-facing), gRPC + Protobuf (internal high-performance), message queues (asynchronous), WebSockets / SSE (streaming).
- Service mesh, distributed tracing, and centralized observability become harder.

## Connections
- [[MonolithicArchitecture]] — the alternative the chapter contrasts microservices against.
- [[RESTAPI]] / [[gRPC]] — common inter-service protocols.
- [[FastAPI]] — Python framework used for the LLM Twin business microservice.
- [[ApplicationLoadBalancer]] — typical front-end for microservice replicas.
- [[ApplicationAutoScaling]] — the elasticity layer microservices depend on.
- [[OnlineRealTimeInference]] — the archetype microservices typically implement for LLMs.
- [[ModelServing]] — the broader practice microservices support.
- [[InferenceComponent]] — SageMaker's microservice-shaped resource.
