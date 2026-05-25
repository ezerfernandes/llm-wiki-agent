---
title: "RLVR"
type: concept
tags: [ml-method]
sources: [2605.02396-heavyskill, 2507.19457-gepa]
last_updated: 2026-05-22
---

# RLVR

Reinforcement Learning from Verifiable Rewards. Uses programmatic / deterministic verifiers (e.g. test cases, math answers) instead of preference models. HEAVYSKILL shows RLVR can scale both depth (deliberation) and breadth (parallel generation) of heavy thinking simultaneously, improving Heavy-Mean@k and Pass@k.

## In [[2507.19457-gepa|GEPA]]

GEPA frames itself against RLVR (Reinforcement Learning with Verifiable Rewards) as the canonical setting where modern compound-AI-system optimization happens. Its argument is that **even when the reward is verifiable**, collapsing the rollout to a scalar reward throws away the natural-language information that the verifier produced *while computing* the reward (compiler errors, judge rationales, profiler output) — content GEPA captures as the [[FeedbackFunction|feedback function]] $\mu_f$. The reflective-prompt-evolution thesis is sharpest precisely in RLVR settings where the verifier emits rich diagnostic text.

## Connections
- [[reinforcementlearning|ReinforcementLearning]]
- [[2605.02396-heavyskill]]
- [[2507.19457-gepa]] — argues even RLVR rollouts under-use their information; the verifier's natural-language byproducts (compiler errors, judge text) are the missing supervision signal.
- [[grpo|GRPO]] — typical RLVR-compatible algorithm.
