---
title: "Eckart-Young Theorem"
type: concept
tags: [linear-algebra, matrix-approximation, svd]
sources: [iir-ch18-lsi-matrix-decompositions]
last_updated: 2026-05-23
---

For any matrix $C$ with [[SingularValueDecomposition]] $C = U\Sigma V^T$, the **truncated SVD**

$$C_k = U_k\,\Sigma_k\,V_k^T$$

(retaining the top-$k$ singular triples) is the **best rank-$k$ approximation** to $C$ in **[[FrobeniusNorm]]**:

$$C_k = \arg\min_{\text{rank}(X) \leq k} \|C - X\|_F$$

with the optimum

$$\|C - C_k\|_F = \sqrt{\sigma_{k+1}^2 + \sigma_{k+2}^2 + \cdots + \sigma_{\min(m,n)}^2}$$

i.e. the residual is the root-sum-of-squares of the *discarded* singular values. (The theorem also holds in the spectral / operator 2-norm, with residual $\sigma_{k+1}$.)

**Why it matters**:
- **[[LatentSemanticIndexing]]**: licenses the use of truncated SVD as the *optimal* low-rank projection of the term-document matrix — there is no better rank-$k$ approximation under Frobenius loss.
- **Dimensionality reduction generally**: justifies PCA (which is SVD after centering) as the optimal linear-projection-to-$k$-dimensions in mean-square error.
- **Compression**: $C_k$ has effective rank $k$ and can be stored as $U_k$ ($m \times k$) + $\Sigma_k$ ($k$) + $V_k$ ($n \times k$), totaling $k(m + n + 1)$ entries vs $mn$ for the full matrix — a major saving when $k \ll \min(m, n)$.

**Choosing $k$**: typical IR practice picks $k$ such that the retained singular values capture some fraction (e.g. 80%) of the total squared spectrum: $\sum_{i \leq k} \sigma_i^2 / \sum_i \sigma_i^2 \geq 0.8$.

Originally proved by Carl Eckart and Gale Young (1936). Full treatment in [[iir-ch18-lsi-matrix-decompositions]] §18.3.
