---
title: "ExLlamaV2"
type: entity
tags: [tool]
sources: [leh-ch08-inference-optimization]
last_updated: 2026-05-22
---

## What it is
Open-source GPU inference library for Llama-family models; backend for the EXL2 quantization format.

## In LLM Engineer's Handbook
ExLlamaV2 (by [[Turboderp]], `turboderp/exllamav2`, 2023) is the open-source GPU inference library that backs the [[EXL2]] mixed-precision quantization format and also supports [[GPTQ]]. Per [[leh-ch08-inference-optimization]] it offers the highest GPU throughput among the three formats (GGUF, GPTQ, EXL2) compared.
