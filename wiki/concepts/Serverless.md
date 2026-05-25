---
title: "Serverless"
type: concept
tags: [cloud, architecture, deployment]
sources: [leh-ch02-tooling-and-installation]
last_updated: 2026-05-22
---

## Definition
**Serverless** is a deployment model in which the cloud provider manages all server provisioning, scaling, patching, and capacity; the user supplies only code (or model) and is billed per request or per execution-second. Serverless products hide infrastructure entirely — no instance types, no auto-scaling rules — at the cost of less control over runtime customization.

## In LLM Engineer's Handbook
[[leh-ch02-tooling-and-installation]] uses "serverless" to describe two distinct things: ZenML Cloud (the trial offering that hides ZenML server self-hosting) and AWS [[AmazonBedrock|Bedrock]] (a serverless LLM API). The chapter explicitly rejects Bedrock for the book's project: "Bedrock would have been an excellent solution for quickly prototyping something, but this is a book on LLM engineering, and our goal is to dig into all the engineering aspects that Bedrock tries to mask away." This captures the central trade-off — serverless gives speed-to-prototype at the cost of teaching opportunity and runtime customization. The book chooses [[AmazonSageMaker|SageMaker]] instead because SageMaker exposes pay-as-you-go training and real-time inference endpoints with full customization.

## Key details
- No server provisioning by the user; the platform manages capacity.
- Billing is per-invocation or per-second of execution, not per-hour-of-instance.
- Cold-start latency is the primary technical downside.
- Customization (custom CUDA kernels, custom model code, custom runtime libs) is often impossible or expensive.
- Examples: AWS Lambda, AWS Bedrock, Google Cloud Functions, ZenML Cloud's hosted control plane.

## Connections
- [[AmazonBedrock]] / [[GoogleCloudVertexAI]] / [[AzureOpenAI]] — serverless LLM API products.
- [[AmazonSageMaker]] — the non-serverless alternative chosen by the book for customization.
- [[ModelServing]] — the broader practice serverless products implement.
- [[OnlineRealTimeInference]] — the deployment archetype serverless LLM APIs typically serve.
- [[ApplicationAutoScaling]] — the mechanism non-serverless deployments use to approximate elastic capacity.
