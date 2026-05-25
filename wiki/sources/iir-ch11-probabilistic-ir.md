---
title: "IIR Ch. 11: Probabilistic Information Retrieval"
type: source
tags: [iir, information-retrieval, textbook, probabilistic-ir, prp, binary-independence-model, bm25]
date: 2026-05-23
source_file: "https://nlp.stanford.edu/IR-book/html/htmledition/probabilistic-information-retrieval-1.html"
---

## Summary

Chapter 11 of *Introduction to Information Retrieval* (Manning, Raghavan & Schütze, 2008) develops the **probabilistic** family of ranking models for [[InformationRetrieval]]. Where the Boolean and vector-space chapters use "a formally defined but semantically imprecise calculus of index terms", this chapter recasts retrieval as **uncertain reasoning about relevance**: given a query *q* and a document representation *d*, the system maintains an estimate `P(R=1|d,q)` and ranks documents to optimise an expected-loss criterion.

The chapter is built around three pillars. First, the [[ProbabilityRankingPrinciple]] (PRP) gives the theoretical justification for ranking by probability of relevance under 1/0 loss and its cost-sensitive generalisation. Second, the [[BinaryIndependenceModel]] (BIM) instantiates the PRP under binary term-incidence vectors and the Naive Bayes term-independence assumption, deriving a closed-form ranking — the [[RetrievalStatusValue]] (RSV) — built from log odds ratios that, after smoothing and a "non-relevant ≈ collection" approximation, reduce to a probabilistic justification for IDF weighting. Third, the chapter surveys empirically successful extensions: tree-structured term dependencies ([[TreeDependency]]), the [[OkapiBM25]] non-binary model (which adds term frequency and document-length normalisation), and Bayesian-network IR systems ([[BayesianNetwork]]) such as InQuery. The chapter closes with an appraisal noting that BM25-style scoring "started to be adopted as a term weighting scheme by many groups" and that vector-space and probabilistic systems differ in practice mainly by the **scoring formula** they plug into the same retrieval architecture.

## Key Claims

- Retrieval is fundamentally an exercise in **uncertain inference about relevance**, naturally cast in probability theory; if some relevant/non-relevant documents are known, term-occurrence probabilities can be estimated systematically.
- The **PRP** states: if documents are ranked in decreasing order of `P(R=1|d,q)` and the probabilities are accurate, the ranking is optimal under 1/0 loss; this remains "a very useful foundation" even though probability estimates are never perfect.
- Under 1/0 loss, the **Bayes-optimal decision** is to classify *d* as relevant iff `P(R=1|d,q) > P(R=0|d,q)`.
- With asymmetric costs `C_1` (missing a relevant doc) and `C_0` (returning a non-relevant doc), the PRP generalises to a comparison `C_0 P(R=0|d) - C_1 P(R=1|d) ≤ C_0 P(R=0|d') - C_1 P(R=1|d')` for every unretrieved `d'`, letting the model directly encode false-positive vs false-negative trade-offs.
- The **BIM** represents documents and queries as binary incidence vectors `x = (x_1,...,x_M)` and assumes **term independence** ("Naive Bayes") plus the simplifying rule that terms absent from the query do not affect the ranking.
- Ranking by **odds of relevance** preserves the order of `P(R=1|x,q)` and yields the additive **RSV**:
  `RSV_d = Σ_{t: x_t = q_t = 1} log[ p_t (1 - u_t) / (u_t (1 - p_t)) ]`,
  where `p_t = P(x_t=1|R=1,q)` and `u_t = P(x_t=1|R=0,q)`.
