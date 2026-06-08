---
title: "MML Ch 3 — Analytic Geometry"
type: source
tags: [textbook, mathematics, analytic-geometry, inner-product, norm, metric, distance, angle, orthogonality, orthogonal-matrix, orthonormal-basis, orthogonal-complement, orthogonal-projection, projection-matrix, gram-schmidt, rotation, bilinear-form, symmetric-positive-definite, cauchy-schwarz, mml-book, foundations]
date: 2020-01-01
source_file: raw/mml-book.pdf
---

## Summary

Chapter 3 of [[mml-book|Mathematics for Machine Learning]] (Deisenroth, Faisal & Ong; book pp. 70–97) **adds geometry to the abstract linear algebra of Ch 2** by equipping a vector space with an [[InnerProduct]]. The single organizing idea (Fig. 3.1 mind map): an inner product **induces** a [[Norm]] (length), which induces a [[Metric]] (distance); the [[CauchySchwarzInequality]] makes the inner product define an [[Angle]] and hence [[Orthogonality]]; orthogonality gives [[OrthonormalBasis|orthonormal bases]], [[OrthogonalComplement|orthogonal complements]], and — the chapter's payload — [[OrthogonalProjection|orthogonal projections]], the central operation behind regression (Ch 9), PCA (Ch 10), and SVM/classification (Ch 12). The chapter closes with [[Rotation|rotations]] as a special, geometry-preserving class of [[OrthogonalMatrix|orthogonal transformations]]. Throughout, the book works in $\mathbb{R}^n$ with the dot product as the *default* inner product (Euclidean norm by default), but is careful to distinguish the general inner product (any [[SymmetricPositiveDefiniteMatrix|symmetric positive definite matrix]] $\mathbf{A}$ via $\langle\mathbf{x},\mathbf{y}\rangle=\hat{\mathbf{x}}^\top\mathbf{A}\hat{\mathbf{y}}$, Thm 3.5) from the dot-product special case. The deep takeaway: *lengths, distances and angles are not absolute properties of vectors — they depend on which inner product you choose* (Examples 3.5, 3.7).

## Key Claims

### 3.0 Opening / mind map (p. 70)

- **Geometry is layered onto Ch 2's abstract vectors** by *equipping the vector space with an inner product that induces the geometry of the vector space* (p. 70). Inner products and their corresponding norms and metrics capture the intuitive notions of **similarity** and **distance** used to develop the SVM (Ch 12), and lengths/angles feed [[OrthogonalProjection]], which is central to PCA (Ch 10) and regression (Ch 9).
- **Mind map (Fig. 3.1):** [[InnerProduct]] *induces* [[Norm]] (dashed edge); inner product → Lengths, [[OrthogonalProjection]], [[Angle|Angles]], [[Rotation|Rotations]], and Chapter 12 (Classification); Norm → Lengths; Lengths/Orthogonal projection/Angles feed Chapter 9 (Regression), Chapter 4 (Matrix decomposition), Chapter 10 (Dimensionality reduction).

### 3.1 Norms (pp. 71–72)

- **Definition 3.1 ([[Norm]])** (Eqs. 3.1–3.2, p. 71): a norm on a vector space $V$ is a function $\|\cdot\|:V\to\mathbb{R}$, $\mathbf{x}\mapsto\|\mathbf{x}\|$, assigning each vector its *length* $\|\mathbf{x}\|\in\mathbb{R}$, such that for all $\lambda\in\mathbb{R}$ and $\mathbf{x},\mathbf{y}\in V$: (i) **absolutely homogeneous** $\|\lambda\mathbf{x}\|=|\lambda|\,\|\mathbf{x}\|$; (ii) **triangle inequality** $\|\mathbf{x}+\mathbf{y}\|\leq\|\mathbf{x}\|+\|\mathbf{y}\|$; (iii) **positive definite** $\|\mathbf{x}\|\geq 0$ and $\|\mathbf{x}\|=0\iff\mathbf{x}=\mathbf{0}$.
- **Geometric reading** (p. 71): for a geometric vector (directed line segment from the origin) the length is the distance of its "end" from the origin. The triangle inequality says that for any triangle the sum of the lengths of any two sides is $\geq$ the remaining side (Fig. 3.2, $c\leq a+b$). The book only ever uses finite-dimensional $\mathbb{R}^n$ (§2.4) and writes $x_i$ for the $i$-th element of $\mathbf{x}$.
- **Example 3.1 (Manhattan / $\ell_1$ norm)** (Eq. 3.3, p. 71): $\|\mathbf{x}\|_1:=\sum_{i=1}^n |x_i|$, using the absolute value. The left panel of Fig. 3.3 shows all $\mathbf{x}\in\mathbb{R}^2$ with $\|\mathbf{x}\|_1=1$ — a diamond. Also called the **$\ell_1$ norm**.
- **Example 3.2 (Euclidean / $\ell_2$ norm)** (Eq. 3.4, p. 72): $\|\mathbf{x}\|_2:=\sqrt{\sum_{i=1}^n x_i^2}=\sqrt{\mathbf{x}^\top\mathbf{x}}$, the **Euclidean distance** of $\mathbf{x}$ from the origin. The right panel of Fig. 3.3 shows the unit circle $\|\mathbf{x}\|_2=1$. Also called the **$\ell_2$ norm**.
- **Default convention** (Remark, p. 72): *"Throughout this book, we will use the Euclidean norm (3.4) by default if not stated otherwise."*

### 3.2 Inner Products (pp. 72–75)

- **Purpose** (p. 72): inner products introduce intuitive geometrical concepts — the length of a vector and the angle or distance between two vectors. *A major purpose of inner products is to determine whether vectors are orthogonal to each other.*

#### 3.2.1 Dot Product (p. 72)

- **Scalar / dot product** (Eq. 3.5): the familiar inner product in $\mathbb{R}^n$ is $\mathbf{x}^\top\mathbf{y}=\sum_{i=1}^n x_iy_i$, called the *scalar product* / *dot product*. The book refers to this *particular* inner product as **the dot product**, but stresses inner products are more general. See [[DotProduct]].

#### 3.2.2 General Inner Products (pp. 72–73)

