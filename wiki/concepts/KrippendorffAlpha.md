---
title: "Krippendorff's Alpha"
type: concept
tags: [statistics, inter-rater-agreement, evaluation, stub]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# Krippendorff's $\alpha$

**Inter-rater agreement statistic** for categorical / ordinal data with arbitrary numbers of raters and arbitrary missing-data patterns. Ranges from 0 (chance agreement) to 1 (perfect agreement); $\alpha \ge 0.80$ is conventionally treated as "reliable rating quality for drawing triangulated conclusions."

## Use in MedVAL

[[2507.03152-medval]] reports Krippendorff's $\alpha$ on the 90/840 multi-physician-annotated subset:

**Overall $\alpha = 0.848$** (substantial-to-near-perfect agreement).

**Per-task** (from Table 3 / Table S3):

| Task | $\alpha$ |
|---|---|
| `bhc2spanish` | 0.943 |
| `medication2answer` | 0.904 |
| `impression2simplified` | 0.872 |
| `report2impression` | 0.861 |
| `dialogue2note` | 0.830 |
| `query2question` | 0.560 |

**For safe/unsafe binary collapsing**: $\alpha = 0.754$. MedVAL ensembles reach F1 = 0.864 / accuracy = 0.848 on this collapsed metric — **at the upper end of human consistency**.

**Pearson $r = 0.67$ between per-task $\alpha$ and GPT-4o MedVAL F1** — MedVAL is most consistent on tasks where physicians themselves are most consistent.

## Connections
- [[2507.03152-medval]] — the application paper.
- [[MedVALBench]] — the dataset whose agreement is measured.
- [[CohensKappa]] — sibling agreement statistic for two raters.
- [[NonInferiorityTest]] / [[McNemarTest]] — sibling statistical tools.
