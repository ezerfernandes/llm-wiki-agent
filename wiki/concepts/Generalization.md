---
title: "Generalization"
type: concept
tags: [theory, evaluation]
sources: [d2l-linear-regression, d2l-linear-classification, d2l-multilayer-perceptrons, mml-ch01-introduction-and-motivation, mml-ch08-when-models-meet-data]
last_updated: 2026-06-04
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

## From [[mml-ch01-introduction-and-motivation|MML Ch 1]]

*[[mml-book|Mathematics for Machine Learning]]* makes generalization the *goal* of [[Training|training]] from the very first chapter. The aim is "to find good models that generalize well to yet unseen data, which we may care about in the future" (§1, p. 11). Crucially, Ch 1 warns that strong performance on the training set may be *memorization* rather than learning: "Performing well on data that we have already seen (training data) may only mean that we found a good way to memorize the data. However, this may not generalize well to unseen data, and, in practical applications, we often need to expose our machine learning system to situations that it has not encountered before" (§1.1, p. 13). The book's three-bullet summary closes with the same point — we learn "with the aim that the model performs well on data not used for training" (§1.1, p. 13). The honest evaluation set-ups that guard against overly optimistic estimates are deferred to MML Ch 8.

## From [[mml-ch08-when-models-meet-data|MML Ch 8]]

[[mml-ch08-when-models-meet-data|MML Ch 8]] delivers the formal machinery Ch 1 deferred, and the term-for-term correspondence with the [[d2l-linear-regression|D2L]] framing above is exact:

- D2L's **training error** $R_{\text{emp}}$ is MML's [[EmpiricalRisk|empirical risk]] $\mathbf{R}_{\text{emp}}(f,\mathbf{X},\mathbf{y})=\frac1N\sum_n\ell(y_n,\hat y_n)$ (§8.2.2, Eq. 8.6).
- D2L's **generalization error** $R$ is MML's [[ExpectedRisk|expected risk]] $\mathbf{R}_{\text{true}}(f)=\mathbb{E}_{\mathbf{x},y}[\ell(y,f(\mathbf{x}))]$ (§8.2.2, Eq. 8.10), which MML's margin also calls **population risk**.
- The **biased-training-error / unbiased-test-error** asymmetry is MML's §8.2.3 [[Overfitting|overfitting]] diagnostic: the training risk *under-estimates* the expected risk, so a test risk much larger than the training risk signals overfitting.
- The **IID** premise is MML §6.4.5 (used in §8.2.2 to justify the empirical mean and in §8.3.1 to factorize the likelihood).

MML's mitigations are [[Regularization|regularization]] (§8.2.3), priors / [[MAPEstimation|MAP]] (§8.3.2), [[CrossValidation|cross-validation]] (§8.2.4) and [[NestedCrossValidation|nested CV]] / [[ModelSelection|model selection]] (§8.6). The whole "balance fit against simplicity" enterprise is framed philosophically as [[Abduction|abduction]] (§8.1.4).

## Connections

- [[mml-ch08-when-models-meet-data]] — §8.2 makes generalization formal: empirical vs expected risk, overfitting, cross-validation.

- [[mml-ch01-introduction-and-motivation]] — generalization framed as the goal of learning vs. memorization (§1, §1.1).
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
