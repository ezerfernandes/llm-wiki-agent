---
title: "LogSumExp"
type: concept
tags: [numerical-stability, softmax, classification, deep-learning]
sources: [d2l-linear-classification]
last_updated: 2026-05-16
---

# LogSumExp (LSE) Trick

A numerical-stability transformation that lets us compute $\log\sum_k\exp(o_k)$ without overflow or underflow, by subtracting $\bar o = \max_k o_k$ from every term:

$$
\mathrm{LSE}(\mathbf o) = \log\sum_k\exp(o_k) = \bar o + \log\sum_k\exp(o_k - \bar o).
$$

Each $o_k - \bar o \leq 0$, so every $\exp(o_k - \bar o) \in (0,1]$; the sum is bounded in $[1, q]$ for $q$ classes, and the leading $\bar o$ is added back as a scalar. Both overflow and underflow are eliminated.

## Why it matters for [[Softmax|softmax]] + [[CrossEntropyLoss|cross-entropy]]

Plain softmax exponentiates logits in FP32, which overflows at $\sim e^{90}$ and underflows below $\sim e^{-90}$. Subtracting $\bar o$ before exponentiating is the standard fix: the numerator $\exp(o_j - \bar o) \leq 1$ and the denominator stays in $[1, q]$.

Better: **fuse softmax with the log inside cross-entropy** so the framework never materializes the exponentiated probabilities. The fused form is:

$$
\log\hat y_j = o_j - \bar o - \log\sum_k\exp(o_k - \bar o)
$$

and the cross-entropy loss is $-\sum_j y_j \log\hat y_j$ computed directly on logits. Per [[d2l-linear-classification]]: passing **logits** (not probabilities) to the framework's cross-entropy operator is the correct interface. Every modern framework's classification loss does this internally:

| Framework | Operator |
|---|---|
| PyTorch | `F.cross_entropy(logits, target)` / `nn.CrossEntropyLoss` |
| MXNet | `gluon.loss.SoftmaxCrossEntropyLoss` |
| TensorFlow | `tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)` |
| JAX / Optax | `optax.softmax_cross_entropy_with_integer_labels` |

## Properties

- **Translation invariance**: $\mathrm{LSE}(\mathbf o + c) = \mathrm{LSE}(\mathbf o) + c$ — what makes the $\bar o$-subtraction a no-op.
- **Convex**: the log-partition function of an [[ExponentialFamily|exponential family]] is convex; its gradient is the softmax and its Hessian is the softmax's covariance matrix.
- **Smooth max**: $\mathrm{LSE}(\mathbf o) \geq \max_k o_k$, with equality in the limit $\lambda\to\infty$ of $\lambda^{-1}\mathrm{LSE}(\lambda \mathbf o)$ — the namesake "softmax."

## Connections

- [[Softmax]] — what the trick stabilizes.
- [[CrossEntropyLoss]] — what the fused operator computes end-to-end.
- [[ExponentialFamily]] — LSE = the family's log-partition function $A(\boldsymbol\theta)$.
- [[d2l-linear-classification]] — corpus anchor (Section *Softmax Revisited*).
