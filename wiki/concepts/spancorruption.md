---
title: "Span Corruption"
type: concept
tags: [concept, pretraining, objective, denoising]
sources: [1910.10683-t5]
last_updated: 2026-05-10
---

# Span Corruption

A denoising pre-training objective in which contiguous spans of input tokens are replaced by unique sentinel tokens, and the model is trained to predict the concatenation of corrupted spans (each prefixed by the sentinel that replaced it) — rather than the full uncorrupted sequence. Introduced as the pre-training objective for [[t5]] in [[1910.10683-t5]], inspired by SpanBERT (Joshi et al., 2019) and the [[maskedlanguagemodel]] objective from [[1810.04805-bert]].

## Concrete example

Original input: `Thank you for inviting me to your party last week .`
Corrupted input fed to encoder: `Thank you <X> me to your party <Y> week .`
Target produced by decoder: `<X> for inviting <Y> last <Z>`

`<X>`, `<Y>`, `<Z>` are sentinel tokens unique to this example, added to the model's vocabulary.

## Why span corruption rather than i.i.d. masking

- **Shorter targets.** Replacing each consecutive corrupted span with a single sentinel produces target sequences ~3× shorter than reconstructing the entire input (as MASS does), and ~3× shorter than predicting all individual masked tokens. This reduces decoder compute.
- **Marginally better quality.** T5's ablation found mean span length 3 slightly but significantly outperformed i.i.d. masking on most non-translation benchmarks; span lengths 2/5/10 were close.
- **Empirically, all denoising variants behave similarly.** T5's most important finding about the objective is that the *choice of denoising variant has limited impact* — among BERT-style mask-and-reconstruct, MASS-style, replace-corrupted-spans, drop-corrupted-tokens, and span-corruption at corruption rates 10/15/25%, all produced near-identical downstream performance. Span corruption with length 3 won mainly on computational efficiency.

## Hyperparameters

- **Corruption rate:** 15% (10–25% all behave similarly; 50% degrades).
- **Mean span length:** 3 (length 2/5 close; 10 underperforms on some tasks).
- **Spans are sampled randomly to satisfy the corruption-rate and span-count constraints.**
- **Sentinel tokens** are added to the vocabulary and never correspond to a wordpiece.

## See also

- [[1910.10683-t5]] — source paper.
- [[t5]] — model trained with this objective.
- [[maskedlanguagemodel]] — the BERT-style ancestor.
- [[bert]] — predecessor whose MLM this generalizes.
- [[pretraining]] — broader context.
