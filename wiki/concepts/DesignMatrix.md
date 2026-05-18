---
title: "Design Matrix"
type: concept
tags: [regression, linear-algebra, foundational]
sources: [mml-book]
last_updated: 2026-05-16
---

# Design Matrix

The matrix $\mathbf{X}\in\mathbb{R}^{N\times D}$ (or $\boldsymbol\Phi\in\mathbb{R}^{N\times K}$ for non-trivial feature maps) collecting training inputs as rows ([[mml-book]] §9.2):

$$\mathbf{X} = \begin{bmatrix}\mathbf{x}_1^\top \\ \mathbf{x}_2^\top \\ \vdots \\ \mathbf{x}_N^\top\end{bmatrix}, \quad \boldsymbol\Phi = \begin{bmatrix}\boldsymbol\phi(\mathbf{x}_1)^\top \\ \boldsymbol\phi(\mathbf{x}_2)^\top \\ \vdots \\ \boldsymbol\phi(\mathbf{x}_N)^\top\end{bmatrix}.$$

The MLE for linear regression is the closed form

$$\boldsymbol\theta_{\text{ML}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}.$$

## Why the design matrix is the central object

- **Rank condition for identifiability**: $\boldsymbol\theta_{\text{ML}}$ exists uniquely iff $\text{rk}(\mathbf{X})=D$ (i.e., $\mathbf{X}^\top\mathbf{X}$ is invertible). When $N<D$ or when columns are linearly dependent, the system is **under-determined**.
- **Gram matrix** $\mathbf{X}^\top\mathbf{X}$: the heart of the normal equations; positive (semi-)definite.
- **Hat matrix** $\mathbf{H} := \mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top$: the orthogonal projection onto $\text{col}(\mathbf{X})$; predictions are $\hat{\mathbf{y}} = \mathbf{H}\mathbf{y}$. Its diagonal entries are *leverage* — how much each training point pulls its own prediction.

## Bias / intercept augmentation

To include an intercept term $\theta_0$ in $f(\mathbf{x}) = \theta_0 + \boldsymbol\theta^\top\mathbf{x}$, [[mml-book]] §8.1 prepends a column of 1's to $\mathbf{X}$ ($x_n^{(0)}\equiv 1$) and absorbs $\theta_0$ into $\boldsymbol\theta$. This is the standard "bias trick."

## Beyond OLS

- **Ridge regression**: $(\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I})^{-1}\mathbf{X}^\top\mathbf{y}$ — adds a regularizer that also fixes the non-invertibility when $N<D$.
- **[[BayesianLinearRegression]]**: posterior precision $\mathbf{S}_N^{-1} = \mathbf{S}_0^{-1} + \sigma^{-2}\mathbf{X}^\top\mathbf{X}$ — same Gram matrix appears as the data-information term.
- **PCA** ([[mml-book]] §10): SVD of the *centered* design matrix gives principal components directly.

## Connections

- [[mml-book]] — §9.2 canonical reference (Eq. 9.10 + Eq. 9.16).
- [[LinearRegression]] — primary consumer.
- [[FeatureMap]] — what makes $\boldsymbol\Phi$ different from $\mathbf{X}$.
- [[OrthogonalProjection]] — hat matrix interpretation.
- [[Rank]] — identifiability condition.
- [[BayesianLinearRegression]] — same Gram matrix.
