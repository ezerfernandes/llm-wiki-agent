---
title: "Text Classification"
type: concept
tags: [nlp, classification]
sources: [madewithml-baselines, madewithml-transformers, d2l-nlp-applications]
last_updated: 2026-05-16
---

# Text Classification

Assigning categorical labels to text inputs. Tackled with baselines like [[SupportVectorMachine]] over TF-IDF and modern [[Transformer]] encoders such as [[bert]] and [[SciBERT]].

## Two axes (per [[d2l-nlp-applications]])

- **Single-text vs. text-pair**: single-text classification ([[SentimentAnalysis]], [[CoLA]]) operates on one sequence; text-pair classification ([[NaturalLanguageInference|NLI]]) on two.
- **Architecture**: hand-crafted ([[BidirectionalRNN]] + [[GloVe]], [[TextCNN]], [[DecomposableAttention]]) or fine-tuned [[BERT]] via [[FineTuningBert]] — the latter dominant when compute permits.
