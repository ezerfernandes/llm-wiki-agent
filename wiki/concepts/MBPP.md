---
title: "MBPP"
type: concept
tags: [benchmark, code-generation, python]
sources: [2604.14585-prompt-optimization-coin-flip]
last_updated: 2026-05-22
---

# MBPP

**MBPP** — *Mostly Basic Python Problems* (Austin, Odena, Nye, Bosma, Michalewski, Dohan, Jiang, Cai, Terry, Le & Sutton, arXiv:2108.07732, 2021) — is a Python program synthesis benchmark: short natural-language problem descriptions paired with reference solutions and unit tests. The canonical evaluation metric is **pass@1** (whether the first generated solution passes all unit tests).

## In Zhang et al. 2026

[[2604.14585-prompt-optimization-coin-flip|Zhang et al. (2026)]] include MBPP in Study 1 as the *a priori* "medium coupling" prediction — code generation seemingly requires Agent A to decompose the task and Agent B to produce executable Python that respects that decomposition.

**Result (Study 1, Table 1):** MBPP shows the **highest interaction-variance share of any task** — 2.15% on Haiku, 1.50% on Nova — but still $F < 1.0$ and $p > 0.52$. The interaction term is non-significant, just as in HotpotQA and XSum.

MBPP is also the only task in Study 1 where **question difficulty does *not* dominate**: it explains only 19.3% on Haiku and 39.9% on Nova, vs 58–91% on the other two tasks. The residual variance is correspondingly large (77.4% / 58.0%) — MBPP test cases vary more in their model-specific difficulty than questions in HotpotQA or XSum.

## Position

MBPP is one of three Study 1 benchmarks alongside [[hotpotqa|HotpotQA]] (tight coupling expected) and [[XSum]] (loose coupling expected). It is the **closest of the three to producing detectable coupling** — but still falls short of the $F = 1$ threshold. The wiki's first concept-page anchor for MBPP.

## Connections

- [[2604.14585-prompt-optimization-coin-flip]] — canonical source.
- [[hotpotqa]] / [[XSum]] — sibling Study 1 tasks.
- [[AgentCoupling]] — the property Study 1 measures.
- [[ANOVAVarianceDecomposition]] — the decomposition applied.
- [[KernelBench]] / [[NPUEval]] — sibling code-generation benchmarks (different domains).
