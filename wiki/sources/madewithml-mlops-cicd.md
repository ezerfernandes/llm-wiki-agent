---
title: "Made With ML — CI/CD for Machine Learning"
type: source
tags: [mlops, made-with-ml, cicd, github-actions, continual-learning, course]
date: 2026-05-15
source_file: raw/madewithml/mlops-cicd.md
---

## Summary
Lesson on wiring GitHub Actions around the [[AnyscaleJobs]] + [[AnyscaleServices]] from the previous chapter to achieve continual learning. Three workflows live in `.github/workflows/`: `workloads.yaml` runs the training/evaluation Job on every pull request to `main` and comments the results tables back on the PR; `serve.yaml` triggers an Anyscale Service rollout on push to `main`; `documentation.yaml` deploys the MkDocs site. Workflows authenticate to AWS via an IAM role for [[GitHubActions]] OIDC (no long-lived secrets) and pull/push the model registry and results to S3. A small helper `json_to_md.py` converts JSON evaluation results to markdown tables for the PR comment.

## Key Claims
- CI/CD over Jobs+Services delivers continual learning: model is retrained, evaluated, and reviewed inside the PR loop, then redeployed only when a human merges.
- Pull request is the right trigger for training: reviewers see training and evaluation metrics as PR comments before merging, so a regression blocks deployment naturally.
- The `anyscale service rollout` command preserves the existing `SECRET_TOKEN` and `SERVICE_ENDPOINT`, so downstream consumers experience zero-config updates.
- Anyscale credentials and AWS IAM role assumption are wired in via GitHub repository secrets and `aws-actions/configure-aws-credentials` — no static AWS keys in CI.
- The same pattern extends to other triggers (new data arrives, performance regresses, scheduled cron) and other orchestrators ([[Prefect]], [[Kubeflow]]) — GitHub Actions is one substrate among many.
- Workflow can be enriched to fetch live evaluation from the production service via its `/evaluate/` endpoint and diff against the candidate model in the same PR comment.

## Key Quotes
> "We have fully control because we can decide not to trigger an event (ex. push to main branch) if we're not satisfied with the results of our model development workloads."

> "When this `workloads` workflow completes, we'll have a comment on our PR with our training and evaluation results."

> "The `anyscale service rollout` command will update our existing service (if there was already one running) without changing the `SECRET_TOKEN` or `SERVICE_ENDPOINT`."

## Connections
- [[GokuMohandas]] — author.
- [[MadeWithML]] — parent course.
- [[GitHubActions]] — CI/CD execution substrate.
- [[GitHub]] — code host providing PR/push events.
- [[AnyscaleJobs]] — invoked by the `workloads` workflow.
- [[AnyscaleServices]] — invoked by the `serve` workflow.
- [[ContinualLearning]] — the umbrella goal of this lesson.
- [[CICD]] — the umbrella concept.
- [[MkDocs]] — used to build and deploy the documentation site.
- [[AmazonS3]] — model registry + results location accessed via IAM role assumption.
- [[AWSIAM]] — role-based, OIDC-backed credentials for GitHub Actions runners.
- [[ModelRegistry]] — artifacts moved between Job and Service via S3.
- [[Prefect]] / [[Kubeflow]] — orchestrators mentioned as alternative substrates.

## Contradictions
None. Directly builds on `madewithml-mlops-jobs-and-services` and feeds `madewithml-mlops-monitoring` (which adds the "regression detected" trigger).
