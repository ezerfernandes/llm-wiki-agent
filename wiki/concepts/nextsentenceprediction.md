---
title: "Next Sentence Prediction"
type: concept
tags: [concept, pretraining, objective]
sources: [1810.04805-bert, d2l-nlp-pretraining]
last_updated: 2026-05-16
---

# Next Sentence Prediction

Auxiliary pre-training objective introduced by [[BERT]] in [[1810.04805-bert]]. For each training example, sentence B is the actual sentence following A in the source corpus 50% of the time (label `IsNext`) and a random sentence from the corpus the other 50% (label `NotNext`). The `[CLS]` token's final hidden state is fed to a binary classifier.

Purpose: pre-train *inter-sentence* relationship signal not captured by token-level language modelling. Targets downstream tasks such as Natural Language Inference, paraphrasing, and Question Answering, which all hinge on the relationship between a pair of sentences.

BERT's NSP classifier achieves 97–98% accuracy after pre-training. Ablations show removing NSP costs ≥0.5–1.5 points on QNLI / MNLI / SQuAD v1.1.

Later work (RoBERTa, ALBERT) argued NSP is too easy and redundant with MLM once corpora and training are scaled, and either drops it (RoBERTa) or replaces it with a harder *Sentence Order Prediction* task (ALBERT). The original BERT paper remains the canonical reference for the objective itself.
