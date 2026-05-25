---
title: "Best-of-N"
type: concept
tags: [ml-method, inference, test-time-scaling]
sources: [2605.08083-autotts, ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Best-of-N

Generate $N$ independent candidate outputs from a base model and select one (by majority vote, verifier score, or reward model). The simplest [[testtimescaling|test-time scaling]] pattern — degenerate case of the [[WidthDepthSearch|width–depth control space]] where width = $N$ and depth is fixed (each candidate runs to a final answer with no intermediate probing or pruning).

In [[2605.08083-autotts|AutoTTS]]'s formalism, BoN corresponds to: BRANCH × $N$, CONTINUE all to completion, ANSWER with majority vote — no PROBE, no PRUNE. [[selfconsistency|Self-Consistency]] is the BoN instance with majority-vote aggregation.

## Connections

- [[testtimescaling|Test-Time Scaling]] — parent.
- [[parallelreasoning|Parallel Reasoning]] — the width-axis pattern.
- [[selfconsistency|Self-Consistency]] — BoN + majority vote.
- [[WidthDepthSearch]] — formalization that places BoN as a degenerate corner.
- [[2605.08083-autotts]] — uses `get_new_branch_final_answer()` API as the BoN primitive in the AutoTTS environment.
- [[DSPyBestOfN|`dspy.BestOfN`]] — the [[DSPy]] framework module instantiating this pattern with a programmable `reward_fn` and threshold-based early-exit; sibling [[DSPyRefine|`dspy.Refine`]] adds an auto-feedback loop between rollouts. Both introduced in DSPy 2.6 as replacements for [[DSPyAssert]] / [[DSPySuggest]].

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

[[ChipHuyen|Chip Huyen]] gives the **production-facing framing** of best-of-N: it's *"the [[TestTimeCompute|test-time compute]] strategy that lets companies skip RL altogether."* Per Ch 2:

> "Some companies find it okay to skip reinforcement learning altogether. ... They get their models to generate multiple outputs and pick the ones given high scores by their reward models. This approach, often referred to as the best of N strategy, leverages how a model samples outputs to improve its performance."

Three Ch-2-named production users:
- **[[StitchFix|Stitch Fix]]** and **[[Grab|Grab]]** — reward model + best-of-N.
- **[[Nextdoor|Nextdoor]]** (2023) — found reward-model-guided BoN to be *the key factor* in lifting their application's performance.

Two named selection methods:
1. **Highest average [[Logprobs|logprob]]** — what OpenAI's `best_of` API parameter uses.
2. **Highest [[RewardModel|reward-model]] / [[Verifier|verifier]] score** — the Stitch Fix / Grab approach.

The chapter ties best-of-N to the **30× verifier result** (Cobbe et al. 2021 on math problems): using a verifier over best-of-N candidates was worth ≈30× model-size increase. [[googledeepmind|DeepMind]] (Snell et al. 2024) generalized this: scaling test-time compute can beat scaling parameters.

Scaling limits debated in Ch 2: OpenAI's experiment peaked at ~400 samples; Stanford's *Monkey Business* (Brown et al. 2024) shows log-linear improvement up to 10,000 samples. Huyen flags both — and notes nobody in production samples 400+ outputs per query because of cost.
