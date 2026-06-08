---
title: "Support Vector"
type: concept
tags: [classification, classical-ml, duality, foundational]
sources: [mml-ch12-classification-svm, mml-book]
last_updated: 2026-06-05
---

# Support Vector

A training example $\mathbf{x}_n$ whose [[DualSVM|dual]] Lagrange multiplier is **strictly positive**, $\alpha_n>0$ — the only examples that determine the [[SupportVectorMachine|SVM]]'s [[SeparatingHyperplane|separating hyperplane]] ([[mml-ch12-classification-svm|MML Ch 12]] §12.3.1 Remark, p. 384). They "support" the hyperplane; everything else could be deleted without changing the solution.

## Why they define the solution — the representer theorem

Solving the dual SVM gives multipliers $\boldsymbol\alpha$; the primal weight is recovered by the **representer theorem** ([[mml-ch12-classification-svm|MML Ch 12]] Eq. 12.38, Kimeldorf & Wahba 1970):

$$\mathbf{w}=\sum_{n=1}^N\alpha_n y_n\mathbf{x}_n.$$

Examples with $\alpha_n=0$ contribute *nothing* to $\mathbf{w}$. So the optimal weight is a linear combination of the support vectors alone — the source of the method's name:

> "The examples $\mathbf{x}_n$, for which the corresponding parameters $\alpha_n=0$, do not contribute to the solution $\mathbf{w}$ at all. The other examples, where $\alpha_n>0$, are called support vectors since they 'support' the hyperplane." — [[mml-ch12-classification-svm|MML Ch 12]] §12.3.1 Remark, p. 384

## This is KKT complementary slackness

A point has $\alpha_n>0$ exactly when its margin constraint is **active** — i.e. it lies on (or, in the soft-margin case, within/beyond) the margin boundary. This is the [[KKTConditions|complementary slackness]] condition $\alpha_n\big(y_n(\langle\mathbf{w},\mathbf{x}_n\rangle+b)-1+\xi_n\big)=0$: either the constraint binds ($\alpha_n>0$, the point is a support vector) or it is slack ($\alpha_n=0$, the point is interior and irrelevant). Sparsity in $\boldsymbol\alpha$ is the dual face of the SVM's geometric story.

## The three KKT regimes (soft margin)

With box constraint $0\le\alpha_n\le C$ ([[SoftMarginSVM]]):

- $\alpha_n=0$ — non-support vector; correctly classified beyond the margin.
- $0<\alpha_n<C$ — support vector lying *exactly on* the margin boundary ($\xi_n=0$); used to recover the bias $b^*=y_n-\langle\mathbf{w}^*,\mathbf{x}_n\rangle$ ([[mml-ch12-classification-svm|MML Ch 12]] Eq. 12.42, margin p. 385).
- $\alpha_n=C$ — support vector inside the margin or misclassified ($\xi_n>0$).

## Why it matters

The support-vector sparsity is what makes SVM prediction efficient (only support vectors are stored/evaluated) and is the basis of the [[Margin|margin]]-generalization story: the decision boundary depends only on the few hardest examples, not the bulk of the data.

## Connections

- [[mml-ch12-classification-svm]] — §12.3.1 canonical reference.
- [[DualSVM]] — where the multipliers $\alpha_n$ live.
- [[SupportVectorMachine]] — the method; named after these points.
- [[KKTConditions]] — complementary slackness ⇒ $\alpha_n>0$ iff constraint active.
- [[LagrangianDuality]] / [[Lagrangian]] — the dual that produces $\boldsymbol\alpha$.
- [[Margin]] / [[SeparatingHyperplane]] — support vectors lie on the margin boundary.
- [[SoftMarginSVM]] — the box constraint $0\le\alpha_n\le C$ and three KKT regimes.
