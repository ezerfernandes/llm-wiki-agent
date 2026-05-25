---
title: "IIR Ch. 14: Vector Space Classification"
type: source
tags: [iir, information-retrieval, textbook, classification, knn, rocchio, bias-variance]
date: 2026-05-23
source_file: "https://nlp.stanford.edu/IR-book/html/htmledition/vector-space-classification-1.html"
---

## Summary

Chapter 14 of Manning, Raghavan & Schütze's *Introduction to Information Retrieval* moves text classification out of the probabilistic world of [[NaiveBayes]] and into the geometric world of the vector space model, where each document is a real-valued point in $\mathbb{R}^{|V|}$ rather than a bag of term indicators. The chapter is built on a single working hypothesis — the **contiguity hypothesis** — that documents of the same class occupy contiguous, non-overlapping regions of vector space, so the classification problem reduces to drawing decision boundaries between regions. Two canonical algorithms are introduced: **Rocchio classification**, which represents each class by its centroid (a mean vector) and assigns documents to the nearest centroid via a piecewise-linear hyperplane partition; and **k-nearest neighbor (kNN)**, which assigns documents by majority vote over the *k* most similar training documents, with 1NN inducing a Voronoi tessellation of training points. The chapter then formalizes the difference between [[LinearClassifier]]s (where Naive Bayes and Rocchio live) and [[NonlinearClassifier]]s (where kNN lives), and extends binary classification to the multiclass setting via **any-of** (multilabel) decomposition into independent binary classifiers and **one-of** (multinomial) via [[OneVsRest]] ranking. The chapter closes with a treatment of the [[BiasVarianceTradeoff]] for classifiers, decomposing learning error into a squared-bias plus variance term and explaining why high-capacity nonlinear methods (kNN) memorize but overfit, while low-capacity linear methods (Rocchio, NB) are stable but systematically biased.

## Key Claims

- **Documents are real-valued vectors, not binary indicators.** Vector space classification represents documents as tf-idf-weighted, length-normalized vectors lying on the surface of a unit hypersphere in $\mathbb{R}^{|V|}$, in contrast to the term-presence vectors used by [[NaiveBayes]].
- **The contiguity hypothesis is the foundational assumption.** "Documents in the same class form a contiguous region and regions of different classes do not overlap." Without this, no boundary-based classifier can succeed.
- **Representation choices determine whether the contiguity hypothesis holds.** Aggressive stoplisting, raw term counts, or omitting length normalization can destroy class contiguity even when the underlying classes are well-separated semantically.
- **Cosine similarity and Euclidean distance are equivalent for length-normalized vectors** but diverge for unnormalized vectors such as Rocchio centroids — so the choice of similarity measure interacts non-trivially with normalization.
- **Rocchio classification's centroid is the vector average** of class members and serves as a class prototype; the decision boundary between two classes is the perpendicular bisecting hyperplane between their centroids.
- **Rocchio requires classes that are approximately spherical with similar radii.** Multimodal classes (e.g., Burma documents clustering separately around pre- and post-1989 name change) break Rocchio because the single centroid is far from both modes.
- **kNN is memory-based / instance-based / lazy learning.** Training stores the data; all computation happens at query time. The standard *k* values are odd (3, 5, 50, 100) to avoid ties.
- **1NN induces a Voronoi tessellation** of training documents — the decision regions are convex polytopes consisting of all points nearer to a given training document than to any other.
- **kNN test time is $\Theta(|D| M_a)$** (with preprocessed inverted index) — *linear in training set size*, which is the price paid for not estimating parameters.
- **1NN error is asymptotically bounded by twice the Bayes error rate** (Cover & Hart 1967). For problems with Bayes error 0, 1NN error also approaches 0 as $|D| \to \infty$.
- **Both Naive Bayes (in log space) and Rocchio are linear classifiers** — their decision rules can be written as $\vec{w} \cdot \vec{x} = b$.
- **kNN is nonlinear** — its decision boundary is locally linear (Voronoi edges) but globally arbitrarily complex.
- **For one-of multiclass with $J$ classes**, build $J$ binary one-vs-rest classifiers and assign the document to the class with the *highest* confidence/distance-from-boundary score, because "$J$ hyperplanes do not divide space into $J$ disjoint regions."
- **Learning error decomposes as $E[(\hat{\gamma}(d) - \gamma(d))^2] = \text{bias}^2 + \text{variance}$.** Bias measures systematic error (model class too restrictive); variance measures instability across training sets.
- **Rocchio and Naive Bayes are high-bias, low-variance**; **kNN is low-bias, high-variance.** Choosing between them is the central modeling decision of the chapter.

