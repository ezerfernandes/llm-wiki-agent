---
title: "Dive into Deep Learning — Gaussian Processes"
type: source
tags: [textbook, d2l, gaussian-processes, bayesian, kernel-methods, uncertainty]
date: 2026-05-16
source_file: raw/d2l-en/chapter_gaussian-processes/
---

## Summary

[[AndrewGordonWilson|Wilson]] ([[NewYorkUniversity|NYU]] / [[amazon|Amazon]])'s guest three-section [[d2l-preface|D2L]] chapter on **[[GaussianProcess|Gaussian processes (GPs)]]** — the canonical *function-space* approach to Bayesian regression. Defines a GP as *"a collection of random variables, any finite number of which have a joint Gaussian distribution"*; specifies the prior by mean + [[KernelFunction|kernel]] (covariance) function; derives the [[RBFKernel|RBF kernel]] from an infinite-basis Bayesian linear regression and the [[NeuralNetworkKernel|neural-network kernel]] from a one-hidden-layer Bayesian NN at infinite width ([[RadfordNeal|Neal]] 1996, a precursor to [[NeuralTangentKernel|NTK]]); gives the **closed-form Gaussian posterior** for GP regression and the [[MarginalLikelihood|marginal-likelihood]] hyperparameter-learning objective. Flags **$\mathcal{O}(n^3)$ Cholesky / log-det** as the scaling bottleneck (≈10k training points without scalable inference) and introduces [[GPyTorch]] ([[JacobGardner|Gardner]] et al. 2018) as the [[PyTorch]]-integrated production library. Wilson's running thesis: GPs and deep neural networks are **complementary, not competing** — *"there is a running joke that 'everything is a special case of a Gaussian process'"*.

## Key Claims

