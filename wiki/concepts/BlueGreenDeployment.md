---
title: "Blue-Green Deployment"
type: concept
tags: [mlops, deployment, rollout, reliability]
sources: [mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Blue-Green Deployment

A zero-downtime deployment strategy that maintains two identical production environments — "blue" (current) and "green" (new) — and switches traffic atomically from one to the other once the new version is validated. Rollback is instant: route traffic back to the still-warm previous environment. In ML serving, blue-green is one of the graduated-rollout strategies (alongside [[CanaryDeployment|canary]] and [[ShadowDeployment|shadow]]) used to validate new model versions before full cutover, and it underpins the *immediate rollback* tier (hot standby, < 1 minute) of a tiered [[RollbackStrategy|rollback strategy]].

Described in [[mlsysbook-ch14-ml-operations]] (mlsysbook Vol 1, Ch 14).

## Connections
- [[CanaryDeployment]] — partial-traffic sentinel rollout (complementary).
- [[ShadowDeployment]] — duplicate inference without serving results.
- [[RollbackStrategy]] — blue-green enables instant immediate rollback.
- [[ModelDeployment]] / [[ModelValidation]] — context.
- [[MLOps]] — production-operations practice.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
