---
title: "GloVe"
type: concept
tags: [nlp, embeddings]
sources: [d2l-nlp-pretraining, hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# GloVe

**Global Vectors for Word Representation** ([[JeffreyPennington|Pennington]], [[RichardSocher|Socher]] & [[ChrisManning|Manning]], [[StanfordUniversity|Stanford NLP]] 2014). A static [[WordEmbedding|word embedding]] trained by **weighted-squared-loss factorization of the global word-word co-occurrence matrix**:
$$\mathcal{L}=\sum_{i,j\in\mathcal{V}} h(x_{ij})\big(\mathbf{u}_j^\top\mathbf{v}_i+b_i+c_j-\log x_{ij}\big)^2,$$
with $x_{ij}$ the co-occurrence count of word $j$ in the context of word $i$, and weight function $h(x)=(x/c)^\alpha$ saturating at 1. Because $x_{ij}=x_{ji}$, the center- and context-word vectors of any word are *mathematically equivalent* in GloVe — the published embedding sums them.

Per [[d2l-nlp-pretraining]] §glove, GloVe is equivalent to skip-gram reinterpreted via global statistics with cross-entropy replaced by a weighted squared loss (avoiding the expensive softmax normalization and the over-weighting of rare-event tails). Justified geometrically by the **ratio of co-occurrence probabilities** $p_{ik}/p_{jk}$, which is large iff $w_k$ is related to $w_i$ but not $w_j$. A staple alongside [[Word2Vec|word2vec]] and [[FastText]] before [[ContextualEmbedding|contextual embeddings]] from [[BERT]] supplanted static vectors.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 uses GloVe as a worked example of **loading pretrained word embeddings via [[Gensim]]**:

```python
import gensim.downloader as api
model = api.load("glove-wiki-gigaword-50")  # 66MB, 50-dim, Wikipedia-trained
model.most_similar([model['king']], topn=11)
# [('king', 1.0), ('prince', 0.82), ('queen', 0.78), ('ii', 0.77), ('emperor', 0.77),
#  ('son', 0.77), ('uncle', 0.76), ('kingdom', 0.75), ('throne', 0.75), ...]
```

The chapter names GloVe in its closing summary as one of the three popular pre-LLM word-embedding methods: *"Before LLMs, word embedding methods like word2vec, GloVe, and fastText were popular. In language processing, this has largely been replaced with contextualized word embeddings produced by language models."*
