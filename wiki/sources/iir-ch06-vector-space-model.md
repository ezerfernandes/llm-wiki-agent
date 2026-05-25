---
title: "IIR Ch. 6: Scoring, Term Weighting and the Vector Space Model"
type: source
tags: [iir, information-retrieval, textbook, tf-idf, vector-space-model, cosine-similarity]
date: 2026-05-23
source_file: "https://nlp.stanford.edu/IR-book/html/htmledition/scoring-term-weighting-and-the-vector-space-model-1.html"
---

## Summary
Chapter 6 of Manning, Raghavan, and Schütze's *Introduction to Information Retrieval* (Cambridge, 2008) is the textbook's pivot from set-based [[BooleanRetrieval]] (Ch. 1) to **ranked retrieval**: the chapter argues that "for large document collections, the resulting number of matching documents can far exceed the number a human user could possibly sift through," so "it is essential for a search engine to rank-order the documents matching a query." It builds the apparatus for ranking in three layers. First, **parametric and zone indexes** (§6.1) extend the [[InvertedIndex]] to typed metadata (author, date) and free-text regions (title, abstract, body), and define [[WeightedZoneScoring]] as a linear combination of per-zone Boolean scores whose weights can be learned from human relevance judgments. Second, **term frequency and weighting** (§6.2) replace presence/absence with the **[[BagOfWords]]** assumption that within-document occurrence counts carry signal, defines `tf_{t,d}` and the collection-level statistic `df_t`, derives the canonical [[InverseDocumentFrequency]] `idf_t = log(N/df_t)` to discount common terms, and composes them into the [[TFIDF|tf-idf]] weight `tf-idf_{t,d} = tf_{t,d} × idf_t`. Third, **the [[VectorSpaceModel]]** (§6.3) embeds each document as a vector `V(d)` in |V|-dimensional term-weight space, embeds the query the same way, scores them by [[CosineSimilarity]] `cos(q,d) = V(q)·V(d) / (|V(q)| |V(d)|)` to length-normalize, and computes the top-K with the **COSINESCORE** term-at-a-time algorithm using a heap. The chapter closes (§6.4) with variant tf-idf functions — **sublinear (log) tf scaling**, **maximum tf normalization**, the **SMART `ddd.qqq` notation** for naming weighting schemes (with `lnc.ltc` as the canonical recommendation), and **[[PivotedLengthNormalization]]** which corrects cosine normalization's bias against long documents. Together these pieces give the first complete ranked-retrieval pipeline of the book; Ch. 7 then adds efficient top-K approximation and Chs. 11–12 extend the same scaffolding to probabilistic IR and language models, with [[BM25]] inheriting the tf-saturation and length-normalization insights developed here.

