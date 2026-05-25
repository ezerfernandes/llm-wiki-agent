---
title: "MLOps"
type: concept
tags: [mlops, operations, lifecycle]
sources: [madewithml-overview, madewithml-mlops, ai-engineering-ch01-intro]
last_updated: 2024-12-04
---

# MLOps

The discipline of operationalizing machine learning: combining DevOps practices with ML-specific concerns like [[ModelRegistry]], [[ModelServing]], [[ModelMonitoring]], [[Reproducibility]], and [[Versioning]]. Spans the full lifecycle from [[ProductDesign]] to retirement.

## From [[ai-engineering-ch01-intro|AI Engineering Ch 1]]

[[ChipHuyen|Chip Huyen]] explicitly contrasts **MLOps** (and the related terms AIOps, LLMOps) with the discipline she names **[[AIEngineering|AI engineering]]**:

> *"I didn't go with all the terms that end with 'Ops' because, while there are operational components of the process, the focus is more on tweaking (engineering) foundation models to do what you want."* — Ch 1

Her position: foundation-model application work is more *engineering* than *operations* — the high-leverage activity is [[ModelAdaptation|adapting models]] via [[PromptEngineering|prompt engineering]], [[rag|RAG]], and [[FineTuning|finetuning]] (engineering), not setting up CI/CD or monitoring (operations). MLOps still covers the bottom **infrastructure layer** of the [[AIEngineeringStack|AI engineering stack]] (serving, compute, monitoring), but it doesn't name the discipline that owns the application and model-development layers.

See [[AIEngineering]] and [[AIEngineeringVsMLEngineering]] for the full taxonomy.
