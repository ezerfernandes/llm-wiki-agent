---
title: "Maximum Likelihood Estimation"
type: concept
tags: [foundational, statistics, estimation]
sources: [pml1-murphy, mml-book, mml-ch08-when-models-meet-data, mml-ch09-linear-regression, mml-ch11-density-estimation-gmm, d2l-linear-regression, d2l-linear-classification, d2l-appendix-mathematics]
last_updated: 2026-06-05
---

# Maximum Likelihood Estimation (MLE)

Pick parameters that maximize the probability the model assigns to the observed training data. Equivalently — and computationally more convenient — minimize the **negative log-likelihood (NLL)**:

$$
\hat{\boldsymbol\theta}_{\text{MLE}} = \arg\max_{\boldsymbol\theta}\;\prod_{n=1}^N p(y_n|f(\mathbf{x}_n;\boldsymbol\theta)) = \arg\min_{\boldsymbol\theta}\;\underbrace{-\frac{1}{N}\sum_{n=1}^N \log p(y_n|f(\mathbf{x}_n;\boldsymbol\theta))}_{\text{NLL}(\boldsymbol\theta)}
$$

[[pml1-murphy]] §1.2.1.6: MLE is [[EmpiricalRiskMinimization|ERM]] with the negative-log-probability loss. It is the bridge between probabilistic modeling and optimization.

## Why MLE = MSE for Gaussian regression

Under $p(y|\mathbf{x};\boldsymbol\theta) = \mathcal{N}(y\,|\,f(\mathbf{x};\boldsymbol\theta), \sigma^2)$ with fixed $\sigma^2$:

$$
\text{NLL}(\boldsymbol\theta) = \frac{1}{2\sigma^2}\text{MSE}(\boldsymbol\theta) + \text{const}
$$

so $\arg\min_{\boldsymbol\theta}\text{NLL} = \arg\min_{\boldsymbol\theta}\text{MSE}$. Least squares is MLE under fixed-variance Gaussian noise. (Murphy §1.2.2.)

## Why MLE = cross-entropy for classification

Under $p(y=c|\mathbf{x};\boldsymbol\theta) = \text{softmax}_c(f(\mathbf{x};\boldsymbol\theta))$, the per-example NLL is the cross-entropy between the one-hot label and the softmax distribution. Hence "training a classifier with cross-entropy loss" *is* MLE under a categorical likelihood.

## Limitations and Bayesian alternatives

MLE is a point estimate — it ignores epistemic uncertainty in $\boldsymbol\theta$. In small-data or safety-critical regimes the book (Ch 4.5, Ch 5.2) prefers MAP estimation (with a prior) or full Bayesian inference (a posterior over $\boldsymbol\theta$). Most LLM pretraining today is still MLE at scale because data is plentiful and posteriors are intractable.

## Role in this wiki

- Underlies *every* generative language model: the LM loss $-\log p(\mathbf{x}_t|\mathbf{x}_{<t})$ is the MLE objective. Papers in Corpus II — [[1706.03762-attention-is-all-you-need]], [[1810.04805-bert]], [[1910.10683-t5]], [[2001.08361-scaling-laws]] — are all training Transformers via NLL minimization.
- The [[ScalingLaws]] power-law fit in [[2001.08361-scaling-laws]] is a fit to MLE loss as a function of $N$, $D$, $C$.
- [[2601.21343-self-improving-pretraining]] modifies *what data* MLE is computed over via a teacher rewriter, not the objective itself.

## Cross-reference: [[mml-book]]

