---
title: "Gaussian Process"
type: concept
tags: [bayesian, kernel-methods, regression, uncertainty]
sources: [d2l-gaussian-processes]
last_updated: 2026-05-16
---

# Gaussian Process (GP)

A **distribution over functions**: a collection of random variables $\{f(x)\}$ indexed by inputs $x$ such that any finite subset $(f(x_1),\dots,f(x_n))$ has a joint multivariate Gaussian distribution ([[d2l-gaussian-processes]] gp-priors §Definition; [[AndrewGordonWilson|Wilson]]). Fully specified by:

- a **mean function** $m(x)=\mathbb{E}[f(x)]$ (typically taken as $0$), and
- a **[[KernelFunction|covariance / kernel function]]** $k(x,x')=\textrm{Cov}(f(x),f(x'))$.

Written $f(x)\sim\mathcal{GP}(m,k)$.

## The two-moment specification

For any inputs $X=\{x_1,\dots,x_n\}$, the vector $\mathbf{f}=(f(x_1),\dots,f(x_n))^\top$ is distributed as $\mathcal{N}(\boldsymbol\mu,K)$ where $\mu_i=m(x_i)$ and $K_{ij}=k(x_i,x_j)$. Because Gaussians are closed under [[Marginalization|marginalization]] and conditioning ([[GaussianDistribution]]), every finite-dimensional projection of a GP — and every conditional given observed values — is again Gaussian.

## Regression posterior — closed form

Under additive [[GaussianNoise|i.i.d. Gaussian noise]] $\epsilon\sim\mathcal{N}(0,\sigma^2)$, observing $\mathbf{y}=\mathbf{f}+\boldsymbol\epsilon$ at $X$ and predicting at $X_*$ gives the joint Gaussian

$$\begin{bmatrix}\mathbf{y}\\\mathbf{f}_*\end{bmatrix}\sim\mathcal{N}\!\left(0,\begin{bmatrix}K(X,X)+\sigma^2 I&K(X,X_*)\\K(X_*,X)&K(X_*,X_*)\end{bmatrix}\right)$$

so that $\mathbf{f}_*\mid\mathbf{y}\sim\mathcal{N}(m_*,S_*)$ with

$$m_*=K(X_*,X)[K(X,X)+\sigma^2 I]^{-1}\mathbf{y}$$

$$S_*=K(X_*,X_*)-K(X_*,X)[K(X,X)+\sigma^2 I]^{-1}K(X,X_*).$$

*"Despite the flexibility of the model class, it is possible to do exact Bayesian inference for GP regression in closed form. Aside from learning the kernel hyperparameters, there is no training."* ([[d2l-gaussian-processes]] gp-inference)

## Weight-space ↔ function-space equivalence

Any $f(x)=w^\top\phi(x)$ with $w\sim\mathcal{N}(u,S)$ is a GP with $m(x)=u^\top\phi(x)$, $k(x,x')=\phi(x)^\top S\phi(x')$. This contains:

- [[BayesianLinearRegression]] (finite $\phi$),
- polynomials, Fourier series, RBF networks ([[BasisFunctions]]),
- Bayesian neural networks at **infinite hidden width** ([[RadfordNeal|Neal 1996]]; the precursor to [[NeuralTangentKernel|NTK]]).

Hence Wilson's running joke: *"everything is a special case of a Gaussian process."*

## Two sources of uncertainty

- **[[EpistemicUncertainty|Epistemic]]** (reducible) — $\textrm{diag}(S_*)$; grows away from training data, shrinks with more data.
- **[[AleatoricUncertainty|Aleatoric]]** (irreducible) — observation noise $\sigma^2$; persists no matter how much data is collected.

A 95% credible set for the *latent function* is $m_*\pm 2\sqrt{\textrm{diag}(S_*)}$; for *observations* it's $m_*\pm 2\sqrt{\textrm{diag}(S_*)+\sigma^2}$.

## The $\mathcal{O}(n^3)$ bottleneck

The posterior mean, variance, and [[MarginalLikelihood|marginal likelihood]] all require solving $[K+\sigma^2 I]^{-1}\mathbf{y}$ and computing $\log|K+\sigma^2 I|$ — naive $\mathcal{O}(n^3)$ via [[CholeskyDecomposition|Cholesky]] with $\mathcal{O}(n^2)$ storage. Historically caps exact GPs at $\sim 10^4$ training points. Scalable inference ([[InducingPoint|inducing points]], [[SKI|KISS-GP]] / [[GPyTorch]]) pushes this to millions.

## Connections

- [[d2l-gaussian-processes]] — canonical D2L reference; [[AndrewGordonWilson|Wilson]] is the chapter author.
- [[KernelFunction]] — what specifies the GP prior beyond the mean.
- [[RBFKernel]] / [[MaternKernel]] / [[NeuralNetworkKernel]] — popular kernel choices.
- [[MarginalLikelihood]] — the hyperparameter-learning objective.
- [[BayesianLinearRegression]] — the weight-space special case; GPs are its kernelized form.
- [[GaussianDistribution]] — the underlying closure-under-conditioning machinery.
- [[NeuralTangentKernel]] — the infinite-width-NN-as-GP correspondence.
- [[KernelTrick]] — GPs are exactly kernelized [[BayesianLinearRegression]].
- [[CholeskyDecomposition]] — the inner numerical primitive.
- [[EpistemicUncertainty]] / [[AleatoricUncertainty]] — the two-component uncertainty decomposition GPs make explicit.
- [[GPyTorch]] — the production-grade scalable-GP library.
- [[BayesianOptimization]] — the canonical downstream application.
