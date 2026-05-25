---
title: "Scaling Policy"
type: concept
tags: [deployment, aws, autoscaling, mlops]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
A **scaling policy** is an AWS Application Auto Scaling configuration that specifies when and how a [[ScalableTarget]] should change capacity. The three policy types are **target tracking** (keep a metric at a target value), **step scaling** (defined thresholds), and **scheduled scaling** (cron-style time-based capacity).

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] introduces scaling policies as step 2 of the two-step autoscaling configuration: after registering a [[ScalableTarget]], attach one or more scaling policies. The book uses [[TargetTrackingScaling]] for the LLM Twin's inference component because the math is simpler — specify metric + target value, and AWS auto-generates the underlying CloudWatch alarms. The chapter argues scaling-policy tuning is analogous to hyperparameter tuning: stress-test in dev/test until the sweet spot between cost, latency, and throughput is found for both average and outlier traffic profiles.

## Key details
- Three policy types: target tracking, step scaling, scheduled scaling.
- Multiple policies can co-exist on one scalable target.
- Each policy carries its own scale-in / scale-out [[CooldownPeriod]].
- Policy choice is driven by traffic-pattern predictability — target tracking for smooth-varying load, scheduled for known peaks, step scaling for hand-tuned response curves.
- Over- and under-scaling are the two opposite failure modes.

## Connections
- [[ApplicationAutoScaling]] — the parent service.
- [[ScalableTarget]] — the resource a policy operates on.
- [[TargetTrackingScaling]] — the dominant LLM-serving policy type.
- [[CooldownPeriod]] — built into every policy.
- [[GPUUtilization]] — typical target-tracking metric for LLM serving.
- [[AmazonCloudWatch]] — the host of the alarms backing policies.
