---
title: "Generalization"
type: concept
tags: [theory, evaluation]
sources: [d2l-linear-regression, d2l-linear-classification, d2l-multilayer-perceptrons]
last_updated: 2026-05-16
---

# Generalization

A model's ability to perform on unseen data drawn from the same distribution as its training set — the central concern of statistical learning. [[d2l-linear-regression]] §3.6: "This problem — how to discover patterns that *generalize* — is the fundamental problem of machine learning, and arguably of all of statistics."

## Training error vs. generalization error

- **Training error** $R_\text{emp}$: a *statistic* on the training sample, $\frac{1}{n}\sum_i \ell(\mathbf{x}^{(i)}, y^{(i)}, f)$.
- **Generalization error** $R$: an *expectation* under the true distribution $P(X,Y)$, $\mathbb{E}_{(X,Y)\sim P}[\ell(X,Y,f(X))]$.

The latter is unknowable in general (we never see $P$ exactly) — so we estimate it on an independent test set, treating it as a sample-mean problem on a *fixed* classifier. Critical asymmetry: the trained model depends on the training set, so training error is a *biased* estimate of $R$; the test set, withheld until after training, gives an unbiased one.

## The IID assumption

The whole edifice rests on training and test being **IID** from the same distribution. [[d2l-linear-regression]]: "While this assumption is strong, it is worth noting that, absent any such assumption, we would be dead in the water."

## Finite-sample guarantees

Per [[d2l-linear-classification]]'s statistical-learning-theory section: the test error converges to the true error at $\mathcal O(1/\sqrt n)$ by the [[CentralLimitTheorem|central limit theorem]], with stricter finite-sample bounds available via [[HoeffdingsInequality|Hoeffding's inequality]]. ~10k test-set sizes on standard benchmarks ([[FashionMNIST]] / CIFAR-10 / ImageNet validation) are roughly the smallest at which a 1% accuracy difference is statistically credible.

For generalization across the *whole hypothesis class* rather than one fixed classifier, the Vapnik–Chervonenkis program gives [[UniformConvergence|uniform-convergence]] bounds via [[VCDimension|VC dimension]]. The bound is foundational but vacuous for deep networks (which routinely have VC dimension exceeding $n$ yet generalize well) — the modern [[DoubleDescent|double-descent]] phenomenon.

## The modern deep-learning twist

[[d2l-multilayer-perceptrons]] §Generalization in Deep Learning surfaces a different story for over-parametrized networks: they can typically achieve **zero training error** on essentially any dataset (even one with random labels — [[ChiyuanZhang|Zhang]] et al. 2021), so the entire generalization story collapses onto the **gap**, not the training error. Counter-intuitively, *adding* capacity (depth / width / epochs) often *reduces* the gap, producing the [[DoubleDescent|double-descent]] curve. Classical [[VCDimension|VC]] / [[RademacherComplexity|Rademacher]]-based bounds are vacuous in this regime; deep networks behave more like [[InterpolationRegime|interpolating]] nonparametric methods, with the [[NeuralTangentKernel|neural tangent kernel]] formalizing the connection in the infinite-width limit.

## Threats to the IID assumption

The IID assumption fails under [[DistributionShift|distribution shift]]: [[CovariateShift|covariate]], [[LabelShift|label]], and [[ConceptShift|concept shift]] are the three canonical types ([[d2l-linear-classification]]). [[TestSetReuse|Adaptive overfitting]] is a subtler IID failure: repeated test-set evaluation by the same modeler silently leaks information and corrupts the unbiased-estimate property.

## Connections

- [[d2l-linear-regression]] — canonical introduction (§3.6, regression context).
- [[d2l-linear-classification]] — extends generalization theory to classification: Hoeffding bounds, uniform convergence, VC dimension, test-set reuse.
- [[d2l-multilayer-perceptrons]] — the deep-learning twist: interpolation regime, double descent, NTK, why classical bounds fail.
- [[DoubleDescent]] / [[InterpolationRegime]] / [[NeuralTangentKernel]] — modern story.
- [[GeneralizationGap]] — $R - R_\text{emp}$; the diagnostic.
- [[Overfitting]] / [[Underfitting]] — the two failure modes.
- [[ModelSelection]] / [[CrossValidation]] — procedures for honest evaluation.
- [[VCDimension]] / [[NatarajanDimension]] / [[UniformConvergence]] / [[HoeffdingsInequality]] — classical complexity-based bounds and concentration results.
- [[DistributionShift]] / [[CovariateShift]] / [[LabelShift]] / [[ConceptShift]] — what breaks the IID premise.
- [[TestSetReuse]] — adaptive-overfitting failure of the IID test-set assumption.
- [[Regularization]] / [[WeightDecay]] — mitigations for the gap.
- [[HoldoutDataset]] — the test set that estimates $R$.
