---
title: "Docker"
type: entity
tags: [tool, container, devops, open-source]
sources: [leh-ch02-tooling-and-installation, leh-ch10-inference-pipeline-deployment, leh-ch11-mlops-and-llmops]
last_updated: 2026-05-22
---

## What it is
Docker is the dominant container platform used to package applications and their dependencies into portable images runnable on any Docker-compatible host. The book uses Docker for local infrastructure and for SageMaker deployment artifacts.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) requires Docker 27.1.1+ as the prerequisite for `poetry poe local-infrastructure-up`, which spins up [[ZenML]], [[MongoDB]], and [[Qdrant]] containers locally. Ch. 10 ([[leh-ch10-inference-pipeline-deployment]]) explains that SageMaker pulls Docker images from [[AmazonECR]] when deploying the LLM microservice on [[HuggingFaceDLC]] base images. Ch. 11 ([[leh-ch11-mlops-and-llmops]]) walks through a multi-stage `Dockerfile` based on `python:3.11-slim-bullseye` (with Google Chrome layered in for the crawler ETLs), built with `docker buildx --platform linux/amd64`, tagged with `latest` plus the commit SHA, and pushed to ECR by the GitHub Actions CD workflow.

## Connections
- [[Kubernetes]] — orchestrates Docker containers.
- [[AmazonECR]] — Docker image registry used by the book.
- [[HuggingFaceDLC]] — Hugging Face's pre-built Docker images for SageMaker.
- [[GitHubActions]] — builds + pushes the Docker image in CD.
- [[ZenML]] / [[MongoDB]] / [[Qdrant]] — local infra run as Docker containers.
- [[CICD]] — Docker is the CD artifact.