- **Definition.** A Gaussian process is a collection of random variables such that any finite subset has a joint multivariate Gaussian distribution. Written $f(x)\sim\mathcal{GP}(m,k)$ with mean function $m(x)=\mathbb{E}[f(x)]$ and [[KernelFunction|kernel]] $k(x,x')=\textrm{Cov}(f(x),f(x'))$ — the two-moment GP specification.
- **Prior over functions = weight-space lifted.** Any model $f(x)=w^\top\phi(x)$ with Gaussian $w\sim\mathcal{N}(u,S)$ is a GP with $m(x)=u^\top\phi(x)$ and $k(x,x')=\phi(x)^\top S\phi(x')$ — recovering polynomials, Fourier series, [[BayesianLinearRegression]], and (via [[RadfordNeal|Neal 1996]]) infinite-width Bayesian neural networks as special cases.
- **[[RBFKernel|RBF / squared-exponential kernel]].** $k_\textrm{RBF}(x,x')=a^2\exp(-\tfrac{1}{2\ell^2}\|x-x'\|^2)$ has two interpretable [[Hyperparameter|hyperparameters]] — *amplitude* $a$ (vertical scale) and *length-scale* $\ell$ (rate of variation). Derivable as the $J\to\infty$ Riemann-sum limit of $J$ Gaussian basis functions with shrinking weight variance — a GP with an RBF kernel is a [[UniversalApproximator|universal approximator]] with a (controlled) infinite-parameter prior.
- **Neural-network kernel (Neal 1996 / NTK lineage).** A one-hidden-layer Bayesian NN $f(x)=b+\sum_i v_i h(x;u_i)$ with i.i.d. weight priors becomes a GP at infinite hidden width by the central limit theorem; for $h=\textrm{erf}$, the kernel has a closed-form $\arcsin$/$\sin$ expression. Foreshadows [[NeuralTangentKernel|NTK]] ([[ArthurJacot|Jacot]] et al. 2018) — *"Neural networks are not as distinct as we make them out to be."*
- **[[Stationarity|Stationary]] vs non-stationary kernels.** [[RBFKernel|RBF]] is stationary ($k(x,x')$ depends only on $\tau=x-x'$ — translation-invariant); the NN kernel is non-stationary (looks qualitatively different near the origin) — kernel choice encodes prior assumptions about *how* function properties vary across input space.
- **GP regression posterior — closed form.** Under additive [[GaussianNoise|i.i.d. Gaussian noise]] $\epsilon\sim\mathcal{N}(0,\sigma^2)$, the joint $(\mathbf{y},\mathbf{f}_*)$ is Gaussian, so $\mathbf{f}_*\mid\mathbf{y}\sim\mathcal{N}(m_*,S_*)$ with $m_*=K(X_*,X)[K(X,X)+\sigma^2 I]^{-1}\mathbf{y}$ and $S_*=K(X_*,X_*)-K(X_*,X)[K(X,X)+\sigma^2 I]^{-1}K(X,X_*)$. *"Despite the flexibility of the model class, it is possible to do exact Bayesian inference for GP regression in closed form."*
- **[[MarginalLikelihood|Marginal likelihood]] for hyperparameter learning.** $\log p(\mathbf{y}\mid\theta,X)=-\tfrac{1}{2}\mathbf{y}^\top[K_\theta+\sigma^2 I]^{-1}\mathbf{y}-\tfrac{1}{2}\log|K_\theta+\sigma^2 I|+c$ decomposes into a data-fit term and a model-complexity log-det term — automatically encoding [[OccamsRazor|Occam's razor]] for $\theta=\{a^2,\ell^2,\sigma^2\}$. The single biggest contribution of ML to GP research before scalable inference.
- **Two sources of uncertainty.** *[[EpistemicUncertainty|Epistemic]]* (reducible — what the GP knows about $f$, captured by $\textrm{diag}(S_*)$) grows away from data; *[[AleatoricUncertainty|aleatoric]]* (irreducible observation noise $\sigma^2$) does not. A 95% credible set is $m_*\pm 2\sqrt{\textrm{diag}(S_*)}$ on the latent function vs $m_*\pm 2\sqrt{\textrm{diag}(S_*)+\sigma^2}$ on observations. *"Without being precise about what the uncertainty represents, it is essentially meaningless."*
- **$\mathcal{O}(n^3)$ scaling bottleneck.** Posterior mean / variance / marginal likelihood all require solving an $n\times n$ linear system and computing $\log|K+\sigma^2 I|$ — naive $\mathcal{O}(n^3)$ compute + $\mathcal{O}(n^2)$ storage via [[CholeskyDecomposition|Cholesky]]. Historically capped GPs at ~10k training points; scalable inference techniques ([[InducingPoint|inducing points]], [[SKI|KISS-GP]]) push this to millions. Adding diagonal $\sigma^2 I$ (or $\sim 10^{-6}$ "jitter" for noise-free) conditions the matrix.
- **Predictive mean is a linear smoother.** $a_*=k_\theta(x_*,X)[K_\theta(X,X)+\sigma^2 I]^{-1}(\mathbf{y}-\boldsymbol\mu)+\mu$ — a linear combination of training targets weighted by the kernel. The kernel (not the training labels) controls predictive variance; uncertainty grows with distance from training points in the kernel-induced metric.
- **[[GPyTorch]] for production.** Wilson's group's [[PyTorch]]-integrated library makes kernel swapping (RBF / [[MaternKernel|Matérn]] / [[SpectralMixtureKernel|spectral mixture]]) a one-line change, supports [[ExactGP|exact]] and approximate inference, scales to >10k points via SKI / KISS-GP, and uses [[Adam]] on the negative marginal log-likelihood as the standard training loop. Wilson estimates "almost a decade" of unfairly persistent "GPs are slow" reputation.

## Key Quotes

> "A Gaussian process is defined as a collection of random variables, any finite number of which have a joint Gaussian distribution." — gp-priors, the canonical definition

> "There is a running joke that 'everything is a special case of a Gaussian process'." — gp-intro, the wider thesis: random walks, AR processes, Bayesian linear regression, polynomials, Fourier series, RBF networks, and infinite-width neural networks are all GPs

> "A Gaussian process with an RBF kernel is a universal approximator, capable of representing any continuous function to arbitrary precision … Perhaps all the fuss about overparametrized neural networks is misplaced." — gp-priors

> "Despite the flexibility of the model class, it is possible to do exact Bayesian inference for GP regression in closed form. Aside from learning the kernel hyperparameters, there is no training." — gp-inference, the structural property that distinguishes GP regression from every other deep-learning workflow in D2L

> "Without being precise about what the uncertainty represents, it is essentially meaningless." — gp-inference, on the routine conflation of epistemic / aleatoric / variance / standard-error / credible-set / confidence-interval in published ML work

> "These bottlenecks have limited GPs to problems with fewer than about 10,000 training points, and have given GPs a reputation for 'being slow' that has been inaccurate now for almost a decade." — gp-inference, on the $\mathcal{O}(n^3)$ Cholesky and the scalable-inference response

## Connections

- [[d2l-preface]] — parent textbook; this is the second-to-last chapter of the **modeling** layer (the [[d2l-reinforcement-learning|RL chapter]] is the formal closer).
- [[AndrewGordonWilson]] — chapter author; NYU / Amazon; co-author of [[GPyTorch]]; published [[rasmussen-williams-gpml|Rasmussen & Williams (2006)]]-successor work on scalable GPs.
- [[NewYorkUniversity]] — Wilson's home institution.
- [[GaussianProcess]] — the central concept; this chapter is the wiki's canonical reference.
- [[KernelFunction]] — what specifies a GP prior beyond the mean function.
- [[RBFKernel]] — the canonical stationary kernel; derived two ways (infinite RBF basis + as the implicit feature map of an infinite-width MLP).
- [[MaternKernel]] — flagged as an alternative kernel (`gpytorch.kernels.matern_kernel()`); GPyTorch one-line swap.
- [[MarginalLikelihood]] — the hyperparameter-learning objective; encodes Occam's razor via the log-det term.
- [[BayesianLinearRegression]] — the *weight-space* counterpart that GPs lift to function space.
- [[GaussianDistribution]] — the closure-under-conditioning property that makes GP posteriors closed-form.
- [[NeuralTangentKernel]] — the modern reincarnation of [[RadfordNeal|Neal's]] 1996 infinite-width-NN-as-GP correspondence; D2L's gp-priors §"Neural Network Kernel" is the textbook bridge.
- [[CholeskyDecomposition]] — the $\mathcal{O}(n^3)$ primitive underneath the $[K+\sigma^2 I]^{-1}$ solve and $\log|K+\sigma^2 I|$.
- [[EpistemicUncertainty]] / [[AleatoricUncertainty]] — the two-component uncertainty decomposition GPs make explicit.
- [[KernelTrick]] — GPs are *exactly* the kernelized version of Bayesian linear regression.
- [[BayesianOptimization]] — flagged as a state-of-the-art GP application (acquisition functions over the GP posterior).
- [[ActiveLearning]] — flagged as a canonical GP application (predictive variance as acquisition signal).
- [[GPyTorch]] — Wilson's group's PyTorch-integrated production library; SKI / KISS-GP scaling.
- [[PyTorch]] — the framework GPyTorch builds on.
- [[Adam]] — the marginal-likelihood optimizer in the GPyTorch example (with full-batch caveat — marginal likelihood does not factorize over data).

## Contradictions

- *No direct contradiction.* The chapter's claim that "Bayesian methods naturally represent epistemic uncertainty" is consistent with [[mml-book]] §9.3 ([[BayesianLinearRegression]]) and [[islr-seventh-printing|ISLR]]'s prediction/inference framing. The position that GPs *complement* (not compete with) deep neural networks is consonant with [[d2l-multilayer-perceptrons]]'s [[NeuralTangentKernel|NTK]] paragraph — both chapters argue infinite-width networks become kernel methods.
- *Mild productive tension* with [[d2l-optimization]]'s default of mini-batch SGD: GP marginal-likelihood optimization does **not** factorize over data, so full-batch optimizers ([[Adam]] full-batch or L-BFGS) are required — a counter-example to D2L's elsewhere-universal "minibatch SGD is the universal DL optimizer" assertion in [[d2l-linear-regression]].
