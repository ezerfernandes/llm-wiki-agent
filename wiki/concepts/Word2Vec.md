---
title: "Word2Vec"
type: concept
tags: [nlp, embeddings]
sources: [madewithml-embeddings, d2l-nlp-pretraining]
last_updated: 2026-05-16
---

# Word2Vec

A family of shallow neural models — [[SkipGram|skip-gram]] (predict context words from a center word) and [[CBOW|continuous bag of words]] (predict the center word from averaged context words) — that learn dense [[WordEmbedding|word embeddings]] from co-occurrence ([[TomasMikolov|Mikolov]] et al. 2013, at [[google|Google]]). Each word has two $d$-dim vectors (as center / as context); the conditional probability is a softmax over dot products. Trained tractably via [[NegativeSampling]] or [[HierarchicalSoftmax]] to avoid the $\mathcal{O}(|\mathcal{V}|)$ softmax bottleneck.

Foundational pre-[[Transformer]] representation, now largely subsumed by contextual encoders like [[bert]], but its **conceptual framework** — self-supervised dense distributed representations trained from co-occurrence — anchors every successor (including [[GloVe]], [[FastText]], and the input-embedding layer of every modern LLM). See [[d2l-nlp-pretraining]] for the from-scratch implementation walk-through on [[PTB]].
