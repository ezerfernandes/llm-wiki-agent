---
title: "Rollback Strategy"
type: concept
tags: [mlops, deployment, reliability, incident-response, agentic-design-patterns]
sources: [mlsysbook-ch14-ml-operations, agentic-design-patterns-ch12-exception-handling]
last_updated: 2026-06-07
---

# Rollback Strategy

The safety net that enables confident model deployment by reverting to a previous stable version when a new one fails. Without reliable rollback, teams become deployment-averse and slow iteration velocity. ML rollback is complicated by model-dependent state (e.g., cached embeddings) that is often incompatible between versions.

[[mlsysbook-ch14-ml-operations]] defines **three tiers**:

| Tier | Trigger | Implementation | State |
|---|---|---|---|
| **Immediate** (< 1 min) | Serving errors, crashes | Hot standby, instant switch ([[BlueGreenDeployment|blue-green]]) | Stateless |
| **Rapid** (< 15 min) | Canary metric degradation | Registry-based redeploy | Clear caches, restart sessions |
| **Delayed** (< 4 hr) | Business-metric decline | Full redeploy with migration | Migrate state, replay if needed |

Untested rollbacks fail at the worst time (3 AM incidents). Required practices: monthly "fire drills," automated thresholds (e.g., "P99 > 2× baseline for 5 min → rollback"), validation that the rolled-back model produces consistent (not stale-cache-corrupted) predictions, and step-by-step runbooks. Stateful models and feedback-contaminated training windows may prevent a clean restoration; use rollback checkpoints capturing state snapshots at deployment boundaries.

## Agentic Design Patterns (Gulli) perspective

[[agentic-design-patterns-ch12-exception-handling|Ch 12 of *Agentic Design Patterns*]] names **state rollback** as a recovery step of the [[ExceptionHandlingAndRecovery|Exception Handling and Recovery]] pattern: *"reversing recent changes or transactions to undo the effects of the error."* This is the agent-runtime analogue of the deployment-rollback discipline above — instead of reverting to a prior *model version*, the agent reverts its own recent *actions/transactions* to a stable state after a failure (and pairs with [[Idempotency]] so undoing/redoing is safe). Both senses share the core idea: a tested path back to a known-good state is what makes risky forward operations safe to attempt.

## Connections
- [[ExceptionHandlingAndRecovery]] — the agentic pattern where "state rollback" is a named recovery step.
- [[BlueGreenDeployment]] / [[CanaryDeployment]] / [[ShadowDeployment]] — rollout strategies rollback complements.
- [[ModelRegistry]] — enables registry-based redeployment.
- [[IncidentResponse]] — rollback as a mitigation option.
- [[MLOps]] — production-operations practice.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
