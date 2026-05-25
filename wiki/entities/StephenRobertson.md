---
title: "Stephen Robertson"
type: entity
tags: [person, researcher, information-retrieval, probabilistic-ir]
sources: [iir-ch11-probabilistic-ir]
last_updated: 2026-05-23
---

British computer scientist; central figure in **probabilistic information retrieval**. Best known for:

1. The **[[ProbabilityRankingPrinciple]]** (1977) — the foundational theorem that ranking by $P(R=1 \mid q, d)$ is optimal under 1/0 loss. This single result licenses the entire probabilistic-IR family of rankers.
2. The **[[OkapiBM25|Okapi BM25]]** ranking function (1994–95, with [[KarenSparckJones]], Susan Walker, Steve Walker, Micheline Hancock-Beaulieu, Mike Gatford) — the workhorse of pre-neural production search, still in use a quarter-century later as the default ranker in Lucene / Elasticsearch / Solr / Whoosh / Tantivy.
3. Joint work with Sparck Jones on **[[InverseDocumentFrequency|idf]]** and the **[[BinaryIndependenceModel|Binary Independence Model]]** — the probabilistic ancestor of BM25.

Career: City University London (PhD 1969), University College London, Cambridge / Microsoft Research Cambridge (joined the founding MSR Cambridge team, retired 2013), now emeritus at MSR Cambridge and UCL. ACM SIGIR Gerard Salton Award (2000) — joint with Sparck Jones — for the probabilistic-IR program.

The Okapi system at City University London (named for the rare Congolese ungulate) was the experimental platform on which BM25 was developed and tuned through the TREC ad-hoc tracks. The "BM" stands for **best match**.
