---
title: "Databricks"
type: entity
tags: [company, platform, analytics]
sources: [madewithml-mlops-experiment-tracking, 2507.19457-gepa, ai-engineering-ch09-inference-optimization, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Databricks

Unified analytics platform built around [[ApacheSpark]] and [[MLflow]]; co-founded by [[MateiZaharia]] and [[IonStoica]]. Mentioned as a managed experiment-tracking option in [[madewithml-mlops-experiment-tracking]].

## Tracked contributions to LLM-systems research

- **[[2507.19457-gepa]]** (ICLR 2026 Oral) — Databricks principal scientists [[OmarKhattab]] (also DSPy creator) and [[MateiZaharia]] are senior co-authors of GEPA, the reflective prompt optimizer. Continues the DSPy / MIPROv2 / GEPA arc of [[CompoundAISystem|compound-AI-system]] optimization research with strong Databricks-author presence.
- **[[DSPy]]** — Khattab's framework; ships as `databricks-dspy` in some forks and is a first-class citizen on the Databricks platform.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 cites Databricks for **the Llama 2-70B FP16 MBU benchmark chart** (Figure 9-5):

> *"Bandwidth utilization for Llama 2-70B in FP16 across three different chips shows a decrease in MBU as the number of concurrent users increases. Image from 'LLM Training and Inference with Intel Gaudi 2 AI Accelerators' (Databricks, 2024)."*

The key observation Ch 9 draws from this:

> *"The decline is likely due to the higher computational load per second with more users, shifting the workload from being bandwidth-bound to compute-bound."*

This is one of the chapter's most-concrete demonstrations that **the [[ComputeBound|compute-bound]] vs [[MemoryBandwidthBound|memory-bandwidth-bound]] regime is workload-dependent** — the same model on the same hardware can shift regimes based on concurrent-user count.
