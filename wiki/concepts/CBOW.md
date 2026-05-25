---
title: "Continuous Bag of Words (CBOW)"
type: concept
tags: [nlp, embeddings, word2vec, self-supervised]
sources: [d2l-nlp-pretraining, hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# Continuous Bag of Words (CBOW)

The second [[Word2Vec|word2vec]] model ([[TomasMikolov|Mikolov]], Chen, Corrado et al. 2013), and the structural mirror of [[SkipGram]]: **predict the center word from its averaged context words**. For context window size $m$, average the context-word vectors $\bar{\mathbf{v}}_o=\frac{1}{2m}\sum_{i=1}^{2m}\mathbf{v}_{o_i}$ and model
$$P(w_c\mid\mathcal{W}_o)=\frac{\exp(\mathbf{u}_c^\top\bar{\mathbf{v}}_o)}{\sum_{i\in\mathcal{V}}\exp(\mathbf{u}_i^\top\bar{\mathbf{v}}_o)}.$$
Maximum-likelihood training is structurally identical to skip-gram and shares the same vocabulary-size softmax bottleneck, fixed by [[NegativeSampling]] or [[HierarchicalSoftmax]].

Unlike skip-gram, CBOW typically uses the **context-word vectors** as the final representation. Empirically CBOW trains faster (one prediction per context window vs $2m$) but skip-gram tends to perform better on rare words and on analogy tasks — which is why [[GloVe]] and [[FastText]] both build on skip-gram. See [[d2l-nlp-pretraining]] §word2vec.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 introduces only **[[SkipGram|skip-gram]]** by name in its word2vec walk-through — the chapter pedagogically emphasizes skip-gram + negative sampling as the canonical word2vec pair. CBOW is implicit in the chapter's "two main word2vec models" framing without being named directly; the wiki keeps both pages in case the reader needs the formal distinction.
