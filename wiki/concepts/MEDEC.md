---
title: "MEDEC"
type: concept
tags: [benchmark, medical-nlp, error-detection, evaluation]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# MEDEC

**Medical error detection / correction benchmark** — external validation suite used by [[2507.03152-medval|MedVAL]] §3.6 as an out-of-distribution test for distilled validators. Listed on the [[MedHELM]] leaderboard, enabling apples-to-apples comparison with prior published baselines. Ref [72] in the MedVAL paper.

## MedVAL on MEDEC

Distinct task and label structure from [[MedVALBench]], so this is a true distribution-shift evaluation. Despite the gap, MedVAL distillation improves zero-shot accuracy:

| Model | Baseline | MedVAL | Δ |
|---|---|---|---|
| GPT-4o Mini | 53.3% | 54.4% | +1.1% |
| GPT-4o | 58.0% | 63.3% | **+5.3%** |

Both proprietary models were chosen because their **baseline performance is already reported on the [[MedHELM]] leaderboard** — letting MedVAL inherit a fair comparison frame without re-running zero-shot baselines.

## Significance

The MEDEC result shows that **MedVAL distillation generalizes beyond the perturbation distribution of its training set** — gains persist on a different benchmark with different label conventions and different task shapes. Together with the +84% F1 improvement on the [[MedVALBench]] held-out tasks, this is the paper's evidence that **MedVAL's improvements stem from learned validation competence, not just from learning the perturbation distribution**.

## Connections

- [[2507.03152-medval]] — the paper that uses MEDEC for OOD validation.
- [[MedVAL]] — the method being externally validated.
- [[MedHELM]] — the leaderboard MEDEC is reported under.
- [[MedicalTextValidation]] — sibling task family.
