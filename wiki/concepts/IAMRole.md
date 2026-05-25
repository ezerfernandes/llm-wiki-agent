---
title: "IAM Role"
type: concept
tags: [aws, security, deployment, iam]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
An **AWS IAM role** is an identity that can be assumed by AWS services or principals to act on AWS resources, without long-lived credentials. Roles are attached to services (e.g., SageMaker, Lambda, EC2) so they can call other AWS APIs on behalf of the workload — distinct from an [[IAMUser]], which represents a human or programmatic identity.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] uses an IAM role as the execution role for the SageMaker inference endpoint. The chapter provides a `poetry poe create-sagemaker-execution-role` command that creates a role with permissions to read [[AmazonS3|S3]] model artifacts, write to [[AmazonCloudWatch|CloudWatch]] logs, and pull [[AmazonECR|ECR]] container images — all on behalf of the SageMaker service when it operates the endpoint. The role's [[ARN]] is passed to `HuggingFaceModel(role=role_arn, ...)`.

## Key details
- Roles have a **trust policy** (who can assume the role) and a **permissions policy** (what the role can do).
- Used by AWS services to act with scoped permissions — better security than embedding long-lived keys.
- Identified globally by an [[ARN]] of form `arn:aws:iam::<account-id>:role/<role-name>`.
- The book's SageMaker execution role is narrowly scoped to S3/CloudWatch/ECR only.
- Two-role pattern: a permissive deployment role for CI and a narrow execution role for the runtime.

## Connections
- [[IAMUser]] — the sibling identity type for humans/programmatic clients.
- [[ARN]] — the global identifier format for IAM roles.
- [[AWSIAM]] — the parent service.
- [[AmazonSageMaker]] / [[AWSSageMakerInferenceEndpoint]] — the runtime consuming the role.
- [[AmazonS3]] / [[AmazonCloudWatch]] / [[AmazonECR]] — the services the role accesses.
- [[Boto3]] — the SDK that assumes the role under the hood.
