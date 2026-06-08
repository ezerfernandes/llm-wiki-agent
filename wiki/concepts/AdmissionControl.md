---
title: "Admission Control (Serving)"
type: concept
tags: [serving, reliability, overload, queuing, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# Admission Control (Serving)

When traffic exceeds capacity, **proactively reject requests once queue depth crosses a threshold** — returning immediate 503s rather than accepting requests likely to time out ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]). This sacrifices throughput to protect latency for *admitted* requests, and is the only way to hold $T_{\text{lat}}$ during overload because (by [[LittlesLaw|Little's Law]]) once service rate μ is maxed out, accepting more requests only grows queue depth and latency.

A practical threshold is 2–3× the worker count (a queue of 2–3 service times of work); adaptive variants tighten when observed p99 rises. **Retry-storm prevention** is the subtle companion failure mode: if a load balancer retries rejected requests at other equally-overloaded replicas, traffic amplifies — **coordinated load shedding** shares load info so replicas collectively reject the same fraction rather than each rejecting independently and triggering retries.

## Connections

- [[QueuingTheory]] / [[LittlesLaw]] — why admission control is necessary once ρ→1.
- [[GracefulDegradation]] — the "approximate result" alternative to outright rejection.
- [[Autoscaling]] — spin up replicas before the knee; admission control bridges the cold-start gap.
- [[TailLatency]] / [[ServiceLevelObjective]] — the tail/SLO admission control protects.
- [[mlsysbook-ch13-model-serving]] — source.
