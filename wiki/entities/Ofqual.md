---
name: Ofqual
title: "Ofqual"
type: entity
tags: [government, education, ai-failure-case-study]
sources: [dmls-ch11-human-side]
last_updated: 2026-05-23
---

# Ofqual

Office of Qualifications and Examinations Regulation — UK government regulator for school qualifications. Deployed the auto-grading algorithm at the center of the **[[OfqualGradingAlgorithm|2020 A-level grading scandal]]**, the canonical [[ResponsibleAI|Responsible AI]] case study in [[ChipHuyen|Huyen]]'s [[dmls-ch11-human-side|DMLS Ch 11]].

## The 2020 case
Due to COVID-19 cancelling in-person exams, Ofqual deployed an algorithm to predict A-level grades from teacher-assessed grades + prior school performance. The algorithm:
- **Used the wrong objective** — it ranked grades to match each school's *historical* grade distribution, locking in historical inequality rather than measuring individual students.
- **Failed on coarse evaluation** — no per-subgroup slice metrics caught that students from disadvantaged backgrounds were systematically downgraded.
- **Had no transparent appeal mechanism** — students couldn't contest the algorithmic decision.
- Result: ~40% of grades downgraded from teacher assessments; political crisis; algorithm withdrawn; manual re-grading.

## Analyses cited in DMLS
- [[AdaLovelaceInstitute|Ada Lovelace Institute]] — UK think tank that published a forensic post-mortem.
- [[RoyalStatisticalSociety|Royal Statistical Society]] — challenged Ofqual's methodology pre-deployment.

## Connections
- [[OfqualGradingAlgorithm]] — the algorithm specifically.
- [[ResponsibleAI]] — the framework Ch 11 frames Ofqual under.
- [[FineGrainedEvaluation]] / [[DataSlicing]] — the evaluation discipline Ofqual lacked.
- [[ModelCard]] — disclosure document type the algorithm should have had.
- [[AlgorithmicBias]] / [[DisparateImpact]] — the failure modes.
