---
title: "Regularization"
type: concept
tags: [training, theory]
sources: [madewithml-training, d2l-linear-regression, d2l-multilayer-perceptrons, mml-ch08-when-models-meet-data, mml-ch09-linear-regression]
last_updated: 2026-06-04
---

# Regularization

Techniques that constrain [[ModelComplexity]] to combat [[Overfitting]]: $\ell_1$ / $\ell_2$ penalties, [[Dropout]], early stopping, data augmentation. Trades a small training-loss increase for better generalization.

[[d2l-linear-regression]] §3.7 introduces **[[WeightDecay|weight decay]]** ($\ell_2$ regularization) as "the first practical regularization technique," motivated by the heuristic that "among all functions $f$, the function $f = 0$ is in some sense the *simplest*, and that we can measure the complexity of a function by the distance of its parameters from zero." Replaces the original objective (minimize prediction loss) with the augmented objective (minimize prediction loss + penalty term).

## Common penalty / constraint families

- **[[WeightDecay|Weight decay]] ($\ell_2$ / ridge)** — penalize $\|\mathbf{w}\|_2^2$; spreads weight across features; standard default.
- **[[Lasso|Lasso]] ($\ell_1$)** — penalize $\|\mathbf{w}\|_1$; performs feature selection by zeroing small weights.
- **[[Dropout]]** — randomly zero activations during training.
- **Early stopping** — halt training when validation loss plateaus.
- **Data augmentation** — synthetic perturbations of training examples.

## From [[mml-ch08-when-models-meet-data|MML Ch 8]]

[[mml-ch08-when-models-meet-data|MML Ch 8]] §8.2.3 introduces regularization as the **third design choice** in [[EmpiricalRiskMinimization|ERM]] — "an addition to empirical risk minimization that allows it to generalize well (approximately minimizing [[ExpectedRisk|expected risk]])." It is a **penalty term** that "makes it harder for the optimizer to return an overly flexible predictor … a way to compromise between accurate solution of empirical risk minimization and the size or complexity of the solution." The worked form is **regularized least squares** (Example 8.3, Eq. 8.12):

$$\min_{\boldsymbol\theta}\;\frac1N\|\mathbf{y}-\mathbf{X}\boldsymbol\theta\|^2+\lambda\|\boldsymbol\theta\|^2,$$

where $\|\boldsymbol\theta\|^2$ is the **regularizer** and $\lambda$ the **regularization parameter** — trading training loss against parameter magnitude (which grows under [[Overfitting|overfitting]], Bishop 2006). MML names the deep connection that ties §8.2 to §8.3: **"the idea of regularization also appears in probabilistic models as the prior probability of the parameters"** — i.e. regularization is to ERM what the [[Prior|prior]] is to [[MAPEstimation|MAP]] (a Gaussian prior ⇔ $\ell_2$/ridge, $\lambda\propto 1/\sigma_0^2$). §8.2.5 identifies the form shown as **Tikhonov regularization** (roots in ill-posed inverse problems, Neumaier 1998), related to the bias–variance trade-off and feature selection; and in Ch 12 "the idea of the regularizer is equivalent to the idea of a large margin" ([[SupportVectorMachine|SVM]]).

## From [[mml-ch09-linear-regression|MML Ch 9]]

[[mml-ch09-linear-regression|MML Ch 9]] §9.2.4 gives the worked **regularized least squares** loss $\|\mathbf{y}-\boldsymbol\Phi\boldsymbol\theta\|^2+\lambda\|\boldsymbol\theta\|_2^2$ (Eq. 9.32): a **data-fit / misfit term** (∝ the negative log-likelihood) plus a **regularizer** with strength $\lambda\geq 0$. The crux of the chapter's regularizer↔prior identity is made explicit: $\lambda\|\boldsymbol\theta\|_2^2$ **is** a negative-log Gaussian prior — with $p(\boldsymbol\theta)=\mathcal{N}(\mathbf{0},b^2\mathbf{I})$, $-\log p(\boldsymbol\theta)=\frac{1}{2b^2}\|\boldsymbol\theta\|_2^2+\text{const}$ (Eq. 9.33), so the RLS solution $(\boldsymbol\Phi^\top\boldsymbol\Phi+\lambda\mathbf{I})^{-1}\boldsymbol\Phi^\top\mathbf{y}$ (Eq. 9.34) **equals the [[MAPEstimation|MAP]] estimate** (Eq. 9.31) at $\lambda=\frac{\sigma^2}{b^2}$ — i.e. [[RidgeRegression|ridge regression]]. A general $p$-norm with smaller $p$ gives sparser solutions; $p=1$ is **[[Lasso|LASSO]]** (Tibshirani 1996) for variable selection (§9.5: a Laplace prior, useful when $N\ll D$). The regularizer also guarantees invertibility of $\boldsymbol\Phi^\top\boldsymbol\Phi+\lambda\mathbf{I}$ even in the underdetermined regime.

## Connections

- [[mml-ch09-linear-regression]] — §9.2.4 regularized least squares = ridge = Gaussian-prior MAP (Eqs. 9.32–9.34).
- [[mml-ch08-when-models-meet-data]] — §8.2.3 canonical reference (Eq. 8.12, Tikhonov); the prior ⇔ regularizer link.

- [[d2l-linear-regression]] — §3.7 canonical reference (introduces weight decay).
- [[d2l-multilayer-perceptrons]] — deep-learning angle: [[Dropout]], [[EarlyStopping]], and the caveat that classical regularizers don't actually constrain capacity in the [[InterpolationRegime|interpolation regime]].
- [[WeightDecay]] / [[RidgeRegression]] — $\ell_2$ form.
- [[Lasso]] — $\ell_1$ form.
- [[Overfitting]] — what regularization combats.
- [[Underfitting]] — what too-strong regularization causes.
- [[ModelSelection]] / [[CrossValidation]] — how the regularization strength $\lambda$ is chosen.
- [[MAPEstimation]] / [[BayesianLinearRegression]] — Bayesian interpretation of regularization as prior.
