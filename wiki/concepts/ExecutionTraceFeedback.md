---
title: "Execution Trace Feedback"
type: concept
tags: [agentic-discovery, observability, search]
sources: [2605.08083-autotts, 2604.25850-agentic-harness-engineering]
last_updated: 2026-05-15
---

# Execution Trace Feedback

History-design principle for [[AgenticAlgorithmDiscovery|agentic algorithm discovery]]: feed the explorer LLM **fine-grained per-step decision traces**, not just scalar accuracy/cost outcomes. Without traces, the explorer can only optimize the bottom-line numbers and cannot diagnose *why* a candidate failed.

## Operationalization in AutoTTS ([[2605.08083-autotts]] §3.2, App. C)

Every controller implements a `MethodTraceRecorder` surface emitting events at each decision: `start`, `init_branches`, `forward`, `update_states`, `prune`, `terminate_check`, `finish`. Each event carries:

- `goal` — high-level intent
- `step_input` / `step_output` — small JSON-serializable payloads (primitive types, short lists)
- `state` — controller's current view (active branches, depths, pool stats)
- `decision` — the chosen action

Per-question traces are written to `training_results/matrix_results_<Model>/<dataset>_trace_new_api.jsonl` and bundled into the round history $\mathcal{H}$ that the explorer reads at the start of each round.

## Ablation Evidence

[[2605.08083-autotts]] §5.4 / Table 3: removing execution traces (history reduced to scalar acc/tokens per controller) yields:
- Worse accuracy (53.1 → 51.6) and *more* tokens used (575.5K → 824.0K).
- Lower search cost ($39.9 → $30.9) — but the resulting controller is dominated on the Pareto frontier.

"Final acc/token numbers alone are insufficient to guide effective search."

## Why It Matters

Scalar feedback is **aliasing-prone**: very different controller behaviors can produce identical (acc, cost) pairs, and the explorer cannot tell which mechanism is responsible. Trace-level feedback exposes:
- *which* branches the controller expanded, probed, pruned, or stopped on;
- *when* aggressive stopping fired prematurely;
- *which* branch-classification decisions led to wasted budget.

This is exactly the [[2604.25850-agentic-harness-engineering|Meta-Harness]] finding (Lee et al. 2026): observability-driven harness evolution beats scalar-reward harness optimization. AutoTTS inherits this design discipline directly.

## Connections

- [[2605.08083-autotts]] — operationalizes the principle for TTS-controller discovery.
- [[2604.25850-agentic-harness-engineering|Meta-Harness]] — methodological precedent; "fine-grained execution feedback improves agentic discovery for harness engineering."
- [[AgenticAlgorithmDiscovery]] — broader paradigm.
- [[AutoTTS]] — concrete framework using execution traces.
- [[BetaParameterization]] — the complementary search-tractability mechanism.
- [[observability]] — adjacent concept; trace feedback is observability for LLM-driven program search.
