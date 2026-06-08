---
title: "Batch Normalization"
type: concept
tags: [deep-learning, regularization, normalization]
sources: [d2l-convolutional-modern, mlsysbook-ch05-neural-computation, mlsysbook-ch06-network-architectures]
last_updated: 2026-06-05
---

# Batch Normalization

A layer that normalizes activations across a minibatch to zero mean and unit variance, then applies learnable scale and shift parameters. Introduced by [[SergeyIoffe|Ioffe]] & [[ChristianSzegedy|Szegedy]] (2015) at [[google|Google]]; one of the most-cited deep-learning papers ever; "applied in nearly all deployed image classifiers" ([[d2l-convolutional-modern]] §batch-norm). Together with [[ResidualConnection|residual connections]] (2015), batch normalization is what made training >100-layer networks routine.

## Definition

For an input $\mathbf{x}$ from minibatch $\mathcal{B}$:

$$\textrm{BN}(\mathbf{x}) = \boldsymbol{\gamma}\odot\frac{\mathbf{x}-\hat{\boldsymbol{\mu}}_\mathcal{B}}{\hat{\boldsymbol{\sigma}}_\mathcal{B}} + \boldsymbol{\beta}$$

where

$$\hat{\boldsymbol{\mu}}_\mathcal{B} = \frac{1}{|\mathcal{B}|}\sum_{\mathbf{x}\in\mathcal{B}}\mathbf{x}, \quad \hat{\boldsymbol{\sigma}}_\mathcal{B}^2 = \frac{1}{|\mathcal{B}|}\sum_{\mathbf{x}\in\mathcal{B}}(\mathbf{x}-\hat{\boldsymbol{\mu}}_\mathcal{B})^2 + \epsilon$$

- **$\boldsymbol{\gamma}$, $\boldsymbol{\beta}$** are learnable scale and shift parameters — recover the degrees of freedom lost in normalization.
- **$\epsilon$** is a small constant ($10^{-5}$) preventing division by zero.

## Per-layer-type semantics

- **Fully connected layers.** Statistics computed per feature, across the minibatch.
- **Convolutional layers.** Statistics computed per *channel*, across $m\cdot p\cdot q$ elements (minibatch × spatial extent). Compatible with translation invariance — each channel has its own scalar $\gamma$, $\beta$.

## Training vs. prediction modes

- **Training:** use *current minibatch* statistics. The minibatch-statistic noise injection is a regularization side-benefit.
- **Prediction:** use a moving-average estimate of mean/variance accumulated during training. This makes BN deterministic at inference time and removes batch-size dependence — but introduces a mode switch that frameworks track via `model.eval()` / `training=False` / `deterministic=True`.

PyTorch: `nn.BatchNorm1d` / `nn.BatchNorm2d`. The "Lazy" variants infer feature/channel count from the first forward pass.

## Three benefits (per D2L)

1. **Preprocessing-like rescaling** inside the network — keeps intermediate activations bounded; allows higher [[LearningRate|learning rates]].
2. **Regularization** via minibatch-statistic noise — works best at batch size 50–100 ("right amount" of noise).
3. **Numerical stability** — variable magnitudes can't diverge; training is much more robust.

## The "internal covariate shift" debate

[[SergeyIoffe|Ioffe]] & [[ChristianSzegedy|Szegedy]]'s original explanation: BN reduces *internal covariate shift* — drift in the distribution of intermediate activations during training. This explanation is now disputed:

- Santurkar, Tsipras, Ilyas et al. (2018) argue BN may actually *increase* internal covariate shift but smooths the optimization landscape.
- [[AliRahimi|Ali Rahimi]]'s 2017 NeurIPS Test-of-Time speech invoked internal covariate shift as the focal example of "alchemy" in deep learning.
- Lipton & Steinhardt (2018) revisit it in their "troubling trends in ML" position paper.

> "Batch normalization has proven an indispensable method, applied in nearly all deployed image classifiers. ... We conjecture, though, that the guiding principles of regularization through noise injection, acceleration through rescaling and lastly preprocessing may well lead to further inventions of layers and techniques in the future." — [[d2l-convolutional-modern]] §batch-norm discussion

The mechanism is debated; the empirical effectiveness is not.

## Variants

- **[[LayerNormalization]]** (Ba, Kiros, Hinton 2016) — per-observation; batch-size independent; identical at train and test. Default in [[transformer|Transformers]].
- **Instance normalization** (Ulyanov et al. 2016) — per-observation, per-channel; default in style transfer.
- **Group normalization** (Wu & He 2018) — per-observation, per-channel-group; useful at very small batch sizes.

## Caveats and practical tips

- **Remove the bias parameter** before BN — BN's $\beta$ subsumes it.
- **Batch-size dependence.** Sweet spot 50–100; tiny batches inject too much noise; huge batches regularize less.
- **Dropout interactions** were historically tricky to debug — modern practice often uses BN + LN in transformers and skips dropout-with-BN.
- **For robust models** that are less sensitive to input perturbations, consider *removing* batch normalization (Wang et al. 2022).

## Connections

- [[d2l-convolutional-modern]] — canonical reference.
- [[SergeyIoffe]] / [[ChristianSzegedy]] — co-authors.
- [[LayerNormalization]] — per-observation cousin; transformer default.
- [[ResNet]] / [[ResNeXt]] / [[DenseNet]] / [[Inception|Inception-v2]] / [[VGG]] — heavy users.
- [[ResidualBlock]] — wraps two BN layers inside each block.
- [[Dropout]] — orthogonal regularizer, sometimes incompatible.
- [[ReLU]] — typically placed *after* BN.
- [[CNN]] / [[Backpropagation]] / [[LearningRate]] — context.
- [[transformer]] — uses LayerNorm instead.
- [[mlsysbook-ch05-neural-computation]] — systems cost: BN adds an all-reduce sync barrier across the batch dim, diverges between train (live batch stats) and inference (frozen running stats), and is small-batch-sensitive (batch <8–16 degrades accuracy 3–8%) — which is *why* [[LayerNormalization|LayerNorm]] (batch-independent) replaced it in transformers. Also a [[DyingReLU|dying-ReLU]] mitigation.
- [[mlsysbook-ch06-network-architectures]] — frames normalization as a *portable building block*: BatchNorm (born in CNNs, cut ImageNet training time 14×) → [[LayerNormalization|LayerNorm]] (batch-independent, for transformers) → [[RMSNorm]] (drops mean-centering, 7–64% faster) — an evolution driven by systems pressure (batch dependency, training-serving skew, LLM latency).