- **Bilinear mapping** (Eqs. 3.6–3.7, p. 72): a *[[BilinearForm|bilinear mapping]]* $\Omega$ is a mapping with two arguments that is linear in each argument: $\Omega(\lambda\mathbf{x}+\psi\mathbf{y},\mathbf{z})=\lambda\Omega(\mathbf{x},\mathbf{z})+\psi\Omega(\mathbf{y},\mathbf{z})$ (linear in the 1st argument) and $\Omega(\mathbf{x},\lambda\mathbf{y}+\psi\mathbf{z})=\lambda\Omega(\mathbf{x},\mathbf{y})+\psi\Omega(\mathbf{x},\mathbf{z})$ (linear in the 2nd argument). (Cf. Eq. 2.87.)
- **Definition 3.2 (Symmetric / positive definite bilinear forms)** (Eq. 3.8, p. 73): $\Omega:V\times V\to\mathbb{R}$ is *symmetric* if $\Omega(\mathbf{x},\mathbf{y})=\Omega(\mathbf{y},\mathbf{x})$ for all $\mathbf{x},\mathbf{y}$ (order doesn't matter); $\Omega$ is *positive definite* if $\forall\mathbf{x}\in V\setminus\{\mathbf{0}\}:\Omega(\mathbf{x},\mathbf{x})>0$ and $\Omega(\mathbf{0},\mathbf{0})=0$.
- **Definition 3.3 (Inner product / inner product space)** (p. 73): a positive definite, symmetric bilinear mapping $\Omega:V\times V\to\mathbb{R}$ is an *[[InnerProduct]]* on $V$, written $\langle\mathbf{x},\mathbf{y}\rangle$ instead of $\Omega(\mathbf{x},\mathbf{y})$. The pair $(V,\langle\cdot,\cdot\rangle)$ is an *inner product space* (or *real vector space with inner product*); if the inner product is the dot product (3.5) it is a *Euclidean vector space*. The book calls these all "inner product spaces."
- **Example 3.3 (An inner product that is not the dot product)** (Eq. 3.9, p. 73): on $V=\mathbb{R}^2$, $\langle\mathbf{x},\mathbf{y}\rangle:=x_1y_1-(x_1y_2+x_2y_1)+2x_2y_2$ is an inner product but is different from the dot product (proof = exercise 3.1).

#### 3.2.3 Symmetric, Positive Definite Matrices (pp. 73–74)

- **SPD matrices are defined via the inner product** (p. 73) and play a key role in ML; revisited in §4.3 (matrix decompositions) and §12.4 (kernels, where *symmetric positive semidefinite* matrices appear).
- **Coordinate form of the inner product** (Eq. 3.10, p. 73): for an $n$-dim inner product space $V$ with ordered basis $B=(\mathbf{b}_1,\ldots,\mathbf{b}_n)$, writing $\mathbf{x}=\sum_i\psi_i\mathbf{b}_i$, $\mathbf{y}=\sum_j\lambda_j\mathbf{b}_j$ and using bilinearity, $\langle\mathbf{x},\mathbf{y}\rangle=\sum_{i,j}\psi_i\langle\mathbf{b}_i,\mathbf{b}_j\rangle\lambda_j=\hat{\mathbf{x}}^\top\mathbf{A}\hat{\mathbf{y}}$, where $A_{ij}:=\langle\mathbf{b}_i,\mathbf{b}_j\rangle$ and $\hat{\mathbf{x}},\hat{\mathbf{y}}$ are coordinates w.r.t. $B$. **The inner product is uniquely determined through $\mathbf{A}$.** Symmetry of $\langle\cdot,\cdot\rangle$ ⇒ $\mathbf{A}$ symmetric; positive definiteness ⇒ $\forall\mathbf{x}\neq\mathbf{0}:\mathbf{x}^\top\mathbf{A}\mathbf{x}>0$ (Eq. 3.11).
- **Definition 3.4 ([[SymmetricPositiveDefiniteMatrix|Symmetric Positive Definite Matrix]])** (p. 74): a symmetric $\mathbf{A}\in\mathbb{R}^{n\times n}$ satisfying $\forall\mathbf{x}\in V\setminus\{\mathbf{0}\}:\mathbf{x}^\top\mathbf{A}\mathbf{x}>0$ (Eq. 3.11) is *symmetric positive definite* (or just *positive definite*); if only $\geq$ holds it is *symmetric positive semidefinite*.
- **Example 3.4 (SPD vs not)** (Eqs. 3.12–3.13, p. 74): $\mathbf{A}_1=\begin{bmatrix}9&6\\6&5\end{bmatrix}$ is SPD because $\mathbf{x}^\top\mathbf{A}_1\mathbf{x}=9x_1^2+12x_1x_2+5x_2^2=(3x_1+2x_2)^2+x_2^2>0$ for $\mathbf{x}\neq\mathbf{0}$. $\mathbf{A}_2=\begin{bmatrix}9&6\\6&3\end{bmatrix}$ is symmetric but *not* positive definite: $\mathbf{x}^\top\mathbf{A}_2\mathbf{x}=(3x_1+2x_2)^2-x_2^2$ can be $<0$ (e.g. $\mathbf{x}=[2,-3]^\top$).
- **SPD matrices define inner products** (Eq. 3.14): if $\mathbf{A}$ is SPD, $\langle\mathbf{x},\mathbf{y}\rangle=\hat{\mathbf{x}}^\top\mathbf{A}\hat{\mathbf{y}}$ is an inner product w.r.t. ordered basis $B$.
- **Theorem 3.5** (Eq. 3.15, p. 74): *for a real-valued, finite-dimensional vector space $V$ and an ordered basis $B$, $\langle\cdot,\cdot\rangle:V\times V\to\mathbb{R}$ is an inner product if and only if there exists a symmetric positive definite $\mathbf{A}\in\mathbb{R}^{n\times n}$ with $\langle\mathbf{x},\mathbf{y}\rangle=\hat{\mathbf{x}}^\top\mathbf{A}\hat{\mathbf{y}}$.* This is the load-bearing identification "inner products = SPD matrices."
- **Two further SPD properties** (p. 74): (i) the null space (kernel) of an SPD $\mathbf{A}$ is only $\mathbf{0}$ because $\mathbf{x}^\top\mathbf{A}\mathbf{x}>0$ for $\mathbf{x}\neq\mathbf{0}$, so $\mathbf{A}\mathbf{x}\neq\mathbf{0}$ for $\mathbf{x}\neq\mathbf{0}$; (ii) the diagonal elements $a_{ii}$ are positive because $a_{ii}=\mathbf{e}_i^\top\mathbf{A}\mathbf{e}_i>0$ ($\mathbf{e}_i$ the $i$-th standard basis vector).

### 3.3 Lengths and Distances (pp. 75–76)

- **Inner products induce norms** (Eq. 3.16, p. 75, marginal "Inner products induce norms."): any inner product induces a norm in a natural way, $\|\mathbf{x}\|:=\sqrt{\langle\mathbf{x},\mathbf{x}\rangle}$, so lengths can be computed from the inner product. **However, not every norm is induced by an inner product** — the Manhattan norm (3.3) is the standard counter-example. The chapter focuses on inner-product-induced norms.
- **Cauchy-Schwarz Inequality** (Remark, Eq. 3.17, p. 75): for an inner product space $(V,\langle\cdot,\cdot\rangle)$ the induced norm satisfies $|\langle\mathbf{x},\mathbf{y}\rangle|\leq\|\mathbf{x}\|\,\|\mathbf{y}\|$. See [[CauchySchwarzInequality]].
- **Example 3.5 (Lengths depend on the inner product)** (Eqs. 3.18–3.20, p. 75): for $\mathbf{x}=[1,1]^\top\in\mathbb{R}^2$, the dot product gives $\|\mathbf{x}\|=\sqrt{1^2+1^2}=\sqrt{2}$. Choosing instead $\langle\mathbf{x},\mathbf{y}\rangle=\mathbf{x}^\top\!\begin{bmatrix}1&-\tfrac12\\-\tfrac12&1\end{bmatrix}\!\mathbf{y}=x_1y_1-\tfrac12(x_1y_2+x_2y_1)+x_2y_2$ yields $\langle\mathbf{x},\mathbf{x}\rangle=1-1+1=1\Rightarrow\|\mathbf{x}\|=1$ — so $\mathbf{x}$ is "shorter" under this inner product. (This inner product returns smaller values than the dot product when $x_1,x_2$ have the same sign, larger otherwise.)
- **Definition 3.6 (Distance and [[Metric]])** (Eq. 3.21, p. 75): for an inner product space $(V,\langle\cdot,\cdot\rangle)$, the *distance* between $\mathbf{x},\mathbf{y}$ is $d(\mathbf{x},\mathbf{y}):=\|\mathbf{x}-\mathbf{y}\|=\sqrt{\langle\mathbf{x}-\mathbf{y},\mathbf{x}-\mathbf{y}\rangle}$. If the inner product is the dot product this is the *Euclidean distance*. The mapping $d:V\times V\to\mathbb{R}$, $(\mathbf{x},\mathbf{y})\mapsto d(\mathbf{x},\mathbf{y})$ (Eqs. 3.22–3.23) is a *metric*.
- **Distance needs only a norm, not an inner product** (Remark, p. 76): unlike length-via-inner-product, distance is well-defined for any norm; but if the norm comes from an inner product, the distance may vary with the choice of inner product.
- **Metric axioms** (p. 76): a metric $d$ is (1) *positive definite* $d(\mathbf{x},\mathbf{y})\geq 0$ for all $\mathbf{x},\mathbf{y}$ and $d(\mathbf{x},\mathbf{y})=0\iff\mathbf{x}=\mathbf{y}$; (2) *symmetric* $d(\mathbf{x},\mathbf{y})=d(\mathbf{y},\mathbf{x})$; (3) *triangle inequality* $d(\mathbf{x},\mathbf{z})\leq d(\mathbf{x},\mathbf{y})+d(\mathbf{y},\mathbf{z})$.
- **Inner products and metrics behave in opposite directions** (Remark, p. 76): comparing Def. 3.3 and Def. 3.6, *very similar $\mathbf{x}$ and $\mathbf{y}$ yield a large inner product but a small metric* — a subtle but important contrast.

### 3.4 Angles and Orthogonality (pp. 76–78)

- **Inner products define [[Angle|angles]]** (Eqs. 3.24–3.25, pp. 76–77): the Cauchy-Schwarz inequality (3.17) forces $-1\leq\frac{\langle\mathbf{x},\mathbf{y}\rangle}{\|\mathbf{x}\|\,\|\mathbf{y}\|}\leq 1$ for $\mathbf{x},\mathbf{y}\neq\mathbf{0}$, so there is a unique $\omega\in[0,\pi]$ with $\cos\omega=\frac{\langle\mathbf{x},\mathbf{y}\rangle}{\|\mathbf{x}\|\,\|\mathbf{y}\|}$ (Fig. 3.4 shows $\cos$ restricted to $[0,\pi]$ is invertible). $\omega$ is the *angle* between $\mathbf{x}$ and $\mathbf{y}$, measuring how similar their orientations are; e.g. $\mathbf{y}=4\mathbf{x}$ (a positive scaling) gives angle $0$.
- **Example 3.6 (Angle between vectors)** (Eq. 3.26, p. 77): for $\mathbf{x}=[1,1]^\top$, $\mathbf{y}=[1,2]^\top$ under the dot product, $\cos\omega=\frac{\mathbf{x}^\top\mathbf{y}}{\sqrt{\mathbf{x}^\top\mathbf{x}}\sqrt{\mathbf{y}^\top\mathbf{y}}}=\frac{3}{\sqrt{10}}$, so $\omega=\arccos\frac{3}{\sqrt{10}}\approx 0.32$ rad $\approx 18°$ (Fig. 3.5).
- **Definition 3.7 ([[Orthogonality]])** (p. 77): $\mathbf{x}$ and $\mathbf{y}$ are *orthogonal* iff $\langle\mathbf{x},\mathbf{y}\rangle=0$, written $\mathbf{x}\perp\mathbf{y}$; if additionally $\|\mathbf{x}\|=1=\|\mathbf{y}\|$ they are *orthonormal*. Implication: the $\mathbf{0}$-vector is orthogonal to every vector.
- **Orthogonality is inner-product-relative** (Remark, p. 77): orthogonality generalizes perpendicularity to bilinear forms that need not be the dot product; geometrically, orthogonal vectors have a "right angle with respect to a specific inner product."
- **Example 3.7 (Orthogonality depends on the inner product)** (Eqs. 3.27–3.28, pp. 77–78): $\mathbf{x}=[1,1]^\top$, $\mathbf{y}=[-1,1]^\top$ are orthogonal ($90°$) under the dot product, but under $\langle\mathbf{x},\mathbf{y}\rangle=\mathbf{x}^\top\!\begin{bmatrix}2&0\\0&1\end{bmatrix}\!\mathbf{y}$ we get $\cos\omega=-\tfrac13\Rightarrow\omega\approx 1.91$ rad $\approx 109.5°$, so they are *not* orthogonal. **Vectors orthogonal w.r.t. one inner product need not be orthogonal w.r.t. another** (Fig. 3.6).
- **Definition 3.8 ([[OrthogonalMatrix|Orthogonal Matrix]])** (Eqs. 3.29–3.30, p. 78): a square $\mathbf{A}\in\mathbb{R}^{n\times n}$ is *orthogonal* iff its columns are orthonormal, so $\mathbf{A}\mathbf{A}^\top=\mathbf{I}=\mathbf{A}^\top\mathbf{A}$, which implies $\mathbf{A}^{-1}=\mathbf{A}^\top$ — **the inverse is obtained by transposing.** Marginal note: *"It is convention to call these matrices 'orthogonal' but a more precise description would be 'orthonormal.' Transformations with orthogonal matrices preserve distances and angles."*
- **Orthogonal transformations preserve length and angle** (Eqs. 3.31–3.32, p. 78): for the dot product, $\|\mathbf{A}\mathbf{x}\|^2=(\mathbf{A}\mathbf{x})^\top(\mathbf{A}\mathbf{x})=\mathbf{x}^\top\mathbf{A}^\top\mathbf{A}\mathbf{x}=\mathbf{x}^\top\mathbf{x}=\|\mathbf{x}\|^2$ (length unchanged), and $\cos\omega=\frac{(\mathbf{A}\mathbf{x})^\top(\mathbf{A}\mathbf{y})}{\|\mathbf{A}\mathbf{x}\|\,\|\mathbf{A}\mathbf{y}\|}=\frac{\mathbf{x}^\top\mathbf{y}}{\|\mathbf{x}\|\,\|\mathbf{y}\|}$ (angle unchanged). Orthogonal matrices with $\mathbf{A}^\top=\mathbf{A}^{-1}$ define transformations that are *[[Rotation|rotations]]* (with the possibility of flips) — developed in §3.9.

### 3.5 Orthonormal Basis (pp. 78–79)

- **Setup** (p. 78): in an $n$-dim space a basis needs $n$ linearly independent vectors (§2.6.1). The *[[OrthonormalBasis|orthonormal basis (ONB)]]* is the special case where basis vectors are mutually orthogonal *and* each has length 1.
- **Definition 3.9 (Orthonormal Basis)** (Eqs. 3.33–3.34, p. 79): a basis $\{\mathbf{b}_1,\ldots,\mathbf{b}_n\}$ of $V$ is *orthonormal* if $\langle\mathbf{b}_i,\mathbf{b}_j\rangle=0$ for $i\neq j$ and $\langle\mathbf{b}_i,\mathbf{b}_i\rangle=1$ for all $i$; if only (3.33) holds it is an *orthogonal basis*. (3.34) says every basis vector has unit length/norm.
- **Construction via Gauss/Gram-Schmidt** (p. 79): concatenate a non-orthogonal, unnormalized basis $\{\tilde{\mathbf{b}}_1,\ldots,\tilde{\mathbf{b}}_n\}$ into a matrix $\tilde{\mathbf{B}}=[\tilde{\mathbf{b}}_1,\ldots,\tilde{\mathbf{b}}_n]$ and apply Gaussian elimination to the augmented matrix $[\tilde{\mathbf{B}}\tilde{\mathbf{B}}^\top\,|\,\tilde{\mathbf{B}}]$ to obtain an ONB. This iterative way to build an orthonormal basis is the *[[GramSchmidt|Gram-Schmidt process]]* (Strang 2003).
- **Example 3.8 (Orthonormal basis)** (Eq. 3.35, p. 79): the canonical/standard basis of a Euclidean $\mathbb{R}^n$ is an ONB under the dot product. In $\mathbb{R}^2$, $\mathbf{b}_1=\tfrac{1}{\sqrt2}[1,1]^\top$, $\mathbf{b}_2=\tfrac{1}{\sqrt2}[1,-1]^\top$ form an ONB ($\mathbf{b}_1^\top\mathbf{b}_2=0$, $\|\mathbf{b}_1\|=1=\|\mathbf{b}_2\|$). ONBs are exploited in SVM (Ch 12) and PCA (Ch 10).

### 3.6 Orthogonal Complement (pp. 79–80)

- **Definition (Orthogonal Complement)** (p. 79): for a $D$-dim space $V$ and $M$-dim subspace $U\subseteq V$, the *[[OrthogonalComplement|orthogonal complement]]* $U^\perp$ is the $(D-M)$-dim subspace of $V$ containing all vectors in $V$ orthogonal to every vector in $U$. Furthermore $U\cap U^\perp=\{\mathbf{0}\}$, so **any $\mathbf{x}\in V$ decomposes uniquely** (Eq. 3.36, p. 80): $\mathbf{x}=\sum_{m=1}^M\lambda_m\mathbf{b}_m+\sum_{j=1}^{D-M}\psi_j\mathbf{b}_j^\perp$, where $(\mathbf{b}_1,\ldots,\mathbf{b}_M)$ is a basis of $U$ and $(\mathbf{b}_1^\perp,\ldots,\mathbf{b}_{D-M}^\perp)$ a basis of $U^\perp$.
- **Normal vector** (p. 80): the orthogonal complement describes a plane $U$ (2-dim subspace) in a 3-dim space: the unit vector $\mathbf{w}$ ($\|\mathbf{w}\|=1$) orthogonal to $U$ is the basis vector of $U^\perp$, called the *normal vector* of $U$ (Fig. 3.7). Generally, orthogonal complements describe *hyperplanes* in $n$-dim vector and affine spaces — the basis for separating hyperplanes (Ch 12). See [[Hyperplane]].

### 3.7 Inner Product of Functions (pp. 80–81)

- **Generalizing inner products to functions** (p. 80): a finite vector $\mathbf{x}\in\mathbb{R}^n$ is a function with $n$ values; inner products generalize to vectors with countably/uncountably infinite entries — i.e. functions — by turning the sum (Eq. 3.5) into an integral.
- **[[InnerProductOfFunctions|Inner product of functions]]** (Eq. 3.37, p. 80): for $u,v:\mathbb{R}\to\mathbb{R}$, $\langle u,v\rangle:=\int_a^b u(x)v(x)\,dx$ for lower/upper limits $a,b<\infty$. As with the usual inner product, this defines norms and orthogonality: if (3.37) is $0$, $u$ and $v$ are *orthogonal functions*. Making this precise requires measures, integrals, and the notion of a **Hilbert space**; on functions the inner product may diverge (infinite value) — details deferred to functional analysis (not covered).
- **Example 3.9 (Orthogonal functions)** (p. 81): $u=\sin(x)$, $v=\cos(x)$ give an *odd* integrand $f(x)=u(x)v(x)$, so $\int_{-\pi}^{\pi}\sin(x)\cos(x)\,dx=0$ — $\sin$ and $\cos$ are orthogonal functions (Fig. 3.8).
- **Fourier connection** (Remark, p. 81): the collection $\{1,\cos(x),\cos(2x),\cos(3x),\ldots\}$ (Eq. 3.38) is orthogonal when integrated over $[-\pi,\pi]$; it spans a large subspace of even periodic functions, and **projecting functions onto this subspace is the fundamental idea behind Fourier series**. (§6.4.6 covers a second unconventional inner product: the inner product of random variables.)

### 3.8 Orthogonal Projections (pp. 81–90)

- **Why projections matter** (pp. 81–82): projections are a key class of linear transformations (besides rotations and reflections), important in graphics, coding theory, statistics and ML. High-dimensional data often has only a few informative dimensions; **projecting onto a lower-dimensional feature space** (marginal: *"'Feature' is a common expression for data representation."*) compresses data while retaining most information. PCA (Pearson 1901; Hotelling 1933) and deep auto-encoders (Deng et al. 2010) exploit this. Orthogonal projections retain as much information as possible and minimize the error between the original data and its projection (Fig. 3.9 shows 2-D data projected onto a line).
- **Definition 3.10 ([[ProjectionMatrix|Projection]] / [[ProjectionMatrix|projection matrix]])** (p. 82): for a vector space $V$ and subspace $U\subseteq V$, a linear mapping $\pi:V\to U$ is a *projection* if $\pi^2=\pi\circ\pi=\pi$ (idempotent). Since linear maps are transformation matrices (§2.7), the corresponding *projection matrices* $\mathbf{P}_\pi$ satisfy $\mathbf{P}_\pi^2=\mathbf{P}_\pi$. Derivations assume the dot product $\langle\mathbf{x},\mathbf{y}\rangle=\mathbf{x}^\top\mathbf{y}$ unless stated otherwise.

#### 3.8.1 Projection onto One-Dimensional Subspaces / Lines (pp. 82–85)

- **Setup** (p. 82): a *line* $U$ through the origin spanned by basis vector $\mathbf{b}\in\mathbb{R}^n$. The projection $\pi_U(\mathbf{x})\in U$ is the closest point in $U$ to $\mathbf{x}$. Two properties: (i) $\pi_U(\mathbf{x})$ minimizes $\|\mathbf{x}-\pi_U(\mathbf{x})\|$, so the segment $\pi_U(\mathbf{x})-\mathbf{x}$ is orthogonal to $U$ and hence to $\mathbf{b}$: orthogonality condition $\langle\pi_U(\mathbf{x})-\mathbf{x},\mathbf{b}\rangle=0$; (ii) $\pi_U(\mathbf{x})=\lambda\mathbf{b}$ for some $\lambda\in\mathbb{R}$ (multiple of the spanning vector).
- **Step 1 — coordinate $\lambda$** (Eqs. 3.39–3.41, p. 83): from $\langle\mathbf{x}-\lambda\mathbf{b},\mathbf{b}\rangle=0$ and bilinearity/symmetry, $\lambda=\frac{\langle\mathbf{x},\mathbf{b}\rangle}{\langle\mathbf{b},\mathbf{b}\rangle}=\frac{\langle\mathbf{b},\mathbf{x}\rangle}{\|\mathbf{b}\|^2}$; for the dot product $\lambda=\frac{\mathbf{b}^\top\mathbf{x}}{\mathbf{b}^\top\mathbf{b}}=\frac{\mathbf{b}^\top\mathbf{x}}{\|\mathbf{b}\|^2}$. If $\|\mathbf{b}\|=1$, then $\lambda=\mathbf{b}^\top\mathbf{x}$ (marginal: with a general inner product $\lambda=\langle\mathbf{x},\mathbf{b}\rangle$ if $\|\mathbf{b}\|=1$).
- **Step 2 — projection point** (Eqs. 3.42–3.44, p. 84): $\pi_U(\mathbf{x})=\lambda\mathbf{b}=\frac{\langle\mathbf{x},\mathbf{b}\rangle}{\|\mathbf{b}\|^2}\mathbf{b}=\frac{\mathbf{b}^\top\mathbf{x}}{\|\mathbf{b}\|^2}\mathbf{b}$ (last equality dot-product only). Its length $\|\pi_U(\mathbf{x})\|=|\lambda|\,\|\mathbf{b}\|=|\cos\omega|\,\|\mathbf{x}\|$ (Eq. 3.44, via Eq. 3.25), recovering the trigonometric picture: if $\|\mathbf{x}\|=1$ the projection onto a unit-$\mathbf{b}$ axis is exactly $\cos\omega$ (Fig. 3.10b).
- **Step 3 — projection matrix** (Eqs. 3.45–3.46, p. 84): $\pi_U(\mathbf{x})=\lambda\mathbf{b}=\mathbf{b}\frac{\mathbf{b}^\top\mathbf{x}}{\|\mathbf{b}\|^2}=\frac{\mathbf{b}\mathbf{b}^\top}{\|\mathbf{b}\|^2}\mathbf{x}$, so $\boxed{\mathbf{P}_\pi=\frac{\mathbf{b}\mathbf{b}^\top}{\|\mathbf{b}\|^2}}$. Marginal: *"Projection matrices are always symmetric."* $\mathbf{b}\mathbf{b}^\top$ is symmetric rank 1, $\|\mathbf{b}\|^2=\langle\mathbf{b},\mathbf{b}\rangle$ a scalar. Remark: $\pi_U(\mathbf{x})$ is still an $n$-dim vector, not a scalar, but only the single coordinate $\lambda$ is needed to express it in the basis $\mathbf{b}$.
- **Example 3.10 (Projection onto a line)** (Eqs. 3.47–3.48, p. 85): for $\mathbf{b}=[1,2,2]^\top$, $\mathbf{P}_\pi=\frac19\begin{bmatrix}1&2&2\\2&4&4\\2&4&4\end{bmatrix}$; for $\mathbf{x}=[1,1,1]^\top$, $\pi_U(\mathbf{x})=\frac19[5,10,10]^\top$. Idempotency check: $\mathbf{P}_\pi\pi_U(\mathbf{x})=\pi_U(\mathbf{x})$. Remark: with Ch 4 results $\pi_U(\mathbf{x})$ is an eigenvector of $\mathbf{P}_\pi$ with eigenvalue 1.

#### 3.8.2 Projection onto General Subspaces (pp. 85–88)

- **Setup** (pp. 85–86): project $\mathbf{x}\in\mathbb{R}^n$ onto an $m$-dim subspace $U\subseteq\mathbb{R}^n$ ($m\geq 1$) with ordered basis $(\mathbf{b}_1,\ldots,\mathbf{b}_m)$. Marginal warning: *"If $U$ is given by a set of spanning vectors, which are not a basis, make sure you determine a basis $\mathbf{b}_1,\ldots,\mathbf{b}_m$ before proceeding."* The projection is $\pi_U(\mathbf{x})=\sum_{i=1}^m\lambda_i\mathbf{b}_i=\mathbf{B}\boldsymbol\lambda$ (Eqs. 3.49–3.50), with $\mathbf{B}=[\mathbf{b}_1,\ldots,\mathbf{b}_m]\in\mathbb{R}^{n\times m}$, $\boldsymbol\lambda=[\lambda_1,\ldots,\lambda_m]^\top$.
- **Step 1 — normal equation** (Eqs. 3.51–3.57, pp. 86–87): "closest" ⇒ the connecting vector $\mathbf{x}-\pi_U(\mathbf{x})$ is orthogonal to *all* basis vectors of $U$, giving $m$ conditions $\mathbf{b}_i^\top(\mathbf{x}-\mathbf{B}\boldsymbol\lambda)=0$; stacking ⇒ $\mathbf{B}^\top(\mathbf{x}-\mathbf{B}\boldsymbol\lambda)=\mathbf{0}\iff\mathbf{B}^\top\mathbf{B}\boldsymbol\lambda=\mathbf{B}^\top\mathbf{x}$ — the *normal equation*. Since $\mathbf{b}_i$ are a basis (independent), $\mathbf{B}^\top\mathbf{B}\in\mathbb{R}^{m\times m}$ is regular and invertible, so $\boldsymbol\lambda=(\mathbf{B}^\top\mathbf{B})^{-1}\mathbf{B}^\top\mathbf{x}$ (Eq. 3.57). The matrix $(\mathbf{B}^\top\mathbf{B})^{-1}\mathbf{B}^\top$ is the *pseudo-inverse* of $\mathbf{B}$ (computable for non-square $\mathbf{B}$ provided $\mathbf{B}^\top\mathbf{B}$ is positive definite, i.e. $\mathbf{B}$ full rank). Marginal/text: in practice (e.g. linear regression) one adds a "jitter term" $\epsilon\mathbf{I}$ to $\mathbf{B}^\top\mathbf{B}$ for numerical stability and positive definiteness — this "ridge" is rigorously derivable via Bayesian inference (Ch 9).
- **Step 2 — projection point** (Eq. 3.58, p. 87): $\pi_U(\mathbf{x})=\mathbf{B}(\mathbf{B}^\top\mathbf{B})^{-1}\mathbf{B}^\top\mathbf{x}$.
- **Step 3 — projection matrix** (Eq. 3.59, p. 87): $\mathbf{P}_\pi=\mathbf{B}(\mathbf{B}^\top\mathbf{B})^{-1}\mathbf{B}^\top$. Remark: this generalizes the 1-D case — for $\dim(U)=1$, $\mathbf{B}^\top\mathbf{B}\in\mathbb{R}$ is a scalar and $\mathbf{P}_\pi$ reduces to $\frac{\mathbf{b}\mathbf{b}^\top}{\mathbf{b}^\top\mathbf{b}}$ (Eq. 3.46).
- **Example 3.11 (Projection onto a 2-D subspace)** (Eqs. 3.60–3.64, pp. 87–88): for $U=\operatorname{span}[[1,1,1]^\top,[0,1,2]^\top]\subseteq\mathbb{R}^3$ and $\mathbf{x}=[6,0,0]^\top$: $\mathbf{B}=\begin{bmatrix}1&0\\1&1\\1&2\end{bmatrix}$, $\mathbf{B}^\top\mathbf{B}=\begin{bmatrix}3&3\\3&5\end{bmatrix}$, $\mathbf{B}^\top\mathbf{x}=[6,0]^\top$, $\boldsymbol\lambda=[5,-3]^\top$, $\pi_U(\mathbf{x})=\mathbf{B}\boldsymbol\lambda=[5,2,-1]^\top$. The *projection error* (Eq. 3.63) is $\|\mathbf{x}-\pi_U(\mathbf{x})\|=\|[1,-2,1]^\top\|=\sqrt{6}$ (marginal: *"The projection error is also called the reconstruction error."*). The projection matrix (Eq. 3.64) is $\mathbf{P}_\pi=\frac16\begin{bmatrix}5&2&-1\\2&2&2\\-1&2&5\end{bmatrix}$. Verify via (a) $\pi_U(\mathbf{x})-\mathbf{x}\perp$ basis of $U$ and (b) $\mathbf{P}_\pi=\mathbf{P}_\pi^2$.
- **Least-squares solution** (text + marginal, p. 88): projections solve unsolvable linear systems $\mathbf{A}\mathbf{x}=\mathbf{b}$ — when $\mathbf{b}$ is not in $\operatorname{span}(\mathbf{A})$, project $\mathbf{b}$ onto the column space to get the *least-squares solution* of an overdetermined system (developed in §9.4). Reconstruction errors (3.63) are one route to derive PCA (§10.3).
- **ONB simplification** (Remark, Eqs. 3.65–3.66, p. 88): if the basis $\{\mathbf{b}_1,\ldots,\mathbf{b}_k\}$ is an ONB (3.33–3.34) then $\mathbf{B}^\top\mathbf{B}=\mathbf{I}$ and the projection collapses to $\pi_U(\mathbf{x})=\mathbf{B}\mathbf{B}^\top\mathbf{x}$ with coordinates $\boldsymbol\lambda=\mathbf{B}^\top\mathbf{x}$ — **no matrix inverse needed**, saving computation.

#### 3.8.3 Gram-Schmidt Orthogonalization (pp. 89–90)

- **[[GramSchmidt|Gram-Schmidt orthogonalization]]** (Eqs. 3.67–3.68, p. 89): constructively turns *any* basis $(\mathbf{b}_1,\ldots,\mathbf{b}_n)$ of an $n$-dim space into an orthogonal/orthonormal basis $(\mathbf{u}_1,\ldots,\mathbf{u}_n)$ with $\operatorname{span}[\mathbf{b}_1,\ldots,\mathbf{b}_n]=\operatorname{span}[\mathbf{u}_1,\ldots,\mathbf{u}_n]$ (such a basis always exists, Liesen & Mehrmann 2015). Recurrence: $\mathbf{u}_1:=\mathbf{b}_1$; $\mathbf{u}_k:=\mathbf{b}_k-\pi_{\operatorname{span}[\mathbf{u}_1,\ldots,\mathbf{u}_{k-1}]}(\mathbf{b}_k)$ for $k=2,\ldots,n$. Each $\mathbf{b}_k$ is projected onto the subspace spanned by the previously constructed $\mathbf{u}_1,\ldots,\mathbf{u}_{k-1}$ and that projection subtracted, yielding $\mathbf{u}_k$ orthogonal to that $(k-1)$-dim subspace. Normalizing the $\mathbf{u}_k$ gives an ONB.
- **Example 3.12 (Gram-Schmidt)** (Eqs. 3.69–3.71, pp. 89–90): for $\mathbf{b}_1=[2,0]^\top$, $\mathbf{b}_2=[1,1]^\top$ in $\mathbb{R}^2$ under the dot product: $\mathbf{u}_1=\mathbf{b}_1=[2,0]^\top$; $\mathbf{u}_2=\mathbf{b}_2-\frac{\mathbf{u}_1\mathbf{u}_1^\top}{\|\mathbf{u}_1\|^2}\mathbf{b}_2=[1,1]^\top-\begin{bmatrix}1&0\\0&0\end{bmatrix}[1,1]^\top=[0,1]^\top$, and indeed $\mathbf{u}_1^\top\mathbf{u}_2=0$ (Fig. 3.12 visualizes the three steps).

#### 3.8.4 Projection onto Affine Subspaces (pp. 90)

- **Projection onto an [[AffineSubspace|affine subspace]]** (Eq. 3.72, p. 90): given an affine space $L=\mathbf{x}_0+U$ with basis vectors $\mathbf{b}_1,\mathbf{b}_2$ of the direction space $U$, project $\mathbf{x}$ onto $L$ by reducing to the linear case: subtract the support point $\mathbf{x}_0$ (so $L-\mathbf{x}_0=U$), project $\mathbf{x}-\mathbf{x}_0$ onto $U$ (§3.8.2), and translate back: $\pi_L(\mathbf{x})=\mathbf{x}_0+\pi_U(\mathbf{x}-\mathbf{x}_0)$ (Fig. 3.13a–c).
- **Distance to an affine subspace** (Eqs. 3.73a–b, p. 90): $d(\mathbf{x},L)=\|\mathbf{x}-\pi_L(\mathbf{x})\|=\|\mathbf{x}-(\mathbf{x}_0+\pi_U(\mathbf{x}-\mathbf{x}_0))\|=d(\mathbf{x}-\mathbf{x}_0,\,\pi_U(\mathbf{x}-\mathbf{x}_0))=d(\mathbf{x}-\mathbf{x}_0,U)$ — the distance of $\mathbf{x}$ from $L$ equals the distance of $\mathbf{x}-\mathbf{x}_0$ from $U$. Used to derive the separating hyperplane in §12.1.

### 3.9 Rotations (pp. 91–94)

- **Setup** (p. 91): length and angle preservation (§3.4) are the two defining characteristics of linear mappings with orthogonal transformation matrices. *Rotations* are a specific such class. A *[[Rotation|rotation]]* is a linear mapping (more precisely, an *automorphism* of a Euclidean vector space) that rotates a plane by an angle $\theta$ about the origin (the origin is a fixed point); by convention a positive $\theta>0$ rotates counterclockwise (Fig. 3.14 example $\mathbf{R}=\begin{bmatrix}-0.38&-0.92\\0.92&-0.38\end{bmatrix}$, a $112.5°$ rotation). Application areas: computer graphics and robotics (Fig. 3.15 robotic arm).

#### 3.9.1 Rotations in $\mathbb{R}^2$ (p. 92)

- **[[ProjectionMatrix|Rotation matrix]] in 2-D** (Eqs. 3.75–3.76): rotating the standard basis $\{\mathbf{e}_1,\mathbf{e}_2\}$ by $\theta$ gives images $\Phi(\mathbf{e}_1)=[\cos\theta,\sin\theta]^\top$, $\Phi(\mathbf{e}_2)=[-\sin\theta,\cos\theta]^\top$ (trigonometry, Fig. 3.16); the rotated vectors remain linearly independent (a basis), so a rotation performs a basis change. The *rotation matrix* is $\mathbf{R}(\theta)=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}$.

