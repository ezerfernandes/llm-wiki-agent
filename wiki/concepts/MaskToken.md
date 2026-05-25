---
title: "`[MASK]` Token"
type: concept
tags: [nlp, bert, tokenization, special-token, pretraining]
sources: [hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# `[MASK]` Token

The **mask** [[SpecialToken|special token]] used during [[maskedlanguagemodel|masked-language-model]] pretraining. Replaces a fraction (typically 15%) of input tokens during training, and the model is trained to predict the original token at each masked position from its surrounding context.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

> "A masking token used to hide tokens during the training process." — Ch 2 (in the BERT special-tokens enumeration)

## Mechanics in [[bert|BERT]]

The original BERT masking scheme (Devlin et al. 2018):
- Pick 15% of tokens uniformly at random.
- Of those: 80% are replaced with `[MASK]`, 10% with a random token, 10% left unchanged.
- The model predicts the original token at every selected position.

The 80/10/10 split mitigates the **train-test distribution gap**: at inference time no `[MASK]` tokens appear, so always masking would bias the model to be unprepared for unmasked input.

## Connections

- [[SpecialToken]] — parent category.
- [[maskedlanguagemodel]] / MLM — the pretraining objective `[MASK]` enables.
- [[bert]] — the canonical model that uses `[MASK]`.
- [[Tokenizer]] / [[Tokenization]] — parent layer.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — source page.
