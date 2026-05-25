---
title: "Cooldown Period"
type: concept
tags: [deployment, aws, autoscaling, mlops]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
A **cooldown period** in autoscaling is the minimum interval that must elapse between scaling actions on the same resource. It exists to prevent rapid oscillation: after a scale-out (or scale-in) event, the policy is paused for the cooldown window so that the system has time to stabilize before the next decision.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] calls the cooldown period "the most important stability lever in autoscaling." Without it, a brief metric spike can trigger scale-out, the freshly-added replicas drive the metric below target, the policy triggers scale-in, and the system oscillates indefinitely. The chapter notes that both scale-out and scale-in get their own cooldown values, and that tuning cooldowns is part of the broader autoscaling-as-hyperparameter-tuning exercise — short cooldowns risk thrashing; long cooldowns risk slow response to real demand.

## Key details
- Two cooldowns per [[ScalingPolicy]]: scale-out cooldown and scale-in cooldown.
- Typical values: tens to hundreds of seconds, tuned by traffic shape.
- Short cooldown → fast response but oscillation risk.
- Long cooldown → stable but lagging response to spikes.
- Pairs with policy aggressiveness — tight target + short cooldown → over-scaling; loose target + long cooldown → under-scaling.

## Connections
- [[ApplicationAutoScaling]] — the parent service.
- [[ScalingPolicy]] / [[TargetTrackingScaling]] — the policies that carry cooldowns.
- [[ScalableTarget]] — the resource being scaled.
- [[GPUUtilization]] — common metric whose noise level dictates cooldown choice.
- [[ApplicationLoadBalancer]] — the front-end that absorbs the cooldown window without surfacing instability to clients.
