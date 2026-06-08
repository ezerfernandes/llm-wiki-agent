---
title: "Data Lineage"
type: concept
tags: [data, governance, mlops]
sources: [ai-engineering-ch08-dataset-engineering, mlsysbook-ch03-ml-workflow, mlsysbook-ch04-data-engineering, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Data Lineage

Tracking where every dataset, feature, and model artifact came from — which upstream sources, transformations, and code produced it. Enables debugging, reproducibility, and impact analysis across a [[DataPipeline]]; complements [[DVC]], [[ExperimentTracking]], and [[DataObservability]].

## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

[[ChipHuyen|Huyen]] in Ch 8 names **obscure data lineage as one of the four major limits of AI-generated data**:

> "AI generation obscures data lineage. AI models are influenced by their training data and can sometimes regurgitate it without the user knowing. This creates risks."

### The two risk scenarios

1. **Copyright propagation.** If model X was trained on copyrighted data, and you use X to generate training data for your model Y, **Y may also violate copyrights** — but you can't detect this from X's outputs alone.
2. **Benchmark contamination propagation.** If X was trained on benchmark B, and you use X to generate data, and you evaluate your model on B → **your result is contaminated**, but you have no audit trail to detect it.

> "Without clear data lineage, it's hard to assess a model's commercial viability or trust its performance."

### Implications

- Always track which models produced which synthetic data.
- Disclose AI involvement when publishing models.
- Treat AI-generated training data as **inheriting all the risks of its generator's training data**.
- For [[ModelCollapse|model collapse]] mitigation, lineage tracking is also required to detect recursive contamination.

This is one of the chapter's most actionable governance recommendations.

## In the ML workflow (mlsysbook)

Reddi's *Machine Learning Systems* ([[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]) treats data lineage as the automated metadata linking each clinic's production logs to the exact data/code/model version that generated them. Without it, correlating a site-specific accuracy drop with a training experiment becomes a multi-week forensic analysis across hundreds of GB of logs instead of a minutes-long metadata query — and it is a hard requirement for [[FDA]] regulatory audit trails. See [[MLTechnicalDebt]] for why this provenance gap compounds.

The dedicated data-engineering chapter ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]) makes lineage the governance pillar of data processing: transformation versioning (code commit hash, library versions, Docker image), parameter tracking (normalization means/std-devs, categorical vocabularies, FFT/MFCC parameters persisted with the model), and processing lineage (Apache Atlas / Amundsen). It is what converts a week-long forensic debugging session into a graph traversal, and underpins GDPR's right to explanation and FCRA adverse-action notices.
