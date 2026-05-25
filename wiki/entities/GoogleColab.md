---
title: "Google Colab"
type: entity
tags: [tool, notebook, gcp]
sources: [madewithml-foundations-notebooks, d2l-appendix-tools, hands-on-llm-ch01-introduction-to-llms, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# Google Colab

Google's hosted Jupyter-style notebook environment with free GPU/TPU access. Entry point for [[madewithml-foundations-notebooks]] and many subsequent foundations lessons in [[MadeWithML]].

In the [[d2l-appendix-tools|D2L appendix]] context (§`colab`), Colab is the **free-tier alternative** to [[AmazonSageMaker]] / [[AmazonEC2]] for readers without an AWS account: every D2L section has a "Colab" button that opens it pre-loaded; if a GPU is needed, Colab automatically requests a GPU instance.

## In *Hands-On LLMs* Ch 1

Google Colab is **the canonical runtime target for *[[HandsOnLLM|Hands-On LLMs]]***. Ch 1:

> "We will make all the code available in Google Colab instances. At the time of writing, a free instance of Google Colab will net you a T4 GPU with 16 GB VRAM, which is the minimum amount of VRAM that we suggest." — Ch 1

The book's *"GPU-poor"* commitment depends on Colab's free T4 tier — the book's primary worked model ([[Phi3Mini|Phi-3-mini]]) is deliberately sized to fit in 16 GB (and <6 GB with quantization).

## In *Hands-On LLMs* Ch 12

Ch 12 — the **book's final chapter** — pushes the *"GPU-poor"* commitment to its operational limit: a **full two-stage fine-tuning pipeline** (QLoRA-SFT + QLoRA-DPO on [[TinyLlama|TinyLlama-1.1B]]) running on the free Colab Tesla T4 in roughly **one hour per stage**:

> *"If you are using the free GPU provided by Google Colab, which is the Tesla T4 at the time of writing, then training might take up to an hour. A good time to take a break!"* — Ch 12

The chapter's wall-clock budget is the book's deliberate pedagogical statement: **modern LLM fine-tuning (SFT + DPO) is accessible to anyone with a free Colab account** — no datacenter, no rented H100s, no paid tier needed. This is the operational corollary of the book's intuition-first, runnable-code thesis, and the **final demonstration** of the GPU-poor commitment across the 12-chapter ingest.
