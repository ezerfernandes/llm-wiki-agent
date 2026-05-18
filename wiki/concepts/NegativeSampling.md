---
title: "Negative Sampling"
type: concept
tags: [nlp, embeddings, word2vec, approximate-training]
sources: [d2l-nlp-pretraining]
last_updated: 2026-05-16
---

# Negative Sampling

Approximate-training trick that replaces the [[Word2Vec|word2vec]] softmax over the full vocabulary with a **per-pair binary-classification game**, dropping per-step cost from $\mathcal{O}(|\mathcal{V}|)$ to $\mathcal{O}(K)$ (typically $K=5\text{–}20$). A simplified variant of [[NoiseContrastiveEstimation|NCE]].

For each true (center, context) pair $(w_c, w_o)$, model "this pair came from the data" as
$$P(D=1\mid w_c, w_o)=\sigma(\mathbf{u}_o^\top\mathbf{v}_c).$$
For each true pair, sample $K$ **noise words** $w_k\sim P(w)$ (typically the unigram distribution raised to the $3/4$ power) and require them to score *low*: $P(D=0\mid w_c, w_k)=1-\sigma(\mathbf{u}_k^\top\mathbf{v}_c)=\sigma(-\mathbf{u}_k^\top\mathbf{v}_c)$. The per-pair log-loss is
$$-\log\sigma(\mathbf{u}_o^\top\mathbf{v}_c)-\sum_{k=1}^K\log\sigma(-\mathbf{u}_k^\top\mathbf{v}_c).$$
Without the negative samples the objective trivially blows up to all-vectors-infinite — they are essential to make the problem well-posed.

The default training scheme for [[SkipGram]] / [[CBOW]] in the original word2vec code release, and for [[FastText]]. Counterpart: [[HierarchicalSoftmax]] ($\mathcal{O}(\log_2|\mathcal{V}|)$ per step). See [[d2l-nlp-pretraining]] §approx-training.
