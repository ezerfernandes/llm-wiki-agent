---
title: "AWS Application Load Balancer"
type: entity
tags: [product, aws, networking, load-balancer, cloud]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## What it is
AWS Application Load Balancer (ALB) is a Layer-7 HTTP/HTTPS load balancer in the AWS Elastic Load Balancing family. It distributes requests across backend targets using strategies like round-robin or least-outstanding-requests.

## In LLM Engineer's Handbook
Ch. 10 ([[leh-ch10-inference-pipeline-deployment]]) explains that an ALB sits in front of multi-replica SageMaker inference endpoints with round-robin routing, so that adding or removing replicas through Application Auto Scaling does not change the client-facing endpoint URL — a load-bearing abstraction for the autoscaling story.

## Connections
- [[AmazonSageMaker]] — endpoint behind the ALB.
- [[ApplicationAutoScaling]] — uses the ALB to keep the URL stable across replica changes.
- [[RoundRobinRouting]] — the default routing strategy in the chapter.
- [[Amazon]] — parent.
