---
title: "GEPA"
type: concept
tags: [dspy, optimizer, gepa, reflection, instruction-tuning, teleprompter]
sources: [dspy-optimizers, dspy-optimization-overview]
last_updated: 2026-05-17
---

# GEPA

**`dspy.GEPA`** is [[DSPy]]'s **reflection-based instruction optimizer** — the only optimizer in [[DSPyOptimizers|the catalog]] that **uses an LM to reflect on the program's trajectory** and propose prompts addressing the gaps. GEPA is also **the only specific optimizer named on [[dspy-optimization-overview|page 12]]** (the workflow-level Optimization Overview) — and the reason GEPA is named there is structurally important: it is the **named carve-out** from the framework-level **inverted 20/80 train/val split** recommendation.

The canonical source is [[dspy-optimizers|page 13 of the DSPy *Learn* corpus]]; the workflow-level disclosure is on [[dspy-optimization-overview|page 12]].

## Mechanism

[[dspy-optimizers|The page]]'s definition:

> *"Uses LM's to reflect on the DSPy program's trajectory, to identify what worked, what didn't and propose prompts addressing the gaps. Additionally, GEPA can leverage domain-specific textual feedback to rapidly improve the DSPy program."*

The mechanism is **introspective**: rather than searching a candidate space (like [[MIPROv2|`MIPROv2`]]'s [[BayesianOptimization|Bayesian Optimization]]) or refining via coordinate ascent (like `COPRO`), GEPA asks an LM to **reflect** on the program's execution traces and **diagnose** what's failing. The diagnosis produces new instructions targeting the identified gaps.

Two ingredients distinguish GEPA from sibling instruction optimizers:

1. **LM reflection on trajectories.** The optimizer feeds the program's trajectories (across multiple training examples) to an LM, which produces a *what-worked / what-didn't* analysis and uses it to draft improved instructions. This is structurally **distinct from [[MIPROv2]]'s "grounded proposal"** stage — MIPROv2 proposes instructions from code+data+traces in a generative pass; GEPA explicitly **reflects** on outcomes and diagnoses failures.

2. **Domain-specific textual feedback.** GEPA can consume **domain-specific text feedback** alongside the metric. This is the only optimizer in the catalog that names a *textual feedback* input distinct from the scalar metric — useful for domains where *why* an output is wrong is easier to articulate than a numeric score.

## The 20/80 split carve-out

[[dspy-optimization-overview|The Optimization Overview]] commits the framework to an **inverted 20/80 train/val split** for *most prompt optimizers* (rationale: prompt optimizers tend to overfit on small training sets, and a large validation set is the overfitting defense). GEPA is the **only named exception**:

> *"However, the GEPA optimizer follows standard ML practice — maximizing the training set size while keeping the validation set sufficiently sized to represent the downstream task distribution."*

The mechanism that justifies GEPA's exemption is **left implicit** on [[dspy-optimization-overview|page 12]] and **only partially developed** on [[dspy-optimizers|page 13]] — the reflection-driven mechanism produces instructions that are **more robust to small training sets** than the search-driven mechanisms used by other optimizers, presumably because reflection generalizes from few examples in a different way than search does. The page doesn't formalize this beyond the empirical claim that GEPA *"follows standard ML practice"*.

This is the **single most non-obvious per-optimizer disclosure** in the *Learn* corpus — the framework names a specific optimizer (GEPA) on the workflow-level page (page 12) precisely because it **violates** a framework-level recommendation, and only to **explicitly grant the exemption**. Reading the [[dspy-optimizers|page-13 per-optimizer documentation]] is **load-bearing** before applying the 20/80 split mechanically — the train/val split is a **per-optimizer recommendation**, not a universal rule.

## Domain-specific textual feedback

GEPA's ability to *"leverage domain-specific textual feedback"* is the **first explicit non-metric supervision signal** in DSPy's optimizer catalog. Most optimizers consume *only* the scalar metric as their feedback channel; GEPA additionally consumes **textual** descriptions of what's wrong with the program's outputs. This is structurally compatible with DSPy's [[llmasjudge|LLM-as-judge]] pattern from [[DSPyMetrics]] — the same LM that produces a *score* can produce a *narrative explanation*, and GEPA can consume both.

The [[dspy-optimizers|page]] does not detail the mechanism; tutorials are linked: *"Detailed tutorials on using GEPA are available at [dspy.GEPA Tutorials](../../../tutorials/gepa_ai_program/)"*.

## Position in the catalog

GEPA belongs to the *Automatic Instruction Optimization* family (alongside `COPRO`, [[MIPROv2]], and `SIMBA`). What it tunes: **instructions only**. The mechanism distinguishes it:

| Optimizer | Search strategy |
|---|---|
| `COPRO` | Coordinate ascent / hill-climbing |
| [[MIPROv2]] | [[BayesianOptimization\|Bayesian Optimization]] over (instructions, demos) |
| `SIMBA` | Stochastic mini-batch sampling + self-reflective rules |
| **GEPA** (this page) | **LM reflection on program trajectory + optional domain-specific textual feedback** |

## Why GEPA is absent from the five-rule rubric

[[dspy-optimizers|The page]]'s five-rule getting-started rubric **does not name GEPA**. The rubric covers `BootstrapFewShot` (10 examples), `BootstrapFewShotWithRandomSearch` (50+), `MIPROv2` (200+ or 0-shot), and `BootstrapFinetune` (post-success efficiency). GEPA, `SIMBA`, `COPRO`, `KNNFewShot`, `Ensemble`, `BetterTogether`, and `LabeledFewShot` are **expert paths** the user must discover via the catalog.

The omission is consistent with GEPA being the most **research-frontier** optimizer in the catalog — the [[dspy-optimization-overview|page-12]] framing of optimization as *"an emerging paradigm"* applies most strongly here.

## Connections

- [[DSPy]] — the framework.
- [[DSPyOptimizers]] — the catalog this optimizer belongs to.
- [[DSPyOptimization]] — the workflow this optimizer operationalizes. **Resolves the long-standing forward reference [[GEPA]]** carried by [[DSPyOptimization]] since [[dspy-optimization-overview|page 12]] named GEPA as the only carved-out optimizer.
- [[dspy-optimizers]] — the canonical source page (page 13).
- [[dspy-optimization-overview]] — the workflow-level source (page 12) that named GEPA as the framework's only specific carve-out from the 20/80 train/val split.
- [[DSPyMetrics]] — the metric contract; GEPA additionally consumes optional domain-specific *textual* feedback alongside the scalar metric.
- [[DSPyModules]] / [[DSPyPredict]] — GEPA mutates each Predict's `signature` (instructions).
- [[DSPyProgrammingModel]] — the *"writing code instead of strings"* discipline; GEPA's reflection step inspects program trajectories the same way [[MIPROv2]]'s grounded proposal does.
- [[llmasjudge]] — the AI-feedback pattern GEPA's textual-feedback channel is structurally compatible with.
- [[MIPROv2]] — alternative instruction-tuning optimizer using Bayesian search instead of LM reflection.
- [[BootstrapFewShot]] / [[BootstrapFewShotWithRandomSearch]] / [[BootstrapFinetune]] — sibling optimizers; GEPA is the reflection-driven alternative to their search-driven mechanisms.
- [[OverFitting]] — the failure mode the inverted 20/80 split defends against; GEPA's reflection-driven mechanism is empirically **more robust** to small training sets than search-driven mechanisms, which is the structural justification for the carve-out.
- [[PromptOptimization]] — the general activity GEPA's instruction-tuning operationalizes.
