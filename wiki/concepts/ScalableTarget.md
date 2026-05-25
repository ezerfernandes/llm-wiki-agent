---
title: "Scalable Target"
type: concept
tags: [deployment, aws, autoscaling, mlops]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
A **scalable target** is an AWS Application Auto Scaling registration that declares the resource (identified by ARN), service namespace, and scalable dimension that autoscaling is allowed to manipulate — along with **MinCapacity** and **MaxCapacity** bounds. Registering a scalable target is step 1 of the two-step Application Auto Scaling configuration.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] frames the scalable target as the first of two autoscaling steps: register-target then create-policy. For the LLM Twin's SageMaker inference component, the resource ID, service namespace (`sagemaker`), and scalable dimension (`sagemaker:inference-component:DesiredCopyCount`) all flow into the `RegisterScalableTarget` call. Min and max bounds are critical: too-low MinCapacity (e.g., 0) means new requests pay cold-start latency; too-high MaxCapacity blows up cost during traffic spikes.

## Key details
- Resource ID points to the specific resource (an [[InferenceComponent]] ARN, an ECS service, a DynamoDB table, etc.).
- Scalable dimension identifies *what* about the resource can grow (replica count, read capacity, etc.).
- MinCapacity floor prevents scale-to-zero (or enables it explicitly).
- MaxCapacity ceiling is a hard cost guardrail.
- One scalable target supports multiple [[ScalingPolicy|scaling policies]] (e.g., one for invocation rate, one for GPU utilization).

## Connections
- [[ApplicationAutoScaling]] — the parent service.
- [[ScalingPolicy]] / [[TargetTrackingScaling]] — the step-2 policies attached to the target.
- [[CooldownPeriod]] — the cross-cutting stability parameter.
- [[InferenceComponent]] / [[AWSSageMakerInferenceEndpoint]] — typical scalable resources for LLM serving.
- [[ARN]] — the identifier referencing the resource.
