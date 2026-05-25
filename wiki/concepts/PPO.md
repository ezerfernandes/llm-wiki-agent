---
title: "PPO"
type: concept
tags: [reinforcement-learning, rlhf, alignment, training]
sources: [ai-engineering-ch02-foundation-models, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# PPO

**Proximal Policy Optimization** — a reinforcement-learning algorithm **released by [[openai|OpenAI]] in 2017** that has become the default RL backbone for [[rlhf|RLHF]]. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]:

> "This training process is often done with proximal policy optimization (PPO), a reinforcement learning algorithm released by OpenAI in 2017."

## How RLHF uses PPO

After the [[RewardModel|reward model]] is trained:

1. **Sample a prompt** from a distribution (e.g., real user prompts).
2. **Generate a response** with the current (SFT-initialized) policy.
3. **Score it** with the reward model.
4. **Update the policy** via PPO to maximize the score, with a **KL-divergence penalty** against the original SFT model to prevent the policy from drifting too far from coherent generation (and to limit reward hacking).

## What "proximal" means

PPO uses a clipped surrogate objective that limits how much the policy can change in a single update — keeping the new policy "proximal" to the old one. This is what gives PPO its empirical stability advantage over earlier policy-gradient methods.

## Position in the RLHF stack

Ch 2 doesn't go into PPO's mathematical detail — only that it's the RL algorithm of choice for the foundation-model update step. The chapter notes:

> "As of this writing, there are debates on why [RLHF and DPO] work. As the field evolves, I suspect that preference finetuning will change significantly in the future."

[[DPO|DPO]] (Rafailov et al. 2023) was developed in part to **eliminate the PPO step** of RLHF — collapsing the reward-model-plus-PPO loop into a single closed-form preference-alignment objective.

## Connections
- [[rlhf]] — the parent algorithm that uses PPO.
- [[RewardModel]] — the model whose scores PPO maximizes.
- [[DPO]] — the alternative that removes the PPO step.
- [[grpo]] — successor RL algorithm in the same family.
- [[KullbackLeiblerDivergence]] — the regularizer keeping the policy close to the SFT model.
- [[PolicyFunction]] / [[reinforcementlearning]] — the broader RL formalism.
- [[ai-engineering-ch02-foundation-models]] — primary source.
- [[openai|OpenAI]] — the lab that released PPO.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* names PPO as the **canonical RL algorithm for fine-tuning LLMs with a reward model** and cites Schulman et al. 2017 (arXiv:1707.06347). The chapter's headline attribution: **PPO was used to train the original ChatGPT (November 2022)**.

### How Ch 12 frames PPO

> *"PPO is a popular reinforcement technique that optimizes the instruction-tuned LLM by making sure that the LLM does not deviate too much from the expected rewards."* — Ch 12

### Why Ch 12 chooses DPO over PPO

The chapter walks PPO + the [[RewardModel|reward model]] as the **baseline** preference-tuning method, then positions [[DPO]] as the **simpler, more stable replacement** in its worked recipe:

> *"A disadvantage of PPO is that it is a complex method that needs to train at least two models, the reward model and the LLM, which can be more costly than perhaps necessary. Compared to PPO, the authors found DPO to be more stable during training and more accurate."* — Ch 12

DPO eliminates **both** the reward model and the RL training loop — a strict simplification of the PPO stack the chapter is willing to pay for.
