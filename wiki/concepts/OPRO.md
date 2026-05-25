---
title: "OPRO"
type: concept
tags: [prompt-optimization, instruction-tuning, lm-as-optimizer, baseline]
sources: [2406.11695-mipro]
last_updated: 2026-05-22
---

# OPRO

**Optimization by PROmpting** (Yang et al. 2023, arXiv:2309.03409). One of the foundational [[PromptOptimization|prompt optimization]] methods: use an LM itself as the optimizer over its own prompts. The proposer LM is repeatedly shown a **history of past (prompt, score) pairs** and asked to propose a new, better prompt. The optimizer relies on the LM's in-context inference to learn which prompts work well — there is no explicit surrogate model.

OPRO is **single-prompt single-stage by design**; the [[2406.11695-mipro|MIPRO paper]] extends it to multi-module LM programs in two variants — [[ModuleLevelOPRO|Module-Level OPRO]] (treats per-module program score as a quality proxy) and Program-Level OPRO (passes the full multi-stage trajectory in the proposer's history; relies on the LM to do credit assignment from long traces).

## Position in the algorithm taxonomy

In the [[2406.11695-mipro|MIPRO paper]]'s framing (Algorithm 1), OPRO sits at the **history-based credit-assignment** position — the LM is the surrogate. This is one of three credit-assignment options the paper studies:

| Credit assignment | Mechanism | Variant in paper |
|---|---|---|
| Greedy | Optimize one stage at a time | CA-OPRO (rejected) |
| **Surrogate** | Bayesian model over parameter space | [[MIPROv2|MIPRO]] (chosen) |
| History-based | LM in-context inference from past evals | [[ModuleLevelOPRO|Module-Level OPRO]] / Program-Level OPRO |

The paper finds **surrogate-based wins on 5/7 tasks** — but the Module-Level OPRO variant still does respectable instruction-only optimization, and its 0-shot scores on HoVer (37.3 dev) come within ~1 point of 0-shot MIPRO.

## Limitations identified by the [[2406.11695-mipro|MIPRO paper]]

- **Program-level OPRO assumes the LM can do credit assignment from long trajectory histories.** As trajectory length grows, *"information contained in histories is likely to be lost"* (Liu et al. 2023 — the [[lostinthemiddle|lost-in-the-middle]] effect). The paper opts for Module-Level OPRO as the more practical extension.

- **History-based credit assignment cannot benefit from a structured prior** the way a Bayesian surrogate can.

- **CA-OPRO** (greedy single-module OPRO) was tested and *"performance did not justify its inefficiency."*

## Connections

- [[2406.11695-mipro]] — the canonical wiki source for OPRO's role in LM-program optimization.
- [[ModuleLevelOPRO]] — the per-module multi-stage extension.
- [[MIPROv2|MIPRO]] — the surrogate-based successor; the credit-assignment alternative.
- [[PromptOptimization]] — parent task.
- [[DSPy]] — DSPy provides MIPRO and its OPRO-derived variants in the optimizer catalog.
- [[lostinthemiddle|lost-in-the-middle]] — the failure mode that motivates Module-Level OPRO over Program-Level OPRO.
