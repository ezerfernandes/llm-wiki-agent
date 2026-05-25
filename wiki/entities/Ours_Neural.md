---
title: "Neural (ArchEHR-QA 2025 team)"
type: entity
tags: [team, bionlp, clinical-nlp, uchicago]
sources: [2025-bionlp-archehr-qa-neural]
last_invariant: 2026-05-22
last_updated: 2026-05-22
---

# Neural (ArchEHR-QA 2025 team)

Six-person team from [[universityofchicago|University of Chicago]] — [[SaiPrasannaTejaReddy|Sai Prasanna Teja Reddy]] (first author), Abrar Majeedi, Viswanatha Reddy Gajjala, Zhuoyan Xu, Siddhant Rai, Vaishnav Potlapalli. **Runner-up (2nd place)** at the [[ArchEHRQA2025|ArchEHR-QA 2025]] shared task with an overall score of **51.5** ([[2025-bionlp-archehr-qa-neural]]).

Method: two-stage [[DSPy]] pipeline (sentence-level evidence ID + answer synthesis), each stage's prompt optimized end-to-end with [[MIPROv2]] on 20 dev cases, [[GPT4_1|GPT-4.1]] backbone, [[SelfConsistency|self-consistency]] $R=5$ at Stage 1 inference. Code: `github.com/ViswanathaReddyGajjala/ArchEHR-QA-Neural`.

## Connections
- [[2025-bionlp-archehr-qa-neural]] — the submission paper.
- [[ArchEHRQA2025]] — shared task.
- [[universityofchicago]] — affiliation.
