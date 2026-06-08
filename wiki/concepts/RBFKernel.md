---
title: "RBF / Squared-Exponential Kernel"
type: concept
tags: [kernel-methods, gaussian-processes]
sources: [d2l-gaussian-processes, mml-ch12-classification-svm]
last_updated: 2026-06-05
---

# RBF (Radial Basis Function) / Squared-Exponential Kernel

The most popular [[KernelFunction|covariance function]] for [[GaussianProcess|Gaussian processes]] and kernel machines in general ([[d2l-gaussian-processes]] gp-priors §"The Radial Basis Function (RBF) Kernel"). Also called the **squared-exponential** or **Gaussian** kernel.

$$k_\textrm{RBF}(x,x') = a^2\exp\!\left(-\frac{1}{2\ell^2}\|x-x'\|^2\right)$$

## Hyperparameters

- **Amplitude $a$** — controls the vertical scale of the function (larger $a$ → larger function values).
- **Length-scale $\ell$** — controls the rate of variation. Larger $\ell$ → more slowly varying functions. At $\|x-x'\|=\ell$, covariance is $a^2 e^{-0.5}\approx 0.61 a^2$; beyond a few $\ell$, function values become essentially uncorrelated.

Both hyperparameters are interpretable in the data space and are learned by maximizing the [[MarginalLikelihood]].

## Derivation as an infinite RBF basis

[[d2l-gaussian-processes]] derives the RBF kernel as the $J\to\infty$ Riemann-sum limit of $f(x)=\sum_{i=1}^J w_i\phi_i(x)$ with $w_i\sim\mathcal{N}(0,\sigma^2/J)$ and $\phi_i(x)=\exp(-\tfrac{(x-c_i)^2}{2\ell^2})$:

$$k(x,x')=\lim_{J\to\infty}\frac{\sigma^2}{J}\sum_i\phi_i(x)\phi_i(x') = \int_{-\infty}^\infty \phi_c(x)\phi_c(x')\,dc \propto k_\textrm{RBF}(x,x').$$

A GP with an RBF kernel is therefore a model with an **infinite number of parameters and a finite amount of computation** — and is a [[UniversalApproximator|universal approximator]] over continuous functions. Yet, with a [[MarginalLikelihood|marginal-likelihood]]-controlled prior, it does **not** overfit, even on small data — Wilson's running argument against "all the fuss about overparametrized neural networks."

## Stationarity & translation invariance

RBF is **stationary**: $k(x,x')$ depends only on $\tau=x-x'$, so high-level properties of sample functions (smoothness, amplitude, length-scale) are the same everywhere in input space. This is the canonical [[TranslationInvariance|translation-invariance]] prior for time-series, spatial, and Euclidean data.

## Sample-path smoothness

Sample functions from a GP with RBF kernel are **infinitely differentiable** ($C^\infty$). This is often *too smooth* for physical processes — practitioners frequently prefer the [[MaternKernel|Matérn]] family which interpolates between RBF ($\nu\to\infty$) and exponential / [[OUKernel|Ornstein–Uhlenbeck]] ($\nu=1/2$, continuous-but-non-differentiable).

## From [[mml-ch12-classification-svm|MML Ch 12]] — the kernel-SVM workhorse

[[mml-ch12-classification-svm|MML Ch 12]] §12.4 (p. 389–390) names the **Gaussian radial basis function kernel** as one of the two flagship kernels for the [[SupportVectorMachine|SVM]] (with the polynomial kernel). Its defining property for kernel machines: the corresponding feature space is **infinite-dimensional**, so "we cannot explicitly represent the feature space but can still compute similarities between a pair of examples using the kernel" — the [[KernelTrick|kernel trick]] in its purest form. Plugged into the [[DualSVM|dual SVM]] (replacing $\langle\mathbf{x}_i,\mathbf{x}_j\rangle$ by $k_\text{RBF}(\mathbf{x}_i,\mathbf{x}_j)$), it yields the smoothly nonlinear decision boundaries of Fig. 12.10(b) — while the underlying hypothesis class stays linear (a [[SeparatingHyperplane|separating hyperplane]] in feature space). The kernel and its parameters are typically chosen by nested [[CrossValidation|cross-validation]] (§8.6.1). RBF is a valid kernel because its [[GramMatrix|Gram matrix]] is symmetric positive-semidefinite (Eq. 12.53), the [[SymmetricPositiveDefiniteMatrix|SPD]] condition of §3.2.3.

## Connections

- [[d2l-gaussian-processes]] — gp-priors §RBF and gp-inference (used in every from-scratch example).
- [[mml-ch12-classification-svm]] — §12.4 kernel-SVM reference.
- [[KernelTrick]] / [[DualSVM]] / [[SupportVectorMachine]] — the kernel-SVM consumers.
- [[GaussianProcess]] — the model class.
- [[KernelFunction]] — the family it belongs to.
- [[MaternKernel]] — the standard alternative when RBF is too smooth.
- [[KernelTrick]] — RBF as the canonical infinite-dimensional-feature-map kernel.
- [[MarginalLikelihood]] — what learns its hyperparameters.
- [[BayesianLinearRegression]] — finite-RBF-basis precursor.
- [[UniversalApproximationTheorem]] — RBF-GP is a universal approximator over continuous functions.
- [[GPyTorch]] — `gpytorch.kernels.RBFKernel()`; canonical default kernel.
