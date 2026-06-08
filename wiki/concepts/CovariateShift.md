---
title: "Covariate Shift"
type: concept
tags: [distribution-shift, generalization, mlops]
sources: [d2l-linear-classification, madewithml-monitoring, mlsysbook-ch04-data-engineering, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Covariate Shift

The form of [[DistributionShift|distribution shift]] in which the **input distribution** $P(\mathbf x)$ changes between training and test time, while the **labeling function** $P(y\mid\mathbf x)$ stays fixed. The most widely studied shift type — the natural assumption whenever $\mathbf x$ causes $y$ (e.g. an image causes its species label).

## Canonical example

[[d2l-linear-classification]]: train a cat-vs-dog classifier on photographs, then evaluate on cartoons. The labeling function ("this depicts a cat") hasn't changed; only the marginal distribution of input pixels has.

## Correction by importance-weighted ERM

The risk under the target distribution can be rewritten as

$$
\int l(f(\mathbf x), y)\, p(y\mid\mathbf x)\,p(\mathbf x)\, d\mathbf x\,dy = \int l(f(\mathbf x), y)\, q(y\mid\mathbf x)\,q(\mathbf x)\, \frac{p(\mathbf x)}{q(\mathbf x)}\, d\mathbf x\,dy
$$

so reweighting each training example $(\mathbf x_i, y_i)$ by $\beta_i = p(\mathbf x_i)/q(\mathbf x_i)$ and minimizing **weighted [[EmpiricalRiskMinimization|empirical risk]]** gives an unbiased estimate of the target-distribution risk.

## Estimating the weights with logistic regression

We rarely know the ratio $p(\mathbf x)/q(\mathbf x)$ directly. The slick trick: train a binary classifier to distinguish "this sample came from $p$" vs "this sample came from $q$" — labeling target examples $+1$ and source examples $-1$. Under [[LogisticRegression|logistic regression]] with $P(z=+1\mid\mathbf x) = 1/(1 + e^{-h(\mathbf x)})$, the desired ratio is exactly

$$
\beta_i = \frac{p(\mathbf x_i)}{q(\mathbf x_i)} = \exp(h(\mathbf x_i)).
$$

Clipped at $\min(\exp(h(\mathbf x_i)), c)$ in practice to prevent runaway weights. Note this is logistic regression — a binary special case of softmax regression — being used to correct **for** softmax regression's distribution-shift bias. The full algorithm: (1) build a binary domain classifier between source and target inputs; (2) train via logistic regression to get $h$; (3) weight training data by $\beta_i$; (4) refit the original task with weighted ERM.

## Crucial assumption

The correction only works when **each target-distribution point had nonzero training-time probability**: $q(\mathbf x) > 0$ wherever $p(\mathbf x) > 0$. If a region of input space appears at test time that was never seen at training, the importance weight is infinite and the correction breaks. (This is also why an Atlanta-only training set cannot be reweighted to cover a Manhattan-only test set.)

## Detection in production

[[AlibiDetect]] / [[EvidentlyAI]] / [[TorchDrift]] / [[WhyLogs]] implement statistical drift detectors (KS, MMD, chi-squared, classifier-based) that operationalize the same idea — flagging covariate shift in deployed systems before accuracy degrades.

## Connections

- [[DistributionShift]] — parent taxonomy.
- [[LabelShift]] / [[ConceptShift]] / [[ConceptDrift]] — sibling shift types.
- [[mlsysbook-ch04-data-engineering]] — Reddi's *Machine Learning Systems* Ch 4: covariate shift ($p(x)$ changes, $p(y\mid x)$ fixed) is detected by monitoring feature distributions with [[PopulationStabilityIndex|PSI]] / [[KullbackLeiblerDivergence|KL divergence]]; the medical-imaging-camera-swap example.
- [[EmpiricalRiskMinimization]] — what gets reweighted.
- [[LogisticRegression]] — the binary classifier used for weight estimation.
- [[Softmax]] — multiclass parent that logistic regression specializes; this is where the recursion closes.
- [[d2l-linear-classification]] — corpus anchor (Section *Covariate Shift Correction*).
- [[AlibiDetect]] / [[EvidentlyAI]] / [[TorchDrift]] / [[WhyLogs]] — operational drift-detection layer.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 notes Shimodaira's importance-weighting correction fails when deployment inputs fall outside training support, requiring full retraining instead of reweighting.

