---
title: "MedVAL-Bench"
type: concept
tags: [benchmark, dataset, medical-nlp, clinical-safety, evaluation]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# MedVAL-Bench

**6-task, 840-output physician-annotated benchmark** for evaluating LM validators on medical text, released alongside [[2507.03152-medval|MedVAL (Aali et al. 2026)]]. Built by a panel of **12 physicians** — 7 internal-medicine MDs + 5 radiologists + 3 bilingual IM residents — across general medical, radiology, and bilingual translation tasks.

## Task suite

| Task | Source dataset | In-dist? | Train | Test | Avg tokens (test) | # physicians |
|---|---|---|---|---|---|---|
| `medication2answer` | [[MedicationQA]] | ✓ | 500 | 135 | 10±4 | 2 |
| `query2question` | [[MeQSum]] | ✓ | 500 | 120 | 82±66 | 3 |
| `report2impression` | [[Openi]] | ✓ | 500 | 190 | 50±22 | 5 |
| `report2simplified` | Open-i | ✓ | 500 | — | — | (train only) |
| `impression2simplified` | [[MIMICIV]] | ✗ | — | 190 | 69±61 | 5 |
| `bhc2spanish` | [[MIMICIVBHC]] | ✗ | — | 120 | 543±391 | 3 |
| `dialogue2note` | [[ACIBench]] | ✗ | — | 85 | 1497±445 | 2 |

Three task families: **summarization** (report2impression, dialogue2note, bhc2spanish), **simplification** (report2simplified, impression2simplified), **question answering** (medication2answer, query2question).

## Annotation protocol

- For each test-time input, generator produces an output by sampling perturbation $\delta \in \{0, 0.33, 0.67, 1.0\}$ uniformly → balanced risk-level spectrum.
- Physicians grade based **solely on observed output** (perturbation-blind, model-blind), with two tasks:
  1. **Risk grading** — assign Level 1–4 per the [[RiskLevelTaxonomy|risk taxonomy]].
  2. **Error assessment** — identify factual-consistency errors per the hallucinations / omissions / certainty-misalignments taxonomy.
- **15 random examples per task** annotated by *multiple* physicians, enabling Krippendorff's $\alpha$ inter-rater estimation (90 examples × 6 tasks = stratified multi-annotated subset).

## Inter-physician agreement ([[KrippendorffAlpha|Krippendorff's $\alpha$]])

| Task | $\alpha$ |
|---|---|
| `bhc2spanish` | **0.943** (highest) |
| `medication2answer` | 0.904 |
| `impression2simplified` | 0.872 |
| `report2impression` | 0.861 |
| `dialogue2note` | 0.830 |
| `query2question` | **0.560** (lowest) |
| **Overall** | **0.848** |

> $\alpha \ge 0.80$ indicates reliable rating quality. The overall 0.848 is in the substantial-to-near-perfect range. Notably, **MedVAL GPT-4o F1 correlates with $\alpha$ at Pearson $r = 0.67$** — *MedVAL is most consistent on tasks where physicians themselves are most consistent*.

## Error distribution

Most frequent errors observed by physicians across the 840 outputs:
- Fabricated claim: **45.7%**
- Missing claim: **14.0%**
- Incorrect recommendation: **12.6%**
- (rest: misleading justification, detail misidentification, false comparison, missing comparison, missing context, overstating/understating intensity, other)

Error frequency rises with risk grade: **0.14 → 3.24 errors** per output across Levels 1 → 4.

## Releases

- HuggingFace: [stanfordmimi/MedVAL-Bench](https://huggingface.co/datasets/stanfordmimi/MedVAL-Bench)
- PhysioNet (gated): canonical clinical-data release.
- Maintained by [[StanfordMIMI]].

## Connections

- [[2507.03152-medval]] — the paper.
- [[MedVAL]] — the validation method this benchmark scores.
- [[MedVAL4B]] — the open-source model trained against this benchmark.
- [[RiskLevelTaxonomy]] / [[KrippendorffAlpha]] — the rating scheme + the agreement statistic.
- [[MedicationQA]] / [[MeQSum]] / [[Openi]] / [[MIMICIV]] / [[MIMICIVBHC]] / [[ACIBench]] — the source datasets the tasks draw from.
- [[MIMIC]] — parent EHR corpus underlying impression2simplified + bhc2spanish.
- [[Hallucination]] — the dominant error category being measured.
- [[MEDEC]] — sibling external benchmark MedVAL is also evaluated against.
