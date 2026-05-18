---
title: "Hierarchical Softmax"
type: concept
tags: [nlp, embeddings, approximate-training, word2vec]
sources: [d2l-nlp-pretraining]
last_updated: 2026-05-16
---

# Hierarchical Softmax

Approximate-training trick for [[Word2Vec|word2vec]] that replaces the flat $|\mathcal{V}|$-way softmax with a **binary tree** whose leaves are the vocabulary words (originally Morin & Bengio 2005; Huffman-style by frequency in practice). Each conditional probability factorizes as a product of $\mathcal{O}(\log_2|\mathcal{V}|)$ sigmoids along the root-to-leaf path:
$$P(w_o\mid w_c)=\prod_{j=1}^{L(w_o)-1}\sigma\big([\![n(w_o,j+1)=\textrm{leftChild}(n(w_o,j))]\!]\cdot\mathbf{u}_{n(w_o,j)}^\top\mathbf{v}_c\big),$$
where $[\![\cdot]\!]\in\{+1,-1\}$ encodes left vs right at each internal node. Because $\sigma(x)+\sigma(-x)=1$ on every internal node, the probabilities of all vocabulary words automatically sum to 1.

Per-step cost: $\mathcal{O}(\log_2|\mathcal{V}|)$ — exponentially better than the $\mathcal{O}(|\mathcal{V}|)$ exact softmax. Counterpart: [[NegativeSampling]] ($\mathcal{O}(K)$ — empirically simpler and just as good for embeddings, so it has largely displaced hierarchical softmax in practice). See [[d2l-nlp-pretraining]] §approx-training.
