---
title: "Model Deployment"
type: concept
tags: [mlops, deployment, serving, operations]
sources: [mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Model Deployment

The process of transforming a trained model artifact into a live production system component — *not a file transfer but a systems engineering problem*. The canonical failure: a fraud model at 99.2% precision in dev predicts every transaction legitimate in production because the serving host runs a different feature-extraction library version (an **environment-parity** failure, the $\text{Environment}_v$ term of reproducibility).

Reliable deployment treats the model, its dependencies, and its configuration as a single deployable unit, typically via containerization ([[Docker]]/[[Kubernetes]]) and a [[ModelRegistry|model registry]]. Validation precedes full rollout through staging/QA and graduated strategies — [[ShadowDeployment|shadow]], [[CanaryDeployment|canary]], [[BlueGreenDeployment|blue-green]] — backed by a tiered [[RollbackStrategy|rollback strategy]]. ML staging validates probabilistic adequacy (is the accuracy distribution acceptable?), which is harder than conventional staging's deterministic correctness check.

Covered as a production-operations topic in [[mlsysbook-ch14-ml-operations]] (mlsysbook Vol 1, Ch 14).

## Connections
- [[ModelServing]] / [[DeploymentSpectrum]] — the runtime serving substrate.
- [[CanaryDeployment]] / [[ShadowDeployment]] / [[BlueGreenDeployment]] / [[RollbackStrategy]] — graduated rollout + recovery.
- [[ModelRegistry]] / [[Docker]] / [[Kubernetes]] — packaging and orchestration.
- [[ModelValidation]] / [[ABTesting]] — pre-deployment gates.
- [[MLOps]] — production-operations practice.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
