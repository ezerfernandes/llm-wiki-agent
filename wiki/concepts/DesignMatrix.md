---
title: "Design Matrix"
type: concept
tags: [regression, linear-algebra, foundational]
sources: [mml-book, mml-ch08-when-models-meet-data, mml-ch09-linear-regression]
last_updated: 2026-06-04
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

## From [[mml-ch09-linear-regression|MML Ch 9]]

[[mml-ch09-linear-regression|MML Ch 9]] §9.2 defines the design matrix twice: $\mathbf{X}:=[\mathbf{x}_1,\dots,\mathbf{x}_N]^\top\in\mathbb{R}^{N\times D}$ for the raw-input model (Eq. 9.10b) and the **feature matrix** $\boldsymbol\Phi\in\mathbb{R}^{N\times K}$ with rows $\boldsymbol\phi^\top(\mathbf{x}_n)$ and entries $\Phi_{ij}=\phi_j(\mathbf{x}_i)$ for the [[FeatureMap|feature-map]] model (Eq. 9.16; Example 9.4 gives the second-order polynomial feature matrix with rows $[1,x_n,x_n^2]$, Eq. 9.17). The [[NormalEquations|normal-equations]] MLE is obtained by **literally substituting $\boldsymbol\Phi$ for $\mathbf{X}$**: $\boldsymbol\theta_{\text{ML}}=(\boldsymbol\Phi^\top\boldsymbol\Phi)^{-1}\boldsymbol\Phi^\top\mathbf{y}$ (Eq. 9.19), invertible iff $\text{rk}(\boldsymbol\Phi)=K$. The MAP / [[RidgeRegression|ridge]] variant adds the jitter: $(\boldsymbol\Phi^\top\boldsymbol\Phi+\tfrac{\sigma^2}{b^2}\mathbf{I})^{-1}\boldsymbol\Phi^\top\mathbf{y}$ (Eq. 9.31), and the [[BayesianLinearRegression|Bayesian]] posterior precision is $\mathbf{S}_N^{-1}=\mathbf{S}_0^{-1}+\sigma^{-2}\boldsymbol\Phi^\top\boldsymbol\Phi$ (Eq. 9.43b) — the same Gram matrix $\boldsymbol\Phi^\top\boldsymbol\Phi$ as the data-information term. §9.4 reads the column space $\text{col}(\boldsymbol\Phi)$ as the subspace onto which $\mathbf{y}$ is [[OrthogonalProjection|orthogonally projected]].

## From [[mml-ch08-when-models-meet-data|MML Ch 8]]

[[mml-ch08-when-models-meet-data|MML Ch 8]] is where the design matrix first appears — §8.1.1 (p. 253) introduces the **example matrix** $\mathbf{X}=[\mathbf{x}_1,\dots,\mathbf{x}_N]^\top\in\mathbb{R}^{N\times D}$ (data are vectors, rows are examples). §8.2.2 uses it to write the [[EmpiricalRisk|empirical risk]] in matrix form: the least-squares problem becomes $\min_{\boldsymbol\theta}\frac1N\|\mathbf{y}-\mathbf{X}\boldsymbol\theta\|^2$ (Eq. 8.9), and the bias-augmentation trick (Example 8.1, the $x^{(0)}=1$ column) lets the affine predictor be written as the linear $\boldsymbol\theta^\top\mathbf{x}_n$. The closed-form solution to this problem is the Ch 9 normal-equations result above.

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
