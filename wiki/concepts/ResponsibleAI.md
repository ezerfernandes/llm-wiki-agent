---
name: ResponsibleAI
title: "Responsible AI"
type: concept
tags: [ethics, fairness, governance, ai-safety]
sources: [dmls-ch01-overview, dmls-ch11-human-side]
last_updated: 2026-05-23
---

# Responsible AI

Umbrella practice of designing, developing, and deploying AI systems for empowerment, trust, fairness, privacy, and positive impact. Per [[ChipHuyen|Huyen]]'s [[dmls-ch11-human-side|DMLS Ch 11]] (co-authored with [[AbhishekGupta|Abhishek Gupta]] of [[MontrealAIEthicsInstitute|Montreal AI Ethics Institute]]) — distinct from a checkbox-compliance activity, it requires critical thinking about whether the product should be built in the first place.

## The six-step practitioner framework (DMLS Ch 11)
1. **Discover sources for model biases** — at every lifecycle stage ([[DataAnnotation|annotation]], [[DataCollection|collection]], [[FeatureEngineering|feature engineering]], [[ClassImbalance|class imbalance]], [[ModelSelection|model selection]]).
2. **Understand the limitations of the data-driven approach** — some questions data alone cannot answer.
3. **Understand fairness-vs-other-desiderata trade-offs** — including [[CompactnessFairnessTradeoff]] (pruning harms disparate impact more than quantization, per Hooker et al.) and [[PrivacyAccuracyTradeoff]] (differential-privacy accuracy loss is non-uniform across subgroups, per Bagdasaryan & Shmatikov).
4. **Establish processes for mitigating biases** — pre-deployment auditing, third-party audits, [[IBMAIF360|AI Fairness 360]] / Infogram / Aequitas.
5. **Create [[ModelCard|model cards]]** — Mitchell et al. (2018) standardized disclosure documents.
6. **Stay up-to-date** — [[ACMFAccT]], [[PartnershipOnAI]], [[AlanTuringInstitute]], [[AINowInstitute]].

## Canonical case studies (DMLS Ch 11)
- **[[OfqualGradingAlgorithm|Ofqual A-level scandal, UK 2020]]** — wrong objective (rank predictions to prior school distribution) + coarse evaluation (no per-subgroup slice) + opacity (no public appeal mechanism).
- **[[StravaHeatmap|Strava heatmap 2018]]** — anonymized aggregate fitness data exposed military base locations; "anonymization is not enough."

## Related concepts
- [[Fairness]] / [[AlgorithmicFairness]] — mathematical & process notions.
- [[AlgorithmicBias]] / [[DisparateImpact]] — failure modes.
- [[Interpretability]] — debugging tool but not a fairness substitute.
- [[DifferentialPrivacy]] — privacy mechanism with fairness side-effects.
- [[ModelCard]] — disclosure artifact.
- [[AIIncidentDatabase]] — public registry of failures.

## Connections
- [[ChipHuyen]] — author who centered this in DMLS.
- [[CathyONeil]] — *Weapons of Math Destruction* (2016); foundational reading.
- [[MargaretMitchell]], [[TimnitGebru]], [[EmilyDenton]] — Model Cards paper and FAccT/ethics tutorials.
- [[SaraHooker]] — compactness/fairness empirical work.
