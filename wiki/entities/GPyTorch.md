---
title: "GPyTorch"
type: entity
tags: [library, gaussian-processes, pytorch]
sources: [d2l-gaussian-processes]
last_updated: 2026-05-16
---

# GPyTorch

[[PyTorch]]-integrated [[GaussianProcess|Gaussian-process]] library — [[JacobGardner|Gardner]], Pleiss, Weinberger, Bindel & [[AndrewGordonWilson|Wilson]] 2018 (NeurIPS) — used for state-of-the-art **scalable GP inference**: SKI / KISS-GP / [[InducingPoint|inducing points]] / blackbox matrix–vector multiplies via Cholesky-free iterative solvers, enabling GPs at millions of points and tight GPU-side integration with deep-learning workflows. [[d2l-gaussian-processes]] uses GPyTorch as the production-grade companion to its from-scratch GP regression code.

## Selected operational primitives (per D2L gp-inference)

- `gpytorch.models.ExactGP` — exact-inference GP base class.
- `gpytorch.kernels.ScaleKernel(gpytorch.kernels.RBFKernel())` — the canonical RBF kernel with learnable amplitude; one-line swap to `MaternKernel` / `SpectralMixtureKernel`.
- `gpytorch.likelihoods.GaussianLikelihood()` — Gaussian observation noise; required for exact inference.
- `gpytorch.mlls.ExactMarginalLogLikelihood(likelihood, model)` — the [[MarginalLikelihood|marginal log-likelihood]] objective; trained with full-batch [[Adam]] or L-BFGS (mini-batches *do not* converge — the marginal likelihood doesn't factorize over data).
- `gpytorch.distributions.MultivariateNormal` — the GP posterior distribution at evaluation time, with `.confidence_region()` returning the 95% credible interval.
- Convention: GPyTorch parameterizes the **squared** length-scale and **variance** (not standard deviation) — *"GPyTorch is working with squared length-scales and observation noise."*

## Connections

- [[d2l-gaussian-processes]] — D2L's production GP backend.
- [[GaussianProcess]] — the model class.
- [[AndrewGordonWilson]] — co-author; D2L chapter author.
- [[PyTorch]] — the host framework.
- [[RBFKernel]] / [[MaternKernel]] / [[MarginalLikelihood]] — wrapped primitives.
- [[Adam]] — the standard marginal-likelihood optimizer in GPyTorch (full-batch).
