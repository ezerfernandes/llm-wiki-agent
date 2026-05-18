---
title: "Steffen Rendle"
type: entity
tags: [researcher, recommender-systems, factorization-machines, bpr]
sources: [d2l-recommender-systems]
last_updated: 2026-05-16
---

# Steffen Rendle

Recommender-systems researcher most associated with **two of the most cited papers in the field**:

- **Rendle 2010** — *Factorization Machines* (ICDM): introduces [[FactorizationMachines|FM]] as a general-purpose model unifying linear regression, matrix factorization, and polynomial-kernel SVMs; the $\mathcal{O}(kd)$ reformulation of pairwise feature interactions made FM the dominant CTR-prediction model of the 2010s and the structural ancestor of [[DeepFM]] / [[NFM]] / [[xDeepFM]].
- **Rendle, Freudenthaler, Gantner & Schmidt-Thieme 2009** — *BPR: Bayesian Personalized Ranking from Implicit Feedback* (UAI): the canonical pairwise-loss formulation for [[ImplicitFeedback|implicit-feedback]] [[PersonalizedRanking|personalized ranking]]; trained the entire field on triples-with-negative-sampling.

Both are foundational to [[d2l-recommender-systems]] (§ranking and §fm). Career: Universität Hildesheim PhD → Google Research.

## Connections
- [[FactorizationMachines]] — his 2010 ICDM paper.
- [[BPR]] — his 2009 UAI paper.
- [[DeepFM]] — direct descendant of FM.
- [[CTRPrediction]] — primary application domain for FM.
- [[YehudaKoren]], [[XiangnanHe]] — co-canonical recommender-systems researchers.
- [[d2l-recommender-systems]] — first source citing Rendle.
