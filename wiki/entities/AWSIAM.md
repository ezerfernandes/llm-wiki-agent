---
title: "AWS Identity and Access Management"
type: entity
tags: [product, aws, security, iam, cloud]
sources: [leh-ch02-tooling-and-installation, leh-ch10-inference-pipeline-deployment, leh-ch11-mlops-and-llmops]
last_updated: 2026-05-22
---

## What it is
AWS IAM (Identity and Access Management) is the AWS service that manages users, roles, access keys, and policies controlling who can do what on which AWS resources.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) walks through creating an IAM user with `AdministratorAccess` for the tutorial — explicitly noted as a least-privilege violation that should not be used in production. The user is given an access key pair which `aws configure` consumes. Ch. 10 ([[leh-ch10-inference-pipeline-deployment]]) deepens the IAM treatment with two roles: a narrow **SageMaker IAM user** (`poetry poe create-sagemaker-role`) scoped to SageMaker/ECR/S3, and a **SageMaker execution role** (`create-sagemaker-execution-role`) attached to the endpoint so it can read S3, write CloudWatch, and pull ECR images. Ch. 11 ([[leh-ch11-mlops-and-llmops]]) re-uses IAM roles inside the [[CloudFormation]] stack that ZenML provisions.

## Connections
- [[Amazon]] — parent.
- [[AmazonSageMaker]] — primary IAM-protected service in the book.
- [[AmazonECR]] / [[AmazonS3]] — services accessed via IAM permissions.
- [[AWSCLI]] — uses IAM access keys.
- [[IAMUser]] / [[IAMRole]] / [[ARN]] — IAM primitives.
