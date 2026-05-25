---
title: "MTTD (Mean Time To Detection)"
type: concept
tags: [observability, monitoring, devops, metric]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# MTTD

**Mean Time To Detection.** The average elapsed time between *when something goes wrong* and *when monitoring catches it*. One of three DevOps observability metrics [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]] adopts for AI-application observability, alongside [[MTTR|MTTR]] and [[ChangeFailureRate|CFR]].

> *"MTTD (mean time to detection): When something bad happens, how long does it take to detect it?"* — Ch 10

## Why it matters for AI applications

Foundation-model failure modes — [[Hallucination|hallucination]], silent prompt-template drift, [[SilentModelUpdate|silent underlying-model updates]], guardrail false-positives — often produce *plausible-looking* outputs. They don't crash the service. Without explicit metrics designed to *catch the AI-specific failure modes*, MTTD can be effectively infinite: the system keeps working from the infrastructure's point of view while quality silently degrades.

Lowering MTTD is the design problem the rest of Ch 10's monitoring section addresses — by enumerating failure-specific metrics (format failures, factual-consistency scores, refusal rates, user complaint signals).

## Pairing with MTTR

A low MTTD with a high [[MTTR|MTTR]] still means long outages — fast detection, slow recovery. A high MTTD with a low MTTR means problems linger before anyone notices but are fixed quickly once spotted. Both must be low for production reliability.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[MTTR]] — paired metric.
- [[ChangeFailureRate]] — third DevOps observability metric.
- [[observability]] / [[Monitoring]] — parent disciplines.
- [[DriftDetection]] / [[SilentModelUpdate]] — failure modes MTTD targets.
- [[Hallucination]] — AI-specific failure that escapes infrastructure metrics.
