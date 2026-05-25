---
title: "Boolean Retrieval"
type: concept
tags: [information-retrieval, boolean-model, set-operations]
sources: [iir-ch01-boolean-retrieval, iir-ch07-complete-search-system]
last_updated: 2026-05-23
---

The simplest retrieval model: queries are expressions in **Boolean algebra** over terms (AND, OR, NOT), and a document either satisfies the query or not — there is no ranking, only a set of matches. Implemented via [[PostingsList]] operations on the [[InvertedIndex]]:

- `term1 AND term2` → intersection of postings.
- `term1 OR term2` → union of postings.
- `term1 AND NOT term2` → set difference (efficient via paired-walk over both lists).

**Query optimization**: process AND-conjunctions in order of increasing $\text{df}_t$ (rarest term first) so the intermediate result set stays small. For long conjunctions, accumulate document scores rather than materializing intermediate result sets.

**Strengths**: precise control for expert users (e.g. lawyers using [[Westlaw]], librarians), deterministic, no parameter tuning, exact match semantics.

**Weaknesses**: binary relevance only — no ranking, no partial match, no weighting; users must construct precise expressions; small wording differences (singular/plural, synonyms) cause matches to be missed. These weaknesses motivate the **extended Boolean model** (ranking over partial matches) and ultimately ranked retrieval via the [[VectorSpaceModel]] / [[BM25]] / [[QueryLikelihoodModel]] (see [[iir-ch01-boolean-retrieval]] §1.4).

In modern systems Boolean operators survive inside ranked retrieval as filter clauses (e.g. `AND site:example.com`) rather than as the sole match criterion — see [[iir-ch07-complete-search-system]] §7.3.
