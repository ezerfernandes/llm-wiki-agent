---
title: "Intrinsic Dimension"
type: concept
tags: [theory, deep-learning, lora, peft]
sources: [ai-engineering-ch07-finetuning, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# Intrinsic Dimension

The **minimum number of parameters required to reach a given training loss** on a given task, as measured by training in a random low-dimensional subspace of the full parameter space. Originally introduced by [[Li2018IntrinsicDimension|Li et al. (2018)]] — *"Measuring the Intrinsic Dimension of Objective Landscapes"* — and made central to the [[PEFT|PEFT]] theory by [[Aghajanyan2020IntrinsicDimension|Aghajanyan et al. (2020)]] — *"Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning."*

## The startling empirical finding

Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "Many papers have argued that while LLMs have many parameters, they have very low intrinsic dimensions. They showed that pre-training implicitly minimizes the model's intrinsic dimension. **Surprisingly, larger models tend to have lower intrinsic dimensions after pre-training.** This suggests that pre-training acts as a compression framework for downstream tasks."

In other words: **bigger, better-pre-trained models need *fewer* trainable parameters to finetune**. This is the inverse of what intuition suggests — you'd expect a 175B-parameter model to require more modifications than a 1B-parameter model. The empirical reality is the opposite.

## Why this is the theoretical basis for [[PEFT]]

If a model's effective parameter dimension after pre-training is, say, ~10⁵ (regardless of whether the model has 10⁹ or 10¹¹ raw parameters), then **any PEFT method that gives you ~10⁵ trainable parameters should be sufficient to finetune the model to a good performance**. This is exactly what [[lora|LoRA]] shows empirically — 4.7M trainable params on GPT-3 175B match full FT on several tasks.

## The recursive question

> "If low-rank factorization works so well, why don't we use LoRA for pre-training as well? Instead of pre-training a large model and applying low-rank factorization only during finetuning, could we factorize a model from the start for pre-training?" — Ch 7

Attempts: [[ReLoRA]] (Lialin et al. 2023; works up to 1.3B); [[GaLore]] (Zhao et al. 2024; promising at 7B).

The conjectured answer: **full-rank pre-training is what compresses intrinsic dimension** in the first place. If you start with low-rank training, the model never achieves the low-intrinsic-dimension state that makes downstream low-rank adaptation work. You need to *earn* the low intrinsic dimension via high-rank pre-training.

## Connection to the bitter lesson

Intrinsic dimension provides a deep-learning-specific instance of compression: pre-training spends enormous compute to discover and compress task-relevant structure into a low-dimensional manifold; downstream tasks only need to navigate that manifold.

## Connections

- [[lora|LoRA]] — the canonical PEFT method whose effectiveness intrinsic dimension explains.
- [[PEFT]] — the family of techniques justified by low intrinsic dimension.
- [[FineTuning]] — the operation that works via intrinsic-dimension navigation.
- [[Pretraining]] — the process that compresses intrinsic dimension.
- [[Li2018IntrinsicDimension]] / [[Aghajanyan2020IntrinsicDimension]] — citations.
- [[ReLoRA]] / [[GaLore]] — attempts at low-rank pre-training.
- [[ai-engineering-ch07-finetuning]] — primary source.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* cites the **same Aghajanyan, Zettlemoyer & Gupta 2020 result** (arXiv:2012.13255) as Huyen Ch 7, naming it explicitly as the **theoretical justification for [[lora|LoRA]]**:

> *"Why does this approach work so well? It was demonstrated that language models have a very low intrinsic dimension. This means that we can find small ranks that approximate even the massive matrices of an LLM."* — Ch 12

The chapter's anchor numerical example: for GPT-3 175B's 12,288×12,288 attention matrices (150M params per block), rank-8 LoRA = two 12,288×2 matrices = **197K parameters per block** — a *small* approximation that works precisely because the model's effective behavioral surface is low-dimensional.
