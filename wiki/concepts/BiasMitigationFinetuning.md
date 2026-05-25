---
title: "Bias Mitigation Finetuning"
type: concept
tags: [finetuning, alignment, fairness, safety]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Bias Mitigation Finetuning

Using **carefully curated finetuning data** to counteract biases the model inherited from pre-training. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "One especially interesting use case of finetuning is bias mitigation. The idea is that if the base model perpetuates certain biases from its training data, exposing it to carefully curated data during finetuning can counteract these biases (Wang and Russakovsky, 2023). For example, if a model consistently assigns CEOs male-sounding names, finetuning it on a dataset with many female CEOs can mitigate this bias."

## Empirical evidence Ch 7 cites

[[Garimella2022Bias|Garimella et al. (2022)]] showed:
- Finetuning BERT-like models on **text authored by women** can reduce gender biases.
- Finetuning on **texts by African authors** can reduce racial biases.

The mechanism is straightforward: re-balance the implicit demographic distribution of the training corpus by finetuning on a counter-skewed corpus.

## Why this is interesting in Ch 7's framing

Bias mitigation is a slight **counterexample to the chapter's "finetuning is for form, RAG is for facts" rule**. It uses finetuning to change the model's *content distribution* — what kinds of facts/associations it generates — not just its format/style. So the rule is approximate, not absolute.

## Limitations

- **Hard to verify**: did the finetune *actually* reduce bias, or did it just shift the bias in another direction?
- **Risk of new biases**: heavily over-representing a counter-population can create the inverse bias.
- **Distribution shift**: the finetune may move the model out of the input distribution it generalizes well over, causing quality drops elsewhere.

## Connections

- [[FineTuning]] — parent operation.
- [[AlignmentRule]] / [[AlignmentHallucination]] — related alignment concepts.
- [[bert|BERT]] — Garimella et al.'s subject model.
- [[Garimella2022Bias]] / [[WangRussakovsky2023BiasMitigation]] — citations.
- [[ai-engineering-ch07-finetuning]] — primary source.
