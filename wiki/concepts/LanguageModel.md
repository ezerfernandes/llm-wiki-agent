---
title: "Language Model"
type: concept
tags: [nlp, sequence-models, language-models]
sources: [d2l-recurrent-neural-networks, ai-engineering-ch01-intro, ai-engineering-ch02-foundation-models, hands-on-llm-ch01-introduction-to-llms]
last_updated: 2026-05-23
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

## From [[ai-engineering-ch01-intro|AI Engineering Ch 1]]

[[ChipHuyen|Chip Huyen]]'s *AI Engineering* Ch 1 supplies the **historical narrative** complementing this page's technical definition:

- **Statistical-language-modeling is centuries old**: Sherlock Holmes's "Dancing Men" cipher (1905) used letter-frequency statistics; [[ClaudeShannon|Claude Shannon's]] 1951 paper *"Prediction and Entropy of Printed English"* (introducing entropy) is still foundational. Both predate any computational LM by half a century.
- **Token, not word, as the basic unit.** Ch 1 supplies the practical reason language models use tokens rather than words or characters: tokens (a) carry meaningful sub-components ("cook"+"ing"), (b) keep vocabulary small enough to be efficient, (c) handle unknown words gracefully ("chatgpting" → "chatgpt"+"ing"). GPT-4 vocab = 100,256; Mixtral 8x7B vocab = 32,000; 100 tokens ≈ 75 words.
- **Two LM types**: [[maskedlanguagemodel|masked]] (bidirectional, BERT-style, for non-generative tasks like sentiment analysis and code debugging) vs. [[AutoregressiveLanguageModel|autoregressive]] (left-to-right, GPT-style, for text generation). Modern usage of "language model" almost always means autoregressive.
- **The completion-machine framing**: an LM is a completion machine — given a prompt, it tries to complete that text. Many tasks (translation, summarization, classification, coding, math) can be **framed as completion**. This is what allowed a single LM to displace many task-specific models.
- **Path to [[LargeLanguageModel|LLMs]]**: scale enabled by [[SelfSupervision|self-supervision]], which extracts labels from the input itself, freeing LMs from the data-labeling bottleneck. Once modalities expand beyond text, the umbrella term becomes [[FoundationModel|foundation model]].
