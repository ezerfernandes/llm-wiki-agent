---
title: "Zero-Shot Learning"
type: concept
tags: [evaluation, llm, prompt-engineering]
sources: [madewithml-transformers, ai-engineering-ch05-prompt-engineering, hands-on-llm-ch04-text-classification, hands-on-llm-ch06-prompt-engineering]
last_updated: 2026-05-23
---

# Zero-Shot Learning

Performing a task without any labeled training examples, relying on prior knowledge encoded in a pretrained model. A hallmark capability of large [[Transformer]] LLMs, contrasting with traditional [[TransferLearning]] fine-tuning.

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

[[ChipHuyen|Huyen]] uses the term within the [[InContextLearning|in-context learning]] taxonomy: **zero-shot = no examples in the prompt**. Pair with [[FewShotLearning|few-shot]] (small number) and many-shot (dozens to hundreds).

**Microsoft 2023 data point**: zero-shot suffices for many GPT-4 use cases — *"few-shot learning led to only limited improvement compared to zero-shot learning on GPT-4."* The gap between zero-shot and few-shot has narrowed as models have improved at instruction-following.

The trade-off is direct: zero-shot prompts are cheaper (fewer tokens) and simpler to write; few-shot prompts add cost and complexity for diminishing accuracy returns on frontier models.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 specializes zero-shot to classification — see [[ZeroShotClassification]]. The chapter's framing is the **classification-task-specific sense**: no labeled training data, only label *names* / *descriptions*. The chapter then demonstrates **three implementations**:

1. **Embedding-based zero-shot** via [[LabelEmbedding|label embeddings]] + [[CosineSimilarity|cosine similarity]] (Ch 4's chosen demo; F1 = 0.78 on [[RottenTomatoes|Rotten Tomatoes]]).
2. **[[NaturalLanguageInference|NLI]]-based zero-shot** — the prior dominant approach, mentioned but not demonstrated.
3. **Prompt-based zero-shot** with a [[GenerativeModel|generative LM]] — covered as [[GenerativeClassification]].

This is consistent with the prompt-engineering-sense definition above (no labeled examples) but operationalized for classification specifically. The two senses are not in conflict — both share the *"no labeled training data"* core.

## From [[hands-on-llm-ch06-prompt-engineering|Hands-On LLMs Ch 6]]

Ch 6 codifies the [[InContextLearning|in-context learning]] spectrum explicitly:

> *"Zero-shot prompting does not leverage examples, one-shot prompts use a single example, and few-shot prompts use two or more examples."* — Ch 6

Ch 6 also names a distinct sub-form: **[[ZeroShotCoT|zero-shot chain-of-thought]]** — appending *"Let's think step-by-step"* to elicit reasoning without examples (Kojima et al. 2022). This is **zero-shot in the example-count sense** (no examples) but **not zero-shot in the reasoning-template sense** (the trigger phrase activates step-by-step pattern). The distinction matters when comparing techniques in the literature.
