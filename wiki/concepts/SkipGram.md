---
title: "Skip-Gram"
type: concept
tags: [nlp, embeddings, word2vec, self-supervised]
sources: [d2l-nlp-pretraining, hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# Skip-Gram

One of the two [[Word2Vec|word2vec]] models ([[TomasMikolov|Mikolov]], Sutskever, Chen et al. 2013). Given a sliding context window of size $m$ over a text sequence, the **skip-gram** model uses a *center* word to predict each of its *context* words: it maximizes
$$\prod_{t=1}^T\prod_{-m\le j\le m,\,j\ne 0}P(w^{(t+j)}\mid w^{(t)})$$
under the conditional-independence assumption that context words are generated independently given the center. Each word $w_i$ has two $d$-dimensional vectors — $\mathbf{v}_i$ as the center, $\mathbf{u}_i$ as a context — and the conditional probability is a softmax over dot products:
$$P(w_o\mid w_c)=\frac{\exp(\mathbf{u}_o^\top\mathbf{v}_c)}{\sum_{i\in\mathcal{V}}\exp(\mathbf{u}_i^\top\mathbf{v}_c)}.$$
The naive gradient sums over the full vocabulary $\mathcal{V}$, so practical training uses [[NegativeSampling]] or [[HierarchicalSoftmax]] to drop the cost from $\mathcal{O}(|\mathcal{V}|)$ to $\mathcal{O}(K)$ or $\mathcal{O}(\log|\mathcal{V}|)$ per step.

In practice the **center-word vectors** $\mathbf{v}_i$ are taken as the final word representations. Skip-gram is the model [[GloVe]] reinterprets via global co-occurrence statistics, and the model [[FastText]] augments with character-$n$-gram [[SubwordEmbedding|subword embeddings]]. Counterpart: [[CBOW]] (the reverse — predict the center from the context). See [[d2l-nlp-pretraining]] §word2vec.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 frames skip-gram as **the method of selecting neighboring words** that generates word2vec's training data: *"the central ideas are condensed here as we build on them when discussing one method for creating embeddings for recommendation engines in the following section."*

The chapter's pedagogical simplification: instead of the full softmax-over-vocabulary formulation, **skip-gram + [[NegativeSampling|negative sampling]]** are presented as the canonical pair — *"With this, we've seen two of the main concepts of word2vec (Figure 2-14): skip-gram, the method of selecting neighboring words, and negative sampling, adding negative examples by random sampling from the dataset."*

The chapter's [[Word2VecRecommender|song-embedding worked example]] uses the [[Gensim]] `Word2Vec` class with `window=20` (a much wider sliding window than the typical 2–5 used for natural-language text — playlists are short enough that any two co-occurring songs are reasonable similarity candidates).
