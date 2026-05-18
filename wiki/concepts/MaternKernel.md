---
title: "Matérn Kernel"
type: concept
tags: [kernel-methods, gaussian-processes]
sources: [d2l-gaussian-processes]
last_updated: 2026-05-16
---

# Matérn Kernel

A family of [[KernelFunction|covariance functions]] parameterized by a smoothness parameter $\nu>0$, generalizing the [[RBFKernel|RBF kernel]] (recovered at $\nu\to\infty$) and the exponential / [[OUKernel|Ornstein–Uhlenbeck]] kernel (recovered at $\nu=1/2$). Standard alternative to RBF in [[GaussianProcess|GP]] modeling when sample paths should be **rougher** than $C^\infty$ smooth.

$$k_\textrm{Matérn}(x,x') = a^2\frac{2^{1-\nu}}{\Gamma(\nu)}\!\left(\frac{\sqrt{2\nu}\,\|x-x'\|}{\ell}\right)^\nu K_\nu\!\left(\frac{\sqrt{2\nu}\,\|x-x'\|}{\ell}\right)$$

where $K_\nu$ is the modified Bessel function of the second kind. Common practical choices $\nu=1/2,3/2,5/2$ give closed-form expressions; sample paths are $\lceil\nu\rceil-1$ times mean-square differentiable.

## Why Matérn

- **Physical processes are rarely $C^\infty$.** [[RBFKernel|RBF]] sample paths are infinitely differentiable, which is unrealistic for most spatial and temporal phenomena. Matérn-$5/2$ ($C^2$) and $3/2$ ($C^1$) are the spatial-statistics defaults.
- **Tunable smoothness.** $\nu$ is interpretable as a control on path roughness; learnable from data via [[MarginalLikelihood]].
- **Includes the OU kernel.** $\nu=1/2$ recovers $k(x,x')=a^2\exp(-\|x-x'\|/\ell)$ — sample paths are continuous but nowhere differentiable, equivalent to a Brownian-bridge-like process.

[[d2l-gaussian-processes]] gp-inference flags Matérn as a one-line swap in [[GPyTorch]]: `gpytorch.kernels.matern_kernel()`. Wilson notes the kernel choice is "easier or harder to train the marginal likelihood" depending on smoothness regime.

## Connections

- [[d2l-gaussian-processes]] — flagged as the standard RBF alternative.
- [[KernelFunction]] — parent family.
- [[RBFKernel]] — the $\nu\to\infty$ limit.
- [[OUKernel]] — the $\nu=1/2$ limit.
- [[GaussianProcess]] — the model class.
- [[GPyTorch]] — `gpytorch.kernels.MaternKernel(nu=2.5)` (typical default).
- [[MarginalLikelihood]] — what learns $\nu$, $\ell$, $a$.
