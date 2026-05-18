---
title: "Neural Network Kernel"
type: concept
tags: [kernel-methods, gaussian-processes, neural-networks, theory]
sources: [d2l-gaussian-processes]
last_updated: 2026-05-16
---

# Neural Network Kernel (Neal 1996)

The [[KernelFunction|kernel]] obtained when a one-hidden-layer Bayesian neural network is taken to **infinite hidden width** — proven by [[RadfordNeal|Radford Neal]] in 1994 / published 1996 ([[d2l-gaussian-processes]] gp-priors §"The Neural Network Kernel"). The historical precursor to the [[NeuralTangentKernel|NTK]] (Jacot, Gabriel & Hongler 2018) and the original bridge between Bayesian neural networks and [[GaussianProcess|Gaussian processes]].

## Derivation

For a one-hidden-layer network $f(x)=b+\sum_{i=1}^J v_i h(x;u_i)$ with $b\sim\mathcal{N}(0,\sigma_b^2)$, $v_i\sim\mathcal{N}(0,\sigma_v^2/J)$, $u_i$ i.i.d., the **central limit theorem** gives that any finite collection of function values $(f(x_1),\dots,f(x_n))$ is jointly Gaussian as $J\to\infty$. The mean is $m(x)=0$; the covariance is

$$k(x,x') = \sigma_b^2 + \sigma_v^2\,\mathbb{E}_u[h(x;u)h(x';u)].$$

For the special case $h(x;u)=\textrm{erf}(u_0+\sum_j u_j x_j)$ with $u\sim\mathcal{N}(0,\Sigma)$, the expectation has a closed-form arcsine expression:

$$k(x,x') = \frac{2}{\pi}\sin^{-1}\!\left(\frac{2\tilde{x}^\top\Sigma\tilde{x}'}{\sqrt{(1+2\tilde{x}^\top\Sigma\tilde{x})(1+2\tilde{x}'^\top\Sigma\tilde{x}')}}\right).$$

## Properties

- **Non-stationary.** Unlike [[RBFKernel|RBF]], the NN kernel depends on $(x,x')$ jointly — not just on $x-x'$. Sample functions look qualitatively different near the origin from elsewhere in input space.
- **The 1996 NeurIPS rejection.** Wilson notes [[RadfordNeal|Neal 1996]] was "one of the most infamous NeurIPS rejections" before its eventual publication.
- **Triggered the mid-1990s neural-net → GP migration.** D2L: *"This connection, discovered by Radford Neal, triggered machine learning researchers to move away from neural networks, and towards Gaussian processes"* — the kernel-methods era of [[d2l-introduction|D2L's "1995–2005 NN winter"]].
- **Reborn as NTK.** Matthews et al. (2018) and Novak et al. (2018) generalized this to deeper networks; [[NeuralTangentKernel|NTK]] (Jacot et al. 2018) gave the gradient-trained version.

## Implication

Wilson's argument in [[d2l-gaussian-processes]]:

> "Neural networks are not as distinct as we make them out to be."

Combined with the [[RBFKernel]]'s derivation as an infinite RBF basis, the NN-kernel result says: many model classes we treat as fundamentally different are equivalent to GPs with specific kernels in the limit. The kernel is the right level of abstraction to compare priors.

## Connections

- [[d2l-gaussian-processes]] — gp-priors §"The Neural Network Kernel".
- [[GaussianProcess]] — the model class.
- [[KernelFunction]] — the family.
- [[RadfordNeal]] — discoverer of the correspondence (1994/1996).
- [[NeuralTangentKernel]] — modern gradient-descent reincarnation.
- [[BayesianDeepLearning]] — broader context.
- [[CentralLimitTheorem]] — the inferential machinery.
- [[Stationarity]] — what NN kernel does *not* have.
