---
title: "Made With ML — Jobs and Services"
type: source
tags: [mlops, made-with-ml, production, deployment, ray, anyscale, course]
date: 2026-05-15
source_file: raw/madewithml/mlops-jobs-and-services.md
---

## Summary
Goku Mohandas's Made With ML lesson on productionizing ML workloads using Anyscale Jobs (for batch model development pipelines) and Anyscale Services (for deploying models behind a scalable REST endpoint). The CLI commands developed earlier in the course are consolidated into a single `workloads.sh` bash script that runs data tests, code tests, training, evaluation, model tests, and pushes model registry artifacts to S3. A YAML config (`workloads.yaml`) wraps the script as an Anyscale Job with retries, persisted logs, and email alerts. A companion `serve_model.py` + `serve_model.yaml` pulls the artifacts back and exposes a Ray Serve deployment with canary rollout, observability via Ray Dashboard + Grafana, and rollback / terminate primitives.

## Key Claims
- The same cluster environment and compute configuration used for development [[AnyscaleWorkspaces]] can be reused verbatim in production, eliminating environment-discrepancy bugs at the dev→prod boundary.
- Anyscale Jobs add fault tolerance, retries, email alerts, and persisted logs around an arbitrary bash entrypoint without rewriting workload code.
- The natural division of labor is Jobs for finite model-development pipelines and Services for long-running inference endpoints; both pull/push to a shared S3 bucket so artifacts move between them via storage, not RPC.
- Scaling production compute is a configuration change, not a code change: either swap the named compute config or inline a `compute_config:` block with head/worker node types directly in the Jobs/Services YAML.
- `ROLLOUT` strategy gives a canary rollout that increasingly shifts traffic to the new version; `IN_PLACE` replaces atomically.
- Manual Jobs + Services is a stepping stone — the next lesson layers [[CICD]] on top so that workloads execute automatically on new data or merged PRs.

## Key Quotes
> "What worked during development will work in production."

> "Combine [all ML workloads] into one script ... at the end of our `workloads.sh` script, we save our model registry (with our saved model artifacts) and the results from the different workloads to S3."

> "We don't have to worry about any environment discrepancies when we deploy our workloads to production."

## Connections
- [[GokuMohandas]] — author of Made With ML.
- [[MadeWithML]] — parent course.
- [[Anyscale]] — sponsor and runtime provider.
- [[Ray]] — distributed compute framework underlying Jobs and Services.
- [[RayServe]] — model serving deployment used here.
- [[AnyscaleJobs]] — finite, fault-tolerant batch workload primitive.
- [[AnyscaleServices]] — long-running canary-rolloutable model endpoint.
- [[AmazonS3]] — model registry and results artifact store.
- [[MLflow]] — model registry referenced via `MODEL_REGISTRY`.
- [[ModelRegistry]] — pattern for storing trained model artifacts.
- [[ModelServing]] — pattern for exposing models as APIs.
- [[CanaryRollout]] — deployment strategy.
- [[CICD]] — natural follow-on automation layer (next lesson).
- [[Grafana]] — metrics dashboard for Services.

## Contradictions
None. Sets up vocabulary (Job, Service, rollout) that subsequent Made With ML lessons (CI/CD, Monitoring) build on directly.
