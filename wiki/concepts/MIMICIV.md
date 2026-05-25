---
title: "MIMIC-IV"
type: concept
tags: [dataset, clinical, ehr, mit, lcp, stub]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# MIMIC-IV

**Medical Information Mart for Intensive Care, version IV** — the successor to [[MIMIC|MIMIC-III]]. De-identified clinical data from Beth Israel Deaconess Medical Center ICU stays, with a modernized schema. Ref [51] in [[2507.03152-medval]]. Partially open-source.

Used in [[MedVALBench]] as the source for the **`impression2simplified`** task: radiology impression → patient-friendly version. Out-of-distribution test only (no train split — train comes from [[Openi]] `report2simplified` for related findings simplification). 190 test samples, avg 69±61 tokens. **5 physicians** annotated.

Sampling ensured **equal distribution of imaging modalities** matching the top indications at Stanford Hospital: chest X-rays, CT abdomen/pelvis, CT head, MR brain, pelvic ultrasound, digital screening mammography, transabdominal/transvaginal pelvic ultrasounds.

## Connections
- [[MIMIC]] — the parent family page.
- [[MIMICIVBHC]] — sibling MIMIC-IV-BHC variant for brief hospital course sections.
- [[2507.03152-medval]] — the application paper.
- [[MedVALBench]] — uses MIMIC-IV for the impression2simplified task.
- [[2025-bionlp-archehr-qa-neural]] — another wiki paper using MIMIC-IV-derived data.
