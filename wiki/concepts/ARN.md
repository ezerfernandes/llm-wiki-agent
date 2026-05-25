---
title: "ARN (Amazon Resource Name)"
type: concept
tags: [aws, identifiers, deployment]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
An **Amazon Resource Name (ARN)** is the globally unique identifier AWS uses to address any resource (IAM role, S3 bucket, SageMaker endpoint, ECR repository, etc.). The canonical form is `arn:<partition>:<service>:<region>:<account-id>:<resource-id>`, e.g., `arn:aws:iam::992382797823:role/sagemaker-execution`.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] uses ARNs throughout the SageMaker deployment automation. The execution-role ARN is read from `settings.ARN_ROLE` and passed into `HuggingFaceModel(role=role_arn, ...)`; the SageMaker endpoint, inference component, ECR image URI, and S3 model-artifact paths are all addressed by ARN. The chapter argues ARN-based addressing makes the deployment configuration portable across environments — only the account ID and region need to change.

## Key details
- Format: `arn:aws:<service>:<region>:<account-id>:<resource>` (region omitted for global services like IAM).
- Globally unique across all AWS accounts.
- Used as the resource-id input to scaling policies, IAM policies, and SDK calls.
- Treat ARNs as configuration — never hardcoded in source.

## Connections
- [[IAMRole]] / [[IAMUser]] — identified by ARN.
- [[AmazonSageMaker]] / [[AWSSageMakerInferenceEndpoint]] / [[InferenceComponent]] — addressed by ARN.
- [[AmazonS3]] / [[AmazonECR]] / [[AmazonCloudWatch]] — all resources have ARNs.
- [[Boto3]] — the SDK that consumes ARNs as input.
- [[ScalableTarget]] — registered against a resource ARN.
