---
title: "RLVR"
type: concept
tags: [ml-method]
sources: [2605.02396-heavyskill, 2507.19457-gepa, agentic-design-patterns-ch17-reasoning]
last_updated: 2026-06-07
---

# RLVR

Reinforcement Learning from Verifiable Rewards. Uses programmatic / deterministic verifiers (e.g. test cases, math answers) instead of preference models. HEAVYSKILL shows RLVR can scale both depth (deliberation) and breadth (parallel generation) of heavy thinking simultaneously, improving Heavy-Mean@k and Pass@k.

## In [[2507.19457-gepa|GEPA]]

GEPA frames itself against RLVR (Reinforcement Learning with Verifiable Rewards) as the canonical setting where modern compound-AI-system optimization happens. Its argument is that **even when the reward is verifiable**, collapsing the rollout to a scalar reward throws away the natural-language information that the verifier produced *while computing* the reward (compiler errors, judge rationales, profiler output) — content GEPA captures as the [[FeedbackFunction|feedback function]] $\mu_f$. The reflective-prompt-evolution thesis is sharpest precisely in RLVR settings where the verifier emits rich diagnostic text.

## Agentic Design Patterns (Gulli, Ch 17) perspective

[[agentic-design-patterns-ch17-reasoning|Chapter 17 of *Agentic Design Patterns*]] presents RLVR (there expanded as *"Reinforcement Learning **with** Verifiable Rewards"*) as **the key innovation enabling a new class of "reasoning models."** The narrative: standard [[ChainOfThought|CoT]] prompting is *"a somewhat basic approach… a single, predetermined line of thought"*; reasoning models instead *"dedicate a variable amount of 'thinking' time before providing an answer,"* producing an extended, dynamic CoT that *"can be thousands of tokens long"* and supports self-correction and backtracking, with more effort spent on harder problems. RLVR is the training strategy that makes this possible: *"by training the model on problems with known correct answers (like math or code), it learns through trial and error to generate effective, long-form reasoning… without direct human supervision."* The chapter's framing — these models *"don't just produce an answer; they generate a 'reasoning trajectory' that demonstrates advanced skills like planning, monitoring, and evaluation"* — ties RLVR directly to the [[ScalingInferenceLaw|Scaling Inference Law]] (variable thinking budget) and to autonomous agents that break down and solve complex tasks with minimal human intervention.

## Connections
- [[reinforcementlearning|ReinforcementLearning]]
- [[2605.02396-heavyskill]]
- [[2507.19457-gepa]] — argues even RLVR rollouts under-use their information; the verifier's natural-language byproducts (compiler errors, judge text) are the missing supervision signal.
- [[grpo|GRPO]] — typical RLVR-compatible algorithm.
- [[agentic-design-patterns-ch17-reasoning]] — Ch 17 frames RLVR as the training method behind variable-thinking-time reasoning models.
- [[ReasoningTechniques]] / [[ScalingInferenceLaw]] — the agentic-pattern context and the inference-budget law RLVR-trained reasoning models operationalize.
- [[ChainOfThought]] — the "basic" baseline reasoning models extend into long dynamic chains.
