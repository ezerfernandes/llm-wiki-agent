---
name: KnightCapital
title: "Knight Capital Group"
type: entity
tags: [company, finance, deployment-failure, war-story]
sources: [mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Knight Capital Group

A major US equities market maker, cited in [[mlsysbook-ch14-ml-operations]] (mlsysbook Vol 1, Ch 14) as a "war story" illustrating that **deployment is a systems problem extending well beyond code**.

## The 2012 deployment error
- New software was deployed to **7 of 8 servers**; the 8th was missed.
- The new code repurposed an old flag (`SMARS`). On the seven updated servers this worked; on the 8th (still running old code), activating `SMARS` triggered a dormant test routine — "Power Peg" — designed years earlier to buy stock aggressively for testing.
- In **45 minutes**, the defective router generated millions of erroneous orders, accumulated an unintended multi-billion-dollar portfolio, and cost Knight **> $460M**, requiring emergency financing within days.

**Lesson (per Ch 14):** configuration drift and partial rollouts are catastrophic failure modes in automated systems. ML deployments inherit the same risk surface — a [[ModelRegistry|model registry]] pointing at the wrong version, a feature schema drifting between training and serving, or a partial [[CanaryDeployment|canary]] that wedges half the fleet on a stale routing rule each reproduce the Knight Capital shape.

## Connections
- [[mlsysbook-ch14-ml-operations]] — source chapter.
- [[ModelDeployment]] / [[RollbackStrategy]] / [[CanaryDeployment]] — the deployment-discipline lessons.
- [[TrainingServingSkew]] — the ML analog of the config-drift failure.
