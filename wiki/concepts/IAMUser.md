---
title: "IAM User"
type: concept
tags: [aws, security, deployment, iam]
sources: [leh-ch02-tooling-and-installation, leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
An **AWS IAM user** is a programmatic or human identity in AWS Identity and Access Management — typically holding long-lived access keys (access key ID + secret) used to authenticate API calls. Distinguished from an [[IAMRole]], which represents a service identity assumed at runtime without persistent credentials.

## In LLM Engineer's Handbook
[[leh-ch02-tooling-and-installation]] introduces IAM users in the context of getting started with AWS: the chapter recommends a tutorial-grade IAM user with `AdministratorAccess` (explicitly noting this violates least-privilege for production) plus an access-key pair configured via `aws configure`. [[leh-ch10-inference-pipeline-deployment]] tightens the practice: the book provides `poetry poe create-sagemaker-role` to create a narrow IAM user scoped to SageMaker / ECR / S3 only — sufficient for the LLM Twin deployment automation but without the broad blast radius of `AdministratorAccess`.

## Key details
- Identified by user name + AWS account ID; addressed via ARN `arn:aws:iam::<account-id>:user/<user-name>`.
- Carries long-lived access keys for SDK / CLI authentication.
- Subject to a permissions policy (allow / deny lists for AWS API calls).
- Production guidance: never use `AdministratorAccess`; create one narrow user per workflow.
- The book uses two distinct IAM principals: a narrow IAM user for the developer CLI + a separate execution role attached to SageMaker.

## Connections
- [[IAMRole]] — the sibling identity type for AWS services.
- [[ARN]] — the global identifier format.
- [[AWSIAM]] — the parent service.
- [[AWSCLI]] — the tool configured with the user's access keys.
- [[Boto3]] — the Python SDK that authenticates with the user's credentials.
- [[AmazonSageMaker]] — the service the book's narrow user is scoped to.
