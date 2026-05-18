---
title: "SQuAD (Stanford Question Answering Dataset)"
type: concept
tags: [dataset, nlp, qa, benchmark]
sources: [d2l-nlp-applications]
last_updated: 2026-05-16
---

# SQuAD

**Stanford Question Answering Dataset v1.1** (Rajpurkar, Zhang, Lopyrev & Liang, EMNLP 2016) — the canonical extractive [[QuestionAnswering|question-answering]] benchmark. Each example: a reading passage, a question, and the **text span** within the passage that constitutes the answer.

## Example (per [[d2l-nlp-applications]] §`finetuning-bert`)

> Passage: "Some experts report that a mask's efficacy is inconclusive. However, mask makers insist that their products, such as N95 respirator masks, can guard against the virus."
> Question: "Who say that N95 respirator masks can guard against the virus?"
> Answer span: "mask makers"

## Fine-tuning [[BERT]]

See [[QuestionAnswering]] / [[FineTuningBert]] — pack `[CLS] Q [SEP] P [SEP]`, predict start / end positions via two independent linear heads, output the span $\arg\max_{i \le j} (s_i + e_j)$.

## Connections

- [[QuestionAnswering]] / [[BERT]] / [[FineTuningBert]].
- [[StanfordUniversity]] — origin (Rajpurkar et al.).
- [[d2l-nlp-applications]] §`finetuning-bert`.
