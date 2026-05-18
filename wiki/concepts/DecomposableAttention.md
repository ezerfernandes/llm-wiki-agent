---
title: "Decomposable Attention"
type: concept
tags: [model, nlp, nli, attention]
sources: [d2l-nlp-applications]
last_updated: 2026-05-16
---

# Decomposable Attention

**Decomposable attention model** ([[AnkurParikh|Parikh]], Täckström, Das & Uszkoreit, EMNLP 2016) — an [[Attention|attention]]-based architecture for [[NaturalLanguageInference|natural language inference]] that has **no recurrent or convolutional layers**, only attention + MLPs. Per [[d2l-nlp-applications]] §`natural-language-inference-attention`: "achieves the best result at the time on the SNLI dataset with much fewer parameters."

## Three jointly-trained steps

Let the premise be $\mathbf{A} = (\mathbf{a}_1, \ldots, \mathbf{a}_m)$ and the hypothesis $\mathbf{B} = (\mathbf{b}_1, \ldots, \mathbf{b}_n)$ (typically [[GloVe]] embeddings).

1. **Attending** — soft cross-sequence alignment. Compute scores
   $$e_{ij} = f(\mathbf{a}_i)^\top f(\mathbf{b}_j)$$
   where $f$ is a shared MLP **applied separately to each token** (the **decomposition trick** — see below). Softmax-weighted averages
   $$\boldsymbol{\beta}_i = \sum_j \mathrm{softmax}(e_{ij}) \, \mathbf{b}_j \qquad \boldsymbol{\alpha}_j = \sum_i \mathrm{softmax}(e_{ij}) \, \mathbf{a}_i$$
   align hypothesis tokens to each premise position and vice versa.
2. **Comparing** — feed concatenations $[\mathbf{a}_i, \boldsymbol{\beta}_i]$ and $[\mathbf{b}_j, \boldsymbol{\alpha}_j]$ through a shared MLP $g$ to get per-token comparison vectors $\mathbf{v}_{A,i}$ and $\mathbf{v}_{B,j}$.
3. **Aggregating** — sum-pool both sets, $\mathbf{v}_A = \sum_i \mathbf{v}_{A,i}$, $\mathbf{v}_B = \sum_j \mathbf{v}_{B,j}$, then feed $[\mathbf{v}_A, \mathbf{v}_B]$ through MLP $h$ to a 3-way (entailment / contradiction / neutral) softmax.

## The decomposition trick

Because $f$ is applied to $\mathbf{a}_i$ and $\mathbf{b}_j$ *separately* before the dot product, only $m + n$ MLP applications are needed — **linear complexity**, vs. the $mn$ quadratic complexity of feeding token pairs through an MLP directly. This is structurally the same trick that makes scaled dot-product [[SelfAttention|self-attention]] efficient: $\mathrm{softmax}(QK^\top/\sqrt{d}) V$ separates the projection of each token before the pairwise score.

## Significance

- **Pre-Transformer attention application**: published one year before [[1706.03762-attention-is-all-you-need]], demonstrated that attention alone (with MLPs and no recurrence / convolution) could match SOTA on a major NLP task.
- **Forerunner of [[SelfAttention]]** in spirit: decomposed token scoring as a dot product of independently-projected representations.

## Connections

- [[Attention]] / [[SelfAttention]] / [[ScaledDotProductAttention]] / [[Transformer]] — direct architectural lineage.
- [[NaturalLanguageInference]] / [[SNLI]] — task and benchmark.
- [[AnkurParikh]] — first author.
- [[GloVe]] — typical input embeddings.
- [[d2l-nlp-applications]] §`natural-language-inference-attention` — D2L's canonical worked example.
