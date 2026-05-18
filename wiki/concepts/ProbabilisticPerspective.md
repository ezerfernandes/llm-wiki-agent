---
title: "Probabilistic Perspective"
type: concept
tags: [foundational, methodology, ml-theory]
sources: [pml1-murphy]
last_updated: 2026-05-15
---

# Probabilistic Perspective

The unifying methodological commitment of [[KevinMurphy]]'s [[pml1-murphy|PML series]]: **every unknown quantity** — future observations, model parameters, latent factors, missing data — is treated as a **random variable** endowed with a probability distribution; learning is **inference** over those distributions.

## Two justifications (Murphy §1.1)

1. **Optimal decision-making under uncertainty requires probability.** This is the [[DecisionMakingUnderUncertainty|decision-theoretic]] argument: any agent that must choose actions whose value depends on uncertain outcomes is provably worse off (in expected utility) than a Bayesian agent unless its beliefs satisfy the probability axioms (Cox / Dutch-book / Savage).
2. **Probability is the lingua franca of every neighboring science.** Stochastic optimization, control theory, OR, econometrics, information theory, statistical physics, biostatistics all speak it. A probabilistic ML framing connects to all of them; alternatives don't. (Shakir Mohamed, DeepMind, quoted in Murphy §1.1.)

## What it commits to

- **Predictions are distributions, not point estimates.** $p(y|\mathbf{x};\boldsymbol\theta)$, not $\hat y$. Point estimates fall out as decision-theoretic summaries (mean / median / mode under a loss).
- **Two kinds of uncertainty are first-class.** **Epistemic** / model uncertainty (ignorance, reducible by data) vs **aleatoric** / data uncertainty (irreducible stochasticity). Conflating them produces overconfident systems.
- **Bayes' rule is the universal inference operator.** $p(H|E) \propto p(E|H)\,p(H)$. The book's machinery — [[MaximumLikelihoodEstimation|MLE]], MAP, full posteriors, variational inference, MCMC — is one ladder of approximations to this object.
- **Probability extends logic** (Jaynes / Cox; Murphy §2.1.3). When propositions are certain, probability collapses to Boolean logic; under uncertainty, the unique consistent calculus is the Kolmogorov-axiomatized one.

## Role in this wiki

- The Corpus II 2026 LLM papers all *use* this framing tacitly: language models output $p(\mathbf{x}_t | \mathbf{x}_{<t})$, RL agents maximize expected return under $p(s_{t+1}|s_t,a_t)$, MoE routers sample $p(\text{expert}|\text{token})$. [[pml1-murphy]] is the canonical reference for what they assume.
- Several Corpus II authors are *more* probabilistic than Murphy formalizes: e.g. [[2605.12966-agentic-ai-to-agi]]'s [[StructuredRealWorldDistribution]] argument, [[2605.10698-bystander-effect-mas]]'s [[SovereigntyDecayLaw]] (an exponential decay model over interaction depth), and [[2605.12357-delta-mem]]'s [[gateddeltarule]] (a stochastic update law).
- The interpretability vocabulary in Corpus III ([[imlbook-shapley]], [[imlbook-pdp]], [[imlbook-counterfactual]]) is mostly *frequentist-flavored*; the probabilistic perspective gives the missing posterior-over-explanations layer (epistemic uncertainty about which feature actually drove a decision).

## Connections

- [[pml1-murphy]] — anchor source.
- [[KevinMurphy]] — proponent.
- [[MaximumLikelihoodEstimation]] — the workhorse instantiation under flat priors.
- [[EmpiricalRiskMinimization]] — non-probabilistic counterpart; recovered as a special case via NLL.
- [[NoFreeLunchTheorem]] — the prior-pricing argument every probabilistic learner makes.
- [[DecisionMakingUnderUncertainty]] — the operational payoff of adopting the perspective.
