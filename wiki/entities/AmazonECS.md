---
title: "Amazon Elastic Container Service"
type: entity
tags: [product, aws, container, orchestration, cloud]
sources: [leh-ch02-tooling-and-installation, leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## What it is
Amazon ECS (Elastic Container Service) is AWS's managed container orchestration service. It runs Docker containers on AWS-managed Fargate or self-managed EC2 nodes.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) names ECS alongside [[AmazonEKS]] as alternatives to [[AmazonSageMaker]] for teams that want more infrastructure control (cheaper but more engineering). Ch. 10 ([[leh-ch10-inference-pipeline-deployment]]) names ECS as one of two candidate destinations (with EKS) for productionizing the FastAPI business microservice — a step the book defers to Chapter 11 because it is not LLM-specific.

## Connections
- [[AmazonEKS]] — Kubernetes-based alternative.
- [[AmazonSageMaker]] — managed compute used in the book instead.
- [[AmazonECR]] — image registry feeding ECS.
- [[Docker]] — container format ECS runs.
- [[Amazon]] — parent.
- [[FastAPI]] — service that would be deployed here.
