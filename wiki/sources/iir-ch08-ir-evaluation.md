---
title: "IIR Ch. 8: Evaluation in Information Retrieval"
type: source
tags: [iir, information-retrieval, textbook, evaluation, precision, recall, map, ndcg, trec]
date: 2026-05-23
source_file: "https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-in-information-retrieval-1.html"
---

## Summary

Chapter 8 of Manning, Raghavan, and Schütze's *Introduction to Information Retrieval* (Cambridge University Press, 2008) sets out the empirical methodology that has shaped IR for half a century: how to decide, with statistical credibility, whether one retrieval system is better than another. The chapter introduces the three pillars of a test collection (document corpus, information needs, relevance judgments), surveys the canonical effectiveness measures for both unranked sets (precision, recall, F-measure) and ranked lists (interpolated precision-recall curves, 11-point average precision, MAP, precision@k, R-precision, ROC, NDCG), examines how human assessors produce the gold standard and how inter-annotator agreement is quantified via Cohen's kappa, and then steps back to interrogate the very concept of "relevance" — its binary versus graded forms, its document-independence assumption, and its limited reach as a proxy for true user utility. The closing sections shift from controlled offline experiments to operational concerns: system speed, A/B testing of deployed engines, clickthrough analysis, and the design of query-biased results snippets.

The chapter is foundational for anyone evaluating retrieval, recommendation, retrieval-augmented generation, or any system that returns a ranked list of items in response to an information need. Its formal apparatus — pooled relevance judgments at TREC, MAP as the dominant single-number summary, NDCG for graded judgments — remains the lingua franca of modern IR papers.

## Key Claims

- IR is an empirical discipline; design choices (stemming, stop lists, IDF weighting, scoring functions) must be validated against representative test collections rather than justified by intuition alone.
- A usable test collection requires three components: a document collection, a set of information needs (typically 50 or more for statistical stability), and binary relevance judgments for each query-document pair.
- Documents are judged against the underlying *information need*, not the surface query string. Two different queries that express the same need should yield the same relevance judgments.
- For unranked retrieval, **accuracy is the wrong metric**: because well over 99.9% of documents are non-relevant for any given query, a system that returns nothing achieves near-perfect accuracy while being useless.
- **Precision** (fraction of retrieved documents that are relevant) and **recall** (fraction of relevant documents that are retrieved) form the canonical dual, combined via the **F-measure** as a weighted harmonic mean. The harmonic mean is preferred because the arithmetic mean rewards trivial 100%-recall strategies.
- For ranked retrieval, **interpolated precision** smooths the saw-tooth precision-recall curve by taking, at each recall point, the maximum precision at any higher recall.
- **Mean Average Precision (MAP)** is the dominant single-number ranked-retrieval metric: for each query, average the precision values obtained at the rank of each relevant document; then average across queries.
- **R-precision** (precision at rank equal to the number of known relevant documents) coincides exactly with the precision-recall **breakeven point**.
- **NDCG** generalizes ranked evaluation to graded relevance judgments via a logarithmic position discount, and is normalized so a perfect ranking scores 1.0.
- Relevance judgments are produced by humans and are inherently noisy. **Cohen's kappa** corrects observed agreement for chance; values above 0.8 indicate good agreement, 0.67-0.8 fair, below 0.67 dubious.
- Pooling — judging only the top-*k* documents returned by participating systems — is the standard practical solution for assessing massive collections.
- Despite modest interjudge agreement, choosing different judges' opinions has little impact on the *relative* ranking of systems being compared.
- The binary, topical, document-independent notion of relevance is a useful simplification but ignores marginal relevance, redundancy, and the diversity of user intent.
- Formal effectiveness measures are a proxy for user happiness, not a substitute for it; A/B testing and clickthrough log analysis are the standard tools for refining deployed engines.

## Section Notes

### Information Retrieval System Evaluation
A standard test collection consists of (1) a document collection, (2) a test suite of information needs expressed as queries, and (3) a set of binary relevance judgments (the *gold standard* or *ground truth*). Evaluation is performed under the **ad hoc retrieval** model: arbitrary queries against a fixed collection. Information needs must be the unit of evaluation — not queries — because the same need may be expressed by many distinct queries. A minimum of approximately 50 information needs is recommended for statistically stable averages, and parameter tuning must be done on a separate development collection to avoid overfitting.

