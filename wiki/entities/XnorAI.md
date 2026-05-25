---
title: "Xnor.ai"
type: entity
tags: [company, model-compression, 1-bit, apple-acquisition]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Xnor.ai

A model-compression startup that **spun off from the [[XnorNet|Xnor-Net]] paper** (Rastegari et al. 2016) — one of the foundational 1-bit neural network papers. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]] footnote:

> "The authors of the Xnor-Net paper spun off Xnor.ai, a startup that focused on model compression. In early 2020, it was acquired by [[Apple]] for a reported $200M."

## Why Ch 7 mentions it

Xnor.ai is part of the **1-bit LLM lineage** Ch 7 traces:
- [[BinaryConnect]] (Courbariaux et al. 2015) — 1-bit weights via stochastic binarization.
- [[XnorNet]] (Rastegari et al. 2016) — 1-bit weights *and* activations using XNOR + popcount ops.
- [[BitNet]] (Wang et al. 2023) — applied to transformer LLMs.
- [[BitNetB158|BitNet b1.58]] (Ma et al. 2024) — the 1.58-bit ternary LLM.

The Apple acquisition is one data point that **extreme quantization had production value** well before the LLM era — Xnor was working on edge AI inference for cameras and phones years before BitNet.

## Connections

- [[XnorNet]] — the originating paper.
- [[BitNet]] / [[BitNetB158]] — descendants in the 1-bit LLM family.
- [[Apple]] — the acquirer.
- [[Quantization]] — the broader field.
- [[ai-engineering-ch07-finetuning]] — wiki source.
