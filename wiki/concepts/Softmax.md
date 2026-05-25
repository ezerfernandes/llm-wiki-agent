---
title: "Softmax"
type: concept
tags: [activation-function, classification, foundational]
sources: [madewithml-baselines, d2l-linear-classification, ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Softmax

A normalization that maps a vector of logits $\mathbf o \in \mathbb R^q$ to a probability distribution on $q$ categories:

$$
\hat y_i = \mathrm{softmax}(\mathbf o)_i = \frac{\exp(o_i)}{\sum_{j=1}^q \exp(o_j)}.
$$

Standard output layer for multi-class classification and the core of attention in the [[Transformer]]. Trained almost universally with [[CrossEntropyLoss]] — together they form the canonical classification loss in deep learning.

## Properties

- **Order-preserving**: $\arg\max_j \hat y_j = \arg\max_j o_j$, so hard predictions can be read off the logits without exponentiation.
- **Differentiable** with the clean derivative $\partial_{o_j} l = \hat y_j - y_j$ when paired with cross-entropy on a one-hot target — exactly the regression-style "prediction minus target" signal, a general property of any [[ExponentialFamily|exponential-family]] log-likelihood.
- **Translation-invariant**: $\mathrm{softmax}(\mathbf o + c\mathbf 1) = \mathrm{softmax}(\mathbf o)$. The basis of the [[LogSumExp|LogSumExp trick]] for numerical stability: subtract $\bar o = \max_k o_k$ before exponentiating.
- **Maximum-entropy** distribution on $K$ categories with linear constraints — the natural choice from the exponential-family perspective.

## Historical origin

Per [[d2l-linear-classification]]: the construction dates back to **Gibbs (1902)**, adapted from Boltzmann's $\exp(-E/kT)$ distribution over thermodynamic energy states in statistical physics. The "temperature" terminology in modern ML and in attention scaling (e.g., dividing logits by $\sqrt{d_k}$ in [[Transformer]] attention) is this same $T$.

## Numerical stability

Naive softmax overflows in FP32 when any logit exceeds ~90 and underflows when all logits are very negative. Production code never does $\exp(o_j)/\sum\exp(o_k)$ directly; it uses the [[LogSumExp|LogSumExp trick]] (subtract the max before exponentiating) and, where possible, **fuses softmax with the log inside cross-entropy** so probabilities are never materialized. Pass **logits**, not probabilities, to framework cross-entropy losses (`F.cross_entropy`, `SparseCategoricalCrossentropy(from_logits=True)`, `optax.softmax_cross_entropy_with_integer_labels`).

## Connections

- [[CrossEntropyLoss]] — the loss softmax is almost universally trained with.
- [[LogSumExp]] — numerical-stability trick fusing softmax and cross-entropy.
- [[Classification]] — the task softmax serves as the canonical output head for.
- [[LogisticRegression]] — binary case ($q=2$); softmax generalizes the sigmoid.
- [[ExponentialFamily]] — softmax is the categorical-family log-partition gradient.
- [[Attention]] / [[Transformer]] — attention weights are a softmax over scaled dot-product logits.
- [[d2l-linear-classification]] — corpus anchor for the historical origin, derivation, and gradient.

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

Ch 2 treats softmax as the **logit-to-probability conversion at the heart of LLM sampling**:

> "Logits don't sum up to one. Logits can even be negative, while probabilities have to be non-negative. To convert logits to probabilities, a softmax layer is often used."

For a vocab of N tokens with logit vector $(x_1, \ldots, x_N)$, $p_i = \exp(x_i) / \sum_j \exp(x_j)$.

### Modifications used by sampling controls

- **[[Temperature|Temperature]] T** rescales logits to $x_i / T$ before applying softmax. The same T from statistical physics that underlies the Boltzmann distribution.
- **[[Topk|Top-k]]** restricts softmax to the top k logits — reduces compute on large vocabularies.
- **[[Topp|Top-p]] / nucleus sampling** runs softmax fully then keeps only the smallest set of tokens whose cumulative probability exceeds p.
- **[[ConstrainedSampling|Constrained sampling]]** masks logits to −∞ for tokens that don't satisfy a grammar before softmax.

### [[Logprobs|Logprobs]] vs probabilities

Probabilities for a 100K-vocab LM are often too small to represent without **underflow**. Log-scale probabilities (logprobs) avoid this — and log of a product = sum of logs makes sequence-level scoring numerically clean.