## Key Claims
- Boolean retrieval is inadequate at scale because matching sets are unordered and frequently too large; a usable search engine must "assign a score — a measure of how well document and query match" and rank by it.
- A **parametric index** is built per structured field (author, date, language) with a finite known value set; ordered fields support range queries via [[BTree|B-trees]], and parametric indexes can be combined with content queries (e.g. `author=Shakespeare AND year=1601 AND "alas poor Yorick"`).
- A **zone** is a free-text region (title, abstract, references, body); each zone may get its own inverted index, or — preferred — zone information is encoded directly inside postings entries to keep the dictionary small.
- [[WeightedZoneScoring]] (a.k.a. *ranked Boolean retrieval*) scores a document as `score(d,q) = Σ_{i=1}^{ℓ} g_i · s_i`, where `s_i ∈ {0,1}` is the zone-`i` Boolean score, `g_i ∈ [0,1]` is a fixed weight, and the `g_i` sum to 1; with weights (0.2, 0.3, 0.5) over (author, title, body), a term hitting title and body but not author scores `0.3 + 0.5 = 0.8`.
- The per-zone weights `g_i` can be **machine-learned** from labeled `(query, document, Relevant/Non-relevant)` tuples by minimizing squared error between the computed score and the editorial judgment — an early instance of [[LearningToRank|machine-learned relevance]].
- For the two-zone case the optimal weight has a closed form: `g* = (n_{01r} + n_{10n}) / (n_{01r} + n_{10n} + n_{01n} + n_{10r})`, where `n_{xys}` is the number of training examples with title-match `x`, body-match `y`, and judgment `s` (`r` = relevant, `n` = non-relevant); training pairs where both zone signals agree contribute nothing to `g*`.
- **Term frequency** `tf_{t,d}` is the raw count of term `t` in document `d`; under the [[BagOfWords]] assumption, "Mary is quicker than John" and "John is quicker than Mary" are treated as identical, but documents with similar tf profiles are presumed similar in content.
- Raw tf is a bad weight on its own: collection-wide common words ("auto" in an auto-industry collection) saturate every document and add no discriminative signal — motivating term *specificity*.
- **Document frequency** `df_t` (number of documents containing `t`) is preferred over **collection frequency** `cf_t` (total occurrences) because it captures discriminative power; in the Reuters-RCV1 collection (N = 806,791), `try` and `insurance` have nearly identical `cf ≈ 10,400`, yet `df_{insurance} = 3,997` while `df_{try} = 8,760`, so `insurance` is the more informative term.
- [[InverseDocumentFrequency]] is `idf_t = log(N/df_t)`; rare terms get a high idf, ubiquitous terms get a low idf, the log base is irrelevant for ranking, and idf has no effect on **one-term queries** (it shifts all scores by the same constant).
- The **tf-idf weight** is `tf-idf_{t,d} = tf_{t,d} × idf_t`; it is (i) highest when `t` is frequent in a few documents, (ii) lower when `t` is rare in `d` or appears in many documents, and (iii) lowest when `t` appears in essentially every document.
- The basic **overlap score** for a free-text query sums tf-idf across query terms: `Score(q,d) = Σ_{t∈q} tf-idf_{t,d}`; each document becomes a sparse vector in |V|-dimensional term-weight space.
- **[[CosineSimilarity]]** scores documents by the cosine of the angle between their tf-idf vectors: `sim(d_1, d_2) = V(d_1)·V(d_2) / (|V(d_1)| |V(d_2)|) = v(d_1)·v(d_2)` after length-normalizing each vector to its [[EuclideanNorm|Euclidean]] unit form `v(d) = V(d)/|V(d)|`; this is the canonical "more like this" operation.
- The query is treated as a "very short document": it is embedded in the same vector space as documents and ranked by `score(q,d) = V(q)·V(d) / (|V(q)| |V(d)|)`. Documents do **not** need to contain every query term to score highly.
- The **COSINESCORE** algorithm computes the top-K documents in time roughly proportional to total postings traversed plus heap maintenance; it uses an accumulator array `Scores[]`, processes one query term at a time, multiplies each posting's stored `tf` by the precomputed query weight, divides each `Scores[d]` by `Length[d]` at the end, and extracts top-K with a heap (≈ 2N comparisons to build, O(log N) per extraction, so O(K log N) total).
- The textbook recommends **storing `tf` in postings** (not the full tf-idf weight) so that `idf` can be applied at query time and re-tuning the weighting scheme doesn't require re-indexing; `Length[d]` (the document's Euclidean norm) is stored once per document.
- **Sublinear tf scaling** dampens the effect of repeated occurrences: `wf_{t,d} = 1 + log(tf_{t,d})` if `tf_{t,d} > 0`, else `0`; rationale — "it seems unlikely that twenty occurrences of a term in a document truly carry twenty times the significance of a single occurrence." Substitute `wf` for `tf` everywhere, yielding `wf-idf_{t,d} = wf_{t,d} · idf_t`.
- **Maximum tf normalization** rescales tf relative to the document's most frequent term: `ntf_{t,d} = a + (1-a) · tf_{t,d}/tf_{max}(d)` with smoothing `a ∈ [0,1]` (typically `a = 0.4`, originally `0.5`); designed so that appending a document to itself does not change scores (it would under raw tf-idf). Limitations: brittleness to stop-list changes, sensitivity to outlier high-frequency terms, and inability to distinguish flat vs peaked tf distributions.
- The **SMART `ddd.qqq` notation** (Salton, Cornell) compactly names a weighting scheme as three letters for the document vector and three for the query vector, in the order (tf-component) (df-component) (normalization). Letters include `n` natural / `l` logarithm / `a` augmented / `b` boolean / `L` log average for tf; `n` none / `t` idf / `p` prob-idf for df; `n` none / `c` cosine / `u` pivoted / `b` byte size for normalization. The canonical recommended setting is **`lnc.ltc`**: documents use log tf, no idf, cosine normalization; queries use log tf, idf, cosine normalization. Using different schemes for document and query is normal and motivated by efficiency.
- **[[PivotedLengthNormalization]]** corrects cosine normalization's empirical bias: cosine over-penalizes long documents (which are relevant more often than the unit-sphere geometry predicts) and under-penalizes short ones. It pivots the normalization curve about a **pivot length** `ℓ_p` (the document length where probability of relevance matches probability of retrieval); the modified normalizer is `a·|V(d)| + (1-a)·piv`, with slope `a < 1` rotating the curve counter-clockwise. A cheap approximation replaces `|V(d)|` with `u_d`, the count of unique terms in `d`. Pivoted normalization underlies SMART's `u`-class schemes and the length-normalization terms in [[BM25|Okapi BM25]].
- Computing exact cosine scores over a large collection is expensive (a one-million-document collection with even modest vocabulary requires tens of thousands of arithmetic ops per document); the chapter defers efficient top-K approximation, champion lists, and tiered indexes to Chapter 7.

