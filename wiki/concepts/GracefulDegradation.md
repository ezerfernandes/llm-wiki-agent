---
title: "Graceful Degradation (Serving)"
type: concept
tags: [serving, reliability, overload, tail-latency, mlsysbook, agentic-design-patterns]
sources: [mlsysbook-ch13-model-serving, mlsysbook-ch14-ml-operations, agentic-design-patterns-ch12-exception-handling, agentic-design-patterns-ch16-resource-aware]
last_updated: 2026-06-07
---

# Graceful Degradation (Serving)

A tail-tolerant overload strategy: **when load exceeds capacity, return approximate results rather than timing out** ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]). Examples: cached predictions for similar inputs (classification), shorter outputs (generative models), a subset of models (ensembles). This maintains responsiveness at the cost of some accuracy — which users typically prefer to outright failure.

One of several techniques for tolerating latency variance rather than eliminating it (Dean & Barroso), alongside **[[HedgedRequests|hedged requests]]** (duplicate a slow request to another replica), **tied requests** (send to multiple servers, cancel once one starts), **canary requests** (test 1–2 backends before full fan-out), and **[[AdmissionControl|admission control]]** (reject when the queue is too deep). Together these protect the SLO when [[QueuingTheory|queuing]] pushes the tail above target.

## Agentic Design Patterns (Gulli) perspective

[[agentic-design-patterns-ch12-exception-handling|Ch 12 of *Agentic Design Patterns*]] lists graceful degradation as one of the five **error-handling strategies** of the [[ExceptionHandlingAndRecovery|Exception Handling and Recovery]] pattern. Gulli's framing is broader than the serving-overload sense above: *"Where complete recovery is not immediately possible, the agent can maintain partial functionality to provide at least some value."* The trigger is any unrecoverable failure (a failed [[ToolUse|tool call]], a dead service), not just overload — e.g. the chapter's smart-home agent that, unable to toggle a light, still notifies the user and suggests manual intervention rather than failing silently. Same principle (partial value beats total failure), wider triggering condition.

### Model-level fallback ([[agentic-design-patterns-ch16-resource-aware|Ch 16, Resource-Aware Optimization]])

[[agentic-design-patterns-ch16-resource-aware|Ch 16]] applies graceful degradation specifically to **model availability**: when a preferred LLM is overloaded or throttled, the agent automatically **switches to a default or more affordable model** to maintain service continuity rather than failing. [[OpenRouter]]'s [[SequentialModelFallback|sequential model fallback]] (a hierarchical `models` list re-routed on any error — unavailability, rate-limiting, content filtering) is the concrete mechanism. This is the failure-time half of the [[ResourceAwareOptimization|Resource-Aware Optimization]] pattern, complementing success-time [[DynamicModelSelection|dynamic model selection]].

## Connections

- [[ExceptionHandlingAndRecovery]] — the agentic pattern that lists graceful degradation as a core error-handling strategy.
- [[AdmissionControl]] — the complementary "reject excess" lever; coordinated load shedding prevents retry storms.
- [[HedgedRequests]] — the redundant-request tail-tolerance technique.
- [[TailLatency]] / [[QueuingTheory]] — the tail-at-scale problem these techniques address.
- [[ServiceLevelObjective]] — what degradation protects under overload.
- [[mlsysbook-ch13-model-serving]] — source.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 makes graceful degradation the defining edge-AI pattern (Oura tiered fallback) and shows ClinAIOps elevates it to a mandatory, regulation-driven design constraint.