#### 3.9.2 Rotations in $\mathbb{R}^3$ (pp. 92–93)

- **3-D rotations rotate a 2-D plane about a 1-D axis** (p. 92). "Counterclockwise" in $>2$ dimensions is defined by looking at the axis "head on, from the end toward the origin." The three planar rotations about the standard basis vectors (Eqs. 3.77–3.79, Fig. 3.17): about $\mathbf{e}_1$, $\mathbf{R}_1(\theta)=\begin{bmatrix}1&0&0\\0&\cos\theta&-\sin\theta\\0&\sin\theta&\cos\theta\end{bmatrix}$ (fixes $\mathbf{e}_1$, rotates the $\mathbf{e}_2\mathbf{e}_3$ plane); about $\mathbf{e}_2$, $\mathbf{R}_2(\theta)=\begin{bmatrix}\cos\theta&0&\sin\theta\\0&1&0\\-\sin\theta&0&\cos\theta\end{bmatrix}$; about $\mathbf{e}_3$, $\mathbf{R}_3(\theta)=\begin{bmatrix}\cos\theta&-\sin\theta&0\\\sin\theta&\cos\theta&0\\0&0&1\end{bmatrix}$.

#### 3.9.3 Rotations in $n$ Dimensions (pp. 93–94)

- **Definition 3.11 (Givens Rotation)** (Eqs. 3.80–3.81, pp. 93–94): generalizing to $n$ dimensions fixes $n-2$ dimensions and rotates a 2-D plane. For an automorphism $\Phi:V\to V$ with transformation matrix $\mathbf{R}_{ij}(\theta)$ equal to the identity $\mathbf{I}_n$ except $r_{ii}=\cos\theta$, $r_{ij}=-\sin\theta$, $r_{ji}=\sin\theta$, $r_{jj}=\cos\theta$ (for $1\leq i<j\leq n$), $\mathbf{R}_{ij}(\theta)$ is a *Givens rotation*. For $n=2$ this recovers (3.76).