## Section Notes

### 6.1 Parametric and zone indexes
Documents have **structured metadata** (zones with restricted vocabularies — language, format, publication date, author) and **zones** (free-text regions such as title, abstract, references, body). A **parametric index** is one inverted index per field with values as dictionary entries; ordered fields use a [[BTree|B-tree]] to support range queries. **Zone indexes** can be built per zone, but the recommended encoding folds the zone label into each posting (e.g. `william.author:7`, `william.title:11`) so the dictionary stays small. A motivating sample query combines parametric and zone search: "find documents authored by William Shakespeare in 1601 containing `alas poor Yorick`." Zone indexes are the substrate for the next subsection's weighted zone scoring and for [[FieldedSearch|fielded search]] in production engines like [[Lucene]] and [[Elasticsearch]].

### 6.1.1 Weighted zone scoring
[[WeightedZoneScoring]], also called **ranked Boolean retrieval**, is the chapter's first ranking function: `score(d,q) = Σ_{i=1}^{ℓ} g_i · s_i`, with `s_i` a Boolean per-zone match (0/1) — optionally graded by partial query coverage — and `g_i ∈ [0,1]` zone weights summing to 1. Worked example with zones (author, title, body) and weights (0.2, 0.3, 0.5): a document where `shakespeare` hits only title and body scores `0 + 0.3 + 0.5 = 0.8`. Implemented as a slight variant of the [[PostingsListIntersection]] merge — accumulate `g_i · s_i` into a `Scores[]` array as you walk the postings — and generalized to arbitrary Boolean functions over zones.

### 6.1.2 Learning weights
Rather than asking a domain expert to set `g_i`, treat weight choice as **supervised learning**: given training tuples `(q, d, judgment ∈ {Relevant, Non-relevant})`, choose `g` to minimize `Σ ε(judgment, score(d,q))² ` (squared loss against `r(q,d) ∈ {0,1}`). Introduces the chapter's framing of **[[LearningToRank|machine-learned relevance]]**, foreshadowing Ch. 15. The dominant practical cost is the **labor of human relevance judgments**, especially for a moving target like the web.

### 6.1.3 The optimal weight g
For two zones (title, body) the squared-error objective has a closed form. Partition training pairs by their zone-match pattern and judgment into eight bins `n_{xys}` (`x` = title match 0/1, `y` = body match 0/1, `s` = `r`/`n`). The optimum is `g* = (n_{01r} + n_{10n}) / (n_{01r} + n_{10n} + n_{01n} + n_{10r})`. **Agreeing examples** (both zones matched or both missed) drop out of the formula entirely — they tell you nothing about the relative importance of the two zones. This is the textbook's first concrete optimization result and a template for later learning-to-rank derivations.

### 6.2 Term frequency and weighting
The unweighted Boolean view ("does `t` appear in `d`?") wastes signal because the **count** matters. Define **term frequency** `tf_{t,d}` as the raw count and adopt the [[BagOfWords]] model — discard word order, retain a multiset of types. The bag-of-words assumption is acknowledged as deliberately impoverished ("Mary is quicker than John" ≡ "John is quicker than Mary") and will be re-introduced indirectly via phrase indexes (Ch. 2.4) and proximity scoring (Ch. 7). Stop words are still removed before computing tf.