## Section Notes

### 14.1 Document representations and measures of relatedness in vector spaces

Documents become tf-idf vectors in $\mathbb{R}^{|V|}$, length-normalized to lie on the unit hypersphere. The chapter emphasizes a small but consequential geometric fact: **for length-normalized vectors, cosine similarity and Euclidean distance produce identical rankings**, so the two measures are interchangeable when classifying normalized documents. However, Rocchio centroids — computed by *averaging* document vectors — are themselves *not* length-normalized, and at that point "dot product, cosine similarity and Euclidean distance all have different behavior." This subtlety motivates careful pairing of distance measure to representation. Within small local regions of the hypersphere, the curvature is negligible and 2-D projections used in textbook diagrams remain faithful to the underlying geometry.

### 14.2 Rocchio classification

Rocchio classification adapts the **Rocchio relevance feedback algorithm** (Ch. 9) to text classification by *dropping the original query term* — there is no query in classification, only labeled training documents. Each class $c$ is summarized by a single prototype, its **centroid**:

$$\vec{\mu}(c) = \frac{1}{|D_c|} \sum_{d \in D_c} \vec{v}(d)$$

A test document $d$ is assigned to the class whose centroid is closest:

$$\text{class}(d) = \arg\max_{c} \cos(\vec{\mu}(c), \vec{v}(d))$$

The decision boundary between classes $c_1$ and $c_2$ is the set of points equidistant from $\vec{\mu}(c_1)$ and $\vec{\mu}(c_2)$ — a **hyperplane** with normal $\vec{w} = \vec{\mu}(c_1) - \vec{\mu}(c_2)$. Rocchio with $J$ classes therefore partitions space by hyperplanes into regions, much like a Voronoi tessellation but over *centroids* rather than individual training points.

**Failure mode**: classes must be approximate spheres of similar radius. The textbook example is the Burma/Myanmar problem — documents about the country form two clusters (pre-1989 "Burma" and post-1989 "Myanmar") whose centroid lies between them, far from both, leading to misclassification.

