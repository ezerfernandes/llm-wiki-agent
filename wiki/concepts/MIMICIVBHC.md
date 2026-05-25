---
title: "MIMIC-IV-BHC"
type: concept
tags: [dataset, clinical, ehr, brief-hospital-course, multilingual, stub]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# MIMIC-IV-BHC

**MIMIC-IV Brief Hospital Course** — curated BHC sections from discharge summaries, written by healthcare providers at Beth Israel Deaconess Medical Center. Ref [52] in [[2507.03152-medval]]; the dataset itself is the publication output of an earlier benchmark by [[AsadAali|Aali]] et al. — *"A dataset and benchmark for hospital course summarization with adapted large language models"*, JAMIA 32(3):470–479, 2025 (ref [5]).

Used in [[MedVALBench]] as the source for the **`bhc2spanish`** task: brief hospital course (English) → Spanish translation. Out-of-distribution test only. 120 test samples, **avg 543±391 tokens — the second-longest task** after `dialogue2note`. **3 bilingual internal-medicine residents** annotated.

The Spanish translation task reflects the multilingual nature of U.S. clinical practice (Spanish is the second most spoken language). **Highest inter-physician Krippendorff's $\alpha = 0.943$** of any MedVALBench task — translation correctness is the most physician-consistent assessment in the suite.

## Connections
- [[MIMIC]] / [[MIMICIV]] — parent datasets.
- [[2507.03152-medval]] — the application paper.
- [[AsadAali]] — author of both this dataset's source paper and MedVAL.
- [[MedVALBench]] — uses MIMIC-IV-BHC for bhc2spanish.
- [[KrippendorffAlpha]] — agreement metric where bhc2spanish is the top scorer.
