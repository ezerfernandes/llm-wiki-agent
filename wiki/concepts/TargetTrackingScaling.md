---
title: "Target Tracking Scaling"
type: concept
tags: [deployment, aws, autoscaling, mlops]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
**Target tracking scaling** is the AWS Application Auto Scaling policy type that adjusts replica count to keep a tracked CloudWatch metric at (or near) a target value. The scaling group autonomously adds replicas when the metric is above target and removes them when it is below — no explicit step thresholds required.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] uses target tracking as the canonical scaling-policy type for the LLM Twin's SageMaker inference component. Two example tracking metrics: **`SageMakerInferenceComponentInvocationsPerCopy`** (the recommended invocation-density metric) and **GPU utilization** (target ~70% to leave headroom for spikes while limiting idle cost). The chapter argues target tracking is the right default because its math is simpler than step-based scaling and CloudWatch alarms are managed automatically — you specify metric + target value and the policy infers the alarms.

## Key details
- Policy type: `TargetTrackingScaling`.
- Inputs: metric name, target value, scale-in cooldown, scale-out cooldown, MinCapacity / MaxCapacity (on the [[ScalableTarget]]).
- AWS auto-generates the underlying CloudWatch alarms.
- Common LLM-serving metrics: `SageMakerInferenceComponentInvocationsPerCopy`, `GPUUtilization`.
- Pairs with a [[CooldownPeriod]] to prevent oscillation.

## Connections
- [[ApplicationAutoScaling]] — the parent service.
- [[ScalableTarget]] — the resource being scaled.
- [[ScalingPolicy]] — the broader category (target tracking is one of three types alongside step and scheduled scaling).
- [[CooldownPeriod]] — the stability lever.
- [[GPUUtilization]] — common target metric for LLM serving.
- [[AmazonCloudWatch]] — the metric/alarm host.
- [[InferenceComponent]] / [[AWSSageMakerInferenceEndpoint]] — the typical resources scaled.
