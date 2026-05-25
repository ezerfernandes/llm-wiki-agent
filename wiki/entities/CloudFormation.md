---
title: "AWS CloudFormation"
type: entity
tags: [tool]
sources: [leh-ch11-mlops-and-llmops]
last_updated: 2026-05-22
---

## What it is
AWS-native infrastructure-as-code service.

## In LLM Engineer's Handbook
AWS CloudFormation is the AWS-native IaC service. [[leh-ch11-mlops-and-llmops]] notes that [[ZenML]]'s in-browser AWS stack creation generates a CloudFormation template that provisions [[AmazonS3]] (artifact storage), [[AmazonECR]] (container registry), [[AmazonSageMaker]] (orchestrator), and [[AWSIAM]] roles. [[Terraform]] is offered as a more flexible alternative.
