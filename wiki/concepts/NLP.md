---
title: "Natural Language Processing"
type: concept
tags: [application-domain]
sources: [d2l-preface, d2l-introduction, d2l-nlp-pretraining, d2l-nlp-applications]
last_updated: 2026-05-16
---

# Natural Language Processing

Application domain dealing with computational understanding and generation of human language. Per [[d2l-preface]], NLP is one of the fields most transformed by [[DeepLearning]]; [[Attention]] / [[transformer]] architectures have "displaced [[RNN|RNNs]] as the dominant architecture for most natural language processing tasks."

## Tasks surveyed in [[d2l-introduction]]

- **Question answering** (free-form text in, factoid answer out).
- **[[machinetranslation|Machine translation]]** — the canonical sequence-to-sequence task; the German verb-at-the-end example illustrates **unaligned** sequences.
- **Part-of-speech tagging** — aligned tagging; one tag per token.
- **Named-entity recognition** — span tagging.
- **Text classification / sentiment / tagging** — with multi-label and hierarchical variants.
- **Sequence-to-sequence learning** — the unifying framework.
- **Dialogue** — long-temporal-context modeling.
- **[[languagemodel|Language modeling]]** — the [[pretraining|pretraining]] objective behind every modern LLM; ChatGPT cited as the consumer-facing demo.

## D2L's downstream-task taxonomy (per [[d2l-nlp-applications]])

[[d2l-nlp-applications]] organizes NLP applications on two axes:

- **Sequence-level vs. token-level**: sequence-level outputs one label per text (e.g. [[SentimentAnalysis]], [[NaturalLanguageInference|NLI]], [[SemanticTextualSimilarity|STS]]); token-level outputs one label per token (POS tagging, NER, [[QuestionAnswering|SQuAD]] span prediction).
- **Single-text vs. text-pair**: [[SentimentAnalysis]] / [[CoLA]] are single-text; [[NaturalLanguageInference|NLI]] / [[SemanticTextualSimilarity|STS]] / [[QuestionAnswering|QA]] are text-pair.

Four architectural choices for the same downstream task: RNN ([[BidirectionalRNN]] + [[GloVe]]), CNN ([[TextCNN]] + GloVe), attention+MLP ([[DecomposableAttention]]), or fine-tuned [[BERT]] ([[FineTuningBert]]). The trade-off: BERT requires minimal architecture changes but maximum compute; hand-crafted models are feasible when compute is constrained.
