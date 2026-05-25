---
title: "ANOVA Variance Decomposition"
type: concept
tags: [statistics, anova, evaluation, methodology, compound-ai-system]
sources: [2604.14585-prompt-optimization-coin-flip]
last_updated: 2026-05-22
---

# ANOVA Variance Decomposition

**Analysis of variance (ANOVA) variance decomposition** is a classical statistical technique that partitions the total variance of a measured outcome into additive components attributable to each design factor and to factor-factor interactions. [[2604.14585-prompt-optimization-coin-flip|Zhang et al. (2026)]] introduce ANOVA decomposition to the wiki as a **falsifiable evaluation protocol for compositional behavior in [[CompoundAISystem|compound AI systems]]** — a structured alternative to ad hoc aggregate-benchmark reporting.

## The decomposition (paper Appendix A)

Let $Y_{ijk}$ denote the score for Agent A prompt $i$, Agent B prompt $j$, and question $k$. Subtract question means to obtain $\tilde{Y}_{ijk} = Y_{ijk} - \bar{Y}_{\cdot\cdot k}$, then decompose:

$$\mathrm{SS}_A = n K_B \sum_i (\tilde{\bar Y}_{i\cdot\cdot} - \tilde{\bar Y}_{\cdot\cdot\cdot})^2$$

$$\mathrm{SS}_B = n K_A \sum_j (\tilde{\bar Y}_{\cdot j\cdot} - \tilde{\bar Y}_{\cdot\cdot\cdot})^2$$

$$\mathrm{SS}_{A \times B} = n \sum_{i,j} (\tilde{\bar Y}_{ij\cdot} - \tilde{\bar Y}_{i\cdot\cdot} - \tilde{\bar Y}_{\cdot j\cdot} + \tilde{\bar Y}_{\cdot\cdot\cdot})^2$$

The interaction term has $(K_A - 1)(K_B - 1) = 81$ degrees of freedom (for $K=10$) vs $K_A - 1 = 9$ for each main effect. This is why **2% of total variance can still be non-significant** — $\mathrm{MS}_{A \times B} = 2\%/81$ per df, while $\mathrm{MS}_A = 0.6\%/9$ per df yields a larger $F$.

## What the F-test answers

The interaction $F$-test answers a directly actionable question: **does the optimal prompt for one agent depend on the prompt of another?**

- $F_{A \times B} < 1$ → no detectable coupling → optimize agents independently.
- $F_{A \times B} > 1$ and significant → joint optimization is warranted.

This replaces hand-wavy intuition about "how coupled are the agents in my pipeline?" with a concrete statistical test.

## The result in Zhang et al. 2026

Across six model×task conditions (Claude Haiku 4.5 + Amazon Nova Lite × HotpotQA / XSum / MBPP), **every condition has $F_{A \times B} < 1$** and $p > 0.52$. Interaction explains 0.18–2.15% of total variance. **Question difficulty dominates** — 19–91% of total variance — meaning evaluation noise from question sampling overwhelms most real optimization signal.

The visual companion (Figure 2 of the paper): $10 \times 10$ score matrices show row/column banding (additive structure) without off-diagonal patterns.

## As a methodological proposal

The paper argues ANOVA decomposition generalizes beyond two-agent pipelines to **any compositional system**:

> *"Our ANOVA decomposition produces falsifiable predictions — if a pipeline's interaction F > 1, joint optimization is warranted; if F < 1, it is not — that can be tested on any architecture. This contrasts with typical compound AI evaluation, which reports aggregate task scores without decomposing why a pipeline succeeds or fails."*

This is the wiki's first use of ANOVA as an LLM-system evaluation methodology. The protocol's generalization candidates: deeper pipelines (3+ way ANOVA), $\Pi \times \Theta$ axis decomposition for [[BetterTogether]]-style bi-axial schedules, and module-vs-tool decomposition for [[react|ReAct]]-style agents.

## Cost

- $K = 10$ prompts per agent, $n = 30$ questions, $100 \times 30 = 3{,}000$ evaluations per model×task.
- For mid-tier executors + a judge, ~$80 per coupling test (paper Stage 1).
- ~1 day wall-clock with parallel evaluation.

## Connections

- [[2604.14585-prompt-optimization-coin-flip]] — canonical source; introduces the methodology.
- [[AgentCoupling]] — the structural property the decomposition measures.
- [[CompoundAIDiagnostic]] — Stage 1 of the practitioner framework.
- [[BiasVarianceDecomposition]] — sibling variance-decomposition concept (model-level rather than experiment-level).
- [[CompoundAISystem]] — the structural object being decomposed.
- [[HeadroomTest]] — Stage 2 of the diagnostic; complementary measurement.
