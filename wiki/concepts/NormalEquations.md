---
title: "Normal Equations"
type: concept
tags: [regression, linear-algebra, least-squares, foundational]
sources: [mml-ch09-linear-regression, mml-book]
last_updated: 2026-06-04
---

# Normal Equations

The linear system whose solution is the [[LeastSquares|ordinary least-squares]] / maximum-likelihood estimate of a [[LinearRegression|linear-regression]] model. Setting the gradient of the squared-error loss to zero ([[mml-ch09-linear-regression|MML Ch 9]] §9.2.1, Eq. 9.12) yields

$$\mathbf{X}^\top\mathbf{X}\,\boldsymbol\theta = \mathbf{X}^\top\mathbf{y} \quad\Longleftrightarrow\quad \boldsymbol\theta_{\text{ML}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y},$$

where $\mathbf{X}$ is the [[DesignMatrix|design matrix]] (or $\boldsymbol\Phi$ for a [[FeatureMap|feature map]], giving $\boldsymbol\theta_{\text{ML}}=(\boldsymbol\Phi^\top\boldsymbol\Phi)^{-1}\boldsymbol\Phi^\top\mathbf{y}$, Eq. 9.19). The name is geometric: the residual $\mathbf{y}-\mathbf{X}\boldsymbol\theta$ is required to be **normal (orthogonal)** to the column space of $\mathbf{X}$ — exactly the [[OrthogonalProjection|orthogonal-projection]] condition $\mathbf{X}^\top(\mathbf{y}-\mathbf{X}\boldsymbol\theta)=\mathbf{0}$.

## Why this is the global minimum

The squared-error loss $\mathcal{L}(\boldsymbol\theta)=\frac{1}{2\sigma^2}\|\mathbf{y}-\mathbf{X}\boldsymbol\theta\|^2$ is **quadratic** in $\boldsymbol\theta$, with row-vector gradient $\frac{d\mathcal{L}}{d\boldsymbol\theta}=\frac{1}{\sigma^2}(-\mathbf{y}^\top\mathbf{X}+\boldsymbol\theta^\top\mathbf{X}^\top\mathbf{X})\in\mathbb{R}^{1\times D}$ (Eq. 9.11c, MML's deliberate Ch 5 numerator-layout convention) and **Hessian** $\nabla^2_{\boldsymbol\theta}\mathcal{L}=\mathbf{X}^\top\mathbf{X}$, which is positive definite when $\mathbf{X}$ has full column rank. Hence the zero-gradient condition is **necessary and sufficient** for the unique global minimum ([[mml-ch09-linear-regression|MML]] §9.2.1 Remark, p. 294).

## Existence & the rank condition

$(\mathbf{X}^\top\mathbf{X})^{-1}$ exists iff $\text{rk}(\mathbf{X})=D$ (full column rank) — i.e. the [[GramMatrix|Gram matrix]] $\mathbf{X}^\top\mathbf{X}$ is invertible. Ignoring duplicate points this needs $N\geq D$ (no more parameters than data). When $N<D$ or columns are collinear the system is **under-determined** with infinitely many solutions — fixed by the regularizer in [[RidgeRegression|ridge regression]], whose normal equations are $(\mathbf{X}^\top\mathbf{X}+\lambda\mathbf{I})\boldsymbol\theta=\mathbf{X}^\top\mathbf{y}$ (always invertible since $\mathbf{X}^\top\mathbf{X}+\lambda\mathbf{I}$ is strictly positive definite).

## In practice

The closed form is rarely formed as a literal inverse — solving the linear system $\mathbf{A}\boldsymbol\theta=\mathbf{b}$ with $\mathbf{A}=\mathbf{X}^\top\mathbf{X}$, $\mathbf{b}=\mathbf{X}^\top\mathbf{y}$ (Remark, p. 294) via Cholesky or, more stably, via the QR/SVD of $\mathbf{X}$ avoids squaring the condition number. For very large $N$ or $D$, iterative [[StochasticGradientDescent|SGD]] (the [[d2l-linear-regression|D2L]] route) is preferred even though a closed form exists.

## Connections

- [[mml-ch09-linear-regression]] / [[mml-book]] — §9.2.1 canonical reference (Eqs. 9.11–9.12, 9.19).
- [[LeastSquares]] — the objective the normal equations solve.
- [[DesignMatrix]] — supplies $\mathbf{X}$ / $\boldsymbol\Phi$ and the Gram matrix $\mathbf{X}^\top\mathbf{X}$.
- [[OrthogonalProjection]] — the residual-orthogonality reading; predictions $\hat{\mathbf{y}}=\mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$ are the projection of $\mathbf{y}$ onto $\text{col}(\mathbf{X})$.
- [[LinearRegression]] — the model.
- [[RidgeRegression]] — regularized normal equations.
- [[MaximumLikelihoodEstimation]] — the normal-equations solution is the Gaussian-noise MLE.
