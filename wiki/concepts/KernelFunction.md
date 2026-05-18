---
title: "Kernel / Covariance Function"
type: concept
tags: [kernel-methods, gaussian-processes, bayesian]
sources: [d2l-gaussian-processes]
last_updated: 2026-05-16
---

# Kernel / Covariance Function

A symmetric positive-semidefinite function $k(x,x')$ that specifies the covariance between function values $f(x)$ and $f(x')$ under a [[GaussianProcess]] prior, i.e. $k(x,x')=\textrm{Cov}(f(x),f(x'))$ ([[d2l-gaussian-processes]] gp-priors). The kernel **encodes the high-level properties** of functions the GP considers plausible — smoothness, periodicity, length-scale of variation, [[Stationarity|stationarity]], conditional independence, [[TranslationInvariance|translation invariance]]. Choosing a kernel is the GP analogue of choosing an architecture for a neural network.

## Two viewpoints

- **Function-space view.** $k(x,x')$ is the covariance of $f(x), f(x')$ as random functions; $k$ alone (with a mean function) defines the GP prior.
- **Weight-space view ([[KernelTrick|kernel trick]]).** For any $f(x)=w^\top\phi(x)$ with $w\sim\mathcal{N}(u,S)$, $k(x,x')=\phi(x)^\top S\phi(x')$. Mercer's theorem says every PSD $k$ corresponds to *some* feature map $\phi$ (possibly infinite-dimensional).

## Popular kernels (per D2L gp-priors)

| Kernel | Form | Notes |
|---|---|---|
| Linear | $\mathbf{x}^\top\mathbf{x}'$ | Recovers Bayesian linear regression. |
| Polynomial | $(\mathbf{x}^\top\mathbf{x}'+c)^d$ | All monomials up to degree $d$. |
| [[RBFKernel\|RBF / squared-exp]] | $a^2\exp(-\tfrac{1}{2\ell^2}\|x-x'\|^2)$ | Most popular; stationary; universal approximator. |
| [[MaternKernel\|Matérn]] | Family parameterized by $\nu$; less smooth than RBF | Standard alternative when RBF is too smooth. |
| [[OUKernel\|Ornstein–Uhlenbeck]] | $\exp(-\tfrac{1}{2\ell}\|x-x'\|)$ | Rougher than RBF (continuous-but-non-differentiable sample paths). |
| [[NeuralNetworkKernel\|Neural-net]] | $\frac{2}{\pi}\arcsin(\cdots)$ for $\textrm{erf}$ activation | Non-stationary; from infinite-width Bayesian NN ([[RadfordNeal\|Neal 1996]]). |
| [[SpectralMixtureKernel\|Spectral mixture]] | Sum of Gaussians in frequency domain | Approximates any stationary kernel; in [[GPyTorch]]. |

## Stationarity

A kernel is **stationary** if it depends only on $\tau=x-x'$ — i.e. $k(x,x')=k_\tau(x-x')$. [[RBFKernel|RBF]] is stationary; the [[NeuralNetworkKernel|NN kernel]] is not (sample functions look qualitatively different near the origin). Stationarity means the function's high-level properties (rate of variation, amplitude) don't change as we move in input space — usually a desirable inductive bias for time-series and spatial data.

## Hyperparameters

Even within a single kernel family, the [[Hyperparameter|hyperparameters]] are interpretable:

- [[Amplitude|Amplitude]] $a$ — vertical scale of the function.
- [[LengthScale|Length-scale]] $\ell$ — input distance over which function values become decorrelated; at $\|x-x'\|=\ell$, RBF covariance is $a^2\exp(-1/2)\approx 0.61 a^2$.

These are learned by maximizing the [[MarginalLikelihood]].

## Building new kernels

Closure properties allow constructing more expressive kernels:

- $k_1+k_2$ is a kernel.
- $k_1 \cdot k_2$ is a kernel.
- $\phi(x)^\top k(\cdot,\cdot)\phi(x')$ is a kernel for any function transformation.
- Periodic kernels can be built from $\sin$ of input distances.

This is the GP equivalent of stacking neural-network layers — a *kernel grammar* in which interpretable function classes compose.

## Connections

- [[d2l-gaussian-processes]] — canonical reference.
- [[GaussianProcess]] — the prior the kernel specifies.
- [[RBFKernel]] / [[MaternKernel]] / [[NeuralNetworkKernel]] / [[OUKernel]] — instances.
- [[KernelTrick]] — the Mercer / weight-space-equivalence machinery.
- [[Stationarity]] — translation-invariance property.
- [[MarginalLikelihood]] — what's optimized to learn kernel hyperparameters.
- [[BayesianLinearRegression]] — finite-feature special case.
- [[NeuralTangentKernel]] — kernel derived from infinite-width gradient-trained NNs.