### Standard Test Collections
The **Cranfield collection** (UK, late 1950s) was the first reusable IR test bed: 1,398 aerodynamics abstracts, 225 queries, exhaustive query-document judgments. Too small for modern research, but pedagogically important.

The **Text Retrieval Conference (TREC)**, run by **NIST** since 1992, produced the dominant evaluation infrastructure: the Ad Hoc track (1992-1999) used six CDs totaling 1.89 million documents with judgments over 450 topics; TRECs 6-8 used 150 information needs over ~528,000 newswire and FBIS articles. **GOV2** (25M web pages) is the largest publicly available research web collection. **NTCIR** focuses on East Asian languages and cross-lingual retrieval; **CLEF** focuses on European multilingual retrieval. For text classification: **Reuters-21578** (~21,578 newswire articles), **Reuters RCV1** (806,791 documents), and Ken Lang's **20 Newsgroups** (18,941 articles after dedup).

### Evaluation of Unranked Retrieval Sets
The 2×2 contingency table partitions outcomes into true positives (tp), false positives (fp), false negatives (fn), and true negatives (tn). Three derived measures:

- Precision: `P = tp / (tp + fp)`
- Recall: `R = tp / (tp + fn)`
- Accuracy: `(tp + tn) / (tp + fp + fn + tn)` — degenerate for IR

Because relevant documents are extremely rare in the global collection, accuracy is dominated by tn and rewards systems that retrieve nothing. The **F-measure** combines P and R as a weighted harmonic mean (see formulas below), with β controlling the relative weight: β > 1 weights recall more, β < 1 weights precision more, β = 1 (the balanced F₁) treats them equally.

### Evaluation of Ranked Retrieval Results
A ranked list defines a precision-recall pair at each rank position. The curve is jagged ("saw-tooth"): each relevant document increases recall and tends to bump precision, while each non-relevant document leaves recall unchanged but reduces precision. **Interpolated precision** at recall level *r* is defined as the maximum precision observed at any recall ≥ *r*; this produces a monotonically non-increasing curve.

- **11-point interpolated average precision** averages interpolated precision at recall levels {0.0, 0.1, ..., 1.0}, per query, then across queries.
- **Mean Average Precision (MAP)** is the dominant modern summary: for each query, average the precision at the rank of each relevant document (treating unretrieved relevants as precision = 0); MAP averages these per-query AP values across the query set.
- **Precision@k** (e.g., P@10) is the precision in the top *k* results — practical for web search where users rarely scroll past the first page, but unstable when the number of relevant documents per query varies widely.
- **R-precision** is precision at rank |Rel|, the number of known relevant documents. It is mathematically identical to the precision-recall breakeven point.
- **ROC curves** plot true positive rate against false positive rate; in IR they compress almost all interest into a small region near the origin because non-relevant documents vastly outnumber relevant ones.
- **NDCG (Normalized Discounted Cumulative Gain)** is the standard metric when relevance is graded rather than binary, accommodating ordinal scales like {0, 1, 2, 3}. NDCG normalizes DCG by the DCG of the ideal ranking so that 1.0 represents perfect performance.

### Assessing Relevance
Relevance assessment is performed by human judges. For large collections, exhaustive judgment is infeasible, so TREC uses **pooling**: assessors judge the union of the top-*k* results from each participating system. Documents outside the pool are treated as non-relevant.

Inter-annotator agreement is quantified by Cohen's kappa, which corrects observed agreement P(A) by the agreement expected under chance P(E). Kappa above 0.8 indicates good agreement; 0.67-0.8 is fair (the typical range for IR relevance judgments); below 0.67 the evaluation is on dubious ground. The reassuring empirical finding is that, although judges disagree substantially in absolute terms, their disagreement does not change the *ranking* of competing systems — relative comparisons are robust to judge choice.

### Critiques and Justifications of the Concept of Relevance
The binary, topical, judge-independent, document-independent relevance model is a deliberate simplification. Critiques:

