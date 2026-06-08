---
title: "Latent Variable"
type: concept
tags: [probabilistic-modeling, foundational, latent-variable-models]
sources: [mml-ch08-when-models-meet-data, mml-book, mml-ch10-dimensionality-reduction-pca, mml-ch11-density-estimation-gmm]
last_updated: 2026-06-05
---

# Latent Variable

An **unobserved random variable $\mathbf{z}$** included in a probabilistic model in addition to the model parameters $\boldsymbol\theta$ ([[mml-book]] §8.4.3, p. 275). Crucially, latent variables are *distinct from parameters*: they do **not** parametrize the model explicitly. They may describe the data-generating process (aiding interpretability), and they "often simplify the structure of the model and allow us to define simpler and richer model structures" — typically with *fewer* parameters.

## The generative process and the marginalized likelihood

Denoting data $\mathbf{x}$, parameters $\boldsymbol\theta$, latents $\mathbf{z}$, the model gives the conditional $p(\mathbf{x}\,|\,\mathbf{z},\boldsymbol\theta)$ (Eq. 8.24) with a prior $p(\mathbf{z})$ on the latents. The key two-step move: **marginalize out the latents to get a likelihood that depends only on the data and the parameters** (Eq. 8.25):

$$p(\mathbf{x}\,|\,\boldsymbol\theta)=\int p(\mathbf{x}\,|\,\mathbf{z},\boldsymbol\theta)\,p(\mathbf{z})\,d\mathbf{z}.$$

This likelihood then feeds [[MaximumLikelihoodEstimation|MLE]], [[MAPEstimation|MAP]], or [[BayesianInference|Bayesian inference]] exactly as in the no-latent case — yielding a parameter posterior $p(\boldsymbol\theta\,|\,\mathcal{X})$ (Eq. 8.26).

## Posteriors over latents

One can also compute a **latent posterior** $p(\mathbf{z}\,|\,\mathcal{X})$ (Eq. 8.27), but marginalizing out *both* $\mathbf{z}$ and $\boldsymbol\theta$ at once is generally impossible. The tractable object is the latent posterior **conditioned on the parameters** (Eq. 8.28):

$$p(\mathbf{z}\,|\,\mathcal{X},\boldsymbol\theta)=\frac{p(\mathcal{X}\,|\,\mathbf{z},\boldsymbol\theta)\,p(\mathbf{z})}{p(\mathcal{X}\,|\,\boldsymbol\theta)}.$$

computed explicitly for PCA and GMMs in Chs 10–11.

## The headline examples

- **[[PrincipalComponentAnalysis|PCA]]** (Ch 10) — dimensionality reduction; the low-dimensional code is latent.
- **[[GaussianMixtureModel|Gaussian mixture models]]** (Ch 11) — the cluster assignment is latent; MLE has **no closed form**, solved by the [[EMAlgorithm|EM algorithm]].
- **Hidden Markov models** / dynamical systems — time-series modeling.

Learning in latent-variable models is *generally hard* (Ch 11); MLE is done principledly via **expectation maximization** (Dempster et al. 1977).

## From [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] (PPCA as the continuous-latent example)

[[mml-ch10-dimensionality-reduction-pca|MML §10.7]] instantiates the §8.4.3 machinery with a **continuous** latent $\mathbf z\in\mathbb R^M$: [[ProbabilisticPCA|probabilistic PCA]] sets $\mathbf z\sim\mathcal N(\mathbf 0,\mathbf I)$ and $\mathbf x=\mathbf B\mathbf z+\boldsymbol\mu+\boldsymbol\epsilon$ (Eq. 10.63). The marginalized likelihood $p(\mathbf x\mid\mathbf B,\boldsymbol\mu,\sigma^2)=\int\mathcal N(\mathbf x\mid\mathbf B\mathbf z+\boldsymbol\mu,\sigma^2\mathbf I)\mathcal N(\mathbf z\mid\mathbf 0,\mathbf I)\,d\mathbf z=\mathcal N(\mathbf x\mid\boldsymbol\mu,\mathbf B\mathbf B^\top+\sigma^2\mathbf I)$ (Eq. 10.68) is the §8.4.3 "integrate out $\mathbf z$" move made concrete — and the chapter is explicit (Remark, p. 342) that the conditional $p(\mathbf x\mid\mathbf z,\dots)$ **cannot** be used for MLE because "it still depends on the latent variables." The latent posterior $p(\mathbf z\mid\mathbf x)=\mathcal N(\mathbf z\mid\mathbf m,\mathbf C)$ (Eqs. 10.74–10.75) is computed in closed form via Gaussian conditioning — the rare tractable case where the latent posterior given parameters is exact. The directed graphical model (Fig. 10.14) draws $\mathbf z$ as the unshaded cause of the shaded observation $\mathbf x$. This is the **continuous-latent counterpart** to the discrete cluster-assignment latent of the Ch 11 GMM.

