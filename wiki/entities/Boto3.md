---
title: "boto3"
type: entity
tags: [tool, aws, python, sdk]
sources: [leh-ch10-inference-pipeline-deployment, leh-ch11-mlops-and-llmops]
last_updated: 2026-05-22
---

## What it is
Boto3 is Amazon's official AWS SDK for Python. It exposes both a control-plane client (`boto3.client("sagemaker")`) for creating and managing AWS resources and a runtime client (`boto3.client("sagemaker-runtime")`) for invoking those resources programmatically.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] uses Boto3 throughout the SageMaker deployment automation: a `ResourceManager` checks/creates endpoint configurations and inference components via the `sagemaker` client, and `LLMInferenceSagemakerEndpoint.inference()` calls `invoke_endpoint` on the `sagemaker-runtime` client to actually serve user prompts. [[leh-ch11-mlops-and-llmops]] uses the same SDK paths under the hood when [[ZenML]] orchestrates SageMaker steps as part of the AWS stack.

## Connections
- [[AmazonSageMaker]] — primary control-plane and runtime target.
- [[AmazonECR]] / [[AmazonS3]] / [[AWSIAM]] — adjacent services Boto3 touches in the LLM Twin deployment.
- [[InvokeEndpoint]] — the runtime API surface used.
