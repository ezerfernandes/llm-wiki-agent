---
title: "Hedged Requests"
type: concept
tags: [serving, reliability, tail-latency, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# Hedged Requests

A tail-tolerant technique (Dean & Barroso): **when a request has not completed within the expected time, send a duplicate to another replica and use whichever response arrives first**, cancelling the other ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]). The term is borrowed from finance — the redundant request is an offsetting bet against a slow server.

Overhead is modest: hedging at the 95th percentile means only ~5% of requests generate duplicates, a ~5% load increase that dramatically reduces tail latency. The ML caveat: **CUDA kernels cannot be preempted mid-execution**, so a losing hedged request still occupies a GPU for one full inference cycle — the 5% load increase translates to ~5% wasted GPU compute. Related variants: **tied requests** (send to multiple servers simultaneously with a cancellation tag, eliminating the wait-to-detect delay) and **canary requests** (test 1–2 backends before committing a full fan-out).

## Connections

- [[GracefulDegradation]] / [[AdmissionControl]] — the other tail-tolerant levers.
- [[TailLatency]] / [[QueuingTheory]] — the variance hedging tolerates.
- [[CUDA]] — non-preemptible kernels make cancellation lossy.
- [[LoadBalancing]] — routing slow requests to alternative replicas.
- [[mlsysbook-ch13-model-serving]] — source.