#### 3.9.4 Properties of Rotations (p. 94)

- **Rotation properties** (p. 94), derivable from orthogonal-matrix structure (Def 3.8): (i) **rotations preserve distances** $\|\mathbf{x}-\mathbf{y}\|=\|\mathbf{R}_\theta(\mathbf{x})-\mathbf{R}_\theta(\mathbf{y})\|$; (ii) **rotations preserve angles** between $\mathbf{R}_\theta\mathbf{x}$ and $\mathbf{R}_\theta\mathbf{y}$; (iii) **rotations in 3+ dimensions are generally not commutative**, so order matters — *only in 2-D are rotations commutative*, $\mathbf{R}(\phi)\mathbf{R}(\theta)=\mathbf{R}(\theta)\mathbf{R}(\phi)$ for all $\phi,\theta\in[0,2\pi)$, forming an Abelian group (under multiplication) only when they rotate about the same point (e.g. the origin).

### 3.10 Further Reading (pp. 94–95)

- **Recommended texts** (p. 94): Axler (2015) and Boyd & Vandenberghe (2018) for broader/deeper coverage.
- **Where the geometry feeds ML** (pp. 94–95): inner products let us find orthogonal/orthonormal bases via Gram-Schmidt, important in optimization and numerical solvers — e.g. *Krylov subspace methods* (conjugate gradients, GMRES) minimize residual errors that are orthogonal to each other (Stoer & Bulirsch 2002). Inner products are central to *kernel methods* (Schölkopf & Smola 2002): many linear algorithms are expressible purely via inner products, and the *kernel trick* computes these implicitly in a (possibly infinite-dim) feature space without knowing it explicitly — enabling the "non-linearization" of algorithms (kernel-PCA, Schölkopf et al. 1997; Gaussian processes, Rasmussen & Williams 2006 — state of the art in probabilistic regression). Kernels are explored in Ch 12. Projections appear in computer graphics (shadows), optimization (iterative residual minimization), linear regression (Bishop 2006; §9.4), and PCA (Pearson 1901; Hotelling 1933; Ch 10).

