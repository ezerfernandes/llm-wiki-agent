---
title: "Round-Robin Routing"
type: concept
tags: [networking, load-balancing, deployment]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
**Round-robin routing** is the simplest load-balancing strategy: incoming requests are distributed in turn to each available backend replica, cycling through the list. It assumes replicas are roughly homogeneous and that no request is significantly more expensive than another.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] cites round-robin as the typical routing policy on the [[ApplicationLoadBalancer]] in front of multi-replica SageMaker inference components. The implicit caveat for LLM serving — that round-robin assumes homogeneous request cost — is partially relaxed by [[ContinuousBatching|continuous batching]] inside each replica, which absorbs request-cost variance after dispatch.

## Key details
- Simplest dispatch strategy: stateless, no per-request awareness.
- Works well when replicas are identical and per-request cost variance is moderate.
- Alternatives: least-connections, weighted round-robin, latency-aware routing.
- Combined with health checks, removes unhealthy replicas from the rotation automatically.

## Connections
- [[ApplicationLoadBalancer]] — the AWS service implementing round-robin by default.
- [[ApplicationAutoScaling]] — the elasticity layer the load balancer serves.
- [[ContinuousBatching]] — softens round-robin's assumption that requests cost the same.
- [[MicroservicesArchitecture]] — the deployment topology where round-robin lives.
- [[OnlineRealTimeInference]] — the archetype this routing strategy serves.