[[mml-book]] §8.3 introduces MLE in parallel with Murphy and Ch 9 then derives the linear-regression closed form $\boldsymbol\theta_{\text{ML}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$ explicitly as the gradient-zero solution to Gaussian NLL (§9.2.1, Eq. 9.12c). [[mml-book]] §11 then exhibits the *failure case* — GMM MLE has no closed form (p. 351), which motivates the [[EMAlgorithm]] as the iterative work-around.

## From [[mml-ch08-when-models-meet-data|MML Ch 8]]

[[mml-ch08-when-models-meet-data|MML Ch 8]] §8.3.1 defines MLE as **minimizing the [[NegativeLogLikelihood|negative log-likelihood]]** $\mathcal{L}(\boldsymbol\theta)=-\log p(\mathbf{x}\,|\,\boldsymbol\theta)$ (Eq. 8.14) — the subscript-$\mathbf{x}$ notation $\mathcal{L}_{\mathbf{x}}(\boldsymbol\theta)$ stresses that the data are fixed and $\boldsymbol\theta$ varies. Under the [[IID|i.i.d.]] assumption the data likelihood factorizes (Eq. 8.16), so the NLL becomes a sum $\mathcal{L}(\boldsymbol\theta)=-\sum_{n}\log p(y_n\,|\,\mathbf{x}_n,\boldsymbol\theta)$ (Eq. 8.17) — easier to optimize. The **negative sign is a "historical artifact"** (we want to maximize likelihood, but optimization minimizes), which is precisely what makes MLE an [[EmpiricalRiskMinimization|ERM]] instance with the NLL as its [[LossFunction|loss]]. For a Gaussian likelihood, the NLL reduces to the least-squares objective (Example 8.5, Eqs. 8.18a–d).

The chapter frames MLE within its three-way analogy: **the likelihood is to MLE what the loss function is to ERM** (§8.3 intro). MLE's **small-data failure mode is overfitting** (§8.3.2 Remark, p. 270); its properties are asymptotic consistency, $1/N$ error-variance decay, and the need for potentially large samples (Lehmann & Casella 1998). MLE is **frequentist** (originally Fisher); adding a [[Prior|prior]] gives [[MAPEstimation|MAP]] (the probabilistic regularizer), and treating $\boldsymbol\theta$ as a full random variable gives [[BayesianInference|Bayesian inference]] (§8.4).

## From [[mml-ch09-linear-regression|MML Ch 9]]

[[mml-ch09-linear-regression|MML Ch 9]] §9.2.1 is the **worked closed-form MLE** for linear regression. The likelihood factorizes over the i.i.d. data (Eq. 9.5); the log-transform (avoiding underflow over a product of $N$ probabilities like $10^{-256}$, and turning the product into a sum of per-example gradients) reduces the Gaussian NLL to least squares $\mathcal{L}(\boldsymbol\theta)=\frac{1}{2\sigma^2}\|\mathbf{y}-\mathbf{X}\boldsymbol\theta\|^2$ (Eqs. 9.8–9.10). The **row-vector gradient** $\frac{d\mathcal{L}}{d\boldsymbol\theta}\in\mathbb{R}^{1\times D}$ (Eq. 9.11c) set to $\mathbf{0}^\top$ gives the [[NormalEquations|normal equations]] $\boldsymbol\theta_{\text{ML}}=(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$ (Eq. 9.12c) — a **unique global minimum** because the Hessian $\mathbf{X}^\top\mathbf{X}$ is PD (Remark, p. 294). A useful Remark (p. 293): **the likelihood is not a probability distribution in $\boldsymbol\theta$** (unnormalized, possibly non-integrable in $\boldsymbol\theta$), only in $\mathbf{y}$. MLE also estimates the noise variance: $\sigma^2_{\text{ML}}=\frac1N\sum_n(y_n-\boldsymbol\phi^\top(\mathbf{x}_n)\boldsymbol\theta)^2$ (Eq. 9.22). Its overfitting (large parameter magnitudes, high-degree polynomials, §9.2.2) is the concrete motivation for [[MAPEstimation|MAP]] (§9.2.3).

## From [[mml-ch11-density-estimation-gmm|MML Ch 11]] (the no-closed-form failure case)

[[mml-ch11-density-estimation-gmm|MML Ch 11]] is the chapter where MLE **stops being closed-form**. For a [[GaussianMixtureModel|GMM]] the i.i.d. log-likelihood is $\mathcal L(\boldsymbol\theta)=\sum_{n=1}^N\log\sum_{k=1}^K\pi_k\mathcal N(\mathbf x_n\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)$ (Eq. 11.10), and the obstruction is exact and quotable: "we cannot move the log into the sum over $k$ so that we cannot obtain a simple closed-form maximum likelihood solution" (p. 351–352). The contrast with the single-Gaussian case is explicit — there the sum over $k$ vanishes, the $\log$ hits the Gaussian directly (Eq. 11.11), and Ch 8-style closed-form estimates of $\boldsymbol\mu,\boldsymbol\Sigma$ follow. Setting $\partial\mathcal L/\partial\boldsymbol\theta=\mathbf 0$ instead yields **dependent simultaneous equations** coupled through the [[Responsibility|responsibilities]] $r_{nk}$, solvable only iteratively by the [[EMAlgorithm|EM algorithm]] (§11.3) — MLE under [[LatentVariable|latent variables]]. §11.5 also records the **standard MLE criticisms made concrete for GMMs**: overfitting via singularities (a component collapsing onto a single point with $\boldsymbol\Sigma\to\mathbf 0$ sends the likelihood to $+\infty$), and the point-estimate limitation (no parameter uncertainty; a Bayesian treatment would need a prior, but no conjugate prior exists, forcing variational approximations). This is the **density-estimation counterpart** to the closed-form regression MLE of [[mml-ch09-linear-regression|Ch 9]].

## Connections

- [[pml1-murphy]] — §1.2.1.6.
- [[mml-book]] — §8.3, §9.2, §11 canonical references.
- [[mml-ch11-density-estimation-gmm]] — §11.2, the no-closed-form GMM MLE solved by EM.
- [[mml-ch09-linear-regression]] — §9.2.1 closed-form linear-regression MLE (normal equations).
- [[NormalEquations]] / [[LeastSquares]] — the closed-form Gaussian MLE.
- [[EmpiricalRiskMinimization]] — MLE is ERM with NLL.
- [[MAPEstimation]] — MLE with an additional log-prior term.
- [[BayesianLinearRegression]] — full Bayesian alternative.
- [[ProbabilisticPerspective]] — MLE is the workhorse under flat priors.
- [[EMAlgorithm]] — iterative scheme for MLE under latent variables.
- [[ScalingLaws]] — pretraining loss in [[2001.08361-scaling-laws]] is MLE NLL.
