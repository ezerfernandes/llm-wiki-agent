---
title: "Independent Optimization"
type: concept
tags: [prompt-optimization, compound-ai-system, independence, multi-agent]
sources: [2604.14585-prompt-optimization-coin-flip]
last_updated: 2026-05-22
---

# Independent Optimization

**Independent optimization** treats each module's prompt as a separately searchable object — running a per-module optimizer over $\pi_i$ in isolation while holding the other modules' prompts fixed. The opposite of [[JointOptimization|joint optimization]].

## When it suffices

[[2604.14585-prompt-optimization-coin-flip|Zhang et al. (2026)]] empirically establish that independent optimization **matches** joint optimization across six model×task conditions on two-agent feed-forward pipelines:

- The $A \times B$ interaction term is non-significant in every condition ($p > 0.52$, $F < 1.0$).
- The joint optimum (best cell of the $10 \times 10$ grid) and independent optimum (best row × best column) are **adjacent or identical**, with a gap of 0.0–3.3 pts.
- **Budget-equalized simulations** (1,000 trials) confirm independent search matches joint search at every budget level.

When the [[ANOVAVarianceDecomposition|ANOVA coupling test]] returns $F_{A \times B} < 1$, independent per-agent optimization is the correct default.

## The procedure

1. Identify the bottleneck agent (largest main effect from the ANOVA decomposition).
2. Run [[APE]]-style generate-and-rank (or any per-module optimizer) on **that agent only**.
3. Repeat for other agents if their main effects are non-trivial.

No cross-module interaction term to optimize → no joint search → linear cost in agents instead of exponential.

## Why it works

The mechanism — per [[2604.14585-prompt-optimization-coin-flip|Zhang et al.]] — is that [[InstructionTuning|instruction-tuning]] + [[rlhf|RLHF]] compress diverse input phrasings into narrow output distributions. Agent B's output variance is dominated by the *semantic content* of Agent A's response (set by the question), not by Agent A's *stylistic variation*. The pipeline composes as **independently-robust functions**.

## Cost contrast

| Approach | Cost | Budget for 3-agent pipeline |
|---|---|---|
| Independent per-agent search | Linear in $\|M\|$ | $3 \times$ single-agent cost |
| Joint cross-module search | Exponential in $\|M\|$ | $\sim N^{\|M\|}$ |

When agents don't interact, the cost of joint search buys nothing.

## Connections

- [[2604.14585-prompt-optimization-coin-flip]] — empirical validation source.
- [[JointOptimization]] — the alternative this concept replaces under coupling absence.
- [[AgentCoupling]] / [[ANOVAVarianceDecomposition]] — the test that licenses this default.
- [[CompoundAIDiagnostic]] — practitioner framework Stage 1 → independent.
- [[APE]] — recommended per-agent optimizer (non-iterative, no overfitting risk).
- [[HeadroomTest]] — Stage 2 check on each agent individually.
- [[CompoundAISystem]] — structural target.
