---
title: "Application Load Balancer (ALB)"
type: concept
tags: [deployment, aws, networking, autoscaling]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
An **Application Load Balancer (ALB)** is AWS's Layer-7 (HTTP/HTTPS) load balancer that distributes incoming requests across a pool of backend replicas using a routing strategy (most commonly [[RoundRobinRouting|round-robin]]). It is the abstraction that lets autoscaling add or remove replicas without changing the client-facing endpoint.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] introduces the ALB as load-bearing for [[ApplicationAutoScaling]]: "Adding or removing new replicas doesn't affect the server and client communication protocol." Without an ALB, every scale-out event would force clients to discover and re-route to new replicas; with the ALB, the ALB's stable hostname is the only contact point and the autoscaling control plane manipulates the backend pool transparently.

## Key details
- Layer-7 (HTTP/HTTPS aware) — can route based on URL path, headers, host, query string.
- Most common policy: round-robin distribution across healthy replicas.
- Health checks: ALB probes each replica's `/health` endpoint and removes failing replicas from rotation.
- Sticky sessions optional — usually disabled for stateless inference.
- Pairs with [[ApplicationAutoScaling]] to provide the public-facing stability for elastic replica pools.

## Connections
- [[ApplicationAutoScaling]] — the AWS service ALB partners with for elasticity.
- [[RoundRobinRouting]] — the default routing strategy.
- [[ScalableTarget]] — the resource autoscaling adjusts behind the ALB.
- [[AWSSageMakerInferenceEndpoint]] / [[InferenceComponent]] — typical ALB-backed resources.
- [[MicroservicesArchitecture]] — the topology ALBs typically front.
- [[OnlineRealTimeInference]] — the deployment archetype ALBs serve.
