---
title: "Pretraining"
type: concept
tags: [concept, transfer-learning, foundational]
sources: [1810.04805-bert, 1910.10683-t5, 2001.08361-scaling-laws, ai-engineering-ch01-intro, ai-engineering-ch02-foundation-models, hands-on-llm-ch01-introduction-to-llms]
last_updated: 2026-05-23
---

# Pretraining

Training a model on a data-rich auxiliary task before fine-tuning it on a downstream task with limited labeled data. In modern NLP, pre-training is unsupervised (or self-supervised) — the model learns from unlabeled text via a denoising or next-token objective — and the resulting weights become a general-purpose initialization for downstream tasks.

## Canonical recipes

- **[[bert]] (2018).** Bidirectional Transformer **encoder** + [[maskedlanguagemodel]] objective + downstream task-specific head. Established the pretrain-then-finetune paradigm for NLU.
- **GPT-style (2018+).** Causal decoder + next-token prediction + (later) in-context prompting.
- **[[t5]] (2020).** Encoder-decoder Transformer + [[spancorruption]] denoising on [[c4]] + unified [[texttotextframework]] for fine-tuning. The [[1910.10683-t5]] ablation supplies the systematic empirical case for this recipe.

## How pretraining scales

[[2001.08361-scaling-laws]] (Kaplan, McCandlish et al., 2020) supplies the **quantitative law** governing autoregressive pretraining loss. Across more than seven orders of magnitude in compute, the cross-entropy loss follows clean power laws in non-embedding parameter count $N$, dataset size $D$, and compute $C$ (see [[ScalingLaws]]). Two practical consequences for any pretraining run:

- **[[ComputeEfficientTraining]] regime.** For a fixed pretraining compute budget, the optimal allocation is $N \propto C^{0.73}$, $B \propto C^{0.24}$, $S \propto C^{0.03}$. Most additional compute should go into a **larger model**; serial training steps grow almost not at all. Compute-efficient pretraining **stops short of convergence** — the prevailing pre-2020 practice of training small models to convergence is provably suboptimal.
- **Architecture is second-order.** Depth/width ratio, attention-head count, and feed-forward ratio change the loss by only a few percent at fixed $N$, $D$, $C$. Pretraining design decisions should mostly be about scale, not shape.

## What the T5 ablation established

[[1910.10683-t5]] is the definitive controlled empirical study of pre-training choices as of 2020:
- **Architecture:** encoder-decoder > shared-param encoder-decoder > prefix-LM > decoder-only LM at matched compute.
- **Objective:** denoising > causal LM, robustly; within denoising, all variants perform similarly — pick the cheapest.
- **Data:** filtered web text (C4, 745 GB) > unfiltered web text, but in-domain narrower corpora beat C4 on matched downstream tasks.
- **Data size:** repeating a corpus 64× during pre-training is roughly harmless; 1,024–4,096× causes memorization and degrades fine-tuning.
- **Fine-tuning:** full > [[adapterlayers]] > [[gradualunfreezing]] on most tasks.
- **Multi-task pre-training + per-task fine-tuning** matches plain unsupervised pre-training.
- **Scale dominates.** Doubling compute via larger model and/or more steps reliably beats careful method engineering.

## See also

- [[bert]], [[t5]] — the two canonical pre-trained models in this wiki.
- [[c4]] — the canonical large diverse pre-training corpus.
- [[spancorruption]], [[maskedlanguagemodel]] — denoising objectives.
- [[texttotextframework]] — unified post-pretraining task interface.
- [[transformer]] — the architecture being pre-trained.
- [[ScalingLaws]], [[ComputeEfficientTraining]], [[PowerLaw]] — the quantitative framework for budgeting a pretraining run.

## From [[ai-engineering-ch01-intro|AI Engineering Ch 1]]

[[ChipHuyen|Chip Huyen]] in *AI Engineering* Ch 1 adds practitioner-flavored context to the pretraining definition above:

> *"Pre-training refers to training a model from scratch — the model weights are randomly initialized. For LLMs, pre-training often involves training a model for text completion. Out of all training steps, pre-training is often the most resource-intensive by a long shot. For the InstructGPT model, pre-training takes up to 98% of the overall compute and data resources."* — Ch 1

Key practitioner notes from Ch 1:

- **Pre-training is an art only a few practice.** Those with expertise *"are heavily sought after"* — and *"offered incredible compensation packages."* (Footnote 24.)
- **Mistakes are expensive**: *"A small mistake during pre-training can incur a significant financial loss and set back the project significantly."*
- **Pre-training vs. [[posttraining|post-training]] vs. [[FineTuning|finetuning]]** make up a spectrum — same operation (continue training a previously-trained model), distinguished primarily by **who** does it (model developers vs. application developers) and **for what goal**.

For the [[AIEngineering|AI engineering]] reader, the practical implication is that **most teams will never pre-train**. The high-leverage AI-engineering activities live downstream of pre-training — at [[posttraining|post-training]] / [[FineTuning|finetuning]] / [[PromptEngineering|prompt engineering]] / [[rag|RAG]].

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

Ch 2 adds **the budgeting/scaling and bottleneck framing** for pre-training:

### Three numbers that signal a model's scale (Ch 2 summary)

1. **Number of parameters** — proxy for *learning capacity*.
2. **Number of training tokens** — proxy for *how much the model learned*. Llama family: 1.4T (Llama 1) → 2T (Llama 2) → 15T (Llama 3).
3. **Number of [[FLOPs|FLOPs]]** — proxy for *training cost*. GPT-3-175B used 3.14 × 10²³ FLOPs ≈ $4.14M and 236 days on 256 H100s at 70% utilization at $2/h.

### The [[ChinchillaScalingLaw|Chinchilla]] recipe

Ch 2 makes the concrete prescription: **≈20 training tokens per parameter**. Model size and training-token count scale equally. A 3B-param model needs ≈60B training tokens to be compute-optimal.

### Two scaling bottlenecks ([[ScalingBottlenecks]])

1. **Training data.** Villalobos et al. project growth outrunning new-data generation. 45% of [[c4|C4]] became restricted between 2023–2024 (Longpre et al.). The web is filling with AI-generated content — recursive training may degrade models (Shumailov et al. 2023, though Ch 8 nuances this).
2. **Electricity.** Data centers go from 1–2% global electricity to 4–20% by 2030 (Patel, Nishball, Ontiveros 2024). At most ≈50× compute growth before a power shortage.

### Data-quality-over-quantity precedent

Gunasekar et al. (2023): a 1.3B-param model on **7B tokens of high-quality coding data** outperformed much larger models on coding benchmarks. *"Quantity, quality, and diversity are the three golden goals for training data."*

### Inference-aware pre-training

[[meta|Meta]] deliberately trained Llama models *smaller* than Chinchilla-optimal for inference economics. Sardana et al. (2023) formalized this as inference-aware scaling.

## From [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]]

Ch 1 frames pretraining as the **first half of the LLM two-step training paradigm** (the second being [[FineTuning|fine-tuning]]):

> "The first step, called pretraining, takes the majority of computation and training time. An LLM is trained on a vast corpus of internet text allowing the model to learn grammar, context, and language patterns. This broad training phase is not yet directed toward specific tasks or applications beyond predicting the next word. The resulting model is often referred to as a foundation model or base model. These models generally do not follow instructions." — Ch 1

The chapter's training-cost anchor: *"Llama 2 has been trained on a dataset containing 2 trillion tokens. Imagine the compute necessary to create that model!"* And from the GPU section: *"To create the Llama 2 family of models, for example, Meta used A100-80 GB GPUs ... the total costs of creating these models would exceed $5,000,000!"*

The takeaway for AI engineers and Language AI practitioners: pretraining is structurally out of reach for most teams; fine-tuning + prompt engineering + retrieval are the high-leverage entry points.
