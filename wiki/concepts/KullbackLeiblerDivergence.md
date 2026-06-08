---
title: "Kullback-Leibler Divergence"
type: concept
tags: [information-theory, foundational]
sources: [d2l-appendix-mathematics, mlsysbook-ch04-data-engineering, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Kullback-Leibler Divergence

A directional measure of how one probability distribution $P$ differs from a reference distribution $Q$ on the same support ([[d2l-appendix-mathematics]] §information-theory):

$$D_{KL}(P\,\|\,Q) = \mathbb{E}_{x\sim P}\!\left[\log\frac{p(x)}{q(x)}\right] = \sum_i p_i \log\frac{p_i}{q_i}\quad\text{(discrete)}, \qquad \int p(x)\log\frac{p(x)}{q(x)}\,dx\quad\text{(continuous)}.$$

## Properties

- **Non-negative** (Gibbs' inequality): $D_{KL}(P\|Q)\geq 0$, with equality iff $P=Q$ almost everywhere.
- **Asymmetric**: $D_{KL}(P\|Q)\neq D_{KL}(Q\|P)$ in general — *"a distance-like measure, but not a metric"* ([[d2l-appendix-mathematics]]).
- **Not bounded**: $D_{KL}$ can be $+\infty$ if $Q$ assigns zero probability where $P$ does not.
- **Invariant under reparametrization** of the random variable.

## Connection to cross-entropy

$$H(P, Q) = -\mathbb{E}_{x\sim P}[\log q(x)] = H(P) + D_{KL}(P\,\|\,Q).$$

So minimizing [[CrossEntropy|cross-entropy]] w.r.t. $Q$ is identical to minimizing $D_{KL}(P\|Q)$ — the [[Entropy|entropy]] $H(P)$ is a $Q$-independent constant. This is *why* classification with [[CrossEntropyLoss|cross-entropy loss]] is exactly [[MaximumLikelihoodEstimation|maximum likelihood]] under a categorical model: NLL = cross-entropy = KL up to constant.

## Forward vs reverse KL

| | Behavior |
|---|---|
| **Forward KL** $D_{KL}(P\|Q)$ | $Q$ must cover *all* of $P$'s support ("mass-covering" / "mean-seeking"). Used in MLE — fit $Q$ to data $P$. |
| **Reverse KL** $D_{KL}(Q\|P)$ | $Q$ concentrates on *some* mode of $P$ ("mode-seeking"). Used in [[VariationalInference]] — fit a tractable $Q$ to an intractable posterior $P$. |

This asymmetry is *why* [[VariationalAutoencoder|VAEs]] (which minimize reverse KL via ELBO) produce blurry samples and [[GenerativeAdversarialNetwork|GANs]] (which more closely target forward-KL behavior) produce sharper but less-diverse ones — the *mode-seeking* vs *mode-covering* trade-off.

## ML uses

- **MLE = minimum forward KL** between empirical data distribution and model.
- **[[VariationalInference|Variational inference]] / ELBO**: minimize $D_{KL}(q_\phi(z\mid x)\,\|\,p(z\mid x))$ — the [[VariationalAutoencoder|VAE]] training objective.
- **Policy distillation / behavior cloning**: KL between teacher and student policies.
- **[[RLHF]] / [[GRPO]] / [[PPO]]** regularize updates with a KL penalty to the reference policy.
- **Diffusion model training objectives** are derived as a chain of conditional KL terms.
- **Data-engineering drift detection** ([[mlsysbook-ch04-data-engineering|mlsysbook Ch 4]]): KL divergence (with [[PopulationStabilityIndex|PSI]]) measures the degradation equation's divergence term $\mathcal{D}(P_t \lVert P_0)$ between training and serving distributions; the [[TrainingServingConsistency|consistency imperative]] predicts accuracy degradation ∝ $\mathcal{D}_{\text{KL}}(p_{g_{\text{serve}}} \lVert p_{g_{\text{train}}})$.

## Connections
- [[mlsysbook-ch04-data-engineering]] — ML data-engineering drift-detection use.
- [[PopulationStabilityIndex]] — the binned companion drift metric.

- [[d2l-appendix-mathematics]] — §information-theory canonical reference.
- [[Entropy]] — KL is the gap between cross-entropy and entropy.
- [[CrossEntropy]] / [[CrossEntropyLoss]] — equals $H(P) + D_{KL}(P\|Q)$.
- [[MutualInformation]] — equals $D_{KL}(P(X,Y)\,\|\,P(X)P(Y))$.
- [[MaximumLikelihoodEstimation]] — equivalent to forward-KL minimization.
- [[VariationalInference]] — reverse-KL minimization with tractable $Q$.
- [[InformationTheory]] — parent field.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 uses KL divergence as the more-sensitive (asymmetric) alternative to PSI for continuous drift, with $\mathcal{D}(P_t\|P_0)>0.1$ as a common runbook threshold.

