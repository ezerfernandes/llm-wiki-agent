---
title: "Kubernetes"
type: entity
tags: [tool, orchestration, container, open-source]
sources: [leh-ch02-tooling-and-installation, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

## What it is
Kubernetes (k8s) is an open-source container-orchestration system originally developed by [[google|Google]] and now stewarded by the CNCF. It schedules and manages containerized workloads across clusters of machines.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) references Kubernetes as the substrate underneath [[Kubeflow]], [[ArgoWorkflows]], and [[AmazonEKS]] when discussing why the authors prefer a cloud-agnostic [[ZenML]] stack over committing to a k8s-based workflow runtime. Ch. 10 ([[leh-ch10-inference-pipeline-deployment]]) name-checks Amazon EKS (managed Kubernetes) as a future target for the FastAPI business microservice.

## Connections
- [[AmazonEKS]] — managed Kubernetes service used in the book.
- [[Kubeflow]] / [[ArgoWorkflows]] — Kubernetes-native orchestrators.
- [[Docker]] — containers run by Kubernetes.
- [[google]] — original creator.
- [[mlsysbook-ch14-ml-operations]] — Ch 14 uses Kubernetes for containerized ML workload orchestration, autoscaling (1→dozens of replicas in <60s), and KServe scale-to-zero serving.

