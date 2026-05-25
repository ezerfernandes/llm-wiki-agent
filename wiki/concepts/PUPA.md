---
title: "PUPA"
type: concept
tags: [benchmark, privacy, delegation, llm-systems]
sources: [2507.19457-gepa, papillon-colab-tutorial, dspy-tutorial-rl-papillon, dspy-tutorial-gepa-papillon]
last_updated: 2026-05-24
---

# PUPA

**P**rivacy-**U**tility **PA**reto benchmark (Li et al., 2025a). Evaluates **privacy-aware LLM delegation**: given a private user query, a smaller local LLM must construct a *redacted / generalized* request for a powerful external LLM, such that the external LLM can help without learning private information about the user.

The benchmark scores both **utility** (does the external LLM's answer solve the user's task?) and **privacy** (how much PII / proprietary info leaked into the external request?) — the Pareto frontier of these is the namesake.

Used by [[2507.19457-gepa|GEPA]] as one of six core benchmarks. PUPA is the benchmark on which the paper's clearest reflective-trajectory illustration (Figure 5) is built — an 11-step iterative refinement of the delegation prompt, each step adding more nuanced privacy reasoning.

## GEPA results on PUPA

| Optimizer | Qwen3 8B | GPT-4.1 Mini |
|---|---|---|
| Baseline | 80.82 | 74.18 |
| [[grpo|GRPO]] | 86.66 | — |
| [[MIPROv2]] | 81.55 | 85.37 |
| **GEPA** | **91.85** | 94.47 |
| **GEPA+Merge** | 86.26 | **96.46** |

PUPA shows GEPA's strongest absolute gain over baseline (+11–22 pts depending on model) and one of the cleanest demonstrations of progressively-richer prompt evolution — the optimized prompt ends at a *"Rigorous, Exhaustive Protocol"* enforcing strict stepwise PII abstraction with "zero leakage tolerated."

## The PAPILLON program

PUPA's *delegation program* — the thing being evaluated — is [[PAPILLON]] (same authors, Li et al. 2025a). PAPILLON composes a `CraftRedactedRequest` ([[chainofthought|ChainOfThought]]) module that strips PII before delegation, and a `RespondToQuery` ([[DSPyPredict|Predict]]) module that combines the external LLM's answer with the original private query. Two DSPy tutorials supply complementary PUPA training receipts:

| Tutorial | Optimizer | Splits | Composite lift |
|---|---|---|---|
| [[papillon-colab-tutorial]] | **[[MIPROv2]]** (authors-of-record, Llama-3.1-8B-Instruct via [[SGLang]] × GPT-4o-mini remote) | `pupa_new` only — **150 train / 150 dev / remainder test** | **not printed** (runnable-receipt-only) |
| [[dspy-tutorial-rl-papillon]] | [[ArborGRPO]] (weight-space, [[LoRA]] on Qwen2.5-1.5B) | `pupa_new` only — 225 train / 225 dev / 450 test | 54.6 → 60.0 (devset) |
| [[dspy-tutorial-gepa-papillon]] | [[GEPA]] (prompt-space, GPT-4.1 Nano student × GPT-4.1 reflection) | **`pupa_tnb` + `pupa_new`** — 225 train / 225 dev / 214 test | 76.5 → 86.1 (testset) at `max_full_evals=1` |

**Split discrepancy across three tutorials**: the [[papillon-colab-tutorial|Colab]] uses `pupa_new` only with the smallest training budget (150 train); `rl_papillon` uses `pupa_new` only with 225 train; `gepa_papillon` mixes `pupa_tnb` and `pupa_new`. The three tutorials therefore evaluate on **non-overlapping test sets** — their composite numbers are **not on the same metric base** and must not be compared head-to-head. The qualitative ordering (prompt-space lift > weight-space lift on this program family) matches the [[2507.19457-gepa|GEPA paper's]] central thesis.

**Canonical authors-of-record conventions** (per [[papillon-colab-tutorial]]): `pii_units` field is `||`-separated; `pii_units` is GPT-4o-mini-extracted with documented over-redaction; the paper used `PUPA-TNB` for standardized cross-model evaluation while tutorials use `PUPA-New` for demonstration. The `pupa_tnb` config is **derived from the [Trust No Bot paper (arXiv:2407.11438)](https://arxiv.org/abs/2407.11438) annotations**; `pupa_new` is the rest of the [[WildChat]] dataset not annotated in that paper.

## Connections
- [[2507.19457-gepa]] — uses PUPA as a core benchmark and as the headline reflective-trajectory illustration.
- [[PAPILLON]] — the *delegation program* PUPA evaluates.
- [[papillon-colab-tutorial]] — **canonical author-of-record tutorial** that loads `Columbia-NLP/PUPA` via HuggingFace with both `pupa_tnb` and `pupa_new` configs; trains on 150 examples from `pupa_new["train"]`. **The wiki's first MIPROv2-on-PUPA tutorial-grade receipt.**
- [[dspy-tutorial-rl-papillon]] — DSPy tutorial that trains PAPILLON on PUPA via [[ArborGRPO]] (weight-space).
- [[dspy-tutorial-gepa-papillon]] — DSPy tutorial that optimizes PAPILLON on PUPA via [[GEPA]] (prompt-space) — **the wiki's first GEPA-on-PUPA tutorial-grade receipt** complementing the [[2507.19457-gepa|paper-scale GEPA-on-PUPA receipt]].
- [[ArborGRPO]] — the multi-module GRPO optimizer used for the PAPILLON+PUPA training run.
- [[GEPA]] — the reflective prompt optimizer used in the gepa_papillon tutorial.
- [[promptinjection|Privacy / Security]] — adjacent concern.
- [[2605.00424-skills-as-verifiable-artifacts]] — adjacent privacy-via-verification framing.