### 6.2.1 Inverse document frequency
Raw tf treats `auto` and `arachnocentric` symmetrically; we need to scale terms by **specificity**. Two collection-level statistics compete: **collection frequency** `cf_t` (total occurrences) and **document frequency** `df_t` (number of documents containing `t`). The chapter prefers `df_t` because it captures dispersion better — the Reuters example (`try` vs `insurance`, both with `cf ≈ 10,400`, but `df_{insurance} = 3,997` vs `df_{try} = 8,760`) makes the case quantitatively. The **idf** is then `idf_t = log(N/df_t)` (N = collection size). idf is **constant per term** across the collection (not per document), the log base is irrelevant for ranking, and idf has **no effect on one-term queries** since it shifts all candidate scores uniformly.

### 6.2.2 Tf-idf weighting
Compose the two pieces: `tf-idf_{t,d} = tf_{t,d} × idf_t`. The classic three regimes are: (i) highest when `t` is frequent in `d` and rare in the collection, (ii) lower when `t` is rare in `d` or common in the collection, (iii) lowest when `t` is in essentially every document. The simple **overlap score** for a free-text query is `Score(q,d) = Σ_{t∈q} tf-idf_{t,d}`. The implicit move here — representing each `d` as a vector of tf-idf weights indexed by the vocabulary — sets up the vector space model.

