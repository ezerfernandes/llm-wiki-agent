---
title: "Cohen's Kappa"
type: concept
tags: [statistics, inter-rater-agreement, evaluation, stub]
sources: [2507.03152-medval, mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Cohen's $\kappa$

**Categorical agreement statistic** between two raters, correcting for chance agreement. Ranges from −1 (complete disagreement) to 1 (perfect agreement); 0 = agreement no greater than chance.

## Use in MedVAL

[[2507.03152-medval]] §2.3.3 reports **linearly-weighted Cohen's $\kappa$** for the ordinal 4-class risk-grading agreement between LM-predicted and physician-assigned labels. Linear weighting penalizes adjacent-class disagreements less than far-class disagreements — appropriate for the [[RiskLevelTaxonomy|ordinal risk levels]] where Level 2 vs Level 3 is a less serious mismatch than Level 1 vs Level 4.

Cohen's $\kappa$ complements the F1 score and the [[KrippendorffAlpha|Krippendorff's $\alpha$]] (for *inter-physician* agreement); it is reported in Figure S1.

## In ML label-quality monitoring

Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]) uses Cohen's $\kappa$ (and its multi-rater generalization, Fleiss' $\kappa$) as the **detector for label-quality drift**: monitoring inter-annotator agreement over rolling windows surfaces degradation invisible to feature monitoring. $\kappa < 0.4$ signals unreliable training data; a medical-imaging project declined from $\kappa = 0.85$ to $0.72$ over six months as untrained annotators joined. The chance-correction matters: two annotators labeling 90% of items "not spam" agree 82% of the time by pure chance, making raw agreement dangerously misleading. Consensus labeling routes low-$\kappa$ (<0.4) cases to expert review rather than forcing majority votes.

## Connections
- [[2507.03152-medval]] — the application paper.
- [[KrippendorffAlpha]] — sibling statistic for multi-rater agreement.
- [[NonInferiorityTest]] / [[McNemarTest]] — sibling statistical tools.
- [[RiskLevelTaxonomy]] — the ordinal scheme that motivates linear weighting.
- [[DataLabeling]] / [[DataDrift]] — label-quality-drift detection in ML pipelines.
- [[mlsysbook-ch04-data-engineering]] — source.
