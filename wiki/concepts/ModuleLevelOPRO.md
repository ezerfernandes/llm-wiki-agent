---
title: "Module-Level OPRO"
type: concept
tags: [prompt-optimization, instruction-tuning, lm-as-optimizer, multi-stage, baseline]
sources: [2406.11695-mipro]
last_updated: 2026-05-22
---

# Module-Level OPRO

The per-module multi-stage extension of [[OPRO|OPRO]] (Yang et al. 2023), introduced as a baseline in the [[2406.11695-mipro|MIPRO paper]] (§4.2).

## Algorithm

Module-Level OPRO assumes **program score is a good enough proxy for an individual instruction's quality** — i.e. it sidesteps the [[CreditAssignment|credit-assignment]] problem by treating each module's instruction history as if it were the only thing being varied.

| Method | What it does |
|---|---|
| `Initialize` | Seed instruction parameterizes each of $m$ modules in $\Phi$; evaluated end-to-end. |
| `Propose` | For each module $i$: the proposer LM is shown the *score* and the *$i_{th}$ module's instruction history* and asked to draft a new instruction for module $i$. Repeats for all $m$ modules. |
| `Update` | The $m$ new instructions parameterize $\Phi$, $\Phi$ is evaluated, the resulting score is appended to **every** module's history (the same score per module). |
| `ExtractOptimizedSets` | Return the best end-to-end-scoring instruction set across the $I$ iterations. |

## Variants

- **Module-Level OPRO −G** ("no grounding"): drop the **grounding** (dataset summary + program summary + bootstrapped demo context) — the paper uses this as an ablation; **grounding hurts on [[ScoNe]] but helps on [[hotpotqa|HotPotQA]] and [[HoVer]]** (Lesson 4: *"Grounding is helpful for instruction proposal overall, but the best proposal strategy varies by task"*).

- **Program-Level OPRO**: passes the **full multi-stage trajectory** through the proposer LM's history and relies on the LM to do credit assignment from the trace. The paper found this *"more complex and did not appear to provide additional performance gains"* over Module-Level OPRO.

- **CA-OPRO** (Coordinate-Ascent OPRO): greedy per-module variant — iterate through each module, propose $N$ instructions while holding others fixed, pick best, advance. Tested in initial experiments; **rejected: *"From initial experiments, we found CA-OPRO's performance did not justify its inefficiency."***

## Position in the catalog

Module-Level OPRO is the **instructions-only history-based baseline** in the [[2406.11695-mipro|MIPRO benchmark]] (Table 2). It's the algorithm the paper compares against to establish that **Bayesian-surrogate credit assignment beats LM-in-context credit assignment** on 5/7 tasks.

## Connections

- [[2406.11695-mipro]] — the canonical source.
- [[OPRO]] — the single-stage Yang et al. 2023 predecessor.
- [[MIPROv2|MIPRO]] — the surrogate-based alternative the paper introduces as its main contribution.
- [[CreditAssignment]] — the structural problem this approach sidesteps via the program-score-as-proxy assumption.
- [[DSPy]] — implementation context.
