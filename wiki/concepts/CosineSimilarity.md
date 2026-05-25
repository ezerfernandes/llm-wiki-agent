---
title: "Cosine Similarity"
type: concept
tags: [analytic-geometry, similarity, foundational]
sources: [d2l-appendix-mathematics, hands-on-llm-ch04-text-classification, hands-on-llm-ch05-text-clustering-topic-modeling, hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# Cosine Similarity

The cosine of the angle between two vectors — a magnitude-invariant similarity measure ([[d2l-appendix-mathematics]] §geometry-linear-algebraic-ops):

$$\cos(\theta) = \frac{\mathbf{v}\cdot\mathbf{w}}{\|\mathbf{v}\|\,\|\mathbf{w}\|}.$$

Maximum value $+1$ when $\mathbf{v}$ and $\mathbf{w}$ point in the same direction, minimum $-1$ when they point opposite, and $0$ when they are orthogonal.

## Why magnitude-invariant matters

[[d2l-appendix-mathematics]] §geometry-linear-algebraic-ops motivates cosine similarity via image brightness: an image and its $0.1\times$-brightness duplicate sit at very different Euclidean distances but at *zero* angle to each other — *"the angle between $\mathbf{v}$ and $0.1\mathbf{v}$ is zero."* For most ML applications (image content, document topic, semantic similarity) we want similarity to ignore overall magnitude.

For text counts, doubling the document length doubles the word-count vector but leaves cosine similarity unchanged — exactly the desired behavior.

## Caveat in high dimensions

[[d2l-appendix-mathematics]] flags: *"if the components of high-dimensional vectors are sampled randomly with mean 0, their cosine will nearly always be close to 0."* In $d$ dimensions, two random Gaussian vectors are nearly orthogonal with high probability — so cosine similarity needs to be calibrated against this baseline when used at scale.

## ML uses

- **Embedding similarity**: word / sentence / image embeddings ([[Word2Vec]] / [[GloVe]] / [[BERT]] [CLS] / [[CLIP]] image-text) routinely use cosine similarity for retrieval, clustering, and analogy tasks.
- **[[ContrastiveLearning|Contrastive learning]]** (SimCLR, CLIP, [[InfoNCE]]): the temperature-scaled cosine similarity $\text{sim}(\mathbf{z}_i, \mathbf{z}_j)/\tau$ is the standard score function.
- **[[Attention]]**: scaled dot-product attention $\mathbf{q}^\top\mathbf{k}/\sqrt{d}$ is unnormalized cosine similarity times the magnitudes.
- **[[VectorDatabase|Vector databases]]** ([[Pinecone]], [[Weaviate]], [[Faiss]]) use cosine similarity / inner-product as the primary distance metric.
- **Document retrieval / TF-IDF**: classical pre-neural document search.

## Relation to other distances

| Measure | Formula | Invariance |
|---|---|---|
| Euclidean | $\|\mathbf{v}-\mathbf{w}\|_2$ | none |
| Cosine similarity | $\langle\mathbf{v},\mathbf{w}\rangle/(\|\mathbf{v}\|\|\mathbf{w}\|)$ | magnitude |
| Cosine distance | $1 - \cos\theta$ | magnitude |
| Inner product | $\langle\mathbf{v},\mathbf{w}\rangle$ | none (depends on both magnitude and angle) |

For **unit-norm vectors**, cosine similarity, inner product, and (a monotonic transform of) Euclidean distance all coincide.

## Connections

- [[d2l-appendix-mathematics]] — §geometry-linear-algebraic-ops canonical reference.
- [[InnerProduct]] / [[DotProduct]] — numerator of the cosine.
- [[Norm]] — denominator factors.
- [[Attention]] / [[ScaledDotProductAttention]] — uses unnormalized cosine.
- [[ContrastiveLearning]] / [[InfoNCE]] — modern primary use.
- [[Word2Vec]] / [[GloVe]] / [[CLIP]] — embedding spaces designed for cosine retrieval.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 uses cosine similarity as **the label-assignment metric for [[ZeroShotClassification|zero-shot classification]] via [[LabelEmbedding|label embeddings]]**:

```python
from sklearn.metrics.pairwise import cosine_similarity

# Compare each document embedding to each label embedding
sim_matrix = cosine_similarity(test_embeddings, label_embeddings)
y_pred = np.argmax(sim_matrix, axis=1)
```

The chapter walks the geometric intuition: *"the cosine of the angle between vectors, which is calculated through the dot product of the embeddings and divided by the product of their lengths"* — and frames the application as *"checking how similar a given document is to the description of the candidate labels."* On [[RottenTomatoes|Rotten Tomatoes]] with [[AllMPNetBaseV2|`all-mpnet-base-v2`]] embeddings: **F1 = 0.78** with no labeled training data.

This is the wiki's **first worked instance of cosine similarity used as a zero-shot classification primitive** (the [[d2l-appendix-mathematics|D2L]] treatment is purely geometric; the wiki's other uses of cosine are in [[Attention]] / [[rag|RAG]] / contrastive losses).

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5 uses cosine similarity at **every stage** of the [[BERTopic]] pipeline:

- **[[UMAP]] distance metric** — `metric='cosine'` on the input 384-dim embeddings (*"Euclidean-based methods have issues dealing with high-dimensional data"*).
- **[[KeyBERTInspired]] representation reranking** — rerank candidate keywords by cosine similarity to the **average document embedding per topic**.
- **[[MaximalMarginalRelevance|MMR]]** — uses cosine similarity for both the relevance term and the diversity penalty.
- **BERTopic's `find_topics()`** — cosine similarity between a query embedding and each topic's embedding (e.g., `find_topics("topic modeling")` returns topic 22 with similarity 0.95).
- **Most-representative document selection** — picking the top-K documents per topic by cosine similarity to the topic's c-TF-IDF vector for the [[GenerativeTopicLabeling|generative topic labeling]] prompt.

Ch 5 thus extends Ch 4's *"cosine as zero-shot label-assignment metric"* pattern to **cosine as the multi-purpose similarity primitive of an entire clustering + topic-modeling pipeline**.

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 promotes cosine similarity to **the cross-modal alignment metric** in the [[CLIP]] training recipe — its first wiki appearance as a **multimodal** scoring function:

> *"The pair of embeddings that are generated are compared through cosine similarity ... the cosine of the angle between vectors, which is calculated through the dot product of the embeddings and divided by the product of their lengths."* — Ch 9

The chapter operationalizes this with an L2-normalize-then-dot-product idiom:

```python
text_embedding /= text_embedding.norm(dim=-1, keepdim=True)
image_embedding /= image_embedding.norm(dim=-1, keepdim=True)
score = np.dot(text_embedding, image_embedding.T)
# array([[0.33149648]], dtype=float32)
```

The AI-generated puppy-in-the-snow image paired with the caption *"a puppy playing in the snow"* scores **0.33** — counter-intuitively, this is **high** in CLIP's distribution. *"In isolation, this similarity score is difficult to interpret because we have no reference point to compare it to."* The chapter then computes a 3×3 similarity matrix (three images × three captions) and shows 0.33 is the *highest in its row* — operationalizing the **"cosine scores are best read comparatively, not absolutely"** discipline.

Ch 9 also names sentence-transformers' `util.cos_sim(...)` as the one-line wrapper around the normalize-and-dot-product step. The cosine-similarity-on-shared-multimodal-embeddings primitive is the substrate for [[CLIP]]'s four named applications (zero-shot classification / clustering / search / generation) — each of which reduces to the same dot-product-in-shared-space operation.
