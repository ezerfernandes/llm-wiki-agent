---
title: "Text Classification"
type: concept
tags: [nlp, classification]
sources: [madewithml-baselines, madewithml-transformers, d2l-nlp-applications, hands-on-llm-ch04-text-classification]
last_updated: 2026-05-23
---

# Text Classification

Assigning categorical labels to text inputs. Tackled with baselines like [[SupportVectorMachine]] over TF-IDF and modern [[Transformer]] encoders such as [[bert]] and [[SciBERT]].

## Two axes (per [[d2l-nlp-applications]])

- **Single-text vs. text-pair**: single-text classification ([[SentimentAnalysis]], [[CoLA]]) operates on one sequence; text-pair classification ([[NaturalLanguageInference|NLI]]) on two.
- **Architecture**: hand-crafted ([[BidirectionalRNN]] + [[GloVe]], [[TextCNN]], [[DecomposableAttention]]) or fine-tuned [[BERT]] via [[FineTuningBert]] — the latter dominant when compute permits.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

[[JayAlammar|Alammar]] and [[MaartenGrootendorst|Grootendorst]]'s Ch 4 frames text classification across **four pretrained-LLM regimes** rather than four architecture choices, on a single [[RottenTomatoes|Rotten Tomatoes]] binary sentiment task with side-by-side [[F1Score|F1]] scores:

| Regime | Mechanism | F1 |
|---|---|---|
| **[[TaskSpecificModel|Task-specific]] [[RepresentationModel|representation model]]** | Pretrained [[bert|BERT]]-family classifier (head + softmax) used as-is | 0.80 ([[TwitterRoBERTa]]) |
| **[[EmbeddingModel|Embedding model]] + [[LogisticRegression|logistic regression]]** | Frozen [[SentenceTransformers|sentence-transformer]] embeddings → sklearn classifier | 0.85 ([[AllMPNetBaseV2]]) |
| **[[ZeroShotClassification|Zero-shot]] via [[LabelEmbedding|label embeddings]] + [[CosineSimilarity]]** | Embed label descriptions; argmax cosine to documents | 0.78 (no labeled data) |
| **[[GenerativeClassification|Generative]] via [[PromptEngineering|prompt]]** | Instruct an LLM; parse text output back to label | 0.84 ([[FLANT5]]-small) / 0.91 ([[ChatGPT]]) |

The chapter explicitly endorses the **[[TFIDF|TF-IDF]] + [[LogisticRegression|logistic regression]] classical baseline** as the comparison floor every LLM-based classifier must beat to justify itself — consistent with [[ai-engineering-ch04-evaluate-ai-systems|Huyen Ch 4]]'s baselining discipline.

## Connections

- [[hands-on-llm-ch04-text-classification]] — the chapter-level treatment.
- [[TaskSpecificModel]] / [[EmbeddingModel]] / [[ZeroShotClassification]] / [[GenerativeClassification]] — the four Ch 4 regimes.
- [[F1Score]] / [[ConfusionMatrix]] / [[ClassificationReport]] — Ch 4's evaluation primitives.
- [[d2l-nlp-applications]] / [[SentimentAnalysis]] / [[NaturalLanguageInference]] — D2L's architecture-level treatment.
