---
title: "Maximum Likelihood Estimation"
type: concept
tags: [foundational, statistics, estimation]
sources: [pml1-murphy, mml-book, d2l-linear-regression, d2l-linear-classification, d2l-appendix-mathematics]
last_updated: 2026-05-16
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

## Connections

- [[pml1-murphy]] — §1.2.1.6.
- [[mml-book]] — §8.3, §9.2, §11 canonical references.
- [[EmpiricalRiskMinimization]] — MLE is ERM with NLL.
- [[MAPEstimation]] — MLE with an additional log-prior term.
- [[BayesianLinearRegression]] — full Bayesian alternative.
- [[ProbabilisticPerspective]] — MLE is the workhorse under flat priors.
- [[EMAlgorithm]] — iterative scheme for MLE under latent variables.
- [[ScalingLaws]] — pretraining loss in [[2001.08361-scaling-laws]] is MLE NLL.