**Time complexity**: Training is $\Theta(|D| L_{ave} + |C| |V|)$ (read documents once, then compute one centroid per class); testing is $\Theta(|C| M_a)$ (compare against $|C|$ centroids using the test document's $M_a$ types). Both training and testing scale very well — Rocchio is essentially free compared to kNN at test time.

### 14.3 k-nearest neighbor (kNN)

kNN defers all classification work to query time. Training is just memorization — there are no parameters, no model. At test time, the algorithm:
1. Computes similarity between the test document and every training document.
2. Selects the $k$ most similar training documents (the *k* nearest neighbors).
3. Assigns the test document to the **majority class** among those neighbors.

**Probability estimate**: kNN naturally yields class-membership probabilities — $\hat{P}(c \mid d) = \frac{1}{k} \sum_{d' \in S_k(d)} \mathbb{1}[d' \in c]$. With $k=3$ neighbors of which 1 is class A and 2 are class B, $\hat{P}(A) = 1/3, \hat{P}(B) = 2/3$.

**Weighted kNN with cosine similarity**:

$$\text{score}(c, d) = \sum_{d' \in S_k(d)} \mathbb{1}_c(d') \cdot \cos(\vec{v}(d'), \vec{v}(d))$$

Weighting by similarity makes closer neighbors count more — often more accurate than unweighted majority vote, especially in ties.

**1NN and the Voronoi tessellation**: when $k=1$, every training document "owns" a convex polytope (its Voronoi cell) of all points nearer to it than to any other training document. The decision boundary of 1NN is the union of Voronoi edges between training documents of different classes — a piecewise-linear, generally non-convex boundary. This is the geometric reason kNN is classified as nonlinear.

### 14.4 Time complexity and optimality of kNN

| Phase | With preprocessing | Without preprocessing |
|---|---|---|
| Training | $\Theta(|D| L_{ave})$ | $\Theta(1)$ |
| Testing | $\Theta(L_a + |D| M_{ave} M_a) = \Theta(|D| M_a)$ | $\Theta(|D| L_{ave} M_a)$ |

The headline result: **kNN test time is linear in $|D|$**, in stark contrast to [[NaiveBayes]] ($\Theta(|C| M_a)$) and Rocchio ($\Theta(|C| M_a)$). For large collections this is the principal limitation. The compensating advantage is independence from $|C|$: kNN's cost does not grow with the number of classes, which is attractive for problems with many fine-grained labels.

**Bayes error rate and asymptotic optimality**: the *Bayes error* is the minimum achievable error of any classifier, given the true class-conditional distributions. Cover & Hart (1967) proved that **1NN error is asymptotically at most twice the Bayes error rate** as $|D| \to \infty$. The intuition is that 1NN's error comes from two independent noise sources — the true class of the test document and the true class of its nearest neighbor — each contributing roughly the Bayes error. When Bayes error is 0 (perfectly separable problem), 1NN error also approaches 0.

### 14.5 Linear versus nonlinear classifiers

A **linear classifier** decides class membership by comparing a linear combination of features to a threshold:

$$\vec{w} \cdot \vec{x} = b$$

Assign $d$ to $c$ iff $\vec{w} \cdot \vec{x} > b$, otherwise to $\bar{c}$.

**Rocchio is linear**: the decision boundary between two centroids has normal $\vec{w} = \vec{\mu}(c_1) - \vec{\mu}(c_2)$ and is exactly a hyperplane.

**Naive Bayes is linear in log space**: taking logs of the multinomial NB decision rule gives $w_i = \log[\hat{P}(x_i \mid c) / \hat{P}(x_i \mid \bar{c})]$, so the NB decision rule becomes a linear function of the term-count vector.

**kNN is nonlinear**: its boundary is the union of Voronoi edges, which is locally linear but globally arbitrary. With enough training data, kNN can approximate any decision boundary.

**Noise documents** are outliers — training points whose features don't reflect their labels. They harm all methods but especially low-capacity linear ones, which have no degrees of freedom to "ignore" them. Conversely, when classes are **linearly separable**, there are infinitely many separating hyperplanes, raising the question of which is best (a question deferred to Ch. 15's treatment of SVMs).

The decision rule for choosing between linear and nonlinear: use linear classifiers when class boundaries are well-approximated by hyperplanes; use nonlinear when they are not, but only if you have enough data to control variance.

### 14.6 Classification with more than two classes

Two distinct multiclass settings:

**Any-of (multilabel / multivalue) classification**: classes are *not* mutually exclusive. A document can belong to many classes, one, or none. The standard approach is to train $J$ **independent binary classifiers**, one per class, each predicting $c_j$ vs $\bar{c}_j$.

**One-of (multinomial / polytomous / multiclass / single-label) classification**: classes are mutually exclusive. Each document gets exactly one label. The obvious approach — train $J$ binary classifiers and pick the one that fires — fails because *"$J$ hyperplanes do not divide space into $J$ disjoint regions."* Multiple classifiers may fire, or none may fire.

The fix is the [[OneVsRest]] **scoring** scheme: train $J$ binary classifiers as before but instead of taking the boolean decisions, **assign the document to the class with the maximum score, confidence, or probability**. The motivating intuition: "documents close to a class's separator are more likely to be misclassified, so the greater the distance from the separator, the more plausible it is that a positive classification decision is correct."

**Confusion matrix**: a $J \times J$ table where entry $(i,j)$ counts documents of true class $i$ predicted as class $j$. Off-diagonal cells highlight systematic class-pair confusions and guide improvement priorities.

### 14.7 The bias-variance tradeoff

The chapter formalizes a result that underlies the rest of the book's treatment of supervised learning. For a learning method $\Gamma$ that maps a labeled training set $\mathbb{D}$ to a classifier $\Gamma_{\mathbb{D}}$, define the squared-error learning error:

$$\text{learning-error}(\Gamma, d) = E_{\mathbb{D}}\big[(\Gamma_{\mathbb{D}}(d) - P(c \mid d))^2\big]$$

This decomposes exactly as:

$$\text{learning-error}(\Gamma, d) = \text{bias}^2(\Gamma, d) + \text{variance}(\Gamma, d)$$

where

- $\text{bias}^2(\Gamma, d) = \big[P(c \mid d) - E_{\mathbb{D}}\Gamma_{\mathbb{D}}(d)\big]^2$
- $\text{variance}(\Gamma, d) = E_{\mathbb{D}}\big[\Gamma_{\mathbb{D}}(d) - E_{\mathbb{D}}\Gamma_{\mathbb{D}}(d)\big]^2$

**Bias** is the systematic gap between the *average* classifier produced by $\Gamma$ and the true conditional class probability. High bias means the learner's hypothesis class is too restrictive to capture the truth — Rocchio with multimodal classes is high-bias because no centroid placement can model two-mode classes.

**Variance** is the spread of classifiers produced from different training sets. High variance means small changes in training data produce big changes in the learned classifier — kNN is high-variance because changing a few training points shifts Voronoi boundaries dramatically.

The **tradeoff**: more complex models (kNN, deep nets) tend to reduce bias but raise variance. Simpler models (Rocchio, NB) raise bias but lower variance. **Overfitting** is the regime where variance dominates and the learner memorizes noise; **underfitting** is the regime where bias dominates and the learner can't represent signal. The choice between Rocchio and kNN, then, is fundamentally a choice on the bias-variance frontier conditional on training-set size, noise level, and intrinsic class geometry.

## Algorithms & Formulas

**Document representation (length-normalized tf-idf)**:
$$\vec{v}(d) = \frac{\vec{\text{tfidf}}(d)}{\|\vec{\text{tfidf}}(d)\|_2}$$

**Rocchio centroid**:
$$\vec{\mu}(c) = \frac{1}{|D_c|} \sum_{d \in D_c} \vec{v}(d)$$

**Rocchio assignment**:
$$\text{class}(d) = \arg\max_{c} \cos(\vec{\mu}(c), \vec{v}(d)) \quad\text{or}\quad \arg\min_{c} \|\vec{\mu}(c) - \vec{v}(d)\|$$

**Linear classifier decision rule**:
$$\text{assign } d \text{ to } c \iff \vec{w} \cdot \vec{x} > b$$

For Rocchio between $c_1, c_2$:
$$\vec{w} = \vec{\mu}(c_1) - \vec{\mu}(c_2), \quad b = \frac{1}{2}\big(\|\vec{\mu}(c_1)\|^2 - \|\vec{\mu}(c_2)\|^2\big)$$

For multinomial NB in log space:
$$w_i = \log \frac{\hat{P}(x_i \mid c)}{\hat{P}(x_i \mid \bar{c})}, \quad b = -\log \frac{\hat{P}(c)}{\hat{P}(\bar{c})}$$

**kNN majority vote**:
$$\hat{c}(d) = \arg\max_{c} \sum_{d' \in S_k(d)} \mathbb{1}[d' \in c]$$

**Weighted kNN**:
$$\text{score}(c, d) = \sum_{d' \in S_k(d)} \mathbb{1}_c(d') \cdot \cos(\vec{v}(d'), \vec{v}(d))$$

**kNN probability estimate**:
$$\hat{P}(c \mid d) = \frac{1}{k} \sum_{d' \in S_k(d)} \mathbb{1}[d' \in c]$$

**Voronoi cell** of training document $d_i$:
$$V(d_i) = \{x \in \mathbb{R}^{|V|} : \|x - d_i\| \leq \|x - d_j\| \text{ for all } j \neq i\}$$

**kNN time complexity** (preprocessed):
- Training: $\Theta(|D| L_{ave})$
- Testing: $\Theta(|D| M_a)$

**1NN asymptotic error bound** (Cover & Hart 1967):
$$\text{err}_{1NN} \leq 2 \cdot \text{err}_{Bayes}$$

**Bias-variance decomposition**:
$$E_{\mathbb{D}}\big[(\Gamma_{\mathbb{D}}(d) - P(c \mid d))^2\big] = \underbrace{\big[P(c \mid d) - E_{\mathbb{D}}\Gamma_{\mathbb{D}}(d)\big]^2}_{\text{bias}^2} + \underbrace{E_{\mathbb{D}}\big[\Gamma_{\mathbb{D}}(d) - E_{\mathbb{D}}\Gamma_{\mathbb{D}}(d)\big]^2}_{\text{variance}}$$

## Key Quotes

> "Documents in the same class form a contiguous region and regions of different classes do not overlap."
> — The **contiguity hypothesis**, the assumption underlying all vector space classification.

> "For length-normalized vectors, there is a direct correspondence between cosine similarity and Euclidean distance... For unnormalized vectors, dot product, cosine similarity and Euclidean distance all have different behavior."
> — On the interaction between normalization and similarity measure.

> "We omit the query component of the Rocchio formula in Rocchio classification since there is no query in text classification."
> — On the derivation of Rocchio classification from Rocchio relevance feedback.

> "In addition to respecting contiguity, the classes in Rocchio classification must be approximate spheres with similar radii."
> — On Rocchio's chief geometric assumption and failure mode.

> "kNN simply memorizes all examples in the training set and then compares the test document to them."
> — On kNN as instance-based / lazy learning.

> "The error of 1NN is asymptotically bounded by twice the Bayes error rate."
> — The Cover-Hart optimality result.

> "In log space, Naive Bayes is a linear classifier."
> — Connecting probabilistic and geometric perspectives.

> "$J$ hyperplanes do not divide space into $J$ disjoint regions."
> — Why naive one-vs-rest fails for one-of classification without confidence scores.

> "Documents close to a class's separator are more likely to be misclassified, so the greater the distance from the separator, the more plausible it is that a positive classification decision is correct."
> — Rationale for ranking-based one-of decomposition.

> "Learning error decomposes into bias squared plus variance."
> — The central organizing principle of supervised learning, applied here to classifiers.

## Connections

- [[NaiveBayes]] — the probabilistic alternative; the chapter shows NB is *also* a linear classifier (in log space) and contrasts its parametric estimation against kNN's memorization. Same hyperplane geometry, different motivation.
- [[InformationRetrieval]] — the host discipline. Rocchio classification literally repurposes the Rocchio relevance feedback algorithm from IR's query reformulation toolkit. tf-idf and cosine similarity are inherited wholesale from IR scoring.
- [[CentroidBasedClustering]] — Rocchio classification is "supervised k-means": labels tell you which cluster each training document belongs to, then a new document is assigned to the nearest cluster centroid. The same geometric assumptions apply.
- [[RocchioClassification]] — the centroid-prototype method introduced in §14.2. Linear, fast, but assumes spherical equi-radius classes.
- [[KNearestNeighbor]] — the lazy / instance-based method introduced in §14.3. Nonlinear, asymptotically optimal up to 2x Bayes error, but $\Theta(|D| M_a)$ at test time.
- [[VoronoiTessellation]] — the geometric structure induced by 1NN, partitioning space into convex polytopes around training points. Decision boundaries are unions of Voronoi edges.
- [[LinearClassifier]] — the family $\vec{w} \cdot \vec{x} = b$ that contains Rocchio and (log-space) Naive Bayes; setup for Ch. 15's SVMs and logistic regression.
- [[NonlinearClassifier]] — kNN as the canonical example; needed when class boundaries aren't hyperplanes; cost is sensitivity to noise and overfitting.
- [[OneVsRest]] — the standard reduction from multiclass to binary, requiring confidence scores (not just boolean predictions) when classes are mutually exclusive.
- [[BiasVarianceTradeoff]] — formalized in §14.7. Rocchio and NB sit at high-bias/low-variance; kNN at low-bias/high-variance. All later supervised learning chapters operate within this frame.

## Contradictions

No direct contradictions with existing wiki pages. The chapter is consistent with the [[NaiveBayes]] treatment in Ch. 13 — both view NB as a linear classifier — and refines, rather than overturns, the [[CentroidBasedClustering]] perspective by adding labels. The Cover-Hart 2x-Bayes bound for 1NN is more optimistic than the textbook discussion of kNN overfitting elsewhere in the wiki, but the two are reconciled: the 2x bound is *asymptotic in $|D|$*, while overfitting concerns are about *finite-sample* behavior. No revisions required to existing pages.