## Key Quotes

> "In this chapter, we will add some geometric interpretation and intuition to all of these concepts. ... we equip the vector space with an inner product that induces the geometry of the vector space. Inner products and their corresponding norms and metrics capture the intuitive notions of similarity and distances..." — p. 70

> "Throughout this book, we will use the Euclidean norm (3.4) by default if not stated otherwise." — Remark, p. 72
>
> Establishes the default metric of the whole book; deviations from the dot product are always flagged.

> "A major purpose of inner products is to determine whether vectors are orthogonal to each other." — §3.2, p. 72

> "Inner products and norms are closely related in the sense that any inner product induces a norm ... in a natural way ... However, not every norm is induced by an inner product. The Manhattan norm (3.3) is an example of a norm without a corresponding inner product." — §3.3, p. 75 (with marginal note "Inner products induce norms.")

> "Similar to the length of a vector, the distance between vectors does not require an inner product: a norm is sufficient. If we have a norm induced by an inner product, the distance may vary depending on the choice of the inner product." — Remark, p. 76

> "At first glance, the lists of properties of inner products and metrics look very similar. However, by comparing Definition 3.3 with Definition 3.6 we observe that ⟨x, y⟩ and d(x, y) behave in opposite directions. Very similar x and y will result in a large value for the inner product and a small value for the metric." — Remark, p. 76
>
> The cleanest statement of why "similarity" (inner product) and "distance" (metric) are dual notions — the substrate of the SVM (Ch 12).

