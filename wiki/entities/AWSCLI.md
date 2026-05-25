---
title: "AWS CLI"
type: entity
tags: [tool, aws, cli, devops]
sources: [leh-ch02-tooling-and-installation]
last_updated: 2026-05-22
---

## What it is
The AWS CLI is the official command-line client for talking to AWS services. It reads credentials and default region from `~/.aws/credentials` and `~/.aws/config`, populated by `aws configure`.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) installs the AWS CLI and configures it via `aws configure` with the IAM access key pair (region `eu-central-1`, output `json`). The CLI is the entry point for all subsequent AWS operations — Docker login to [[AmazonECR]], inspecting [[AmazonS3]] buckets, and verifying SageMaker resources.

## Connections
- [[AWSIAM]] — provides the access key the CLI authenticates with.
- [[Amazon]] — parent.
- [[AmazonECR]] / [[AmazonS3]] / [[AmazonSageMaker]] — services driven via the CLI.
- [[CLI]] — adjacent concept.
