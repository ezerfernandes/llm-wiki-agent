---
title: "IIR Ch. 15: Support Vector Machines and Machine Learning on Documents"
type: source
tags: [iir, information-retrieval, textbook, svm, learning-to-rank, kernel]
date: 2026-05-23
source_file: "https://nlp.stanford.edu/IR-book/html/htmledition/support-vector-machines-and-machine-learning-on-documents-1.html"
---

## Summary

Chapter 15 of *Introduction to Information Retrieval* (Manning, Raghavan, Schütze 2008) introduces **[[SupportVectorMachine]]s (SVMs)** as a large-margin classifier and then broadens the lens to **machine learning on documents** more generally — covering practical feature engineering, classifier selection, and the application of supervised learning to **ad-hoc IR ranking** ([[LearningToRank]]). The chapter develops the SVM from its core geometric intuition (a hyperplane maximally far from training points) through three principled extensions: the **[[SoftMargin]]** formulation for non-separable data, **multiclass** decomposition strategies, and the **[[KernelTrick]]** for nonlinear decision surfaces. The closing sections argue that SVMs, while not strictly dominant over other modern learners, are theoretically grounded and empirically strong on text, and they motivate the now-standard application of pairwise [[RankingSVM]] to result ranking, which Joachims developed as a foundational learning-to-rank method. Together, the SVM treatment and the ML-for-IR sections form a hinge between classical IR (Chapters 1–14, where weighting was largely hand-designed via [[BM25]] and vector space cosine) and modern, data-driven ranking pipelines.

## Key Claims

- **Large-margin principle.** An SVM is "a vector space based machine learning method where the goal is to find a decision boundary between two classes that is maximally far from any point in the training data." Maximizing the geometric margin ρ = 2/‖w‖ corresponds to minimizing ‖w‖²/2 under the constraints y_i(w·x_i + b) ≥ 1.
- **Support vectors are sparse.** In the dual formulation, the optimum has w = Σ α_i y_i x_i where most α_i are zero; the non-zero α_i identify the **support vectors** that define the boundary.
- **Soft margin is necessary in practice.** Real text data is rarely linearly separable. Adding slack variables ξ_i and a penalty C·Σξ_i turns SVMs into a robust large-margin learner; C trades off margin width against training-error tolerance.
- **Kernel trick generalizes linear SVMs.** Replacing inner products x_i·x_j with a kernel K(x_i, x_j) implicitly maps data into a higher-dimensional space without computing the feature map explicitly. Polynomial and RBF/Gaussian kernels are the canonical examples; valid kernels must satisfy Mercer's condition (symmetric, positive semi-definite Gram matrix).
- **Multiclass SVMs.** The dominant practical strategy is **one-versus-rest** (|C| classifiers, pick the class with greatest margin). One-versus-one builds |C|(|C|−1)/2 pairwise classifiers. A more principled approach learns a joint score w·Φ(x, y) over input-class pairs, the foundation of **[[StructuralSVM]]s**.
- **SVMs are state-of-the-art but not universally dominant.** On Reuters-21578, linear SVMs achieve micro-averaged break-even F₁ ≈ 79.9, RBF-SVMs ≈ 79.4. In the chapter's table, kNN reaches 87.5 and decision trees 86.7 on the top-10 categories — though Manning et al. note that the often-cited Naive Bayes weakness in (Joachims, 1998) appears too low compared to careful replications. The takeaway is that "simple term features can get one a long way."
- **Domain features beat algorithm tweaking.** "Greater performance gains can be achieved from exploiting domain-specific text features than from changing from one machine learning method to another." Understanding the data — zones, sublanguages, named entities — matters more than swapping in a fancier learner.
- **Training-set size dictates classifier choice.** With *no* labels, hand-written rules win. With *little* data, prefer high-bias classifiers like [[NaiveBayes]] or use semi-supervised methods (bootstrapping, EM, transductive SVMs). With *abundant* data, the choice of classifier "probably has little effect"; instead focus on training scalability and runtime cost.
- **Document zones improve classification.** Titles, abstracts, headers, mail subjects, and other zones can be upweighted or given separate feature spaces, typically yielding accuracy gains.
- **Stemming is rarely useful when training data is sufficient.** Different surface forms carry "significantly different cues about the correct document classification," so collapsing them via [[Stemming]] discards signal.
- **Ad-hoc IR ranking is naturally a learning problem.** Cosine score, BM25, title match, proximity, PageRank, and other signals become features; a classifier or ranker learns their relative weights from query–document relevance judgments.
- **Pairwise ranking outperforms classification-style ranking.** The **[[RankingSVM]]** of Joachims learns over feature *differences* Φ(d_i, q) − Φ(d_j, q), enforcing w·(Φ(d_i, q) − Φ(d_j, q)) ≥ 1 − ξ_{ij} when d_i is judged more relevant than d_j. This sidesteps the need for a global relevance scale and is especially valuable in web search where only the top of the ranking matters.

