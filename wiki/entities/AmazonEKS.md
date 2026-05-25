---
title: "Amazon Elastic Kubernetes Service"
type: entity
tags: [product, aws, kubernetes, container, cloud]
sources: [leh-ch02-tooling-and-installation, leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## What it is
Amazon EKS (Elastic Kubernetes Service) is AWS's managed [[Kubernetes]] control plane. It runs Kubernetes clusters on AWS-managed nodes (Fargate or EC2).

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) lists EKS alongside [[AmazonECS]] as the "fullest control" alternative to [[AmazonSageMaker]] — cheaper but more engineering effort. Ch. 10 ([[leh-ch10-inference-pipeline-deployment]]) lists EKS as the recommended productionization target for the FastAPI business microservice (Dockerize → push to ECR → deploy on EKS), deferred to Chapter 11.

## Connections
- [[Kubernetes]] — control plane EKS manages.
- [[AmazonECS]] — peer container service.
- [[AmazonSageMaker]] — managed compute used in the book.
- [[AmazonECR]] — image registry feeding EKS.
- [[Docker]] — container format.
- [[Amazon]] — parent.
- [[FastAPI]] — service that would deploy here.