- **Binary vs graded relevance**: real relevance is gradient. INEX, TREC, and NTCIR now use ordinal scales (often 3-4 classes distinguishing slightly from highly relevant), motivating metrics like NDCG.
- **Subjectivity**: judges disagree; the model treats their decisions as objective.
- **Document independence**: the relevance of document *d₁* is judged without reference to document *d₂*. This ignores redundancy and near-duplicates, especially severe on the web.
- **Marginal relevance**: once a user has seen one document on a topic, the marginal value of a near-duplicate is low. Diversity-aware ranking addresses this.

Justifications: formal evaluation is cheap, repeatable, and enables clear ablation — properties that user studies lack. Documented gains in IR (length normalization, learning-to-rank) emerged from this paradigm.

### A Broader Perspective: System Quality and User Utility
Formal effectiveness measures are at a distance from genuine human utility. Real evaluation must combine quantitative metrics (task completion time, success rate) with qualitative inputs (subjective satisfaction, interface feedback). The chapter pivots here from offline IR metrics to operational and human-centered concerns.

### System Issues
Beyond ranking quality, deployed systems are judged on indexing throughput (documents per hour), query latency as a function of index size, expressiveness of the query language (Boolean, phrase, proximity, fielded), and collection coverage. Most of these are straightforwardly measurable; expressiveness is captured via feature checklists.

### User Utility
User happiness is context-dependent: web search users want to find what they need; e-commerce platforms care about time-to-purchase and conversion; enterprise intranets care about employee productivity. Because user happiness is hard to measure directly, *relevance* serves as a tractable proxy. Direct measurement requires user studies — task-based engagement, observation, ethnographic interviews — which are expensive and require specialist expertise.

### Refining a Deployed System
The dominant production methodology is **A/B testing**: divert a small fraction (1-10%) of traffic to a variant that differs in exactly one factor; compare engagement metrics. **Clickthrough log analysis** (clickstream mining) measures behavior such as the click-through rate on the top result or any result on the first page. These are cheap to run, easy to interpret, and detect subtle effects at scale.

### Results Snippets
Result snippets are presentations of each hit in the SERP. **Static summaries** are query-independent — typically the first sentences, leading paragraphs, or designated zones (title, abstract); they are computed at indexing time and cached. **Dynamic (query-biased) summaries** are computed at query time using a **keyword-in-context (KWIC)** approach: locate windows containing query terms and surrounding context, prefer windows with phrase matches, and use NLP cues to break on sentence boundaries. Dynamic snippets typically beat static ones on user utility but require keeping a generous document prefix (~10,000 characters) cached at the search node.

## Algorithms & Formulas

### Precision and Recall (from the 2×2 contingency table)

```
            Relevant      Non-relevant
Retrieved   tp            fp
Not retr.   fn            tn

Precision  P = tp / (tp + fp)
Recall     R = tp / (tp + fn)
Accuracy   A = (tp + tn) / (tp + fp + fn + tn)   -- NOT useful for IR
```

### F-measure (weighted harmonic mean)

```
F_β = ((β² + 1) · P · R) / (β² · P + R)
F₁  = 2PR / (P + R)              -- balanced F (β = 1)
```

β > 1 weights recall more; β < 1 weights precision more. The harmonic mean is conservative: it is closer to the smaller of P and R, so a system cannot game F by maximizing one at the expense of the other.

### Interpolated Precision

```
P_interp(r) = max { P(r') : r' ≥ r }
```

Yields a monotonically non-increasing curve; used as the basis for 11-point average precision.

### 11-Point Interpolated Average Precision (per query)

```
AvgP_11 = (1/11) · Σ_{r ∈ {0.0, 0.1, ..., 1.0}} P_interp(r)
```

### Average Precision (per query) and Mean Average Precision (across queries)

```
AP(q) = (1 / |Rel_q|) · Σ_{k : doc_k is relevant} Precision@k

MAP   = (1 / |Q|) · Σ_{q ∈ Q} AP(q)
```

Where Rel_q is the set of documents relevant to query q. Unretrieved relevant documents contribute precision = 0.

### R-Precision and Breakeven

```
R-Prec(q) = Precision@|Rel_q|
```

R-Precision equals the precision at the rank where precision equals recall (the **breakeven point**).

### Discounted Cumulative Gain (DCG) and NDCG