## From [[mml-ch11-density-estimation-gmm|MML Ch 11]] (the discrete-latent example)

[[mml-ch11-density-estimation-gmm|MML §11.4]] instantiates the §8.4.3 machinery with a **discrete** latent that "can attain only a finite set of values" — explicitly contrasted with PCA's continuous $\mathbf z\in\mathbb R^M$ (p. 363). The latent is a **binary indicator** $z_k\in\{0,1\}$ collected into a **one-hot / 1-of-$K$ vector** $\mathbf z=[z_1,\dots,z_K]^\top$ with $\sum_k z_k=1$ (Eqs. 11.58, p. 364), with conditional $p(\mathbf x\mid z_k=1)=\mathcal N(\mathbf x\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)$. The prior $p(\mathbf z)=\boldsymbol\pi$ makes the [[MixtureWeight|mixture weight]] $\pi_k=p(z_k=1)$ the prior probability that component $k$ generated a point (Eqs. 11.59–11.60). **Marginalizing out $\mathbf z$** (now a finite sum over the $K$ one-hot configurations, the discrete analogue of PPCA's integral) recovers exactly the [[GaussianMixtureModel|GMM]] density $\sum_k\pi_k\mathcal N(\boldsymbol\mu_k,\boldsymbol\Sigma_k)$ (Eqs. 11.63–11.66b) — "an equivalent way of thinking about a Gaussian mixture model" (p. 366). The latent posterior $p(z_{nk}=1\mid\mathbf x_n)$ computed by Bayes' theorem (§11.4.3, Eqs. 11.68–11.72b) is **exactly the [[Responsibility|responsibility]] $r_{nk}$**, which is what gives EM its principled derivation as maximizing the expected complete-data log-likelihood (§11.4.5). **Generative process**: ancestral sampling — pick a component via $\mathbf z\sim p(\mathbf z)$, then draw $\mathbf x$ from it (Fig. 11.11). This is the **discrete-latent counterpart** to the continuous-latent PPCA of [[mml-ch10-dimensionality-reduction-pca|Ch 10]].

## $\mathbf{z}$ vs $\boldsymbol\theta$ blurs

[[mml-book]] §8.4.3 (Remark, p. 277): in later chapters the distinction softens — uncertain parameters are also "latent/hidden" because unobserved, and placing a prior on a parameter and integrating it out (§8.4.2 Remark) turns it into a random variable.

## Connections

- [[mml-ch08-when-models-meet-data]] — §8.4.3 canonical reference (Eqs. 8.24–8.28).
- [[mml-book]] — §8.4.3.
- [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] — §10.7 PPCA, the continuous-latent example.
- [[mml-ch11-density-estimation-gmm|MML Ch 11]] — §11.4 GMM, the discrete one-hot-latent example.
- [[ProbabilisticPCA]] — the headline continuous-latent model.
- [[EMAlgorithm]] — the MLE algorithm for latent-variable models.
- [[PrincipalComponentAnalysis]] / [[GaussianMixtureModel]] — the Ch 10 / Ch 11 examples.
- [[BayesianInference]] — applies unchanged once latents are marginalized out.
- [[MarginalLikelihood]] — the marginalization-out machinery is the same.
- [[DirectedGraphicalModel]] — latents drawn as unshaded nodes.
