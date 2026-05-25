---
title: "IIR Ch. 18: Matrix Decompositions and Latent Semantic Indexing"
type: source
tags: [iir, information-retrieval, textbook, lsi, lsa, svd, matrix-decomposition]
date: 2026-05-23
source_file: "https://nlp.stanford.edu/IR-book/html/htmledition/matrix-decompositions-and-latent-semantic-indexing-1.html"
---

## Summary

Chapter 18 of *Introduction to Information Retrieval* (Manning, Raghavan, Schütze 2008) introduces the linear algebra machinery — eigendecomposition and the singular value decomposition (SVD) — needed to construct **low-rank approximations of the term–document matrix**, and applies these to **Latent Semantic Indexing (LSI)**. The central object is the m×n term–document matrix C, "each of whose rows represents a term and each of whose columns represents a document." The chapter develops, in order: (1) a linear-algebra review of rank, eigenvalues, and eigenvectors; (2) matrix diagonalization S = UΛU⁻¹ and the symmetric form S = QΛQᵀ; (3) the SVD theorem C = UΣVᵀ that generalizes diagonalization to non-square matrices; (4) the **Eckart–Young theorem**, showing the truncated SVD Cₖ = UₖΣₖVₖᵀ is the optimal rank-k approximation under the [[FrobeniusNorm]] with error σ_{k+1}; and (5) LSI, where the same low-rank approximation is reinterpreted as a projection of documents and queries into a k-dimensional **latent semantic space**. The motivation for LSI is to overcome two fundamental failure modes of the [[VectorSpaceModel]]: **[[Synonymy]]** (different words with the same meaning depress similarity) and **[[Polysemy]]** (one word with multiple meanings inflates similarity). Queries are folded into the latent space via q_k = Σ_k⁻¹ U_kᵀ q. The chapter reports that, empirically (Dumais 1993, 1995), choosing k in the low hundreds can *increase* precision on TREC benchmarks, but notes that LSI has "not been established as a significant force in scoring and ranking for information retrieval" and "remains an intriguing approach to clustering."

## Key Claims