## Section Notes

### 15.0 Introduction
Improvements in text classification effectiveness over two decades have come from a family of modern learners: SVMs, boosted decision trees, regularized logistic regression, neural networks, and random forests. The chapter focuses on SVMs because they bring strong theoretical guarantees, are particularly effective when labeled data is limited, and led to a generation of related "large-margin" methods.

### 15.1 SVMs: the linearly separable case
A linear classifier is f(x) = sign(w·x + b) with classes labeled +1 / −1. Many hyperplanes can separate a linearly separable training set; the **SVM** picks the one **maximally far from any training point**. The geometric margin equals **ρ = 2/‖w‖**. Maximizing ρ is equivalent to minimizing ‖w‖²/2 subject to y_i(w·x_i + b) ≥ 1 — a convex quadratic program with linear constraints, which has a unique global optimum.

The Lagrangian dual introduces multipliers α_i ≥ 0 and yields the solution w = Σ α_i y_i x_i. Only points on the margin boundary (with y_i(w·x_i + b) = 1) get α_i > 0; these are the **support vectors**. The classifier evaluates as f(x) = sign(Σ α_i y_i (x_i·x) + b), depending on training points only through inner products — a property the [[KernelTrick]] later exploits.

### 15.2 Extensions to the SVM model
The basic SVM is extended along three axes: (1) the **soft margin** for non-separable data, (2) **multiclass** SVMs for more than two classes, and (3) **nonlinear** SVMs via kernels. Each is the subject of a subsection.

#### 15.2.1 Soft margin classification
Real text data overlaps. **Slack variables** ξ_i ≥ 0 relax the margin constraint to y_i(w·x_i + b) ≥ 1 − ξ_i, allowing some points inside the margin or even misclassified. The new objective is

   minimize  ½‖w‖² + C · Σ_i ξ_i
   subject to  y_i(w·x_i + b) ≥ 1 − ξ_i,  ξ_i ≥ 0.

C governs the trade-off: small C → fat margin, more violations tolerated; large C → narrow margin, fewer violations. Σξ_i upper-bounds the training error count, and ξ_i can be viewed as **[[HingeLoss]]** on point i.

#### 15.2.2 Multiclass SVMs
- **One-versus-rest (OVA / one-vs-all):** train one binary SVM per class; classify by greatest signed margin. This is the most common practical recipe.
- **One-versus-one:** |C|(|C|−1)/2 pairwise classifiers; each is trained on a smaller subset so total training time can drop, but inference involves voting/aggregation.
- **Joint structured prediction:** learn w over a joint input–class feature map Φ(x, y) and predict ŷ = argmax_y w·Φ(x, y). Training enforces w·Φ(x_i, y_i) − w·Φ(x_i, y) ≥ 1 − ξ_i for every wrong label y. This is the entry point to **[[StructuralSVM]]s** (Tsochantaridis et al. 2005), which generalize the same large-margin idea to arbitrary structured outputs (sequences, parse trees, rankings).

