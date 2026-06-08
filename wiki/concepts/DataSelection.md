---
title: "Data Selection"
type: concept
tags: [ml-systems, efficiency, data, mlsysbook]
sources: [mlsysbook-ch01-introduction, mlsysbook-ch04-data-engineering, mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Data Selection

The **third dimension of the [[EfficiencyFramework|efficiency framework]]** (the Data axis of the [[DAMTaxonomy|D·A·M taxonomy]]): extracting more learning signal from limited examples, thereby reducing the operation count $O$ in the [[IronLawOfMLSystems|iron law]]. Introduced in Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]) as the most recently matured efficiency frontier.

Techniques: [[TransferLearning|transfer learning]], [[ActiveLearning|active learning]], curriculum design, and data filtering/cleaning that raise the "learning value" of each sample. The book's Part III opens with data selection (before model compression and hardware acceleration), reflecting that quality data is prerequisite to effective model optimization.

**Full treatment in [[mlsysbook-ch09-data-selection|Ch 9]]** (opens the Optimize part): data selection is *defined* as maximizing the [[InformationComputeRatio|Information-Compute Ratio]], motivated by the [[DataWall|Data Wall]], and operationalized as a three-stage pipeline — [[StaticDataPruning|static pruning]] ([[CoresetSelection|coresets]], [[DataDeduplication|deduplication]], quality filtering), [[DynamicDataSelection|dynamic selection]] ([[CurriculumLearning|curriculum]], [[ActiveLearning|active]], [[SemiSupervisedLearning|semi-supervised]] learning), and [[SyntheticDataGeneration|synthetic generation]] ([[DataAugmentation|augmentation]], generative synthesis, [[KnowledgeDistillation|distillation]]) — crowned by [[SelfSupervisedLearning|self-supervised]] pretraining and [[CostAmortization|cost amortization]]. Ch 9 adds the systems gate (the [[SelectionInequality|Selection Inequality]]), [[DataEchoing|data echoing]], and a full [[DataSelectionCostModel|cost model]].

## Connections

- [[EfficiencyFramework]] — data selection is one of its three dimensions.
- [[TransferLearning]] / [[ActiveLearning]] — core techniques.
- [[DataEngineering]] — the pipeline/quality infrastructure that makes selected data usable.
- [[InformationEntropy]] / [[DataGravity]] — [[mlsysbook-ch04-data-engineering|Ch 4]]: data selection maximizes the Data Selection Gain (entropy/gravity ratio); the "more data isn't always better" fallacy (test loss follows a power law in dataset size).
- [[DAMTaxonomy]] — the Data axis.
- [[InformationComputeRatio]] / [[DataWall]] / [[SelectionInequality]] — [[mlsysbook-ch09-data-selection|Ch 9]]'s defining metric, motivation, and systems gate.
- [[mlsysbook-ch01-introduction]] / [[mlsysbook-ch04-data-engineering]] / [[mlsysbook-ch09-data-selection]] — sources.
