---
title: "Self-Supervised Learning"
type: concept
tags: [paradigm, pretraining, deep-learning, data-selection, mlsysbook]
sources: [d2l-introduction, 1810.04805-bert, 2601.21343-self-improving-pretraining, mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Self-Supervised Learning

Training paradigm that **leverages structure inside unlabeled data to fabricate supervision** — no human labels are needed. The model is set up to predict one part of the input from another; the implicit "labels" come for free. The learned representations are then **fine-tuned** on a downstream supervised task ([[FineTuning|fine-tuning]], [[TransferLearning|transfer learning]]).

[[d2l-introduction]] catalogs four canonical instances:

1. **Masked text** — predict randomly masked words from surrounding context (the [[bert|BERT]] / [[maskedlanguagemodel|MLM]] recipe, Devlin et al. 2018; the entire LLM pretraining era rests on this).
2. **Relative-position prediction** — given two cropped patches of one image, predict their spatial offset (Doersch / Gupta / Efros 2015).
3. **Occlusion prediction** — predict an occluded region of an image from the rest.
4. **Contrastive perturbation** — predict whether two examples are augmented views of the same underlying image (SimCLR / MoCo lineage).

## Why it matters

Self-supervised learning is the bridge between [[UnsupervisedLearning|unsupervised learning]] (no labels at all) and [[SupervisedLearning|supervised learning]] (labels required). It's how modern pretrained models reach scale: there are **far more** unlabeled tokens / pixels / video frames than there are labeled examples, and pretraining on the unlabeled corpus produces representations that downstream supervised tasks can specialize cheaply.

Per [[2601.21343-self-improving-pretraining]], self-supervised objectives can themselves be refined post-hoc using a post-trained model's signal — collapsing the pretrain / post-train boundary.

## Connections

- [[bert]], [[maskedlanguagemodel]] — the canonical NLP instance.
- [[pretraining]] — the training-stage label this paradigm operationalizes.
- [[FineTuning]], [[TransferLearning]] — what happens *after* self-supervised pretraining.
- [[UnsupervisedLearning]] — sister paradigm that the chapter explicitly frames as the parent.
- [[SupervisedLearning]] — the downstream consumer.
- [[DataSelection]] / [[DataWall]] — [[mlsysbook-ch09-data-selection|Ch 9]] frames SSL as the field's most effective response to the Data Wall: it *breaks the label asymptote* by extracting supervision from data structure (pretext tasks), and via [[CostAmortization|cost amortization]] makes the [[FoundationModel|foundation-model]] paradigm economical (label cost ↓100×, marginal compute ↓20×).
- [[d2l-introduction]] / [[mlsysbook-ch09-data-selection]] — sources.
