---
title: "CoLA (Corpus of Linguistic Acceptability)"
type: concept
tags: [dataset, nlp, grammaticality, benchmark]
sources: [d2l-nlp-applications]
last_updated: 2026-05-16
---

# CoLA

**Corpus of Linguistic Acceptability** (Warstadt, Singh & Bowman 2019) — a single-text classification benchmark for grammatical acceptability. Each example is a sentence labeled as *acceptable* or *not acceptable*.

Per [[d2l-nlp-applications]] §`finetuning-bert`: *"I should study."* is acceptable but *"I should studying."* is not.

## Fine-tuning [[BERT]]

A canonical instance of single-text classification per [[FineTuningBert]] — `[CLS] sentence [SEP]` → MLP head on the [[ClsToken|`[CLS]`]] hidden state → binary output.

## Connections

- [[SentimentAnalysis]] — the other canonical single-text classification task in [[d2l-nlp-applications]].
- [[BERT]] / [[FineTuningBert]] / [[ClsToken]].
- [[SamuelBowman]] — co-author.
- [[d2l-nlp-applications]] §`finetuning-bert`.
