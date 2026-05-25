---
title: "Monolithic Architecture"
type: concept
tags: [architecture, system-design, deployment]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
A **monolithic architecture** packages every layer of an application — UI, business logic, data access, models — into a single deployable unit that runs in a single process. It is simple to operate but cannot scale individual concerns (GPU model vs. CPU business logic) independently.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] uses monolithic ML serving as the foil against [[MicroservicesArchitecture]]. The chapter's critique: a monolith cannot scale GPU and CPU paths independently — the GPU sits idle during business-logic execution, wasting expensive A100/V100/A10G time; teams also cannot split work cleanly. The recommended migration path is **start monolithic, design for modularity (separate Python modules or even packages), then split into services later** — failing to design modularly forces a rewrite during the transition. The chapter is careful not to call monoliths an outright anti-pattern: they are the right starting point, just not the right destination for a GPU-heavy service.

## Key details
- Single deployable unit; single process.
- Operationally simple — one binary, one log stream, one deploy target.
- Cannot independently scale CPU (business) vs. GPU (model) workloads.
- Cannot independently update or swap the LLM runtime (Python ↔ Rust/C++/TensorRT).
- Modular monolith — a monolith built from cleanly separated modules — is the recommended bridge to microservices.

## Connections
- [[MicroservicesArchitecture]] — the contrast pattern the chapter ultimately chooses.
- [[ModelServing]] — the practice both patterns implement.
- [[MonolithicBatchArchitecture]] — the ML-specific monolithic anti-pattern from Ch 1.
- [[FTIArchitecture]] — the broader modular ML architecture that subsumes the monolith-to-microservices migration.
