---
title: "Reward Model"
type: concept
tags: [rlhf, post-training, alignment, evaluation]
sources: [ai-engineering-ch02-foundation-models, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# Reward Model

A model trained on [[ComparisonData|comparison data]] to **score (prompt, response) pairs** for use in [[rlhf|RLHF]]. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]:

> "Given a pair of (prompt, response), the reward model outputs a score for how good the response is."

The reward model is the **proxy for human preference** that lets RLHF optimize the foundation model without needing humans in the gradient loop.

## Training objective

From Ch 2's formula (rewritten):

$$\mathcal{L} = -\mathbb{E}_{(x,\,y_w,\,y_l)} \log \sigma\big(r_\theta(x, y_w) - r_\theta(x, y_l)\big)$$

Where the reward model $r_\theta$ scores winning response $y_w$ above losing response $y_l$. Training maximizes this score gap across the [[ComparisonData|comparison dataset]].

## What to initialize the reward model from

Three options per Ch 2:
1. **From scratch** — possible but typically inferior.
2. **Finetune on top of the pre-trained model** — common.
3. **Finetune on top of the SFT model or the strongest available foundation model** — **best empirical results**.

## "Does the RM need to be as strong as the model it scores?"

Some people argue yes — the RM has to be at least as powerful as the FM to judge the FM's outputs. Ch 2 disagrees:

> "As we'll see in the Chapter 3 on evaluation, a weak model can judge a stronger model, as judging is believed to be easier than generation."

## Use beyond RL

The reward model is useful even without the RL step:

- **[[StitchFix|Stitch Fix]]** and **[[Grab|Grab]]** generate multiple outputs and use only the RM to pick the best — skipping the PPO step entirely.
- **[[Nextdoor|Nextdoor]]** found in 2023 that *using a reward model was the key factor in improving their application's performance*.
- **OpenAI's math verifier** (Cobbe et al. 2021) is essentially an RM applied to math problems; it boosts performance equivalent to a **30× model-size increase**.

## How it powers RLHF's RL step

After the RM is trained, the SFT model is further trained via [[PPO|Proximal Policy Optimization]] to maximize the RM's scores. Prompts are drawn from a distribution of user prompts; the model generates responses; the RM scores them; PPO updates the model to push toward higher-scoring responses (with a KL penalty against the SFT model to prevent reward hacking).

## Connections
- [[ComparisonData]] — the training input.
- [[rlhf]] — the parent algorithm.
- [[PreferenceFinetuning]] — the broader stage.
- [[PPO]] — the RL algorithm that consumes RM scores.
- [[Verifier]] — closely related concept (specifically for tasks with verifiable correctness, e.g., math).
- [[bestofn]] — the "skip RL" pattern that uses only the RM.
- [[LLMAsAJudge]] — the LLM-as-judge pattern is a related (often RM-free) evaluation approach.
- [[ai-engineering-ch02-foundation-models]] — primary source.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* walks the reward model as the **scalable replacement for human scoring** in [[PreferenceFinetuning|preference tuning]] — *"manually scoring is not feasible at scale, so we typically train another model to do this evaluation for us. This is called a reward model."*

### Architecture (Ch 12)

> *"To create a reward model we take a copy of the instruction-tuned model and slightly change it so that instead of generating text, it now outputs a single score."* — Ch 12

Ch 12 narrows Huyen Ch 2's three initialization options to **the SFT-initialization path specifically**: *"replace its language modeling head with a quality classification head"*. Output = scalar score for `(prompt, generation)`.

### Training-data shape (Ch 12)

`prompt + chosen + rejected` triples. Ch 12 makes the **non-binary** point explicit: *"It's not always a good versus bad generation; it can be that the two generations are both good, but one is better than the other."* Training objective: ensure `score(chosen) > score(rejected)`.

### Three stages of preference tuning (Ch 12)

1. Collect preference data ([[PreferenceData]] / [[ComparisonData]]).
2. Train the reward model.
3. Use the reward model to fine-tune the LLM (via [[PPO]]).

### Multi-objective reward models (Ch 12)

Ch 12 surfaces **Llama 2's two-reward-model design** — one for **helpfulness**, one for **safety** — combined at the RL step. The first wiki record of multi-objective preference-tuning as a deliberate Llama 2 architectural choice.

### Why DPO bypasses this (Ch 12)

Ch 12's worked recipe uses [[DPO]] instead of PPO precisely **to avoid training a separate reward model**. *"A disadvantage of PPO is that it is a complex method that needs to train at least two models, the reward model and the LLM, which can be more costly than perhaps necessary."* DPO eliminates the reward model entirely — the trainable model is compared against a frozen **reference policy** rather than a learned reward signal.
