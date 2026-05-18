---
title: "fastText"
type: concept
tags: [nlp, embeddings]
sources: [d2l-nlp-pretraining]
last_updated: 2026-05-16
---

# FastText

A [[fair|Facebook AI Research]] [[WordEmbedding|word-embedding]] model ([[PiotrBojanowski|Bojanowski]], [[EdouardGrave|Grave]], [[ArmandJoulin|Joulin]] et al., TACL 2017) that augments [[Word2Vec|word2vec]] with **character-$n$-gram [[SubwordEmbedding|subword features]]**. Each word is bounded by special `<` / `>` markers and represented as the sum of its 3- to 6-character $n$-gram vectors plus the whole-word symbol:
$$\mathbf{v}_w=\sum_{g\in\mathcal{G}_w}\mathbf{z}_g.$$
The rest is unchanged from [[SkipGram|skip-gram]] (trained with [[NegativeSampling]] or [[HierarchicalSoftmax]]).

Two practical wins versus plain word2vec / [[GloVe]]: (i) **out-of-vocabulary** words and rare words inherit useful representations by composing learned subword vectors, and (ii) **morphological** regularities ("helps" / "helped" / "helping") share parameters via shared $n$-grams. Costs are a larger effective vocabulary (millions of subwords) and the per-word summation. Superseded by [[ContextualEmbedding]] models like [[BERT]] for most downstream NLP tasks, but fastText's pretrained multilingual vectors remain widely used. See [[d2l-nlp-pretraining]] §subword-embedding.
