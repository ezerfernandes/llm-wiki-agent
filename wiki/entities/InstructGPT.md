---
title: "InstructGPT"
type: entity
tags: [model, openai, sft, rlhf]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# InstructGPT

[[openai|OpenAI]]'s 2022 paper introducing the **[[SupervisedFinetuning|SFT]] + [[rlhf|RLHF]] post-training recipe** for aligning a base GPT-3 model to follow user instructions. The precursor to ChatGPT (which is essentially an InstructGPT successor with refinements). Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "OpenAI's InstructGPT paper (2022) suggested viewing finetuning as **unlocking the capabilities a model already has** but that are difficult for users to access via prompting alone."

## The framing Ch 7 carries forward

InstructGPT's framing of finetuning is the **definitional one Ch 7 adopts**: finetuning doesn't add new knowledge; it makes existing knowledge accessible. This view shapes the chapter's "finetuning is for form, RAG is for facts" rule.

The Llama 3.1 paper ([[Llama31Paper]], Dubey et al. 2024) extended this view explicitly: *"post-training should align the model to 'know what it knows' rather than add knowledge."*

## The pipeline

1. **Demonstration data collection** — labelers write target responses for instructions. (Per Ch 2's coverage: ≈90% had college degrees, 1/3 had master's, ~$10/pair × 13,000 pairs = $130k labor cost.)
2. **Supervised finetuning ([[SupervisedFinetuning|SFT]])** on demonstration data.
3. **Comparison data collection** — labelers rank model outputs.
4. **[[RewardModel|Reward model]] training** on comparison data.
5. **[[PPO|PPO]] [[rlhf|RLHF]]** to optimize the SFT model against the reward model.

## Why it matters in Ch 7

Beyond the framing quote, InstructGPT is the **prototype** for the SFT-pipeline Ch 2 covers and the **distinction-from-prompting** Ch 7 reinforces — Huyen often notes that what users call "finetuning" colloquially is actually prompting. InstructGPT is what finetuning *actually* looks like.

## Connections

- [[openai|OpenAI]] — the institution.
- [[SupervisedFinetuning]] / [[rlhf|RLHF]] / [[PreferenceFinetuning]] — the techniques InstructGPT pioneered as a combined recipe.
- [[FineTuning]] — the parent operation.
- [[ChatGPT]] — the successor product.
- [[ai-engineering-ch07-finetuning]] — wiki source.
