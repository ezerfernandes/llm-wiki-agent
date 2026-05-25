---
title: "Application Auto Scaling"
type: concept
tags: [deployment, aws, autoscaling, mlops]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
**AWS Application Auto Scaling** is the AWS control plane that automatically adjusts the replica count of scalable AWS resources (SageMaker inference components, DynamoDB tables, ECS services, etc.) based on tracked metrics. It is the recommended elasticity mechanism for [[AWSSageMakerInferenceEndpoint|SageMaker inference endpoints]] hosting LLMs.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] devotes its closing section to Application Auto Scaling because static replica counts either burn money in idle periods or fail users during spikes. The chapter walks through the two-step configuration: (1) **register a scalable target** (resource ID, service namespace, scalable dimension, MinCapacity / MaxCapacity), and (2) **create a scaling policy** (e.g., [[TargetTrackingScaling]]) with a chosen metric like `SageMakerInferenceComponentInvocationsPerCopy` or a GPU-utilization target (~70%). The chapter's worked-example trajectory: idle → 1 replica (or scale-to-zero); ~10 RPS → 2 replicas; spike to 100 RPS → 20 replicas. Tuning autoscaling is analogous to **hyperparameter tuning** — stress-test in dev/test until the sweet spot between cost, latency, and throughput is found for both average and outlier traffic profiles.

## Key details
- Two-step setup: register scalable target → attach scaling policy.
- Tracks CloudWatch metrics; the policy reacts when the metric breaches its target.
- Cooldown period prevents oscillation by delaying both scale-out and scale-in.
- Failure modes: **over-scaling** (too aggressive policy / too short cooldown → idle replicas → cost blowup) and **under-scaling** (too conservative → user-experience degradation).
- An [[ApplicationLoadBalancer]] sits in front so replica count changes are invisible to clients.
- Always delete the endpoint after testing to avoid runaway pay-as-you-go GPU costs.

## Connections
- [[Autoscaling]] — broader concept.
- [[ScalableTarget]] — step 1's registered resource.
- [[ScalingPolicy]] — step 2's policy.
- [[TargetTrackingScaling]] — the canonical scaling-policy type.
- [[CooldownPeriod]] — the stability lever.
- [[GPUUtilization]] — alternative target metric.
- [[ApplicationLoadBalancer]] — the front-end abstraction.
- [[AWSSageMakerInferenceEndpoint]] / [[InferenceComponent]] — the scaling targets.
- [[AmazonCloudWatch]] — host of the metrics + alarms.
- [[ModelServing]] — the practice autoscaling supports.