> "Orthogonality is the generalization of the concept of perpendicularity to bilinear forms that do not have to be the dot product. In our context, geometrically, we can think of orthogonal vectors as having a right angle with respect to a specific inner product." — Remark, §3.4, p. 77

> "It is convention to call these matrices 'orthogonal' but a more precise description would be 'orthonormal'. Transformations with orthogonal matrices preserve distances and angles." — marginal note, §3.4, p. 78
>
> Flags the standard terminology quirk: an "orthogonal matrix" actually has *orthonormal* columns.

> "Therefore, vectors that are orthogonal with respect to one inner product do not have to be orthogonal with respect to a different inner product." — Example 3.7, p. 78

> "Projection matrices are always symmetric." — marginal note, §3.8.1, p. 84

> "The projection error is also called the reconstruction error." — marginal note, §3.8.2, p. 88
>
> The bridge term to PCA (Ch 10), which is derived by minimizing reconstruction error.

> "The matrix (BᵀB)⁻¹Bᵀ is also called the pseudo-inverse of B ... In practical applications (e.g., linear regression), we often add a 'jitter term' εI to BᵀB to guarantee increased numerical stability and positive definiteness. This 'ridge' can be rigorously derived using Bayesian inference." — §3.8.2, p. 86–87
>
> Ties orthogonal projection directly to the OLS normal equations and ridge/Bayesian regularization (Ch 9).

