---
title: "SNLI (Stanford Natural Language Inference Corpus)"
type: concept
tags: [dataset, nlp, nli, benchmark]
sources: [d2l-nlp-applications]
last_updated: 2026-05-16
---

# SNLI

**Stanford Natural Language Inference corpus** (Bowman, Angeli, Potts & Manning, EMNLP 2015) — the canonical large-scale [[NaturalLanguageInference|NLI]] benchmark. Per [[d2l-nlp-applications]] §`natural-language-inference-and-dataset`: "a collection of over 500000 labeled English sentence pairs."

## Structure

- ~550 000 training pairs + ~10 000 testing pairs (D2L counts).
- Each example: `(premise, hypothesis, label)` where label ∈ {entailment, contradiction, neutral}.
- Labels are **balanced** across the three classes in both splits.
- Premise sentences crowdsourced from Flickr30k captions; hypotheses written by Amazon Mechanical Turk workers given a label prompt.

## Use in [[d2l-nlp-applications]]

- §`natural-language-inference-attention` trains a [[DecomposableAttention|decomposable attention model]] (Parikh et al. 2016) on SNLI with GloVe-100d input and batch size 256 / sequence length 50.
- §`natural-language-inference-bert` fine-tunes a small pretrained [[BERT]] on SNLI with the `SNLIBERTDataset` wrapper that constructs `[CLS] premise [SEP] hypothesis [SEP]` inputs with segment ids.

## Connections

- [[NaturalLanguageInference]] — the task it benchmarks.
- [[StanfordUniversity]] — origin (Bowman et al.).
- [[SamuelBowman]] — first author.
- [[DecomposableAttention]] / [[BERT]] / [[FineTuningBert]] — models trained on it.
- [[d2l-nlp-applications]] — canonical D2L source.
