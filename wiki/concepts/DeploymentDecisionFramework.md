---
title: "Deployment Decision Framework"
type: concept
tags: [ml-systems, deployment, framework, mlsysbook]
sources: [mlsysbook-ch02-ml-systems]
last_updated: 2026-06-05
---

# Deployment Decision Framework

A **four-layer sequential filter** for selecting an ML [[DeploymentSpectrum|deployment paradigm]] from systematic application constraints rather than organizational bias or technology trends. From [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]). The layers are evaluated in order:

1. **Privacy** — can data be transmitted externally? [[GDPR]]/[[HIPAA]]/proprietary restrictions mandate local processing, eliminating cloud-only.
2. **Latency** — does it need sub-10-ms response? Physics-imposed network delay alone exceeds this, eliminating [[CloudML|cloud]].
3. **Compute** — does it need high-performance infrastructure (cloud/edge), or can it fit mobile/tiny budgets?
4. **Cost** — balance CapEx, OpEx, and energy over the deployment lifetime ([[TotalCostOfOwnership|TCO]]).

**Worked example (autonomous emergency braking):** privacy permits cloud, but latency (100 ms = 2.8 m of travel at 100 km/h) eliminates it *before* compute or cost are considered → Edge ML with a local GPU (NVIDIA Drive Orin class), cloud reserved for training/updates. The framework's power is that latency can rule out paradigms before later layers run. A critical pitfall it guards against: **choosing on model accuracy alone** — a 99%-accurate cloud model is useless for braking if latency exceeds reaction time. Feasibility is necessary but not sufficient: team expertise, monitoring capacity, and the [[ComplexityTax|complexity tax]] also gate success. In practice the framework rarely yields one winner, so production systems go [[HybridML|hybrid]].

## Connections

- [[DeploymentSpectrum]] / [[CloudML]] / [[EdgeML]] / [[MobileML]] / [[TinyML]] — the paradigms it filters among.
- [[HybridML]] — what to do when no single paradigm wins.
- [[ComplexityTax]] — the "should you use ML at all?" check that precedes paradigm choice.
- [[GDPR]] / [[HIPAA]] — the privacy-layer drivers.
- [[TotalCostOfOwnership]] — the cost-layer analysis.
- [[SpeedOfLight]] — why the latency layer eliminates the cloud for safety tasks.
- [[mlsysbook-ch02-ml-systems]] — source.