#### 15.2.3 Nonlinear SVMs
If data are not linearly separable even with slack, map them into a higher-dimensional feature space via Φ: X → H. The chapter's central insight is the **[[KernelTrick]]**: training and inference depend only on dot products, so it suffices to define a kernel K(x_i, x_j) = Φ(x_i)·Φ(x_j) that can be computed *directly* in the original space, avoiding ever materializing Φ. Standard kernels:

- **[[PolynomialKernel]]:** K(x, z) = (1 + x·z)^d. d=1 is linear, d=2 is quadratic (captures pairwise term interactions in text).
- **[[RBFKernel]] (Gaussian):** K(x, z) = exp(−‖x − z‖² / (2σ²)). Corresponds to an infinite-dimensional feature space.

**Mercer's condition.** A function K is a valid kernel iff it is symmetric and produces a positive semi-definite Gram matrix on any finite sample. This guarantees an underlying Φ exists and the QP remains convex.

#### 15.2.4 Experimental results
On Reuters-21578 (top 10 categories), break-even F₁ scores (Joachims 1998 / Dumais et al. 1998 style evaluations):

| Classifier | Micro-F₁ |
|---|---|
| Linear SVM (C=1.0) | **79.9** |
| RBF-SVM (σ≈7) | 79.4 |
| Naive Bayes | 79.4 |
| Rocchio | 82.6 |
| Decision Trees | 86.7 |
| kNN | 87.5 |

Manning et al. note that the published Naive Bayes numbers may be artificially low and that linear methods are surprisingly competitive on simple term features. The high-level conclusion: SVMs are a robust, near-state-of-the-art default for text classification.

### 15.3 Issues in the classification of text documents
The chapter argues that *practitioners overweight algorithm choice and underweight data understanding*. Generic, one-size-fits-all categorization tools tend to fail across domains because they ignore document structure and sublanguage. Key practical levers:

- Training-set size (most important).
- Feature engineering tuned to the domain.
- Document structure (zones).
- Hierarchical taxonomy handling.

#### 15.3.1 Choosing what kind of classifier to use
- **No labels:** hand-written rules (Boolean queries, weighted patterns). Cited example: a takeover-news rule reaching 92% precision / 88.5% recall; cost ≈ 2 days/class plus maintenance.
- **Few labels:** high-bias models ([[NaiveBayes]]) or semi-supervised methods — bootstrapping, EM, **transductive SVMs**.
- **Many labels:** classifier choice matters less; prioritize scalability and runtime.
- In production, the chapter recommends layering rule-based overrides atop a trained SVM for interpretability and management adjustments.

#### 15.3.2 Improving classifier performance
"There is usually significant room for improving classifier effectiveness through exploiting features specific to the domain." Sub-topics:

- **Large and difficult category taxonomies.** Real-world taxonomies (e.g., the Yahoo! Directory's 200,000+ categories) are hard because classes are numerous and similar. **Hierarchical classification** mostly helps scalability rather than accuracy; aggressive feature selection and ensemble voting/bagging/boosting yield modest gains. A practical pipeline accepts high-confidence automated decisions and queues low-confidence ones for human review, generating new training data (though non-randomly sampled).
- **Features for text.** Default features are terms. Beyond that: regex-collapsed tokens for years/ISBNs/chemical formulas; **character k-grams** for unknown words (e.g., a suffix "-rase" suggests an enzyme); **multiword features** ("ethnic cleansing" → world news, where the individual words mislead); features from named entity recognizers. Stemming usually does not help if training data is plentiful.
- **Document zones in text classification.** Documents have zones — subject and sender for email; title, abstract, and body for papers. Three options: **upweight** important zones, treat each zone as a **separate feature space**, or apply **text summarization** to extract a high-signal zone.

### 15.4 Machine learning methods in ad-hoc information retrieval
The same machinery used for classification can rank documents for a query. The vision: "view different sources of relevance signal (cosine score, title match, etc.) as features in a learning problem." A classifier or ranker trained on labeled (query, document, relevance) triples learns to weight signals automatically, replacing hand-tuned formulas.

#### 15.4.1 A simple example of machine-learned scoring
Two features: cosine similarity α between query and document, and minimum window width ω containing all query terms (a proximity measure). The score is a learned linear combination:

   **Score(d, q) = a·α + b·ω + c**,

with a, b, c estimated from training data (relevance = 1, non-relevance = 0). The decision boundary is a line in the α–ω plane; choosing a threshold θ converts the regression into a classifier, and ranking falls out of the score itself. This is the minimal viable [[LearningToRank]] system — a pedagogical bridge from classical IR to modern learned ranking.

#### 15.4.2 Result ranking by machine learning
The **[[RankingSVM]]** (Joachims 2002b) replaces absolute relevance prediction with **pairwise ordinal regression**. For each query q and each pair of judged documents (d_i, d_j) where d_i ≻ d_j (i more relevant than j), define the difference vector

   **Φ(d_i, d_j, q) = ψ(d_i, q) − ψ(d_j, q)**

and demand that the learned w put d_i ahead of d_j by a margin:

   **w · Φ(d_i, d_j, q) ≥ 1 − ξ_{ij}**,  ξ_{ij} ≥ 0.

The full optimization minimizes ½‖w‖² + C·Σ ξ_{ij} — structurally identical to a soft-margin SVM but on *difference* vectors. Properties:

- Documents are scored *relative* to other candidates for the *same* query; no global relevance scale needed.
- Click logs supply implicit pairwise preferences ("clicked after skipping") at scale.
- The approach has empirically beaten hand-crafted ranking on standard IR benchmarks.
- Feature engineering still matters: nonlinear transforms of base signals (e.g., log of term frequency) often must be supplied by hand because the linear ranker cannot synthesize them.

### 15.5 References and further reading
- **SVM foundations:** Vapnik (1998) — the originator; Cortes & Vapnik (1995) — soft margin; Burges (1998) — accessible tutorial; Cristianini & Shawe-Taylor (2000), Schölkopf & Smola (2001) — rigorous textbooks; Shawe-Taylor & Cristianini (2004) — practical.
- **Multiclass and structural SVMs:** Weston & Watkins (1999); Crammer & Singer (2001); Tsochantaridis et al. (2005) — general structural SVM framework.
- **Kernel methods:** Aizerman et al. (1964) — original kernel trick; Lodhi et al. (2002), Gärtner et al. (2002) — string and structured kernels.
- **SVMs for text:** Joachims (1998, 2002a, 2006a) — application to text and scaling to large corpora.
- **Comparative evaluation:** Li & Yang (2003) — comparative evaluation of text classifiers.
- **Learning to rank:** Joachims (2002b) — Ranking SVM on clickstream data; Yue et al. (2007) — structural SVM optimizing MAP directly; Burges et al. (2005) — RankNet; Richardson et al. (2006) — alternative effective rankers.

## Algorithms & Formulas

### SVM (hard margin) primal
**Decision rule:** f(x) = sign(w·x + b)
**Primal QP:**

   minimize_w,b   ½ ‖w‖²
   subject to     y_i (w·x_i + b) ≥ 1,   i = 1,…,n.

**Geometric margin:** ρ = 2 / ‖w‖.

### SVM hard-margin dual
**Dual:**

   maximize_α   Σ_i α_i − ½ Σ_{i,j} α_i α_j y_i y_j (x_i · x_j)
   subject to   α_i ≥ 0,   Σ_i α_i y_i = 0.

**Recovered weights:** w = Σ_i α_i y_i x_i. Support vectors are points with α_i > 0.

### Soft-margin SVM
**Primal:**

   minimize_{w,b,ξ}   ½ ‖w‖² + C · Σ_i ξ_i
   subject to         y_i (w·x_i + b) ≥ 1 − ξ_i,   ξ_i ≥ 0.

**Hinge-loss interpretation:** ξ_i = max(0, 1 − y_i(w·x_i + b)) = HingeLoss(y_i, f(x_i)).

### Kernelized SVM
Replace x_i · x_j with kernel K(x_i, x_j):

   f(x) = sign( Σ_i α_i y_i K(x_i, x) + b ).

- **Linear:** K(x, z) = x · z.
- **[[PolynomialKernel]]:** K(x, z) = (1 + x · z)^d.
- **[[RBFKernel]]:** K(x, z) = exp( −‖x − z‖² / (2σ²) ).

**Mercer's condition:** K must be symmetric with a positive semi-definite Gram matrix.

### Multiclass joint scoring (structural SVM seed)
**Predict:** ŷ = argmax_{y' ∈ C}  w · Φ(x, y').
**Train (margin rescaling):**

   minimize_{w,ξ}   ½ ‖w‖² + C · Σ_i ξ_i
   subject to       ∀i, ∀ y ≠ y_i: w·Φ(x_i, y_i) − w·Φ(x_i, y) ≥ 1 − ξ_i.

### Ranking SVM (pairwise loss)
Given pairs (d_i, d_j, q) with d_i ≻ d_j:

   minimize_{w,ξ}   ½ ‖w‖² + C · Σ_{(i,j,q)} ξ_{ij,q}
   subject to       w · ( ψ(d_i, q) − ψ(d_j, q) ) ≥ 1 − ξ_{ij,q},   ξ_{ij,q} ≥ 0.

**Pairwise loss:** ℓ_{ij} = max(0, 1 − w·(ψ(d_i, q) − ψ(d_j, q))) — a hinge loss on the score difference.

### Simple linear scoring example
**Score(d, q) = a·cosine(d, q) + b·minWindowWidth(d, q) + c**, with a, b, c learned from relevance judgments and threshold θ for binary classification.

## Key Quotes

> "An SVM is a kind of large-margin classifier: it is a vector space based machine learning method where the goal is to find a decision boundary between two classes that is maximally far from any point in the training data."

> "The SVM in particular defines the criterion to be looking for a decision surface that is maximally far away from any data point."

> "Each non-zero α_i indicates that the corresponding x_i is a support vector."

> "A non-zero value for ξ_i allows x_i to not meet the margin requirement at a cost proportional to the value of ξ_i."

> "When [C] is small, it is easy to account for some data points with the use of slack variables and to have a fat margin placed so it models the bulk of the data."

> "As C becomes large, it is unattractive to not respect the data at the cost of reducing the geometric margin."

> "The most common technique in practice has been to build |C| one-versus-rest classifiers."

> "Map the original feature space to some higher-dimensional feature space where the training set is separable."

> "The dot product (which is just a real number) could be computed simply and efficiently in terms of the original data points."

> "Greater performance gains can be achieved from exploiting domain-specific text features than from changing from one machine learning method to another."

> "Understanding the data is one of the keys to successful categorization, yet this is an area in which most categorization tool vendors are extremely weak."

> "We can view different sources of relevance signal (cosine score, title match, etc.) as features in a learning problem."

> "If Score(α, ω) > θ we declare the document to be relevant, else we declare the document to be nonrelevant."

> "w^T Φ(d_i, d_j, q) > 0 iff d_i ≺ d_j."

## Connections

- [[SupportVectorMachine]] — the chapter is the canonical IR-textbook treatment; the soft-margin primal/dual, kernel formulation, and multiclass extensions developed here belong on that page.
- [[MaximalMarginClassifier]] — IIR Ch. 15 is the textbook home of the maximum-margin principle (ρ = 2/‖w‖). Strengthens that page's grounding.
- [[MaximumMargin]] — geometric margin maximization as a general principle that recurs in structural SVMs and learning-to-rank.
- [[Margin]] — geometric vs. functional margin; ρ = 2/‖w‖ ties this concept directly to the SVM QP.
- [[SoftMargin]] — slack variables ξ_i, C-parameter trade-off, hinge-loss equivalence.
- [[KernelTrick]] — the foundational technique enabling nonlinear SVMs; this chapter is its IR-context exposition.
- [[Kernel]] / [[KernelFunction]] — Mercer's condition (symmetric, positive semi-definite Gram matrix).
- [[PolynomialKernel]] — K(x, z) = (1 + x·z)^d; captures n-gram-like feature interactions.
- [[RBFKernel]] — K(x, z) = exp(−‖x−z‖²/(2σ²)); infinite-dimensional implicit feature space.
- [[StructuralSVM]] — multiclass joint scoring is the seed for structural prediction (Tsochantaridis et al. 2005).
- [[LearningToRank]] — the second half of the chapter is the IIR introduction to learning-to-rank; classifies it as feature-based supervised ranking.
- [[RankingSVM]] — Joachims's pairwise SVM ranker; pairwise hinge loss on score differences.
- [[PairwiseLoss]] — pairwise hinge loss is the central learning objective of Ranking SVM.
- [[HingeLoss]] / [[HingeLossRanking]] — ξ_i in the soft-margin SVM and Ranking SVM are hinge losses; HingeLossRanking is the ranking specialization.
- [[NaiveBayes]] — chapter's comparison baseline on Reuters-21578; recommended when training data is small (high-bias model).
- [[InformationRetrieval]] — the IR textbook context; Ch. 15 reframes ad-hoc retrieval as a supervised learning problem.
- [[BM25]] — IIR Ch. 11's BM25 score becomes one of many *features* in machine-learned ranking; section 15.4 explicitly invites BM25 as a feature.
- [[FeatureSelection]] — emphasized for scaling to large taxonomies and for high-dimensional text.
- [[Stemming]] — Ch. 15 argues stemming does *not* help classification when training data is plentiful — interesting tension with stemming's role in classical IR (Chs. 2–3).
- [[Rocchio]] / [[kNN]] / [[DecisionTrees]] — comparative baselines on Reuters-21578.
- [[VladimirVapnik]] — entity for the SVM originator, cited as Vapnik (1998).
- [[ThorstenJoachims]] — entity for the author of Ranking SVM, SVM^light, and the seminal text-SVM evaluations cited throughout Ch. 15.
- [[AlexanderSmola]] — co-author of Schölkopf & Smola (2001) cited as a rigorous SVM reference.

## Contradictions

- **Stemming.** IIR Ch. 2 ([[iir-ch02-term-vocabulary-postings]]) and Ch. 3 ([[iir-ch03-dictionaries-tolerant-retrieval]]) discuss stemming and lemmatization as useful normalizations for ad-hoc retrieval. Ch. 15 explicitly argues that *for text classification with sufficient training data*, stemming offers "no value" — the surface form is itself a useful classification cue. Not a hard contradiction (the tasks differ), but a notable scope-dependent reversal worth flagging when synthesizing across the IIR series.
- **kNN > SVM on Reuters-21578.** The chapter's own Reuters table shows kNN (87.5) outscoring linear SVM (79.9), which tensions with the broader narrative that "SVMs perform best." Manning et al. reconcile this by noting the published Naive Bayes results are likely too weak and that linear methods are competitive when features are simple terms — but readers should note that "SVMs are state-of-the-art" is *not* unconditional in their own experimental table.
- **Algorithm choice vs. features.** Ch. 14 (vector space classification) emphasizes choosing the right learner; Ch. 15 partially reverses this, arguing feature engineering and domain understanding usually matter more than algorithm choice. This is a refinement, not a contradiction, but readers of the IIR series should hold both ideas simultaneously.
