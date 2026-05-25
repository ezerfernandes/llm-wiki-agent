---
title: "Latent Semantic Indexing (LSI)"
type: concept
tags: [information-retrieval, dimensionality-reduction, svd, latent-semantics]
sources: [iir-ch18-lsi-matrix-decompositions]
last_updated: 2026-05-23
---

Apply truncated [[SingularValueDecomposition]] to the term-document matrix $C$ to project queries and documents into a lower-dimensional "latent concept" space:

$$C \approx C_k = U_k\,\Sigma_k\,V_k^T$$

where $C_k$ retains the top-$k$ singular triples. By the **Eckart-Young theorem**, $C_k$ minimizes $\|C - C_k\|_F$ over all rank-$k$ matrices (in [[FrobeniusNorm]]), so it is the optimal $k$-dimensional approximation.

**Query folding** maps a new query into the latent space:

$$q_k = \Sigma_k^{-1} U_k^T q$$

Retrieval proceeds via cosine similarity *in the reduced space*. The $k$ latent dimensions are interpretable (loosely) as **concepts** — clusters of co-occurring terms — which gives LSI two partial fixes for the lexical-matching brittleness of the raw [[VectorSpaceModel]]:

- **Synonymy** (different terms for the same concept): synonyms project to similar latent coordinates because they share documents.
- **Polysemy** (same term for different concepts): partially handled because one term contributes to multiple latent dimensions, but LSI does not fully disambiguate.

Outside the IR context the same construction is called **LSA** (Latent Semantic Analysis). LSI is the conceptual ancestor of modern dense neural [[EmbeddingBasedRetrieval]] — both project terms and documents into a learned lower-dimensional space where semantically related items are nearby — but LSI's projection is a deterministic linear-algebra computation, whereas neural embeddings are learned with gradient descent on a downstream objective. Originated in [[ScottDeerwester]] / [[SusanDumais]] et al. (1990). Full treatment in [[iir-ch18-lsi-matrix-decompositions]].