For ranked position *i* and graded relevance score rel_i:

```
DCG_p = Σ_{i=1}^{p}  rel_i / log_2(i + 1)
```

(An equivalent form weights gain exponentially: gain = 2^{rel_i} - 1.) Normalize by the DCG of the ideal ranking (sorting documents by relevance descending):

```
NDCG_p = DCG_p / IDCG_p
```

NDCG_p ∈ [0, 1]; 1.0 is a perfect ranking. The log₂(i+1) discount expresses the assumption that users attend less to lower-ranked positions.

### Cohen's Kappa Coefficient

```
κ = (P(A) - P(E)) / (1 - P(E))
```

P(A) is the proportion of items on which the two judges agree. P(E) is the agreement expected by chance, computed from the marginal probabilities of each label. κ = 1 is perfect; κ = 0 is chance; κ < 0 is worse than chance. Interpretation: > 0.8 good, 0.67-0.8 fair, < 0.67 dubious for evaluation.

## Key Quotes

> "Information retrieval has developed as a highly empirical discipline, requiring careful and thorough evaluation to demonstrate the superior performance of novel techniques on representative document collections."

> "Most of the time we will assume that the relevance of each document to each query is a binary judgment."

> "We would normally like to test the system on a different collection of documents than that used in its construction."

> "Using accuracy as a measure of effectiveness ... in normal circumstances, the data is extremely skewed: normally over 99.9% of the documents are in the non-relevant category."

> "Precision-recall curves have a distinctive saw-tooth shape."

> "Mean Average Precision ... provides a single-figure measure of quality across recall levels."

> "Two judges agreeing does not necessarily mean that they are correct."

> "Formal evaluation measures are at some distance from our ultimate interest in measures of human utility."

> "User happiness is elusive to measure, and this is part of why the standard methodology uses the proxy of relevance of search results."

## Connections

- [[InformationRetrieval]] — this chapter defines the standard methodology for evaluating any IR system.
- [[Precision]] — fraction of retrieved that is relevant; the canonical precision-recall partner.
- [[Recall]] — fraction of relevant that is retrieved.
- [[FMeasure]] — weighted harmonic mean of precision and recall; F₁ is the balanced case.
- [[F1Score]] — the balanced F-measure with β = 1.
- [[PrecisionRecall]] — joint metric pair foundational to IR evaluation.
- [[PrecisionRecallCurve]] — graphical plot of precision against recall across rank cutoffs.
- [[PrecisionAtK]] — practical metric for fixed-cutoff evaluation (e.g., P@10).
- [[MeanAveragePrecision]] — dominant single-number ranked-retrieval metric.
- [[MAP]] — alias for Mean Average Precision in the IR literature.
- [[AveragePrecision]] — per-query precursor to MAP.
- [[RPrecision]] — precision at rank equal to the number of relevant documents; coincides with breakeven.
- [[NDCG]] — normalized discounted cumulative gain for graded relevance.
- [[ROCCurve]] — true-positive rate vs false-positive rate; less natural for IR than P-R.
- [[KappaCoefficient]] — inter-annotator agreement metric for relevance judgments.
- [[CohensKappa]] — the classical formulation of κ used in IR assessor agreement.
- [[CranfieldParadigm]] — the experimental methodology this chapter formalizes.
- [[TRECCollection]] — the family of test collections produced by the NIST evaluation series.
- [[TREC]] — the Text Retrieval Conference evaluation program.
- [[NIST]] — the U.S. National Institute of Standards and Technology, which administers TREC.
- [[Cranfield]] — the original test collection and project (UK, late 1950s).

## Contradictions

No direct contradictions with existing wiki content. Worth noting for future synthesis:

- The chapter's binary-relevance default sits in tension with later modern practice (and INEX/TREC graded tracks); subsequent wiki pages on NDCG and learning-to-rank should reconcile this evolution.
- The claim that "different judges yield similar *relative* system rankings" is sometimes nuanced by later work on judgment depth and pool incompleteness; surface this if a contradicting source is ingested.
- The 2008 framing treats A/B testing and clickthrough analysis as the deployed-system tools; later sources may extend this to interleaving, counterfactual evaluation, and bandit-based exploration not covered here.
