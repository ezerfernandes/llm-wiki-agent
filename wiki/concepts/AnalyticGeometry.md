---
title: "Analytic Geometry"
type: concept
tags: [analytic-geometry, linear-algebra, foundational]
sources: [mml-ch03-analytic-geometry, mml-book]
last_updated: 2026-06-04
---

# Analytic Geometry

Geometric structure added to vector spaces via [[InnerProduct]]s and [[Norm]]s — gives length, distance, angle, [[OrthogonalProjection]]. Covered in [[mml-book]] Ch 3.

## From [[mml-ch03-analytic-geometry|MML Ch 3]]

Analytic geometry is what you get when you **equip the abstract vector space of Ch 2 with an [[InnerProduct]]**, inducing all of geometry. The dependency chain (Fig. 3.1 mind map):

$$\text{[[InnerProduct|Inner product]]} \;\xrightarrow{\text{induces}}\; \text{[[Norm|Norm]] (length)} \;\rightarrow\; \text{[[Metric|Metric]] (distance)}$$

and, via the [[CauchySchwarzInequality]], the inner product also defines the [[Angle]] between vectors and hence [[Orthogonality]]. Orthogonality yields [[OrthonormalBasis|orthonormal bases]] (built by [[GramSchmidt]]), the [[OrthogonalComplement]] (normal vectors, [[Hyperplane|hyperplanes]]), and — the chapter's payload — the [[OrthogonalProjection]] (via a [[ProjectionMatrix]]). The chapter closes with [[Rotation|rotations]] as a geometry-preserving [[OrthogonalMatrix|orthogonal transformation]].

**The recurring lesson**: lengths, distances, angles, and orthogonality are *not intrinsic* to vectors — they depend on the chosen inner product. The book uses the dot product / Euclidean norm by default but flags every deviation ([[mml-book]] Examples 3.5, 3.7).

**Downstream**: orthogonal projection is the operation behind least-squares [[LinearRegression]] (Ch 9), [[PrincipalComponentAnalysis|PCA]] (Ch 10), and SVM margins / [[SeparatingHyperplane|separating hyperplanes]] (Ch 12); [[SymmetricPositiveDefiniteMatrix|SPD matrices]] characterize all inner products (Thm 3.5), tying into kernels (Ch 12.4) and covariance/Gaussian objects.

See the [[mml-ch03-analytic-geometry|Ch 3 deep dive]] for the full per-section treatment.
