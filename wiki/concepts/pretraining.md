---
title: "Pretraining"
type: concept
tags: [concept, transfer-learning, foundational]
sources: [1810.04805-bert, 1910.10683-t5, 2001.08361-scaling-laws]
last_updated: 2026-05-10
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
