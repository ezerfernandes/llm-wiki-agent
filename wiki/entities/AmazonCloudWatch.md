---
title: "Amazon CloudWatch"
type: entity
tags: [product, aws, monitoring, observability, cloud]
sources: [leh-ch02-tooling-and-installation, leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## What it is
Amazon CloudWatch is AWS's managed monitoring and observability service that collects logs, metrics, and events from AWS resources and applications, and triggers alarms or autoscaling actions.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) recommends setting CloudWatch billing alarms to bound the $50–$100 expected AWS spend while running the book. Ch. 10 ([[leh-ch10-inference-pipeline-deployment]]) calls out CloudWatch as the host of endpoint logs and CPU/GPU/memory/disk metrics for the LLM SageMaker endpoint, and as the backing store for the alarms that drive **Application Auto Scaling** target-tracking policies on metrics like `SageMakerInferenceComponentInvocationsPerCopy`.

## Connections
- [[AmazonSageMaker]] — emits the metrics CloudWatch tracks.
- [[Amazon]] — parent.
- [[ApplicationAutoScaling]] — relies on CloudWatch alarms.
- [[TargetTrackingScaling]] — scaling policy backed by CloudWatch metrics.
- [[Monitoring]] — discipline.