- The term–document matrix C is an m×n matrix; m is vocabulary size, n is document count. Rank r ≤ min{m, n}.
- For a square matrix C and non-zero vector x satisfying Cx = λx, λ is an eigenvalue and x a right eigenvector; the eigenvector for the eigenvalue of largest magnitude is the **principal eigenvector**.
- The number of non-zero eigenvalues of a matrix is at most its rank.
- Eigenvalues are roots of the characteristic polynomial |C − λI| = 0 and can be complex even when C is real.
- For a real symmetric matrix, eigenvalues are real and eigenvectors corresponding to distinct eigenvalues are orthogonal.
- **Matrix diagonalization theorem**: any square real matrix S with n linearly independent eigenvectors admits S = UΛU⁻¹, where columns of U are eigenvectors and Λ is diagonal with eigenvalues sorted in decreasing order (λ₁ ≥ λ₂ ≥ … ≥ λₙ). The decomposition is unique when eigenvalues are distinct.
- **Symmetric diagonalization theorem**: a symmetric S admits S = QΛQᵀ, with Q orthogonal (Q⁻¹ = Qᵀ) and all entries real.
- **SVD theorem**: any m×n matrix C of rank r factors as C = UΣVᵀ, where U is m×m with orthonormal columns equal to eigenvectors of CCᵀ, V is n×n with orthonormal columns equal to eigenvectors of CᵀC, and Σ is an m×n diagonal-shaped matrix whose first r diagonal entries are the **singular values** σᵢ = √λᵢ, σ₁ ≥ σ₂ ≥ … ≥ σ_r > 0.
- The non-zero eigenvalues of CCᵀ equal those of CᵀC; CCᵀ = UΣ²Uᵀ and CᵀC = VΣ²Vᵀ.
- A "reduced SVD" drops zero columns/rows of Σ and unused columns of U, V — important for computational efficiency on real corpora.
- **Eckart–Young theorem (Theorem 18.3)**: the rank-k truncation Cₖ = UₖΣₖVₖᵀ obtained by zeroing the r − k smallest singular values is the closest rank-k matrix to C in Frobenius norm; its error equals σ_{k+1}.
- Cₖ is the sum of k rank-1 matrices: Cₖ = Σᵢ₌₁ᵏ σᵢ uᵢ vᵢᵀ — each term weighted by a singular value.
- LSI applies Eckart–Young to the term–document matrix and reinterprets the k retained dimensions as **latent concepts** or **semantic dimensions** capturing co-occurrence structure.
- LSI mitigates **synonymy** ("car" and "automobile" can map to similar latent dimensions) and partially addresses **polysemy** (a polysemous term's vector is a blend of its senses, weighted by document mix).
- **Query folding**: a query (or new document) vector q is projected into the latent space by q_k = Σ_k⁻¹ U_kᵀ q. Similarity is then computed in ℝᵏ (typically via cosine) against rows of Σ_k V_kᵀ (the document vectors in latent space).
- A value of k in the low hundreds can *improve* precision on benchmarks (Dumais 1993, 1995), particularly when query and relevant documents share few literal terms.
- LSI is computationally expensive: SVD on large sparse term–document matrices is costly; reported experiments did not exceed ~1M documents, and folded-in documents degrade representation quality over time, requiring periodic re-decomposition.
- LSI inherits vector-space limitations: it cannot express negation or enforce Boolean constraints. Folded query vectors become **dense**, increasing scoring cost.
- LSI can be viewed as **soft clustering**, with the k retained dimensions interpreted as fractional cluster memberships of terms/documents.

## Section Notes

### 18.1 Linear algebra review

The chapter opens with a compressed review. **Rank** is the number of linearly independent rows (equivalently columns). For C ∈ ℝᵐˣⁿ, rank(C) ≤ min(m, n). An **eigenvalue** λ and **right eigenvector** x of a square matrix C satisfy C x = λ x; left eigenvectors satisfy yᵀ C = λ yᵀ. The **principal eigenvector** is the one whose eigenvalue has largest magnitude — this notion underlies PageRank and many spectral methods. Eigenvalues solve |C − λI| = 0, an nth-order polynomial with up to n complex roots. For real symmetric S, all eigenvalues are real and eigenvectors for distinct eigenvalues are orthogonal — this is what allows the orthonormal symmetric diagonalization that grounds the SVD.

### 18.2 Matrix decompositions

Two diagonalization results anchor everything else. The general **matrix diagonalization theorem** says S = U Λ U⁻¹ whenever S has n linearly independent eigenvectors; columns of U are those eigenvectors, Λ is diagonal with eigenvalues in decreasing order, and the factorization is unique up to ordering when eigenvalues are distinct. The **symmetric diagonalization theorem** strengthens this: if S is real symmetric, U can be chosen orthogonal — written Q with Q⁻¹ = Qᵀ — giving S = Q Λ Qᵀ. Because CCᵀ and CᵀC are symmetric positive semidefinite for any real C, this symmetric form is exactly what makes the SVD work.

### 18.3 Term–document matrices and singular value decompositions

The SVD generalizes diagonalization to rectangular matrices. For an m×n matrix C of rank r:

**C = U Σ Vᵀ**

with U (m×m) holding eigenvectors of CCᵀ ("term–term co-occurrence"), V (n×n) holding eigenvectors of CᵀC ("document–document co-occurrence"), and Σ (m×n) diagonal in shape with entries σᵢ = √λᵢ where λᵢ are the (shared) non-zero eigenvalues of CCᵀ and CᵀC. The σᵢ are the **singular values**, ordered σ₁ ≥ σ₂ ≥ … ≥ σ_r > 0. Squaring the SVD recovers the eigendecompositions: CCᵀ = U Σ² Uᵀ and CᵀC = V Σ² Vᵀ. In practice the **reduced SVD** drops the zero block of Σ, keeping only an r×r diagonal matrix and the corresponding columns of U and V.

### 18.4 Low-rank approximations

Given C and a target rank k < r, the goal is to find the rank-k matrix Cₖ minimizing the **Frobenius norm** ‖C − Cₖ‖_F (the square root of the sum of squared entries). The constructive recipe is:

1. Compute SVD C = U Σ Vᵀ.
2. Form Σₖ by zeroing the r − k smallest singular values (keeping σ₁, …, σₖ).
3. Set Cₖ = U Σₖ Vᵀ.

The **Eckart–Young theorem** asserts this is optimal: no rank-k matrix achieves lower Frobenius error, and the error is exactly σ_{k+1}. Equivalently Cₖ = Σᵢ₌₁ᵏ σᵢ uᵢ vᵢᵀ — a sum of k rank-1 outer products weighted by decreasing singular values, so the leading terms carry most of the spectral energy. The truncated form uses Uₖ (first k columns of U), the k×k diagonal Σₖ, and Vₖ (first k columns of V), avoiding multiplications that vanish.

### 18.5 Latent semantic indexing

LSI replaces C with its low-rank approximation Cₖ and treats columns of Cₖ as **documents in a k-dimensional latent space**. The k retained dimensions are the directions of largest spectral variance in term–document co-occurrence — interpreted as **latent concepts** or **semantic dimensions** that group co-occurring terms. This addresses two failures of the literal [[VectorSpaceModel]]:

- **Synonymy**: when two terms (e.g. *car*, *automobile*) tend to occur in similar documents, the SVD assigns them similar coordinates in the latent space, so documents using only one of the pair still appear close to queries using the other.
- **Polysemy**: less perfectly handled; a polysemous term receives a single latent vector that is a blend of its senses, so similarity can still be inflated or distorted depending on the corpus mix.

**Query folding** projects a query vector q ∈ ℝᵐ into the latent space:

**q_k = Σ_k⁻¹ U_kᵀ q**

Documents live at the rows of Σ_k V_kᵀ (equivalently, the columns of Cₖ projected via U_kᵀ and rescaled by Σ_k⁻¹ when one wants both queries and documents in the same coordinates). Cosine similarity between q_k and document vectors in the latent space then ranks results. The same fold-in trick can incrementally insert new documents without re-running SVD, though Dumais and others note that this degrades the approximation quality over time and periodic re-decomposition is needed.

Empirically (Dumais 1993, 1995, on TREC benchmarks using the Lanczos algorithm for sparse SVD), choosing k in the **low hundreds** can increase precision relative to the literal vector space — especially when relevant documents share few literal terms with the query. The chapter cautions that SVD on million-document corpora is computationally heavy, and that no successfully reported experiment had exceeded roughly that scale at time of writing. LSI further inherits the vector-space inability to express **negation** or **Boolean conditions**, and the folded query becomes **dense**, raising per-document scoring cost. The chapter ends by framing LSI as a form of **soft clustering** — the k dimensions act as fractional cluster memberships of terms and documents — and suggests this clustering interpretation is where LSI remains most interesting.

### 18.6 References and further reading

Strang (1986) is recommended as the introductory reference for matrix decompositions and SVD. The Eckart–Young theorem appears in Eckart & Young (1936). The connection between IR and low-rank approximation was introduced by **Deerwester, Dumais, Furnas, Landauer & Harshman (1990)** in the foundational LSI paper; **Berry et al. (1995)** provided a subsequent survey. **Dumais (1993, 1995)** reports the TREC experiments. **Schütze & Silverstein (1997)** evaluate LSI for clustering. **Bast & Majumdar (2005)** analyze the role of k. Cross-language IR applications are due to **Berry & Young (1995)** and **Littman et al. (1998)**. Probabilistic extensions include **Hofmann (1999a,b)** (PLSA) and **Blei, Ng & Jordan (2003)** (LDA); further developments by **Rosen-Zvi et al. (2004)**, **Wei & Croft (2006)**, and **Teh et al. (2006)** (Hierarchical Dirichlet Processes).

## Algorithms & Formulas

**Eigendecomposition (general square S with n linearly independent eigenvectors)**

S = U Λ U⁻¹
- U: columns are eigenvectors of S
- Λ: diag(λ₁, λ₂, …, λₙ), sorted |λ₁| ≥ |λ₂| ≥ … ≥ |λₙ|

**Symmetric eigendecomposition (real symmetric S)**

S = Q Λ Qᵀ, with Qᵀ Q = I (Q orthogonal, all entries real).

**Singular Value Decomposition (any real m×n matrix C of rank r)**

C = U Σ Vᵀ
- U ∈ ℝᵐˣᵐ orthonormal columns; columns are eigenvectors of CCᵀ.
- V ∈ ℝⁿˣⁿ orthonormal columns; columns are eigenvectors of CᵀC.
- Σ ∈ ℝᵐˣⁿ diagonal-shaped; Σᵢᵢ = σᵢ = √λᵢ (eigenvalues shared by CCᵀ and CᵀC), σ₁ ≥ σ₂ ≥ … ≥ σ_r > 0; remaining entries zero.
- Consequences: CCᵀ = U Σ² Uᵀ, CᵀC = V Σ² Vᵀ.

**Reduced SVD**

Keep only the r non-zero singular values: C = U_r Σ_r V_rᵀ, with U_r ∈ ℝᵐˣʳ, Σ_r ∈ ℝʳˣʳ, V_r ∈ ℝⁿˣʳ.

**Truncated SVD / low-rank approximation (rank k ≤ r)**

Cₖ = Uₖ Σₖ Vₖᵀ = Σᵢ₌₁ᵏ σᵢ uᵢ vᵢᵀ
- Uₖ: first k columns of U (m×k).
- Σₖ: top-left k×k block of Σ (or full Σ with σ_{k+1}…σ_r zeroed).
- Vₖ: first k columns of V (n×k).

**Eckart–Young theorem (Theorem 18.3)**

For every rank-k matrix Z ∈ ℝᵐˣⁿ:
‖C − Cₖ‖_F ≤ ‖C − Z‖_F
with equality achieved by Cₖ, and ‖C − Cₖ‖_F = σ_{k+1}.

**Frobenius norm**

‖A‖_F = √(Σᵢⱼ Aᵢⱼ²) = √(Σᵢ σᵢ²)

**LSI document representation**

Documents are the columns of Cₖ; equivalently, in latent coordinates, the rows of Σₖ Vₖᵀ (k×n matrix).

**LSI query folding**

For a query vector q ∈ ℝᵐ (e.g. TF-IDF-weighted):
q_k = Σ_k⁻¹ U_kᵀ q ∈ ℝᵏ
Then rank documents d_j by cosine similarity in the latent space:
score(q, d_j) = cos(q_k, (Σₖ Vₖᵀ)_{:,j})

**Fold-in (incremental new document d ∈ ℝᵐ)**

d_k = Σ_k⁻¹ U_kᵀ d
(degrades approximation over time; periodic re-SVD needed).

## Key Quotes

> "[An] m × n matrix C, each of whose rows represents a term and each of whose columns represents a document." — defining the term–document matrix.

> "The eigenvector corresponding to the eigenvalue of largest magnitude is called the principal eigenvector." — §18.1.

> "The number of non-zero eigenvalues of C is at most rank(C)." — §18.1.

> "These eigenvalues can in general be complex, even if all entries of C are real." — §18.1.

> "If S is both real and symmetric, the eigenvalues are all real." — §18.1.

> "Let S be a square real-valued matrix with n linearly independent eigenvectors. Then there exists an eigen decomposition S = UΛU⁻¹." — §18.2.

> "C = UΣVᵀ" — §18.3, the SVD theorem applied to the term–document matrix.

> "For 1 ≤ i ≤ r, let σᵢ = √λᵢ, with λᵢ ≥ λᵢ₊₁." — §18.3, definition of singular values.

> "The eigenvalues λ₁, …, λᵣ of CCᵀ are the same as the eigenvalues of CᵀC." — §18.3.

> "Cₖ = Σᵢ₌₁ᵏ σᵢ uᵢ vᵢᵀ" — §18.4, low-rank decomposition as a sum of rank-1 outer products.

> "The rank-k approximation incurs an error (measured by Frobenius norm) equal to σ_{k+1}." — §18.4, Eckart–Young.

> "Two different words (say car and automobile) have the same meaning." — §18.5, on synonymy.

> "Could we use the co-occurrences of terms … to capture the latent semantic associations?" — §18.5, the LSI motivation.

> "q_k = Σ_k⁻¹ U_kᵀ q" — §18.5, query-folding formula.

> "A value of k in the low hundreds can actually increase precision on some query benchmarks." — §18.5, Dumais's TREC finding.

> "Latent semantic indexing has not been established as a significant force in scoring and ranking for information retrieval, [but] it remains an intriguing approach to clustering." — chapter overview.

## Connections

- [[InformationRetrieval]] — LSI is an IR retrieval model layered over the term–document matrix.
- [[VectorSpaceModel]] — LSI extends the vector space model by replacing literal term axes with k latent semantic axes.
- [[LatentSemanticIndexing]] — the IR-side name for the technique introduced in this chapter.
- [[LatentSemanticAnalysis]] — the same construction studied outside IR (psycholinguistics, semantic similarity); equivalent math, different applications.
- [[SingularValueDecomposition]] — the core matrix factorization C = UΣVᵀ.
- [[LowRankApproximation]] — the general problem; LSI uses truncated SVD as its specific instance.
- [[EckartYoungTheorem]] — formal optimality result for truncated SVD under Frobenius norm.
- [[FrobeniusNorm]] — the matrix norm under which Eckart–Young is optimal.
- [[Eigenvector]] — columns of U and V in the SVD are eigenvectors of CCᵀ and CᵀC respectively.
- [[Eigenvalue]] — singular values are square roots of the (shared) eigenvalues of CCᵀ and CᵀC.
- [[Eigendecomposition]] — SVD reduces to eigendecomposition when applied to CCᵀ or CᵀC.
- [[MatrixDecomposition]] — general framework; SVD is the rectangular generalization of symmetric eigendecomposition.
- [[Synonymy]] — the primary linguistic phenomenon LSI is designed to mitigate.
- [[Polysemy]] — partially addressed by latent dimensions; remains a known LSI weakness.
- [[SusanDumais]] — TREC experiments demonstrating LSI precision gains (1993, 1995); co-author of original LSI paper.
- [[ScottDeerwester]] — lead author of Deerwester et al. (1990), the foundational LSI paper.

## Contradictions

- LSI's clustering interpretation (soft cluster memberships via the k latent dimensions) overlaps and partially contests the hard-partition view of [[KMeansClustering]] and the agglomerative hierarchy view in [[HierarchicalClustering]] (IIR Ch. 16–17); LSI offers a *continuous*, dimensionality-reduction perspective on the same co-occurrence signal.
- LSI's "ignore literal term match" stance contradicts the [[VectorSpaceModel]] assumption (IIR Ch. 6) that exact term overlap is the primary similarity signal — LSI deliberately blurs term identity to gain semantic recall, at some cost to precision when queries are already well-matched lexically.
- Probabilistic topic models (PLSA, LDA — Hofmann 1999; Blei, Ng, Jordan 2003) reframe LSI's latent dimensions as generative latent variables with proper probabilistic semantics, and are often presented as superseding LSI on principled grounds, though direct precision comparisons remain mixed.