- Estimating `p_t, u_t` from a relevance contingency table uses `p_t = s/S` and `u_t = (df_t - s)/(N - S)`; add-½ smoothing (`(s+0.5)/(S+1)` etc.) keeps the log-odds finite when no relevant document contains a given term.
- In practice, relevance judgements are scarce. Assuming the **collection ≈ non-relevant set** gives `u_t ≈ df_t / N`, so `log[(1 - u_t)/u_t] ≈ log(N/df_t)` — a **probabilistic re-derivation of IDF**.
- **Probabilistic relevance feedback** iteratively refines `p_t, u_t` from user-judged relevant (`VR`) and non-relevant (`VNR`) sets, with smoothing such as `p_t^(k+1) = (|VR_t| + κ·p_t^(k)) / (|VR| + κ)` (Robertson/Sparck Jones, κ≈5). Pseudo-relevance feedback uses the top retrieved set as a proxy for `VR`.
- The **BIM's** restrictive assumptions (binary representation, independence, non-query terms irrelevant, independent relevance across documents) limit its raw effectiveness, but its scoring formula plugs into the same indexing and inverted-list architecture as a vector-space system.
- **Term dependencies** can be relaxed by restricting interactions to a **tree** (each term depends on at most one other), as in van Rijsbergen (1979) and the Tree-Augmented Naive Bayes revival of the 1990s.
- **Okapi BM25** generalises BIM to a non-binary model by inserting saturating term-frequency components and document-length normalisation, becoming "the empirically successful Okapi BM25 weighting scheme" adopted widely in TREC and modern engines.
- **Bayesian-network IR** (Turtle & Croft's InQuery) models documents, terms, query concepts, and information need as nodes in a DAG, combining evidence with probabilistic "noisy" AND/OR operators and weighted sums.

## Section Notes

### 11.1 Review of basic probability theory
Restates the axioms used throughout: `0 ≤ P(A) ≤ 1`; chain rule `P(A,B) = P(A|B)P(B) = P(B|A)P(A)`; partition `P(B) = P(A,B) + P(Ā,B)`; **Bayes' Rule** `P(A|B) = P(B|A) P(A) / P(B)` (prior → posterior via likelihood); **odds** `O(A) = P(A) / (1 - P(A))`. The odds form is the workhorse for the BIM derivation because monotone transformations preserve ranking.

### 11.2 The Probability Ranking Principle
Frames retrieval as a **decision-theoretic** problem. The system has an information need *q* and must order documents to maximise expected utility.

- **11.2.1 The 1/0 loss case.** Lose one point per non-relevant returned or relevant missed. Ranking by `P(R=1|d,q)` (descending) is optimal; the Bayes-optimal binary classifier is `P(R=1|d,q) > P(R=0|d,q)`. The authors flag that perfect estimation "is never the case in practice".
- **11.2.2 PRP with retrieval costs.** Introduces asymmetric costs `C_0, C_1` and the comparison rule above, letting the system model differential costs of false positives and false negatives **inside ranking** rather than only at evaluation time.

### 11.3 The Binary Independence Model
Documents and queries become **binary vectors** over the vocabulary; the model treats terms as independent ("naive" but tractable). The chapter writes `O(R|q,x)` and applies Bayes' Rule to factor it into prior odds of relevance and a product of per-term likelihood ratios. The "binary" name reflects the bag-of-binary-incidence representation; the "independence" reflects Naive Bayes over terms.

#### 11.3.1 Deriving a ranking function for query terms
For each term *t* define `p_t = P(x_t=1|R=1,q)` and `u_t = P(x_t=1|R=0,q)`. Assuming `p_t = u_t` for non-query terms (their factors cancel), the log-odds collapses to a sum over query terms appearing in *d*:

```
c_t  = log[ p_t (1 - u_t) / (u_t (1 - p_t)) ]
RSV_d = Σ_{t ∈ q, x_t=1} c_t
```

This is the **Retrieval Status Value** — the additive score used to rank documents. It decomposes into two log-odds ratios: log-odds of seeing *t* in a relevant doc vs not seeing it, minus log-odds of seeing *t* in a non-relevant doc vs not seeing it.

#### 11.3.2 Probability estimates in theory
With a contingency table of (relevant/not, contains-term/not):

| | Relevant | Non-relevant | Total |
|---|---|---|---|
| `x_t = 1` | `s` | `df_t − s` | `df_t` |
| `x_t = 0` | `S − s` | `(N−S) − (df_t−s)` | `N − df_t` |
| Total | `S` | `N − S` | `N` |

MLE gives `p_t = s/S`, `u_t = (df_t − s)/(N − S)`. To dodge zero counts (which would send `c_t` to ±∞), add `0.5` to each cell — a weak uniform prior with α = ½, i.e. MAP estimation. This is the "add-½ smoothing" mentioned across the chapter.

#### 11.3.3 Probability estimates in practice
Two practical moves:

1. **Collection ≈ non-relevant.** Because relevant documents are a tiny fraction of *N*, set `u_t ≈ df_t / N`. Then `log[(1 - u_t)/u_t] ≈ log(N/df_t)` — recovering **IDF** from probabilistic first principles.
2. **Constant prior on `p_t`.** Without relevance data, set `p_t = 0.5`, making the relevance term log-odds `log(p_t/(1-p_t)) = 0` and leaving only the IDF-like factor. Greiff (1998) proposes `p_t = 1/3 + (2/3)(df_t/N)`, an empirically motivated alternative.

#### 11.3.4 Probabilistic approaches to relevance feedback
Iterative pipeline: (i) initial guess for `p_t, u_t` (often `p_t = 0.5`, `u_t = df_t/N`); (ii) retrieve and present candidates; (iii) collect user judgements into `VR` (relevant) and `VNR` (non-relevant); (iv) re-estimate using smoothed counts, e.g.
`p_t^(k+1) = (|VR_t| + κ · p_t^(k)) / (|VR| + κ)`
with κ≈5 so that the prior keeps weight when user feedback is sparse; (v) iterate. **Pseudo-relevance feedback** replaces `VR` with the top-*k* retrieved documents and re-estimates automatically. Resulting term weights resemble tf-idf but their numerator is a proportion of *relevant* documents containing *t*, not a raw term frequency.

### 11.4 An appraisal and some extensions

#### 11.4.1 An appraisal of probabilistic models
Critical inventory of BIM assumptions: Boolean doc/query representation; term independence; non-query terms ignored; independence of relevance across documents. The book notes "the severity of the modelling assumptions ... makes achieving good performance difficult" and that early probabilistic systems either needed partial relevance information or settled for inferior weights. The 1990s changed the picture: BM25 "showed very good performance, and started to be adopted as a term weighting scheme by many groups". The practical takeaway — vector-space and probabilistic IR engines look almost identical operationally; what differs is the scoring formula.

#### 11.4.2 Tree-structured dependencies between terms
Van Rijsbergen's 1979 model permits each term to depend directly on **one** other term, organised as a tree. Mutual-information-weighted maximum spanning trees (Chow-Liu style) pick the structure. The 1970s suffered from estimation problems; the 1990s' Tree-Augmented Naive Bayes (Friedman & Goldszmidt) revived the idea on standard ML benchmarks. Real linguistic examples like "Hong" and "Kong" motivate dropping strict independence for highly correlated term pairs.

#### 11.4.3 Okapi BM25: a non-binary model
The textbook walks from BIM to BM25 in three formulas:

- **(11.21 / 84) Pure IDF:** `RSV_d = Σ_{t ∈ q} log(N/df_t)`.
- **(11.22 / 86) BM11-style with TF + length normalisation:**
  `RSV_d = Σ_{t ∈ q} log(N/df_t) · [(k_1 + 1) · tf_td] / [k_1 ((1 - b) + b · L_d/L_ave) + tf_td]`.
- **(11.23 / 87) Full BM25 with query-side normalisation:**
  `RSV_d = Σ_{t ∈ q} log(N/df_t) · [(k_1 + 1) · tf_td] / [k_1 ((1 - b) + b · L_d/L_ave) + tf_td] · [(k_3 + 1) · tf_tq] / [k_3 + tf_tq]`.

Parameters: `k_1` (≈1.2–2.0) controls how quickly TF saturates (k_1=0 reduces to the binary model); `b` (≈0.75) blends "no length normalisation" (b=0) with "full normalisation" (b=1) using the ratio `L_d / L_ave` of document length to average; `k_3` scales query-side term frequency for long queries (often set very high or to 0–1000 depending on use). The book recommends tuning on a development set rather than treating these as constants.

#### 11.4.4 Bayesian network approaches to IR
Turtle & Croft's **InQuery** uses a DAG with two sub-networks:

- A precomputed **document collection network**: documents → terms → thesaurus/concept expansions.
- A per-query **query network**: query terms → query subexpressions → information-need node.

Combination operators include probabilistic "noisy AND/OR" and weighted sums, generalising both Boolean and probabilistic retrieval. InQuery "performed very well in TREC evaluations and for a time was sold commercially", but required tractability approximations.

### 11.5 References and further reading
Foundational and survey references: Maron & Kuhns (1960); Robertson & Sparck Jones (1976) — BIM; van Rijsbergen (1979) — textbook treatment plus tree dependencies; Fuhr (1992); Crestani et al. (1998); [[KarenSparckJones]] et al. (2000) — definitive experimental survey; [[StephenRobertson]] (2005) — Okapi BM25 retrospective; Robertson et al. (2004) — BM25 extended to multiple weighted fields.

## Algorithms & Formulas

### Probability Ranking Principle (PRP)
> Rank documents by `P(R=1|d, q)` in decreasing order. Under 1/0 loss this minimises expected loss; with costs `C_0, C_1` choose, as the next document to retrieve, any *d* that minimises `C_0 P(R=0|d) - C_1 P(R=1|d)` among unretrieved candidates.

### BIM derivation (sketch)
1. Score documents by **odds** `O(R=1|q,x) = P(R=1|q,x) / P(R=0|q,x)`; odds are monotone in `P(R=1|·)`, so ranking is preserved.
2. Apply Bayes' Rule: `O(R|q,x) = O(R|q) · P(x|R=1,q) / P(x|R=0,q)`.
3. Under term independence, the likelihood ratio factors: `Π_t P(x_t|R=1,q) / P(x_t|R=0,q)`.
4. Use the simplifying assumption `p_t = u_t` for non-query terms ⇒ their factors drop out.
5. Split the remaining product into `x_t = 1` and `x_t = 0` cases and take logs to get the additive **RSV**.

### Retrieval Status Value
```
c_t   = log[ p_t (1 - u_t) / (u_t (1 - p_t)) ]
RSV_d = Σ_{t ∈ q, x_t = 1} c_t
```

### Probability estimates
- MLE: `p_t = s/S`, `u_t = (df_t - s)/(N - S)`.
- Add-½ smoothing (MAP, α=0.5): `p̂_t = (s + 0.5)/(S + 1)`, `û_t = (df_t - s + 0.5)/(N - S + 1)`.
- Collection approximation: `u_t ≈ df_t / N` ⇒ `log[(1-u_t)/u_t] ≈ log(N/df_t)` (IDF).
- Relevance feedback update: `p_t^(k+1) = (|VR_t| + κ · p_t^(k)) / (|VR| + κ)`, κ ≈ 5.

### Okapi BM25 (full)
```
RSV_d = Σ_{t ∈ q}
        log(N / df_t)
      · (k_1 + 1) · tf_{t,d} / ( k_1 ((1 - b) + b · L_d / L_ave) + tf_{t,d} )
      · (k_3 + 1) · tf_{t,q} / ( k_3 + tf_{t,q} )
```
Defaults / ranges: `k_1 ∈ [1.2, 2.0]`, `b ≈ 0.75`, `k_3 ∈ [0, 1000]`. Setting `k_1 = 0` recovers the binary model; `b = 0` removes length normalisation; very large `k_3` makes query-side TF effectively linear.

### Tree-dependency model
Each term is conditioned on at most one parent term; the dependency tree is a maximum-weight spanning tree over the pairwise mutual-information graph (Chow-Liu). Estimation uses pairwise term-cooccurrence statistics from relevant/non-relevant samples.

### Bayesian network (InQuery)
- Nodes: documents `d_i`; index terms `t_j`; concepts/expansions `c_k`; query operators (AND/OR/weighted sum); information-need `I`.
- Edges encode conditional dependence (document → its terms; terms → concepts; concepts → operator nodes → `I`).
- Score = `P(I = true | d_i)` under various approximations (e.g. canonical noisy-OR for disjunctions).

## Key Quotes

> "Given the query and document representations, a system has an uncertain guess of whether a document has content relevant to the information need."

> "If we have some known relevant and nonrelevant documents, then we can straightforwardly start to estimate the probability of a term appearing in a relevant document."

> "Rank by P(R=1|d,q) ... If documents are ranked in this order, the effectiveness of the system will be the best possible." — paraphrase of the PRP.

> "The presence or absence of a word in a document is independent of the presence or absence of any other word." — Naive Bayes assumption of the BIM.

> The independence assumption is "far from correct, but it nevertheless often gives satisfactory results in practice."

> "The severity of the modelling assumptions ... makes achieving good performance difficult."

> The BM25 weighting scheme "showed very good performance, and started to be adopted as a term weighting scheme by many groups."

> InQuery "performed very well in TREC evaluations and for a time was sold commercially."

## Connections

- [[InformationRetrieval]] — chapter sits within the IR family of models, contrasted with Boolean and vector-space chapters.
- [[BM25]] — existing concept page; this chapter provides the probabilistic derivation that motivates [[OkapiBM25]] as the production realisation.
- [[NaiveBayes]] — the term-independence assumption of the BIM is precisely Naive Bayes over term features.
- [[ProbabilityRankingPrinciple]] — formal optimality criterion that justifies ranking by `P(R=1|d,q)`.
- [[BinaryIndependenceModel]] — concrete instantiation of the PRP under binary incidence and Naive Bayes.
- [[RetrievalStatusValue]] — additive log-odds score used by the BIM and (with TF/length factors) by BM25.
- [[OkapiBM25]] — BIM extended with saturating TF, document-length normalisation, and optional query TF scaling.
- [[BayesianNetwork]] — InQuery generalises both Boolean and probabilistic IR via DAGs and noisy operators.
- [[BayesRule]] — derivational engine for converting `P(R|x,q)` into a tractable likelihood-ratio form.
- [[TreeDependency]] — relaxation of term independence with at-most-one parent per term (van Rijsbergen, Tree-Augmented Naive Bayes).
- [[StephenRobertson]] — co-author of the BIM (1976) and chief architect of Okapi BM25; 2005 retrospective cited.
- [[KarenSparckJones]] — co-author of the BIM and of the 2000 "definitive" probabilistic IR experiments paper.

## Contradictions

- No direct contradictions identified with existing wiki pages. Note that [[BM25]] in the wiki currently emphasises BM25 as a vector-space-style TF-IDF refinement; this chapter complements that view by deriving BM25 as a **probabilistic** extension of the BIM rather than as a heuristic patch to TF-IDF. The two framings are consistent — the chapter explicitly observes that "an organisation has effectively changed an existing vector-space IR system into ... probabilistic ... simply by adopting term weighting formulas from probabilistic models."
- The chapter's claim that the **collection-≈-non-relevant** approximation recovers IDF should be reconciled with any wiki claim treating IDF as a purely heuristic weighting — it is also a principled MAP estimate under BIM assumptions.