### 6.3 The vector space model for scoring
The vector space model (Salton's SMART system, Cornell, 1971) represents each document as a vector `V(d) ∈ R^{|V|}` whose components are term weights (default: tf-idf). This is the substrate "fundamental to a host of information retrieval operations ranging from scoring documents on a query, document classification and document clustering," and the same representation will be reused for [[TextClassification]] (Ch. 13) and [[Clustering]] (Chs. 16–17).

### 6.3.1 Dot products
Define **document similarity** as the dot product `V(d_1)·V(d_2) = Σ x_i y_i`. A naive Euclidean *distance* between vectors is wrong because a long document and its copy-paste duplicate would be "far apart" simply due to magnitude. Fix with [[CosineSimilarity]]: `sim(d_1, d_2) = V(d_1)·V(d_2) / (|V(d_1)| |V(d_2)|) = v(d_1) · v(d_2)`, where `v(d) = V(d)/|V(d)|` is the unit-length form. The cosine is 1 for identically directed vectors and 0 for orthogonal vectors (no shared terms). Application: **"more like this"** — fix a document, dot it against every other, rank by cosine. Worked example on three short novels (`Sense and Sensibility`, `Pride and Prejudice`, `Wuthering Heights`) shows that the two Austen novels have higher mutual cosine than either does to Brontë.

### 6.3.2 Queries as vectors
Treat the query as a "very short document" in the same |V|-dimensional space: `score(q,d) = V(q)·V(d) / (|V(q)| |V(d)|)`. This unifies free-text retrieval, document-document similarity, classification, and clustering under one geometry. Worked example: the query `best car insurance` against a million-document collection — query gets idf-weighted unit vector; documents get tf-weighted, length-normalized vectors; the dot product accumulates `(query weight) × (document weight)` per shared term. Documents **need not contain every query term** to rank highly.

### 6.3.3 Computing vector scores: the COSINESCORE algorithm
The full top-K algorithm:

```
CosineScore(q):
  float Scores[N] = 0
  float Length[N]                    # precomputed Euclidean norms
  for each query term t in q:
    calculate w_{t,q} and fetch postings list for t
    for each pair(d, tf_{t,d}) in postings list:
      Scores[d] += wf_{t,d} × w_{t,q}
  for d in 1..N:
    Scores[d] /= Length[d]
  return Top-K(Scores) using a heap
```

This is **term-at-a-time** scoring: each query term's postings list is walked, contributions accumulated into `Scores`. The dual strategy is **document-at-a-time**, which advances all postings lists in lockstep; the trade-off (memory for accumulators vs cursor management) is taken up in Ch. 7. Engineering details: postings store `tf_{t,d}` (not full tf-idf) so idf and the weighting scheme can be retuned without re-indexing; `Length[d]` is computed once per document at index time; the top-K heap is built in ≈ 2N comparisons and yields K results in O(K log N).

### 6.4 Variant tf-idf functions
Section 6.4 catalogues alternatives to plain tf and tf-idf.

### 6.4.1 Sublinear tf scaling
The plain tf is linear in raw count, but "it seems unlikely that twenty occurrences of a term in a document truly carry twenty times the significance of a single occurrence." Replace with **log-scaled tf**: `wf_{t,d} = 1 + log(tf_{t,d})` when `tf_{t,d} > 0`, else `0`. Substitute everywhere: `wf-idf_{t,d} = wf_{t,d} · idf_t`. This is the SMART `l` letter for tf, and it underlies the saturation curves used by [[BM25]].

### 6.4.2 Maximum tf normalization
A second tf adjustment normalizes by the document's own max tf: `ntf_{t,d} = a + (1-a) · tf_{t,d}/tf_{max}(d)`, with a smoothing constant `a ∈ [0,1]` (recommended `a = 0.4`; originally `0.5` in Salton & Buckley). Motivation: if you concatenate a document to itself, its tf-idf score should be unchanged — but under raw tf it would double. The smoothing term `a` prevents large swings from small changes in tf. Three caveats: (i) brittle to stop-list edits (changing the stop list can change `tf_{max}` discontinuously), (ii) one outlier high-frequency term distorts every other weight, (iii) cannot distinguish documents with flat tf distributions from documents with one dominant peak.

### 6.4.3 Document and query weighting schemes — SMART `ddd.qqq` notation
Different choices of (tf, df, normalization) are encoded by a six-letter mnemonic `ddd.qqq`: the first triple specifies the **document** vector's tf, df, and normalization; the second the **query** vector's. The standard letter codes are:

- **tf component**: `n` natural (raw tf), `l` logarithm `1 + log(tf)`, `a` augmented `0.5 + 0.5 · tf/tf_max`, `b` boolean (1 if tf > 0), `L` log average `(1 + log(tf)) / (1 + log(avg_d(tf)))`.
- **df component**: `n` none (= 1), `t` idf `log(N/df)`, `p` prob-idf `max{0, log((N − df)/df)}`.
- **normalization**: `n` none, `c` cosine `1/√(Σ w²)`, `u` pivoted unique, `b` pivoted byte length.

The recommended canonical scheme is **`lnc.ltc`**: documents use log tf, no idf, cosine; queries use log tf, idf, cosine. Asymmetric schemes (documents and queries weighted differently) are normal and motivated by the fact that idf changes slowly and can be applied cheaply at query time, while document weights must be precomputed and stored.

### 6.4.4 Pivoted normalized document length
Cosine normalization treats all documents as unit vectors, but empirically — across TREC test collections — relevance is **not** uniform across document lengths: long documents are relevant more often than cosine retrieves them, and short documents less often. The chapter plots probability-of-relevance vs probability-of-retrieval as functions of document length, finds them crossing at a **pivot length** `ℓ_p`, and **rotates the normalization curve** counter-clockwise about that pivot: replace `|V(d)|` with `a · |V(d)| + (1 - a) · piv`, where slope `a < 1`. The cheap approximation `a · u_d + (1 - a) · piv` uses the count of unique terms `u_d` in place of the Euclidean norm. Pivoted normalization is **not universal** — for FAQ collections (where length is roughly content-neutral) it can hurt. It is the conceptual ancestor of BM25's `b · |d|/avgdl + (1 − b)` length term.

### 6.5 References and further reading
Anchors the chapter in the historical literature:
- **Luhn (1957, 1958)** — earliest term weighting, advocates medium-frequency terms (neither too common nor too rare), anticipating tf-idf.
- **Spärck Jones (1972)** — original experimental case for idf.
- **Robertson and Spärck Jones (1976), Croft and Harper (1979), Salton and Buckley (1987), Papineni (2001)** — theoretical justifications for idf; Robertson maintains a historical IDF page at `http://www.soi.city.ac.uk/~ser/idf.html`.
- **Salton (1971b)** — the SMART system at Cornell, "among the first to view a document as a vector of weights."
- **Salton and Buckley (1988), Singhal et al. (1995, 1996b)** — the SMART weighting notation in Figure 6.15.
- **Zobel and Moffat (1998, 2006)** — efficient cosine score computation; foundational reference for production implementations.
- **Turtle and Flood (1995)** — analysis of term-at-a-time vs document-at-a-time query evaluation.
- **Moffat and Zobel (1998)** — expanded the SMART notation and used hill-climbing to identify high-performing weighting combinations.

## Algorithms & Formulas

### Inverse document frequency
- `idf_t = log(N / df_t)` where `N` = total documents, `df_t` = number of documents containing term `t`.
- Rare terms get high idf; ubiquitous terms approach `idf = 0`.
- Constant per term across the collection; log base is irrelevant for ranking; idf has no effect on single-term queries.

### Tf-idf
- `tf-idf_{t,d} = tf_{t,d} × idf_t`
- Overlap score: `Score(q, d) = Σ_{t ∈ q} tf-idf_{t,d}`.

### Sublinear (log) tf
- `wf_{t,d} = 1 + log(tf_{t,d})` if `tf_{t,d} > 0`, else `0`.
- `wf-idf_{t,d} = wf_{t,d} · idf_t`.

### Maximum tf normalization
- `ntf_{t,d} = a + (1 - a) · tf_{t,d} / tf_{max}(d)`, with `a ∈ [0,1]`, recommended `a = 0.4`.

### Vector space cosine similarity
- Document vector: `V(d) ∈ R^{|V|}` with `V(d)_t = tf-idf_{t,d}` (or any weighting variant).
- Unit vector: `v(d) = V(d) / |V(d)|`, where `|V(d)| = √(Σ_t V(d)_t²)`.
- Document-document: `sim(d_1, d_2) = V(d_1) · V(d_2) / (|V(d_1)| |V(d_2)|) = v(d_1) · v(d_2)`.
- Query-document: `score(q, d) = V(q) · V(d) / (|V(q)| |V(d)|)`.

### Weighted zone scoring
- `score(d, q) = Σ_{i=1}^{ℓ} g_i · s_i`, with `Σ_i g_i = 1`, `s_i ∈ [0,1]`.
- Closed-form optimum for two zones (title, body):
  `g* = (n_{01r} + n_{10n}) / (n_{01r} + n_{10n} + n_{01n} + n_{10r})`
  where `n_{xys}` counts training tuples with title-match `x`, body-match `y`, judgment `s`.

### COSINESCORE algorithm
```
CosineScore(q):
  Scores[1..N] := 0
  for each query term t in q:
    w_{t,q} := query-weight for t (e.g. (1 + log tf_{t,q}) · idf_t)
    fetch postings list for t
    for each (d, tf_{t,d}) in postings:
      Scores[d] += wf_{t,d} · w_{t,q}
  for d in 1..N:
    Scores[d] /= Length[d]
  return Top-K(Scores) via heap
```
- `Length[d]` = precomputed Euclidean norm of document vector `V(d)`.
- Postings store `tf_{t,d}` (not full tf-idf) so the weighting scheme can be retuned without re-indexing.
- Top-K heap: O(N) to build (≈ 2N comparisons), O(K log N) to extract K winners.

### SMART `ddd.qqq` notation
Six-letter mnemonic naming a (document, query) weighting pair. Each triple is (tf-letter, df-letter, normalization-letter):

| Position | Codes |
|---|---|
| tf | `n` natural · `l` log `1+log(tf)` · `a` augmented `0.5 + 0.5·tf/tf_max` · `b` boolean (1 if tf>0) · `L` log-avg `(1+log tf)/(1+log avg_d tf)` |
| df | `n` none (=1) · `t` idf `log(N/df)` · `p` prob-idf `max{0, log((N−df)/df)}` |
| normalization | `n` none · `c` cosine `1/√Σ w²` · `u` pivoted unique · `b` pivoted byte |

Canonical recommendation: **`lnc.ltc`** — documents log-tf / no-idf / cosine; queries log-tf / idf / cosine.

### Pivoted length normalization
- Replace `|V(d)|` in the cosine denominator with `a · |V(d)| + (1 − a) · piv`, with `0 < a < 1` rotating the curve about the pivot length `ℓ_p`.
- Cheap approximation: `a · u_d + (1 − a) · piv`, where `u_d` = count of unique terms in `d`.
- Effect: larger normalizer for short documents, smaller for long ones — corrects the systematic length bias of plain cosine.

## Key Quotes
> "Thus far, our queries have all been Boolean. Documents either match or do not. In the case of large document collections, the resulting number of matching documents can far exceed the number a human user could possibly sift through. Accordingly, it is essential for a search engine to rank-order the documents matching a query." — chapter intro, motivating ranked retrieval.

> "If the term shakespeare were to appear in the title and body zones but not the author zone of a document, the score of this document would be 0.8." — §6.1.1, illustrating weighted zone scoring with weights `(0.2, 0.3, 0.5)`.

> "It seems unlikely that twenty occurrences of a term in a document truly carry twenty times the significance of a single occurrence." — §6.4.1, motivating sublinear tf scaling.

> "The vector space model is fundamental to a host of information retrieval operations ranging from scoring documents on a query, document classification and document clustering." — §6.3, framing the model's role across the book.

> "Pivoted document length normalization is not appropriate for all applications" — §6.4.4, e.g. FAQ collections where document length is roughly orthogonal to relevance.

## Connections
- [[InformationRetrieval]] — Ch. 6 is the textbook's transition from set-based retrieval to ranked retrieval inside the IR field this book defines.
- [[BooleanRetrieval]] — the model Ch. 6 supersedes; weighted zone scoring is a graded generalization of Boolean conjunction.
- [[InvertedIndex]] — the substrate; Ch. 6 enriches it with per-zone postings, stored `tf`, and per-document length.
- [[VectorSpaceModel]] — the central abstraction the chapter develops; reused for [[TextClassification]] and [[Clustering]] in later chapters.
- [[TermFrequency]] — `tf_{t,d}` is defined here as the raw count; the chapter studies many normalizations of it.
- [[InverseDocumentFrequency]] — `idf_t = log(N/df_t)`; this chapter is the canonical textbook reference.
- [[TFIDF]] / [[TfIdf]] — `tf-idf_{t,d} = tf_{t,d} × idf_t`; everything in Ch. 6.3 builds on this product.
- [[CosineSimilarity]] — the chapter's scoring function `cos(q,d) = V(q)·V(d)/(|V(q)||V(d)|)`.
- [[DotProduct]] — primitive operation behind cosine and the COSINESCORE loop.
- [[VectorSpace]] — the geometric object documents and queries are embedded in.
- [[BagOfWords]] — the modeling assumption that makes tf-based ranking possible.
- [[ZoneIndex]] — the data structure introduced in §6.1 for free-text regions like title/abstract/body.
- [[WeightedZoneScoring]] — §6.1.1's `Σ g_i s_i` linear combination of zone scores.
- [[LearningToRank]] — §6.1.2 introduces machine-learned relevance, foreshadowing Ch. 15.
- [[SmartNotation]] — the `ddd.qqq` mnemonic for naming weighting schemes.
- [[PivotedLengthNormalization]] — §6.4.4's correction for cosine's length bias; conceptual ancestor of BM25's length term.
- [[BM25]] — inherits sublinear tf saturation and pivoted-length normalization from this chapter, then adds a tunable saturation parameter `k_1`.
- [[ClassBasedTFIDF]] (c-TF-IDF) — modern variant that aggregates tf-idf at the cluster level; rests on the same `tf × idf` decomposition.
- [[EuclideanNorm]] — the document-length normalizer `|V(d)| = √Σ_t V(d)_t²`.
- [[BTree|B-tree]] — backing structure for ordered parametric fields supporting range queries (e.g. dates).
- [[PostingsListIntersection]] — Ch. 1 merge primitive, reused inside weighted-zone scoring and document-at-a-time COSINESCORE variants.
- [[Lucene]] / [[Elasticsearch]] — production systems whose scorers descend directly from this chapter's tf-idf, length normalization, and zone weighting.

## Contradictions
- **Bag of words vs phrase / proximity search.** Ch. 6 explicitly adopts the bag-of-words assumption and notes that under it "Mary is quicker than John" and "John is quicker than Mary" are identical. Ch. 2.4 (biword indexes) and Ch. 7 (proximity scoring) walk that back. The chapter flags this internally as a deliberate simplification, not a true contradiction.
- **Cosine vs pivoted length normalization.** §6.3.2 presents cosine normalization as the canonical document-length correction; §6.4.4 then shows empirically that cosine systematically over-penalizes long documents and replaces it with the pivoted form. The textbook resolves the tension by treating cosine as a strong default and pivoted normalization as an empirical refinement.
- **Raw tf vs sublinear / maximum-tf.** §6.2.2 sums raw `tf_{t,d}` for the overlap score, then §6.4.1–6.4.2 argue against linear tf. Again the chapter is explicit that 6.2 is a baseline that 6.4 refines.
- No contradictions with other wiki sources are introduced. The chapter is upstream of [[BM25]] (which extends it), so any apparent tension with the BM25 page reflects the BM25 page's later refinements rather than a disagreement with this source.
