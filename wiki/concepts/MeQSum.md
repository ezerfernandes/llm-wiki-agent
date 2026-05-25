---
title: "MeQSum"
type: concept
tags: [dataset, medical-nlp, summarization, query, stub]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# MeQSum

**Medical question summarization dataset** — Ref [49] in [[2507.03152-medval]]. Comprises (1) health-related queries from patients sourced from messages sent to the U.S. National Library of Medicine, and (2) corresponding abbreviated questions formulated by three medical experts to facilitate complete and accurate answer retrieval.

Used as the **`query2question`** task source in [[MedVALBench]]: patient query → concise health question. Train 500 / test 120; avg 82±66 input tokens.

**Lowest inter-physician Krippendorff's $\alpha = 0.560$** of any MedVALBench task — query summarization has the most ambiguous "correctness" criterion, and MedVAL F1 is correspondingly lower than on other tasks.

## Connections
- [[2507.03152-medval]] — the application paper.
- [[MedVALBench]] — uses MeQSum for the query2question task.
- [[KrippendorffAlpha]] — the inter-physician agreement metric.
- [[MedicalTextValidation]] — the task family.
