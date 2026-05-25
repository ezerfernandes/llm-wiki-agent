---
title: "Cohen's Kappa"
type: concept
tags: [statistics, inter-rater-agreement, evaluation, stub]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# Cohen's $\kappa$

**Categorical agreement statistic** between two raters, correcting for chance agreement. Ranges from −1 (complete disagreement) to 1 (perfect agreement); 0 = agreement no greater than chance.

## Use in MedVAL

[[2507.03152-medval]] §2.3.3 reports **linearly-weighted Cohen's $\kappa$** for the ordinal 4-class risk-grading agreement between LM-predicted and physician-assigned labels. Linear weighting penalizes adjacent-class disagreements less than far-class disagreements — appropriate for the [[RiskLevelTaxonomy|ordinal risk levels]] where Level 2 vs Level 3 is a less serious mismatch than Level 1 vs Level 4.

Cohen's $\kappa$ complements the F1 score and the [[KrippendorffAlpha|Krippendorff's $\alpha$]] (for *inter-physician* agreement); it is reported in Figure S1.

## Connections
- [[2507.03152-medval]] — the application paper.
- [[KrippendorffAlpha]] — sibling statistic for multi-rater agreement.
- [[NonInferiorityTest]] / [[McNemarTest]] — sibling statistical tools.
- [[RiskLevelTaxonomy]] — the ordinal scheme that motivates linear weighting.
