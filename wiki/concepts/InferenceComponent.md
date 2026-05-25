---
title: "Inference Component (SageMaker)"
type: concept
tags: [deployment, aws, sagemaker, inference, architecture]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
A **SageMaker inference component** is one of the four sub-artifacts that compose a SageMaker inference deployment — alongside endpoint, model, and endpoint configuration. The inference component binds a specific model + configuration to an endpoint and is the SageMaker resource that the `InvokeEndpoint` API targets. It is the unit at which copies (replicas), CPU/GPU, and memory are allocated and at which autoscaling policies apply.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] introduces inference components as the SageMaker abstraction that lets a single endpoint host multiple models (or multiple replica configurations of one model) with independent scaling. The book's [[AWSSageMakerInferenceEndpoint|LLM Twin endpoint]] declares an inference component via `ResourceRequirements(requests={"copies": ..., "num_accelerators": ..., "num_cpus": ..., "memory": ...})` and the chapter shows the deployment script invoking `HuggingFaceModel(...).deploy(... endpoint_type=EndpointType.INFERENCE_COMPONENT_BASED ...)`. Autoscaling targets the inference component, with `SageMakerInferenceComponentInvocationsPerCopy` as the canonical [[TargetTrackingScaling]] metric.

## Key details
- Four-part anatomy of SageMaker inference: endpoint, model, endpoint configuration, **inference component**.
- The `InvokeEndpoint` API targets a specific inference component on the endpoint.
- ResourceRequirements: `copies` (replica count), `num_accelerators` (GPUs), `num_cpus`, `memory` (MB).
- Allows independent scaling of multiple models behind one endpoint.
- The autoscaling primitive is **per-inference-component**, not per-endpoint.

## Connections
- [[AWSSageMakerInferenceEndpoint]] — the parent endpoint resource.
- [[InvokeEndpoint]] — the runtime API that targets an inference component.
- [[TargetTrackingScaling]] / [[ApplicationAutoScaling]] / [[ScalableTarget]] — the autoscaling stack acting on inference components.
- [[AmazonSageMaker]] — the AWS service hosting inference components.
- [[ModelServing]] — the broader practice.
- [[MicroservicesArchitecture]] — the inference component is a microservice-shaped resource.