> "The collection of functions in (3.38) spans a large subspace of the functions that are even and periodic on [−π, π), and projecting functions onto this subspace is the fundamental idea behind Fourier series." — Remark, §3.7, p. 81

> "A rotation is a linear mapping (more specifically, an automorphism of a Euclidean vector space) that rotates a plane by an angle θ about the origin ... For a positive angle θ > 0, by common convention, we rotate in a counterclockwise direction." — §3.9, p. 91

## Connections

- [[mml-book]] — umbrella source page; this is the Ch 3 deep dive (append in the Per-Chapter Deep Dives section).
- [[mml-ch02-linear-algebra|MML Ch 2]] — the abstract linear algebra (vector spaces, bases, linear mappings, affine spaces) this chapter adds geometry to. Inner products / norms were explicitly *deferred* to Ch 3 there.
- [[MarcDeisenroth]], [[AAldoFaisal]], [[ChengSoonOng]] — authors. [[CambridgeUniversityPress]] — publisher.
- [[AnalyticGeometry]] — the topic this chapter *is*.
- [[InnerProduct]] / [[DotProduct]] / [[BilinearForm]] — §3.2; the bilinear-symmetric-positive-definite mapping and its dot-product special case.
- [[Norm]] / [[Metric]] — §3.1, §3.3; inner products induce norms induce metrics.
- [[CauchySchwarzInequality]] — §3.3–3.4; makes the angle definition well-formed.
- [[Angle]] / [[Orthogonality]] — §3.4; cosine via inner product, orthogonality as zero inner product.
- [[OrthogonalMatrix]] — §3.4 Def 3.8; $\mathbf{A}^\top=\mathbf{A}^{-1}$, preserves length/angle.
- [[OrthonormalBasis]] — §3.5 Def 3.9 (resolves the Ch 2 forward-reference); [[OrthogonalComplement]] — §3.6; [[Hyperplane]] — normal vectors / separating hyperplanes.
- [[OrthogonalProjection]] / [[ProjectionMatrix|Projection]] / [[ProjectionMatrix]] / [[GramSchmidt]] — §3.8; the central ML operation, its closed forms, and the constructive ONB builder.
- [[InnerProductOfFunctions]] — §3.7; the integral inner product, Fourier-series substrate.
- [[Rotation]] — §3.9; geometry-preserving orthogonal transformation; Givens rotations.
- [[SymmetricPositiveDefiniteMatrix]] / [[GramMatrix]] — §3.2.3 Thm 3.5; SPD matrices characterize all inner products.
- [[AffineSubspace]] / [[VectorSubspace]] / [[Basis]] — §3.6, §3.8.4 reuse Ch 2 structures.
- **Downstream**: [[LinearRegression]] (Ch 9, least-squares = projection onto column space; ridge = jitter term), [[PrincipalComponentAnalysis|PCA]] (Ch 10, reconstruction-error projection), [[SupportVectorMachine|SVM]] / [[SeparatingHyperplane]] / [[Margin]] (Ch 12, distance to affine subspace), [[KernelTrick]] (Ch 12.4, inner-products-only algorithms), [[CholeskyDecomposition]] / [[Eigendecomposition]] (Ch 4, SPD revisited).

