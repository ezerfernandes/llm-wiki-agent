---
title: "Continuous Deployment"
type: concept
tags: [mlops, deployment, ci-cd, mlsysbook]
sources: [mlsysbook-ch03-ml-workflow, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Continuous Deployment

The practice of shipping changes to production frequently and automatically. For ML systems, Reddi's *Machine Learning Systems* ([[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]) stresses that ML demands **continuous *retraining* loops that traditional CI/CD does not have**: deployment insights reshape data collection, monitoring drives model updates, and production data reveals distributional properties invisible in development.

This dynamism is incompatible with traditional release cycles. ML rollback is also harder than software rollback: it restores a model artifact but cannot restore the past *data environment*, creating a temporal state mismatch — so even a sub-60-second rollback is a mitigation, not a true system restore.

## Connections

- [[WaterfallModel]] — the rigid alternative ML cannot use.
- [[MLOps]] — the operational layer that automates continuous deployment/retraining.
- [[CanaryDeployment]] / [[ShadowDeployment]] / [[ABTesting]] — the progressive-rollout mechanisms.
- [[MLSystemLifecycle]] — deployment as a continuous phase, not an endpoint.
- [[mlsysbook-ch03-ml-workflow]] — source.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 frames continuous delivery of models via CI/CD with graduated rollout (canary/blue-green/shadow) and automated rollback.

