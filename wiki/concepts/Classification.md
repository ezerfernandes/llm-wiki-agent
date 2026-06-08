---
title: "Classification"
type: concept
tags: [supervised-learning, ml-task]
sources: [d2l-introduction, d2l-linear-classification, islr-seventh-printing, mml-ch12-classification-svm, mml-book]
last_updated: 2026-06-05
---

# Classification

[[SupervisedLearning|Supervised-learning]] task where the **label is one of a discrete set of categories** (classes). Rule of thumb from [[d2l-introduction]]: any *which one?* problem is classification — digit recognition, cat-vs-dog, poisonous mushroom detection.

## Output forms

Models can return *firm* class assignments ("cat") but these are hard to optimize; almost always we output a **probability** over classes (a softmax distribution). The magnitude of the predicted-class probability conveys [[ModelCalibration|uncertainty]]. The dominant loss is [[CrossEntropyLoss|cross-entropy]] (the negative log-likelihood under a categorical likelihood).

## Sub-varieties

| Name | Defining feature |
|---|---|
| **Binary classification** | Two classes (cat / dog; spam / not-spam) |
| **Multiclass classification** | $K>2$ mutually-exclusive classes (digits 0–9, letters a–z) |
| **Hierarchical classification** | Classes form a taxonomy; not-all-errors-equal (Linnaeus-style) — confusing rattlesnake for garter snake costs more than confusing rattlesnake for cottonmouth |
| **Multi-label classification (tagging)** | Classes are *not* mutually exclusive — the "Town Musicians of Bremen" image is simultaneously cat, dog, donkey, rooster. PubMed's 28k-tag MeSH ontology is the extreme case |

## Decision theory beyond likelihood

The most-likely class is **not necessarily** the right action. The chapter's death-cap example: a poisoning classifier says 80% safe, but eating the mushroom carries risk $0.2 \times \infty + 0.8 \times 0 = \infty$ vs discarding it $0.8 \times 1 = 0.8$. Action selection requires **expected loss** computation — the bridge to [[DecisionMakingUnderUncertainty|Bayesian decision theory]].

## From [[mml-ch12-classification-svm|MML Ch 12]] — the geometric / loss-first treatment

[[mml-ch12-classification-svm|MML Ch 12]] is MML's classification pillar, and it treats **binary** classification ($f:\mathbb{R}^D\to\{+1,-1\}$, Eq. 12.1) through the [[SupportVectorMachine|SVM]] — the *geometric / loss-function-first* counterpart to the probabilistic classifiers above. Rather than modeling $P(Y\mid\mathbf{x})$ and maximizing likelihood, the SVM designs a loss (the [[HingeLoss|hinge loss]], a convex upper bound on the otherwise-combinatorial zero-one loss) and minimizes it under [[EmpiricalRiskMinimization|ERM]] (§12.2.5). §12.6 explicitly contrasts this with the probabilistic route: the SVM "does not naturally lend itself to a probabilistic interpretation," and recovering a calibrated $P(Y=1\mid\mathbf{x})$ needs a separate step (Platt scaling) — whereas [[LogisticRegression|logistic regression]] is the maximum-likelihood method whose squashing is *already* calibrated. So the wiki's two classification framings — probabilistic (softmax/cross-entropy above) and geometric (SVM/hinge) — are the two halves of §12.6's closing discussion.

## Connections

- [[SupervisedLearning]] — parent paradigm.
- [[mml-ch12-classification-svm]] — MML's classification pillar (the SVM, geometric/loss-first).
- [[SupportVectorMachine]] / [[HingeLoss]] — the geometric/loss-first binary classifier.
- [[Regression]] — sibling supervised task (continuous labels).
- [[LogisticRegression]] — simplest model for binary classification.
- [[Softmax]] — multiclass probabilistic output.
- [[CrossEntropyLoss]] — canonical loss.
- [[LinearDiscriminantAnalysis|LDA]], [[QuadraticDiscriminantAnalysis|QDA]] — generative-Bayesian classifiers.
- [[DecisionMakingUnderUncertainty]] — bridges class probabilities to actions.
- [[ModelCalibration]] — the predicted probabilities should reflect reality.
- [[ClassImbalance]] — classification pathology.
- [[d2l-introduction]], [[d2l-linear-classification]], [[islr-seventh-printing|ISLR]] Ch 4 — corpus-anchor introductions. [[d2l-linear-classification]] is the canonical end-to-end "softmax regression" walkthrough — one-hot labels → affine → softmax → cross-entropy → SGD → Fashion-MNIST.
- [[DistributionShift]] — what happens when the IID assumption underlying training-time classification fails at test time.
