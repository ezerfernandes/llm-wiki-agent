---
title: "Non-Inferiority Test"
type: concept
tags: [statistics, clinical-trial, evaluation]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# Non-Inferiority Test

**Statistical test that aims to show a new method is not meaningfully worse than a comparator**, given a pre-specified clinically negligible margin $\Delta_\mathrm{NI}$. Standard tool in clinical-trial methodology, adopted here to compare an LM evaluator against a single human expert.

## Form used in MedVAL

[[2507.03152-medval]] §2.3.3 applies a **paired item-level bootstrap** non-inferiority test on 90/840 multi-physician-annotated test cases to compare GPT-4o MedVAL against a randomly-sampled single expert:

1. **Reference label**: majority consensus across multiple physician annotations.
2. **Contrast**: $\Delta = \mathrm{F1}(\mathrm{model}) - \mathrm{F1}(\mathrm{single\ expert})$.
3. **Bootstrap**: B = 10,000 paired resamples to estimate the 95% lower confidence bound of $\Delta$.
4. **Decision rule**: **non-inferiority declared if $\mathrm{LCB}_{95\%}(\Delta) > -0.05$** — a 5-point F1 drop is the clinically negligible margin chosen by the paper's physician panel.

No multiplicity adjustment applied (the comparison is a single pre-specified contrast: GPT-4o MedVAL vs single expert).

## Result

**Non-inferiority declared at $p < 0.001$.** Together with the strong inter-physician agreement on the multi-annotated subset (Krippendorff's $\alpha = 0.848$ overall), this is the paper's evidence that **MedVAL has crossed the single-human-expert reliability bar** on the binary safe/unsafe classification.

## When non-inferiority is the right frame

Standard "is A better than B" superiority tests can't show that a smaller / cheaper / scalable evaluator is *good enough* — only that it's *as good or better*. Non-inferiority lets the paper claim **deployment-readiness with a single expert in the loop**: if MedVAL is non-inferior to one expert, replacing one expert per output with MedVAL (and keeping other experts) is statistically defensible.

## Connections

- [[2507.03152-medval]] — the application paper.
- [[MedVAL]] — the method evaluated.
- [[MedVALBench]] — the benchmark on which non-inferiority is tested.
- [[McNemarTest]] / [[KrippendorffAlpha]] / [[CohensKappa]] — sibling statistical tools used in the paper.
- [[F1Score]] — the metric on which $\Delta$ is computed.
