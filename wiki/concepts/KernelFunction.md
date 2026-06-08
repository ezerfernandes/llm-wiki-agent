---
title: "Kernel / Covariance Function"
type: concept
tags: [kernel-methods, gaussian-processes, bayesian]
sources: [d2l-gaussian-processes, mml-ch12-classification-svm]
last_updated: 2026-06-05
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

## From [[mml-ch12-classification-svm|MML Ch 12]] — the SVM / kernel-machine view

> This page is the canonical wiki home for the **ML kernel concept** (the bare [[Kernel]] page is the *operating-system* kernel; see its disambiguation note). [[mml-ch12-classification-svm|MML Ch 12]] §12.4 anchors the SVM/kernel-machine view here.

§12.4 (book pp. 388–390) *defines* a kernel as a function $k:\mathcal{X}\times\mathcal{X}\to\mathbb{R}$ for which there exists a Hilbert space $\mathcal{H}$ and a [[FeatureMap|feature map]] $\boldsymbol\phi:\mathcal{X}\to\mathcal{H}$ such that

$$k(\mathbf{x}_i,\mathbf{x}_j)=\langle\boldsymbol\phi(\mathbf{x}_i),\boldsymbol\phi(\mathbf{x}_j)\rangle_\mathcal{H}\qquad(\text{Eq. } 12.52).$$

The **validity condition** is identical to the GP/Mercer condition above: kernels must be symmetric and positive-semidefinite, so every [[GramMatrix|kernel/Gram matrix]] $K_{ij}=k(\mathbf{x}_i,\mathbf{x}_j)$ satisfies $\forall\mathbf{z}\in\mathbb{R}^N:\mathbf{z}^\top\mathbf{K}\mathbf{z}\ge0$ (Eq. 12.53, §3.2.3 [[SymmetricPositiveDefiniteMatrix|SPD]]). Each kernel has a *unique* reproducing kernel Hilbert space (RKHS, Aronszajn 1950), and $\boldsymbol\phi(\mathbf{x})=k(\cdot,\mathbf{x})$ is its **canonical feature map**. In the [[DualSVM|dual SVM]] the kernel replaces $\langle\mathbf{x}_i,\mathbf{x}_j\rangle$, lifting the classifier to nonlinear decision surfaces via the [[KernelTrick|kernel trick]] without ever materializing $\boldsymbol\phi$. The chapter's flagged kernels are the polynomial $(\mathbf{x}^\top\mathbf{x}'+c)^d$ (cheap even when the monomial expansion is huge) and the Gaussian [[RBFKernel|RBF]] (infinite-dimensional feature space, "cannot be explicitly represented"). A *Remark* (p. 390) disambiguates the three uses of "kernel": this RKHS kernel, the linear-algebra kernel/null-space (§2.7.3), and the KDE smoothing kernel (§11.5).

## Connections

- [[d2l-gaussian-processes]] — canonical GP reference.
- [[mml-ch12-classification-svm]] — §12.4 SVM/kernel-machine reference.
- [[KernelTrick]] / [[DualSVM]] / [[SupportVectorMachine]] — the SVM consumers.
- [[GramMatrix]] / [[SymmetricPositiveDefiniteMatrix]] — the PSD validity condition.
- [[GaussianProcess]] — the prior the kernel specifies.
- [[RBFKernel]] / [[MaternKernel]] / [[NeuralNetworkKernel]] / [[OUKernel]] — instances.
- [[KernelTrick]] — the Mercer / weight-space-equivalence machinery.
- [[Stationarity]] — translation-invariance property.
- [[MarginalLikelihood]] — what's optimized to learn kernel hyperparameters.
- [[BayesianLinearRegression]] — finite-feature special case.
- [[NeuralTangentKernel]] — kernel derived from infinite-width gradient-trained NNs.
