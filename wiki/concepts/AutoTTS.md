---
title: "AutoTTS"
type: concept
tags: [framework, test-time-scaling, agentic-discovery]
sources: [2605.08083-autotts]
last_updated: 2026-05-15
---

# AutoTTS

Environment-driven framework for **automatic discovery of [[testtimescaling|test-time scaling]] controllers** introduced in [[2605.08083-autotts]]. Reframes TTS strategy design — historically a hand-crafting activity (SC@64, ASC, ESC, ST-BoN, Parallel-Probe) — as **controller synthesis over a [[WidthDepthSearch|width–depth]] control space**. An explorer LLM ([[claudecode|Claude Code]]) iteratively edits a Python class (`OptimalController`) and is evaluated against an [[OfflineReplayEnvironment|offline replay environment]] of pre-collected reasoning trajectories; controller evaluation requires **zero LLM calls**, making the search budget feasible (5 rounds, $39.9, 160 minutes total).

## Three Pillars

1. **[[OfflineReplayEnvironment]]** — Pre-collect $N=128$ trajectories per (model, problem) at temperature 0.7, segmented into $\Delta=500$-token intervals. Probe signals $\omega_{i,k}$ live offline; PROBE actions are zero-cost lookups. Evaluation becomes deterministic and LLM-free.
2. **[[BetaParameterization]]** — Each controller exposes a single scalar $\beta\in[0,1]$ and maps it monotonically to every internal hyperparameter via a `_schedule(beta)` method. Collapses the search space; prevents collapse onto extreme search-set optima. Ablation: removing it cuts held-out accuracy 53.1→49.0.
3. **[[ExecutionTraceFeedback]]** — Per-step decision traces (events: `init_branches`, `forward`, `update_states`, `prune`, `terminate_check`, `finish`) given back to the explorer, not just scalar acc/cost. Ablation: removing them produces *worse* accuracy with *more* tokens.

## Discovered Controller

The five-round loop converges to the **[[ConfidenceMomentumController|Confidence Momentum Controller]]** (CMC), exhibiting four non-obvious mechanisms: EMA-momentum stopping, coupled width–depth control, alignment-aware depth allocation, conservative branch abandonment.

## Connections

- [[2605.08083-autotts]] — origin paper.
- [[testtimescaling|Test-Time Scaling]] — the problem class reframed.
- [[WidthDepthSearch]] — the control space.
- [[OfflineReplayEnvironment]] — affordability mechanism.
- [[BetaParameterization]] — tractability mechanism.
- [[ExecutionTraceFeedback]] — feedback richness.
- [[ConfidenceMomentumController]] — discovered controller.
- [[AgenticAlgorithmDiscovery]] — broader paradigm AutoTTS instantiates for TTS.
- [[claudecode|Claude Code]] — explorer LLM.
- [[2604.25850-agentic-harness-engineering|Meta-Harness]] — methodological precedent (execution-trace-driven discovery).
- [[2602.03845-parallel-probe|Parallel-Probe]] — both a baseline and the data-collection protocol AutoTTS reuses.
- [[2605.02396-heavyskill|HEAVYSKILL]] — productive tension: automate the harness vs internalize it as inner skill.
- [[2402.01817-llm-modulo|LLM-Modulo]] — the discovered CMC is an LLM-Modulo instance with the controller as external critic.
