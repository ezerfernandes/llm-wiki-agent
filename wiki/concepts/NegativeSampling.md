---
title: "Negative Sampling"
type: concept
tags: [nlp, embeddings, word2vec, approximate-training]
sources: [d2l-nlp-pretraining, hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# Negative Sampling

Approximate-training trick that replaces the [[Word2Vec|word2vec]] softmax over the full vocabulary with a **per-pair binary-classification game**, dropping per-step cost from $\mathcal{O}(|\mathcal{V}|)$ to $\mathcal{O}(K)$ (typically $K=5\text{–}20$). A simplified variant of [[NoiseContrastiveEstimation|NCE]].

For each true (center, context) pair $(w_c, w_o)$, model "this pair came from the data" as
$$P(D=1\mid w_c, w_o)=\sigma(\mathbf{u}_o^\top\mathbf{v}_c).$$
For each true pair, sample $K$ **noise words** $w_k\sim P(w)$ (typically the unigram distribution raised to the $3/4$ power) and require them to score *low*: $P(D=0\mid w_c, w_k)=1-\sigma(\mathbf{u}_k^\top\mathbf{v}_c)=\sigma(-\mathbf{u}_k^\top\mathbf{v}_c)$. The per-pair log-loss is
$$-\log\sigma(\mathbf{u}_o^\top\mathbf{v}_c)-\sum_{k=1}^K\log\sigma(-\mathbf{u}_k^\top\mathbf{v}_c).$$
Without the negative samples the objective trivially blows up to all-vectors-infinite — they are essential to make the problem well-posed.

The default training scheme for [[SkipGram]] / [[CBOW]] in the original word2vec code release, and for [[FastText]]. Counterpart: [[HierarchicalSoftmax]] ($\mathcal{O}(\log_2|\mathcal{V}|)$ per step). See [[d2l-nlp-pretraining]] §approx-training.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 introduces negative sampling **without the math**, via the pedagogical motivation:

> "If, however, we have a dataset of only a target value of 1, then a model can cheat and ace it by outputting 1 all the time. To get around this, we need to enrich our training dataset with examples of words that are not typically neighbors. These are called negative examples." — Ch 2

The chapter's punchline on *how* to choose negative examples:

> "It turns out that we don't have to be too scientific in how we choose the negative examples. A lot of useful models result from the simple ability to detect positive examples from randomly generated examples (inspired by an important idea called noise-contrastive estimation)." — Ch 2

The pragmatic implementation is **random sampling from the vocabulary** (or, in the chapter's [[Word2VecRecommender|song-embedding example]], `negative=50` random songs per positive playlist co-occurrence in the [[Gensim]] `Word2Vec` constructor).

Ch 2 also names skip-gram + negative sampling as the **prototype of contrastive training** more broadly:

> "This idea of a model that takes two vectors and predicts if they have a certain relation is one of the most powerful ideas in machine learning, and time after time has proven to work very well with language models." — Ch 2

— forward-referencing Ch 10 (sentence-embedding contrastive training) and Ch 9 (image-caption contrastive alignment).
