---
title: "Agentic Algorithm Discovery"
type: concept
tags: [autoresearch, llm-driven-search, automl, framework]
sources: [2605.08083-autotts, 2604.25850-agentic-harness-engineering, 2605.03808-agentic-imodels]
last_updated: 2026-05-15
---

# Agentic Algorithm Discovery

LLM-driven program search: a frontier model (the *explorer*) iteratively proposes and refines code-defined algorithms, with each candidate evaluated in a sandboxed environment whose outputs (scalar scores + execution traces) form the history fed back to the explorer for the next round.

## Lineage

| Year | System | Domain | Explorer | What's new |
|---|---|---|---|---|
| 2016–19 | Neural Architecture Search (Zoph & Le; Elsken et al.) | Network topology | RL controller / evolutionary search | Pre-LLM AutoML; the original "discover the algorithm" framing. |
| 2023 | FunSearch (Romera-Paredes et al., *Nature*) | Mathematical functions | LLM | Used Gemini / Codey to discover new combinatorial constructions. |
| 2024 | EoH (Evolution of Heuristics, Liu et al.) | Algorithmic heuristics | LLM | Population-based LLM-driven heuristic evolution. |
| 2025 | AlphaEvolve (Novikov et al.) | Scientific & algorithmic code | LLM | Frontier coding agent for scientific discovery. |
| 2024 | ADAS (Hu, Lu & Clune) | Agentic systems | LLM | Automated design of agentic system topology. |
| 2026 | [[2604.25850-agentic-harness-engineering\|Meta-Harness]] (Lee et al.) | Agentic harnesses | LLM with full execution histories | First to expose **execution traces** to the proposer, enabling failure-mode diagnosis. |
| 2026 | [[2605.08083-autotts\|AutoTTS]] (Zheng et al.) | Test-time scaling controllers | [[claudecode\|Claude Code]] | Applies the paradigm to TTS; introduces [[BetaParameterization]] and [[OfflineReplayEnvironment]] for affordable controller search. |
| 2026 | TTT-Discover (ref [44]) / ThetaEvolve (ref [45]) | RL-updated test-time policies | LLM + weight updates | Extends discovery to *model-weight* updates at test time. |
| 2026 | [[2605.03808-agentic-imodels\|AGENTIC-IMODELS]] | Interpretable agent-readable models | Coding-agent autoresearch loop | Targets *interpretability* tools rather than performance algorithms. |

## Core Pattern

1. **Define a sandbox / replay environment** that makes candidate evaluation deterministic and affordable.
2. **Define a structured output format** (a Python class, a function signature, a heuristic skeleton).
3. **Constrain the search space** — e.g. [[BetaParameterization|single-knob hyperparameter discipline]], fixed function signatures, monotonicity requirements.
4. **Iterate**: explorer reads history $\mathcal{H}$ → proposes candidate → environment evaluates → traces appended to $\mathcal{H}$ → repeat.
5. **Select** the best candidate by held-out performance, not search-set performance.

## Empirical Patterns

- **[[ExecutionTraceFeedback|Execution traces beat scalar scores]]** ([[2604.25850-agentic-harness-engineering|Meta-Harness]], [[2605.08083-autotts|AutoTTS]] ablations): explorer needs to know *why* a candidate failed, not just *that* it failed.
- **Constraining the search space helps**: AutoTTS's beta parameterization improves held-out generalization despite reducing expressivity.
- **Discovery cost is dominated by explorer API**, not by underlying-task inference: AutoTTS's whole loop costs $39.9 because evaluation is replay-based.
- **Discovered algorithms can reveal non-obvious mechanisms** (CMC's four mechanisms in AutoTTS; Meta-Harness's emergent observability patterns).

## Connections

- [[2605.08083-autotts]] — TTS instantiation.
- [[2604.25850-agentic-harness-engineering|Meta-Harness]] — harness instantiation; methodological precedent for trace-driven feedback.
- [[2605.03808-agentic-imodels|AGENTIC-IMODELS]] — interpretability instantiation.
- [[AutoTTS]] / [[BetaParameterization]] / [[ExecutionTraceFeedback]] / [[OfflineReplayEnvironment]] — AutoTTS-specific machinery.
- [[autoresearch|Autoresearch]] — adjacent concept; agentic algorithm discovery is autoresearch applied to *algorithms*.
- [[recursiveselfimprovement|Recursive Self-Improvement]] — weaker form here: discovery improves the *harness* / *strategy*, not the base model's weights. ThetaEvolve / TTT-Discover bridge into weight updates.
- [[2604.25067-frontier-coding-agents-c4|Frontier Coding Agents for C4]] — uses the same explorer-driven pattern for replicating AI breakthroughs.
- [[claudecode|Claude Code]] — the explorer of choice across several 2026 systems.
