---
title: "Analogy Task"
type: concept
tags: [nlp, embeddings, evaluation]
sources: [d2l-nlp-pretraining]
last_updated: 2026-05-16
---

# Analogy Task

Intrinsic evaluation for [[WordEmbedding|word embeddings]]. Given an analogy *a : b :: c : d* and only $a$, $b$, $c$, predict $d$ by **vector arithmetic + nearest neighbour**:
$$d = \arg\max_w \cos\big(\textrm{vec}(w),\ \textrm{vec}(c)+\textrm{vec}(b)-\textrm{vec}(a)\big),$$
typically excluding $a$, $b$, $c$ themselves. The fact that pretrained [[Word2Vec|word2vec]] and [[GloVe]] embeddings *recover* analogies this way is the canonical demonstration that distributed word vectors encode **linear semantic and syntactic structure**.

[[d2l-nlp-pretraining]] §similarity-analogy demonstrates four flavours of analogy on the 50-d GloVe Wikipedia embeddings:

- **Semantic — male/female**: man : woman :: son : daughter.
- **Semantic — capital/country**: beijing : china :: tokyo : japan.
- **Syntactic — adjective/superlative**: bad : worst :: big : biggest.
- **Syntactic — present/past tense**: do : did :: go : went.

Companion intrinsic evaluation: [[WordSimilarity|word similarity]] via cosine nearest neighbours. The famous *king − man + woman ≈ queen* example is from the original [[TomasMikolov|Mikolov]] et al. 2013 paper. Limitations are well-known (Linzen 2016 / Rogers et al. 2017) — analogy accuracy depends heavily on the exclusion of $a$, $b$, $c$ and is sensitive to vector normalization — but the task remains the standard intrinsic embedding evaluation.
