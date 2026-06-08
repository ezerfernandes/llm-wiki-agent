---
name: ModelCard
title: "Model Card"
type: concept
tags: [responsible-ai, governance, documentation]
sources: [dmls-ch11-human-side, mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Model Card

Standardized disclosure document accompanying a trained ML model — proposed by [[MargaretMitchell|Mitchell]] et al. (2018, *Model Cards for Model Reporting*). Covers intended use, performance across demographic groups, training data provenance, ethical considerations, and caveats. Cited by [[ChipHuyen|Huyen]]'s [[dmls-ch11-human-side|DMLS Ch 11]] as one of the six steps of a [[ResponsibleAI|Responsible AI]] practitioner framework.

## Typical sections
- **Model details** — developer, version, type, training algorithm, parameters.
- **Intended use** — primary use cases, primary users, out-of-scope use cases.
- **Factors** — relevant demographic / phenotypic / environmental groups.
- **Metrics** — task-appropriate metrics + decision thresholds + variation approaches.
- **Evaluation data** — datasets, motivation, preprocessing.
- **Training data** — provenance, distribution properties.
- **Quantitative analyses** — unitary results + intersectional results across factors ([[DataSlicing|slice-based evaluation]]).
- **Ethical considerations** — risk-of-harm analysis.
- **Caveats and recommendations** — known limitations.

## Adoption
- [[HuggingFace]] requires model cards on the Model Hub (2020+).
- [[TensorFlow]] / [[scikitlearn]] ship model-card-generation utilities.
- [[google|Google]] published model cards for several public models (e.g., Face Detection model card).

## Connections
- [[ResponsibleAI]] — the broader framework.
- [[MargaretMitchell]] — first author.
- [[TimnitGebru]] — co-author.
- [[DataSlicing]] — slice-based evaluation is the quantitative-analyses backbone.
- [[FineGrainedEvaluation]] — sibling concept (subgroup-level metrics).
- [[Fairness]] / [[AlgorithmicFairness]] — the property model cards make legible.
- [[mlsysbook-ch15-responsible-engineering]] — mlsysbook Vol 1 Ch 15 treats model cards (with [[Datasheets|datasheets]]) as the documentation "nutrition labels" of its responsible-engineering checklist, while warning that documentation ≠ enforcement (40–60% of models drift outside documented scope within 18 months).
