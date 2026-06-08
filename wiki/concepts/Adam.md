---
title: "Adam Optimizer"
type: concept
tags: [optimization, deep-learning, foundational]
sources: [d2l-optimization, mlsysbook-ch05-neural-computation, mlsysbook-ch08-model-training]
last_updated: 2026-06-05
---

# Adam

**Ada**ptive **M**oment Estimation — [[DiederikKingma|Kingma]] & [[JimmyBa|Ba]] 2014 (ICLR 2015). The dominant deep-learning optimizer of the [[transformer|Transformer]] era. Combines [[Momentum|first-moment momentum]] with [[RMSProp]]-style second-moment scaling and adds **bias correction** to handle the zero-initialization bias of both estimates.

## The algorithm

Maintain two leaky-average state variables per parameter:

$$\begin{aligned}
\mathbf{v}_t &\leftarrow \beta_1\,\mathbf{v}_{t-1} + (1-\beta_1)\,\mathbf{g}_t, \\
\mathbf{s}_t &\leftarrow \beta_2\,\mathbf{s}_{t-1} + (1-\beta_2)\,\mathbf{g}_t^2.
\end{aligned}$$

**Bias correction** (the key novelty over RMSProp + momentum). Since $\mathbf{v}_0 = \mathbf{s}_0 = \mathbf{0}$, both estimates are biased toward zero early in training. The geometric-series identity $\sum_{i=0}^{t-1}\beta^i = (1-\beta^t)/(1-\beta)$ implies a renormalized estimate:

$$\hat{\mathbf{v}}_t = \frac{\mathbf{v}_t}{1-\beta_1^t}, \qquad \hat{\mathbf{s}}_t = \frac{\mathbf{s}_t}{1-\beta_2^t}.$$

Update:

$$\mathbf{x}_t \leftarrow \mathbf{x}_{t-1} - \frac{\eta\,\hat{\mathbf{v}}_t}{\sqrt{\hat{\mathbf{s}}_t} + \epsilon}.$$

## Standard hyperparameters

| Hyperparameter | Default | Role |
|---|---|---|
| $\beta_1$ | $0.9$ | first-moment decay (10-step momentum) |
| $\beta_2$ | $0.999$ | second-moment decay (1000-step variance) |
| $\epsilon$ | $10^{-6}$ to $10^{-8}$ | numerical stability |
| $\eta$ | $10^{-3}$ to $10^{-4}$ | global learning rate |

The variance estimate moves *much more slowly* than the momentum — $\beta_2 \gg \beta_1$ is the design choice.

## Position in the optimizer family

[[d2l-optimization]] §adam framing — Adam unifies prior ideas:

- **[[StochasticGradientDescent]]** — base gradient estimator.
- **[[MinibatchSGD]]** — vectorized computation.
- **[[Momentum]]** — first-moment leaky average (Adam's $\mathbf{v}_t$).
- **[[Adagrad]]** — per-coordinate scaling.
- **[[RMSProp]]** — leaky-average second-moment fix to Adagrad (Adam's $\mathbf{s}_t$).
- **Bias correction** — the novel contribution to handle zero-init bias of the leaky averages.

## Known divergence mode

Reddi, Kale & Kumar 2019 (ICLR) prove that Adam can fail to converge in some *convex* settings due to high-variance second-moment estimates. [[Yogi]] (Zaheer, Reddi et al. 2018) is the canonical fix: replace $(1-\beta_2)(\mathbf{g}_t^2 - \mathbf{s}_{t-1})$ with $(1-\beta_2)\,\mathbf{g}_t^2 \odot \textrm{sgn}(\mathbf{g}_t^2 - \mathbf{s}_{t-1})$ so the update magnitude no longer depends on the deviation magnitude. AMSGrad (same paper) is another fix.

## AdamW vs Adam

A subtle but important practical variant — Loshchilov & Hutter 2017's **AdamW** decouples [[WeightDecay|weight decay]] from the gradient step: rather than adding $\lambda\mathbf{w}$ to the gradient (which Adam then scales by $1/\sqrt{\hat{\mathbf{s}}_t}$, distorting the regularization), AdamW applies $(1-\eta\lambda)\mathbf{w}$ shrinkage *separately* from the Adam update. AdamW is the default for [[transformer|Transformer]] / [[BERT]] / GPT / [[T5]] pretraining.

## Why it became dominant

- **Robust to learning-rate misconfiguration.** Per-coordinate scaling means individual parameters auto-correct for scale mismatch.
- **Fast warm-up.** Bias correction makes the optimizer well-behaved from the very first step.
- **Minimal tuning.** Default $(\beta_1, \beta_2, \epsilon, \eta)$ work well across a remarkably wide range of architectures.

## Typical pairing

[[Adam]] (or AdamW) + [[Warmup|linear warmup]] + [[CosineLRSchedule|cosine annealing]] — the standard recipe for [[transformer|Transformer]] pretraining and most modern LLM training runs.

## Connections

- [[d2l-optimization]] — canonical reference (§adam).
- [[DiederikKingma]] / [[JimmyBa]] — co-authors.
- [[Momentum]] — first-moment ancestor.
- [[RMSProp]] — second-moment ancestor.
- [[Adagrad]] — per-coordinate-scaling progenitor.
- [[Yogi]] — divergence-fix variant.
- [[NesterovMomentum]] — Nadam variant uses NAG lookahead with Adam moments.
- [[StochasticGradientDescent]] / [[MinibatchSGD]] — underlying gradient method.
- [[LearningRateScheduler]] / [[Warmup]] / [[CosineLRSchedule]] — typically composed with Adam in practice.
- [[WeightDecay]] — AdamW handles this correctly; plain Adam distorts it.
- [[FineTuning]] / [[LLMFineTuning]] — Adam (or AdamW) is the default.
- [[OptimizerState]] / [[ModelSize]] / [[mlsysbook-ch05-neural-computation]] — Ch 5's systems point: Adam's two moment buffers (momentum + variance) + FP32 master weight bring total per-parameter training state to ~16 bytes in mixed precision — an ~8× multiplier over the 2-byte FP16 inference weight, *independent of model size*, and the primary reason training needs more accelerators than inference.
- [[mlsysbook-ch08-model-training]] — the training-capstone treatment: Adam imposes a **6× training-memory multiplier** over FP16 inference weights (7B model = 14 GB weights + 14 GB grads + 56 GB FP32 moments = 84 GB before activations); it converges in ~⅓ the iterations of SGD (GPT-2 XL ~50K vs ~150K+ steps) but at 3× per-parameter state, making optimizer choice a first-order memory constraint. [[AdamW]] is the memory-neutral generalization-improving default.
