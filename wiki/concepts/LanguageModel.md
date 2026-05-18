---
title: "Language Model"
type: concept
tags: [nlp, sequence-models, language-models]
sources: [d2l-recurrent-neural-networks]
last_updated: 2026-05-16
---

# Language Model

A statistical model that estimates the **joint probability** of a token sequence

$$P(x_1, x_2, \ldots, x_T) = \prod_{t=1}^T P(x_t \mid x_{t-1}, \ldots, x_1).$$

Language models are the default sequence-modeling formulation in NLP and the foundation underneath modern LLMs ([[d2l-recurrent-neural-networks]] §language-model).

## What an LM lets you do

- **Score sentences** — compute likelihood to disambiguate "to recognize speech" vs "to wreck a nice beach" in a speech recognizer.
- **Generate text** — draw $x_t \sim P(x_t \mid x_{<t})$ token by token. Quality varies from coherent to nonsensical depending on how well the model fits the distribution.
- **Resolve ambiguity** in machine translation / summarization — "dog bites man" is much more frequent than "man bites dog"; "I want to eat grandma" vs "I want to eat, grandma".

## Approaches

- **[[NGram|$n$-gram]] counting** with [[LaplaceSmoothing]] for unseen $n$-grams. Breaks down because (i) most $n$-grams are rare ([[ZipfsLaw]]), (ii) storage is huge, (iii) ignores word meaning ("cat" ≠ "feline").
- **Neural LMs** — Bengio, Ducharme, Vincent et al. (2003) first proposed using a neural network for LM; [[RNN]] LMs are D2L's worked example. Modern incarnations: [[Transformer|Transformer-based LMs]] — GPT, BERT, LLaMA, Gemini.

## Evaluation

- **[[Perplexity]]** = $\exp(\frac{1}{n}\sum_t -\log P(x_t \mid x_{<t}))$ — the NLP-standard length-comparable LM metric.

## Scale

Per [[d2l-recurrent-neural-networks]]: "Language models can be scaled up with increased data size, model size, and amount in training compute. Large language models can perform desired tasks by predicting output text given input text instructions. ... at the present moment large language models form the basis of state-of-the-art systems across diverse tasks." See [[2001.08361-scaling-laws|Kaplan et al.]] for the empirical scaling story.

## Connections

- [[d2l-recurrent-neural-networks]] — chapter-source.
- [[NGram]] / [[MarkovModel]] / [[LaplaceSmoothing]] — pre-neural baselines.
- [[AutoregressiveModel]] — language modeling is autoregressive prediction over discrete tokens.
- [[Perplexity]] — evaluation metric.
- [[RNN]] / [[Transformer]] — neural LM architectures.
- [[2001.08361-scaling-laws]] — LM scaling laws.
- [[maskedlanguagemodel]] — masked-LM variant ([[1810.04805-bert|BERT]]).
- [[1706.03762-attention-is-all-you-need]] — Transformer LM.
