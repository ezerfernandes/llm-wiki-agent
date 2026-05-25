---
title: "Graphcore"
type: entity
tags: [company, hardware, ai-accelerator]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Graphcore

**UK-based AI hardware company; designer of the Intelligent Processing Unit (IPU).** Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"The success of NVIDIA GPUs has inspired many accelerators designed to speed up AI workloads, including ... Graphcore's Intelligent Processing Unit (IPU) ..."*

## The IPU

Graphcore's IPU architecture was designed around **graph-style parallelism** — different from GPU's SIMD style. The chip targets workloads where many small operations run in parallel across thousands of independent threads, rather than large matrix multiplications.

The IPU has been used by some research groups for transformer-style workloads, though it never gained the AI-mind-share of NVIDIA or even AMD.

## Position in the ecosystem

Graphcore is one of several **second-tier AI hardware vendors** alongside [[Cerebras]], [[Groq]], and Intel Habana — all of whom carved out niches but didn't displace NVIDIA. In 2024 the company has faced commercial headwinds (layoffs reported widely).

## Where Graphcore appears in Ch 9

A single mention in the accelerator zoo. No detailed performance numbers in this chapter.

## Connections

- [[AIAccelerator]] — umbrella category.
- [[NVIDIA]] / [[AMD]] / [[Cerebras]] / [[Groq]] — competing vendors.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
