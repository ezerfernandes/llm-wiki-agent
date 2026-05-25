---
title: "Classification Head"
type: concept
tags: [llm, classification, neural-network-architecture, fine-tuning]
sources: [hands-on-llm-ch04-text-classification, hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
---

# Classification Head

The **trainable output layer** appended to a frozen or fine-tuned representation model that turns its final hidden state(s) into **class logits**. The simplest classification head is a single linear layer (`Linear(hidden_dim → num_classes)`); fancier heads include a small MLP or pooling-then-linear.

## Where it sits in the model

For a [[bert|BERT]]-family encoder, the classification head consumes the **[[ClsToken|`[CLS]` token]] hidden state** (position 0) — the aggregate sequence vector. For a [[t5|T5]]-style encoder-decoder used in [[texttotextframework|text-to-text]] mode, there is no classification head at all — class labels are emitted as **decoded token strings** by the LM head.

## From [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

Ch 3 names classification heads as one of multiple swappable [[LMHead|head]] types:

> "The lm_head ... is a simple neural network layer itself. It is one of multiple possible 'heads' to attach to a stack of Transformer blocks to build different kinds of systems. Other kinds of Transformer heads include **sequence classification heads** and **token classification heads**." — Ch 3

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 uses two distinct kinds of "classification head" depending on the model regime:

1. **Task-specific representation model**: the head is **baked into the pretrained checkpoint** — e.g. [[TwitterRoBERTa|`cardiffnlp/twitter-roberta-base-sentiment-latest`]] ships with a 3-class softmax head over RoBERTa-base.
2. **Embedding model + external classifier**: the embedding model has **no classification head**; instead, an external [[LogisticRegression|`sklearn.linear_model.LogisticRegression`]] plays the role of the head, trained on the frozen 768-dim embedding features. The chapter's [[EmbeddingModel|embedding model]] regime is precisely the *"separate the embedding step from the classification step"* recipe.

> "The classifier is trainable and not limited to logistic regression and can take on any form as long as it performs classification." — Ch 4

This generalizes: a classification head can be **any function from hidden representation to class label** — including SVMs, gradient-boosted trees, k-NN, or even another LLM in [[LLMAsAJudge|LLM-as-judge]] form.

## Token-classification vs sequence-classification head

| Head type | Output shape | Use case |
|---|---|---|
| **Sequence classification** | `[batch, num_classes]` | Sentiment, intent, NLI, paraphrase |
| **Token classification** | `[batch, seq_len, num_classes]` | NER, POS tagging, span detection |

Both are surveyed by [[FineTuningBert|fine-tuning-BERT]] templates ([[d2l-nlp-applications]]) and are first-class citizens in Hugging Face Transformers (`AutoModelForSequenceClassification`, `AutoModelForTokenClassification`).

## Connections

- [[LMHead]] — the language-modeling-head sibling that produces vocab-sized logits.
- [[Classification]] / [[TextClassification]] / [[SentimentAnalysis]] — the task family.
- [[bert]] / [[ClsToken]] — the `[CLS]`-based sequence-classification convention.
- [[TaskSpecificModel]] — when the head is baked into the pretrained checkpoint.
- [[EmbeddingModel]] / [[LogisticRegression]] — when the head is an external classifier.
- [[FineTuningBert]] — D2L's canonical fine-tuning template for the head.
- [[hands-on-llm-ch03-looking-inside-llms]] / [[hands-on-llm-ch04-text-classification]] — wiki sources.
