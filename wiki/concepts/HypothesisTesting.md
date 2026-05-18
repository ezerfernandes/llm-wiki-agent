---
title: "Hypothesis Testing"
type: concept
tags: [statistics, foundational]
sources: [d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Hypothesis Testing

The framework for deciding whether observed data are consistent with a stated **null hypothesis** $H_0$ or whether the **alternative** $H_A$ is better supported ([[d2l-appendix-mathematics]] §statistics).

Compute a **test statistic** $T$ from the data and a **rejection region** at significance level $\alpha$. If $T$ lands in the rejection region, reject $H_0$; otherwise fail to reject (note: *failing to reject* is *not* "accepting").

## The four error types

|  | $H_0$ true | $H_A$ true |
|---|---|---|
| **Reject $H_0$** | **Type-I error** (probability $\alpha$) — false positive | Correct rejection (probability $1-\beta$ = **power**) |
| **Fail to reject** | Correct retention (probability $1-\alpha$) | **Type-II error** (probability $\beta$) — false negative |

- $\alpha = P(\text{reject } H_0 \mid H_0)$ — the **significance level**, traditionally fixed at $0.05$ or $0.01$.
- $\beta = P(\text{fail to reject } H_0 \mid H_A)$ — controlled by sample size and effect size.
- $1-\beta$ = **statistical power** — the probability of detecting a true effect.

## The $p$-value

$$p\text{-value} = P\!\left(T \geq T_{\text{obs}} \mid H_0\right).$$

The probability of observing data *at least as extreme* as the observed sample, under the null. Reject $H_0$ iff $p \leq \alpha$.

**What a $p$-value is not**: it is *not* the probability that $H_0$ is true (that would require a Bayesian computation with a prior); it is *not* the probability that the result is due to chance. It is a property of the data conditioned on the null.

## Common tests

| Test | Statistic | Used for |
|---|---|---|
| $z$-test | $\bar X / (\sigma/\sqrt n)$ | known-variance mean test |
| $t$-test | $\bar X / (s/\sqrt n)$ | unknown-variance mean test |
| Two-sample $t$-test | mean-difference / pooled SE | comparing two group means |
| $\chi^2$ test | $\sum (O_i-E_i)^2/E_i$ | categorical goodness-of-fit / independence |
| F-test (ANOVA) | between-group var / within-group var | comparing means across $k$ groups |

The [[CentralLimitTheorem|CLT]] justifies why these test statistics have known distributions under $H_0$ at large $n$ — *every* parametric hypothesis test in classical statistics ultimately leans on it.

## ML uses

- **[[ABTesting|A/B testing]]**: did the new model / feature / UI improve the metric *significantly*, or could the improvement be chance?
- **Comparing model accuracies** on held-out test sets: paired bootstrap, McNemar's test, sign test.
- **[[StatisticalSignificance|Statistical significance]] vs **practical** significance: with enough data, vanishingly tiny effects become "significant" — the [[d2l-appendix-mathematics]] caveat that significance does not imply importance.
- **[[MultipleTesting|Multiple testing]] corrections** (Bonferroni, Holm, Benjamini-Hochberg / FDR) — required whenever many hypotheses are tested simultaneously.

## Bayesian vs frequentist contrast

Hypothesis testing as described is **frequentist** — $\alpha$, $\beta$, and $p$-values are about the *long-run frequency* of decisions under repeated sampling. The Bayesian alternative is to compute the posterior $P(H_0\mid \text{data})$ directly via [[BayesTheorem|Bayes' rule]] — requires a prior and an explicit model under $H_A$.

## Connections

- [[d2l-appendix-mathematics]] — §statistics canonical reference.
- [[Statistics]] — parent discipline.
- [[CentralLimitTheorem]] — justifies the test-statistic distributions.
- [[ConfidenceInterval]] — dual of hypothesis tests (failing to reject $H_0:\mu=\mu_0$ at $\alpha$ ⟺ $\mu_0$ lies in the $1-\alpha$ CI).
- [[ABTesting]] — the dominant ML application.
- [[BayesTheorem]] — the Bayesian alternative.
- [[FalseDiscoveryRate]] — multiple-testing extension.
