---
title: "MIMIC"
type: concept
tags: [dataset, clinical, ehr, mit, lcp]
sources: [2025-bionlp-archehr-qa-neural, 2507.03152-medval]
last_updated: 2026-05-22
---

# MIMIC

**Medical Information Mart for Intensive Care** — a family of de-identified clinical datasets from the Beth Israel Deaconess Medical Center ICU, maintained by the MIT Laboratory for Computational Physiology. The canonical research EHR corpus for biomedical NLP.

**Versions referenced in this wiki:**
- **MIMIC-III** — ~40,000 ICU stays, 2001–2012 admissions, structured (labs, vitals, prescriptions, ICD codes) + unstructured (clinical notes, radiology, discharge summaries).
- **[[MIMICIV|MIMIC-IV]]** — successor, larger and updated to a modern schema. Source for [[2507.03152-medval|MedVAL]]'s `impression2simplified` task.
- **[[MIMICIVBHC|MIMIC-IV-BHC]]** — curated brief-hospital-course sections of MIMIC-IV discharge summaries, originally released by [[AsadAali|Aali et al. (JAMIA 2025)]]. Source for [[2507.03152-medval|MedVAL]]'s `bhc2spanish` (English → Spanish translation) task.

Used as the source for:
- [[ArchEHRQA2025]] shared-task notes ([[2025-bionlp-archehr-qa-neural|Reddy et al. 2025]]).
- Two of the six [[MedVALBench]] tasks ([[2507.03152-medval|Aali et al. 2026]]).
- Many other biomedical NLP benchmarks.

Access requires a credentialed PhysioNet account + ethics certification; the data is gated, not open.

## Connections
- [[ArchEHRQA2025]] — derives its 120 question-note cases from MIMIC-III/IV notes.
- [[2507.03152-medval]] / [[MedVALBench]] — MIMIC-IV underpins two out-of-distribution tasks (impression2simplified, bhc2spanish).
- [[MIMICIV]] / [[MIMICIVBHC]] — specific dataset variants used by MedVAL.
- [[emrQA]] — large-scale earlier QA dataset built on a MIMIC-adjacent EHR corpus.
- [[EvidenceGroundedQA]] — the paradigm clinical QA on MIMIC instantiates.
- [[StanfordMIMI]] — lab name **unrelated** to this dataset family; the Stanford lab uses MIMIC data but is a different organization.
