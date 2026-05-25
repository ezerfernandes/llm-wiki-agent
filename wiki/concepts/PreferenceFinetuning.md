---
title: "Preference Finetuning"
type: concept
tags: [post-training, alignment, llm, rlhf, dpo]
sources: [ai-engineering-ch02-foundation-models, ai-engineering-ch07-finetuning, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# Preference Finetuning

The **second step of [[posttraining|post-training]]**: further finetune the [[SupervisedFinetuning|SFT]] model to **output responses that align with human preference**. Typically done with reinforcement learning. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]:

> "Demonstration data teaches the model to have a conversation but doesn't teach the model what kind of conversations it should have."

## The problem this stage solves

After SFT, the model can hold a conversation — but it doesn't know **which conversations it should refuse, which to comply with, or how to handle culturally / politically contested questions**. Preference finetuning is the stage where the model is taught preferences for these decisions.

## The three named techniques

| Technique | Used by |
|---|---|
| **[[rlhf|RLHF]]** (Reinforcement Learning from Human Feedback) | GPT-3.5, Llama 2 |
| **[[DPO|DPO]]** (Direct Preference Optimization) | Llama 3 (Meta switched from RLHF→DPO to reduce complexity) |
| **[[RLAIF|RLAIF]]** (Reinforcement Learning from AI Feedback) | Potentially [[anthropic|Claude]] |

Ch 2 features RLHF in detail (despite its complexity) because it offers more flexibility to tweak the model than DPO. Per [[meta|Meta]]'s Llama 2 authors: *"the superior writing abilities of LLMs ... are fundamentally driven by RLHF."*

## The two RLHF sub-steps

1. **Train a [[RewardModel|reward model]]** that scores the foundation model's outputs given (prompt, response) → scalar.
2. **Optimize the foundation model** to generate responses that maximize the reward model's scores — typically via [[PPO|Proximal Policy Optimization]].

## The "skip RL" pattern

Some companies find it acceptable to skip the RL step entirely:

- **[[StitchFix|Stitch Fix]]** and **[[Grab|Grab]]** use only the reward model: generate multiple outputs from the model, pick the highest-scoring one ([[bestofn|best-of-N]] / verifier-based selection).
- This approach is the chapter's bridge from preference finetuning to [[TestTimeCompute|test-time compute]].

## Empirical effect

> "Empirically, RLHF and DPO both improve performance compared to SFT alone. However, as of this writing, there are debates on why they work." — Ch 2

## If pre-training were better, would we still need this?

> "Both SFT and preference finetuning are steps taken to address the problem created by the low quality of data used for pre-training. If one day we have better pre-training data or better ways to train foundation models, we might not need SFT and preference at all." — Ch 2

## Connections
- [[posttraining]] — parent stage.
- [[SupervisedFinetuning]] — the preceding stage.
- [[rlhf]] / [[DPO]] / [[RLAIF]] — the three techniques.
- [[RewardModel]] / [[ComparisonData]] / [[PPO]] — the RLHF machinery.
- [[bestofn]] / [[TestTimeCompute]] — the "skip RL" alternative.
- [[ai-engineering-ch02-foundation-models]] — primary source.

## From [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]]

Ch 7 reiterates [[ChipHuyen|Huyen]]'s position that preference finetuning is one of the **memory-heaviest finetuning modes** alongside [[SupervisedFinetuning|SFT]] — both typically require lots of high-quality annotated/comparative data that most application teams can't afford. The chapter's data-format reminder:

> "Preference finetuning requires comparative data that typically follows the format (instruction, winning response, losing response)."

Ch 7's bigger point: most application engineers will never *do* preference finetuning themselves — they'll consume the **preference-finetuned post-trained base model** released by model developers. The post-training stage is positioned as model-developer territory; application developers focus on PEFT-style adaptation on top of the post-trained base.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* contradicts Ch 7's *"only model developers do this"* posture by walking **a fully runnable preference-tuning recipe** on a free Google Colab T4. The chapter frames preference tuning as **stage 2** of the two-stage post-training pipeline, applied on top of a model that has already been SFT'd:

> *"With preference tuning we want to align an instruct-tuned LLM to be more 'aligned' with our preferences."* — Ch 12

### The worked DPO recipe (Ch 12)

- **Base model**: SFT-trained TinyLlama (the result of the chapter's earlier QLoRA-SFT step), reloaded in 16-bit for further DPO training.
- **Trainer**: [[DPOTrainer|`trl.DPOTrainer`]] + [[QLoRA]] (same `LoraConfig` as the SFT stage).
- **Dataset**: `argilla/distilabel-intel-orca-dpo-pairs` — filtered to ~6,000 high-quality triples (`status != "tie"`, `chosen_score >= 8`, `not in_gsm8k_train`).
- **Hyperparameters**: `beta=0.1`, `learning_rate=1e-5` (10× lower than SFT's `2e-4`), cosine schedule, `warmup_ratio=0.1`, `max_steps=200` (illustration).
- **Iterative merge**: merge SFT adapter into base → merge DPO adapter into SFT-merged model.

### Why DPO over PPO (Ch 12's choice)

> *"Compared to PPO, the authors found DPO to be more stable during training and more accurate. Due to its stability, we will be using it as our primary model for preference tuning our previously instruction-tuned model."* — Ch 12

Ch 12 walks both the [[RewardModel|reward-model]] + [[PPO]] baseline (for context) and the [[DPO]] alternative (for the actual recipe), positioning DPO as the **default preference-tuning method** the application engineer reaches for. The chapter forward-references [[ORPO]] (Hong, Lee & Thorne 2024) as the further collapse of SFT + DPO into a single training pass.

### Multi-objective reward models

Ch 12 surfaces **Llama 2's two-reward-model design** — separate helpfulness and safety reward models combined at the RL step — as evidence that preference tuning is inherently **multi-objective**, not a single scalar.