## Concepts introduced or canonicalized here

New pages created from this chapter: [[Metric]], [[BilinearForm]], [[Angle]], [[Orthogonality]], [[OrthogonalMatrix]], [[OrthonormalBasis]], [[OrthogonalComplement]], [[ProjectionMatrix]] (which also documents the *projection* Def 3.10), [[GramSchmidt]], [[Rotation]], [[InnerProductOfFunctions]].

Enriched existing pages: [[Norm]], [[InnerProduct]], [[DotProduct]], [[OrthogonalProjection]], [[CauchySchwarzInequality]], [[AnalyticGeometry]], [[SymmetricPositiveDefiniteMatrix]], [[GramMatrix]].

## Contradictions

- **"Orthogonal matrix" is a misnomer** — the book itself flags it (marginal note, p. 78): an orthogonal matrix has *orthonormal* columns. Noted on [[OrthogonalMatrix]]; not a contradiction of fact, just standard-terminology drift.
- **Default-inner-product dependence is not a contradiction but a recurring quirk**: lengths, angles, and orthogonality are *not* intrinsic to vectors — they change with the chosen inner product (Examples 3.5, 3.7). The wiki's [[DotProduct]]/[[Norm]] pages quietly assume the dot product / Euclidean norm (matching the book's default), so cross-references must remember the general case exists.
- **`GramMatrix.md` was CV/style-transfer-framed** (Gatys-style neural style transfer, [[d2l-computer-vision]]). The MML Ch 3 view (Gram matrix of basis inner products $A_{ij}=\langle\mathbf{b}_i,\mathbf{b}_j\rangle$, and $\mathbf{B}^\top\mathbf{B}$ in the normal equation) is added alongside rather than overwriting that perspective.
- **`OrthogonalProjection.md` already cited a column-space matrix $\mathbf{B}(\mathbf{B}^\top\mathbf{B})^{-1}\mathbf{B}^\top$ using $\mathbf{B}\in\mathbb{R}^{D\times M}$** before this ingest; MML §3.8 uses $\mathbf{B}\in\mathbb{R}^{n\times m}$. Same formula, only index letters differ — harmonized in the enrichment.
- **No deep contradictions of fact.** The treatment is consistent with the existing geometry pages and with [[mml-ch02-linear-algebra|Ch 2]]; it supplies the *inner-product geometry* layer those pages reference.
