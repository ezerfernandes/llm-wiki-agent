---
title: "Risk Level Taxonomy"
type: concept
tags: [taxonomy, clinical-safety, evaluation, medical-nlp]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# Risk Level Taxonomy (MedVAL)

Physician-defined 4-class taxonomy of factual-inconsistency severity for LM-generated medical text, introduced in [[2507.03152-medval|MedVAL (Aali et al. 2026)]]. Designed to map model-output errors onto **deployment-relevant clinical actions** rather than abstract scores.

## The four levels

| Perturbation $\delta$ | Level | Risk | Safety | Action |
|---|---|---|---|---|
| **0%** | **Level 1** | No risk | Safe | Expert review **not required** |
| **33%** | **Level 2** | Low risk | Acceptable | Expert review **optional** |
| **67%** | **Level 3** | Moderate risk | Potentially unsafe | Expert review **required** |
| **100%** | **Level 4** | High risk | Unsafe | Expert **rewrite** required |

Each level pairs with a corresponding instructional prompt for synthetic data generation — e.g. $\delta = 1.0$ injects *"inconsistencies that could result in incorrect or unsafe clinical decisions."*

## Why this shape

The four-class taxonomy was chosen with the [[2507.03152-medval|MedVAL]] physician team for two reasons:

1. **It encodes a clinical decision boundary.** Levels 1–2 (safe deployment) vs Levels 3–4 (review/rewrite) is the *binary safety classification* used for deployment gating. Within "safe," Level 1 vs Level 2 distinguishes confident-pass from acceptable-but-monitor. Within "unsafe," Level 3 vs Level 4 distinguishes correctable from must-rewrite.
2. **It supports continuous degradation.** While the levels are discrete for implementation, the framework supports continuous $\delta \in [0, 1]$ and scalar validator outputs — the discrete strata are a presentation choice, not a theoretical limit.

## Error categories (orthogonal to risk levels)

A separate error taxonomy attaches **error-type tags** to outputs at any risk level:
- **Hallucinations**: fabricated claim, misleading justification, detail misidentification, false comparison, incorrect recommendation.
- **Omissions**: missing claim, missing comparison, missing context.
- **Certainty misalignments**: overstating intensity, understating intensity.
- **Other**.

Observed frequencies across the 840 [[MedVALBench]] outputs:
- Fabricated claim: **45.7%** (most common)
- Missing claim: 14.0%
- Incorrect recommendation: 12.6%

Error count rises **0.14 → 3.24 per output** across risk levels 1 → 4.

## Reuse beyond MedVAL

The taxonomy is **release-licensed alongside MedVAL** and is intended to be the canonical risk-grading rubric for downstream evaluators — the binary safe/unsafe collapsing rule (Levels 1–2 vs 3–4) makes integration into existing safety/eval frameworks straightforward.

## Connections

- [[2507.03152-medval]] — the originating paper.
- [[MedVAL]] — the validator that emits grades against this taxonomy.
- [[MedVALBench]] — the benchmark whose physicians annotate against this taxonomy.
- [[GeneratorValidatorConsistency]] — the metric that scores generator-validator agreement on these grades.
- [[Hallucination]] — the dominant error class.
- [[MedicalTextValidation]] — the task family this taxonomy serves.
