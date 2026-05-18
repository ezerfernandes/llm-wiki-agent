---
title: "Fine-Tuning BERT"
type: concept
tags: [training, nlp, bert, transfer-learning, fine-tuning]
sources: [d2l-nlp-applications]
last_updated: 2026-05-16
---

# Fine-Tuning BERT

The recipe — formalized in [[d2l-nlp-applications]] §`finetuning-bert` — for adapting a pretrained [[BERT]] encoder to downstream NLP applications **with minimal architecture changes**: an extra fully-connected head (or two), trained from scratch, while all BERT parameters are also updated end-to-end. The applied-NLP companion to the [[FineTuning|computer-vision fine-tuning recipe]] from [[d2l-computer-vision]].

## Four application templates

| Task type | Input | Head | Examples |
|---|---|---|---|
| **Single-text classification** | `[CLS] text [SEP]` | MLP on [[ClsToken|`[CLS]`]] hidden state | [[SentimentAnalysis|Sentiment]] ([[IMDb]]), grammaticality ([[CoLA]]) |
| **Text-pair classification** | `[CLS] A [SEP] B [SEP]` with segment ids | MLP on `[CLS]` | [[NaturalLanguageInference|NLI]] ([[SNLI]]) |
| **Text-pair regression** | `[CLS] A [SEP] B [SEP]` | Linear regressor on `[CLS]` + MSE loss | [[SemanticTextualSimilarity|STS-B]] |
| **Token-level tagging** | `[CLS] text [SEP]` | Same FC head applied per-token | Part-of-speech tagging, NER |
| **Question answering ([[SQuAD]] v1.1)** | `[CLS] Q [SEP] P [SEP]` | Two independent linear heads on each passage token → start-score $s_i$, end-score $e_i$; predict $\arg\max_{i \le j} s_i + e_j$ | Reading comprehension |

## Training protocol

- **Output-layer parameters** (`net.output`) — random init, **learn from scratch**.
- **Hidden-layer parameters** (`net.hidden` / encoder) — **fine-tune** end-to-end.
- **Stale parameters** — the `MaskLM` and `NextSentencePred` MLPs used only for pretraining loss are *not* updated; their gradients are explicitly allowed to be stale (`ignore_stale_grad=True`).
- **Learning rate**: $1{\times}10^{-4}$ in D2L's worked SNLI example, Adam optimizer, ~5 epochs.
- **Sequence packing for pairs**: `SNLIBERTDataset` joint-truncates to $|p| + |h| \le \text{max\_len} - 3$ (reserving slots for `<CLS>` + 2× `<SEP>`).

## Trade-off

> "BERT requires minimal architecture changes for a wide range of natural language processing applications. However, this benefit comes at the cost of fine-tuning a huge number of BERT parameters for the downstream applications. When space or time is limited, those crafted models based on MLPs, CNNs, RNNs, and attention are more feasible." — [[d2l-nlp-applications]]

For the SNLI worked example, D2L provides a "bert.small" variant (256 hidden / 512 FFN / 2 heads / 2 blocks) so the demo fits on educational hardware; "bert.base" is also available for production-quality results.

## Connections

- [[BERT]] / [[FineTuning]] — base concepts.
- [[ClsToken]] / [[MaskedLanguageModel]] / [[NextSentencePrediction]] / [[WordPiece]] — BERT machinery.
- [[NaturalLanguageInference]] / [[SentimentAnalysis]] / [[QuestionAnswering]] / [[SemanticTextualSimilarity]] — downstream tasks.
- [[SNLI]] / [[IMDb]] / [[SQuAD]] / [[CoLA]] — canonical datasets.
- [[d2l-nlp-applications]] §`finetuning-bert` / §`natural-language-inference-bert` — D2L's canonical worked examples.
