---
title: "Amazon Elastic Container Registry"
type: entity
tags: [product, aws, container, registry, cloud]
sources: [leh-ch02-tooling-and-installation, leh-ch10-inference-pipeline-deployment, leh-ch11-mlops-and-llmops]
last_updated: 2026-05-22
---

## What it is
Amazon ECR (Elastic Container Registry) is AWS's managed Docker / OCI image registry. It integrates with IAM, ECS, EKS, and SageMaker for private image distribution inside an AWS account.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) introduces ECR as the container registry component of the deployed ZenML stack. Ch. 10 ([[leh-ch10-inference-pipeline-deployment]]) explains that SageMaker pulls [[HuggingFaceDLC]] Docker images from ECR when materializing the LLM endpoint. Ch. 11 ([[leh-ch11-mlops-and-llmops]]) wires ECR into the GitHub Actions CD pipeline: `aws-actions/amazon-ecr-login` authenticates, then `docker/build-push-action` pushes images tagged with both `latest` and the commit SHA (`${{ github.sha }}`) to ECR.

## Connections
- [[Docker]] — image format ECR stores.
- [[AmazonSageMaker]] — pulls images from ECR.
- [[GitHubActions]] — pushes to ECR in CD.
- [[Amazon]] — parent.
- [[AmazonECS]] / [[AmazonEKS]] — peer compute services that also consume ECR.
