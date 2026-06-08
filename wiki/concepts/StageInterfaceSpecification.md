---
title: "Stage Interface Specification"
type: concept
tags: [ml-systems, mlsysbook, workflow, contracts, foundations]
sources: [mlsysbook-ch03-ml-workflow]
last_updated: 2026-06-05
---

# Stage Interface Specification

Treats each [[MLSystemLifecycle|lifecycle]] stage as an **API contract** with an explicit **Input Contract**, **Output Contract**, and **Quality Invariant** that must hold for the stage to count as complete (Reddi, [[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]). "Just as a microservice must adhere to its Swagger definition to prevent system crashes, a data pipeline must adhere to its schema and distribution contracts to prevent model failures."

Examples:

- **Problem Definition** → outputs measurable objectives + **deployment-paradigm selection** + resource constraints; invariant: *all success criteria quantifiable; target paradigm explicit*.
- **Evaluation & Validation** → outputs performance metrics across subgroups + failure-mode analysis + validation certificate; invariant: *no critical subgroup below minimum thresholds; calibration meets domain requirements*.
- **Deployment & Integration** → outputs serving endpoint + monitoring instrumentation + rollback procedures; invariant: *latency/throughput meet paradigm requirements; integration tests pass*.

Validating outputs at each transition — **auditing stage transitions** — catches violations when correction is cheapest. The worked audit: a team that skips paradigm selection ("figure it out later") is *blocked*, because by the [[ConstraintPropagationPrinciple|constraint propagation principle]] resolving it later at stage 5 costs $2^4 = 16\times$, ~2–4 iteration cycles (≈8–16 weeks) of avoidable rework.

## Connections

- [[ConstraintPropagationPrinciple]] — why violated contracts compound exponentially downstream.
- [[MLWorkflow]] / [[MLSystemLifecycle]] — the process being contract-bound.
- [[MLOps]] — the model/data/infrastructure contract practices that implement this at scale.
- [[mlsysbook-ch03-ml-workflow]] — source.
