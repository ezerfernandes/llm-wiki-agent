---
title: "AWS SageMaker Inference Endpoint"
type: concept
tags: [deployment, aws, sagemaker, inference]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
An **AWS SageMaker inference endpoint** is the HTTPS-fronted, fully managed resource that hosts an ML model on SageMaker and exposes it for synchronous (real-time), asynchronous, or batch inference. The endpoint comprises four artifacts: endpoint (HTTPS surface), model (weights + compute logic), endpoint configuration (hardware + software setup), and [[InferenceComponent|inference component]] (binds model + config to the endpoint and is what `InvokeEndpoint` API calls target).

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] is the canonical reference. The LLM Twin's LLM microservice is deployed as a SageMaker real-time inference endpoint running a [[HuggingFaceDLC|Hugging Face Deep Learning Container]] powered by [[TextGenerationInference|TGI]] on a default `ml.g5.xlarge` GPU instance. The chapter implements a three-class strategy pattern — `ResourceManager` (boto3 existence checks), `DeploymentService` (orchestrates `HuggingFaceModel(...).deploy(...)`), `SagemakerHuggingfaceStrategy` (top-level facade) — and configures TGI via env vars (`HF_MODEL_ID`, `SM_NUM_GPUS`, `MAX_INPUT_LENGTH`, `MAX_TOTAL_TOKENS`, `MAX_BATCH_TOTAL_TOKENS`, `MAX_BATCH_PREFILL_TOKENS`, `HUGGING_FACE_HUB_TOKEN`, `HF_MODEL_QUANTIZE=bitsandbytes`). SageMaker deployments typically take 15–30 minutes; the chapter strongly recommends always deleting them after testing (`poetry poe delete-inference-endpoint`) to avoid runaway GPU costs.

## Key details
- Four-part anatomy: endpoint, model, endpoint configuration, inference component.
- Default LLM Twin instance type: `ml.g5.xlarge` (single GPU); A100 recommended for ~30B models.
- Deployment is via SageMaker SDK `HuggingFaceModel(...).deploy(...)`.
- Two IAM steps required: a narrow IAM user (CLI deploys) + an execution role attached to SageMaker (S3 / CloudWatch / ECR access).
- The chosen `EndpointType.INFERENCE_COMPONENT_BASED` enables per-component scaling.
- Pairs with [[ApplicationAutoScaling]] using `SageMakerInferenceComponentInvocationsPerCopy` as the target metric.

## Connections
- [[AmazonSageMaker]] — the parent service.
- [[InferenceComponent]] — the per-deployment sub-resource bound to the endpoint.
- [[InvokeEndpoint]] — the runtime API.
- [[HuggingFaceDLC]] — the Docker image hosting the model.
- [[TextGenerationInference]] — the serving engine inside the DLC.
- [[ApplicationAutoScaling]] / [[TargetTrackingScaling]] / [[ScalableTarget]] / [[ScalingPolicy]] — the autoscaling stack.
- [[IAMUser]] / [[IAMRole]] / [[ARN]] — the auth surface.
- [[Boto3]] — the SDK driving deployment.
- [[OnlineRealTimeInference]] — the archetype this endpoint serves.
- [[ModelServing]] — the broader practice.
