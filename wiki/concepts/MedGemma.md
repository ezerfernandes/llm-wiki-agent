---
title: "MedGemma"
type: concept
tags: [model, llm, google, medical-nlp, gemma]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# MedGemma

Medically-adapted variant of [[gemini|Google]]'s [[google|Gemma]] open-weight LLM family. Referenced in [[2507.03152-medval|MedVAL (Aali et al. 2026)]] as **MedGemma-27B** — one of the strongest zero-shot medical-baseline LMs in the [[MedVALBench]] panel.

## Performance in MedVAL-Bench

- Zero-shot 4-class F1 = **0.482** overall — the **best baseline open-source model** before MedVAL distillation.
- Per-task baseline F1 (selected): medication2answer 0.462, report2impression 0.616 (highest of open baselines), bhc2spanish 0.349, dialogue2note **0.603** (the highest open dialogue2note baseline).
- **Not** fine-tuned in the MedVAL experiments — included as a "pre-medically-adapted" comparator to test whether MedVAL's task-agnostic distillation can beat domain pre-adaptation.

## Why it matters here

The headline finding of [[2507.03152-medval]] is that **[[MedVAL4B|MedVAL-Qwen3-4B]] (F1 = 0.527) beats MedGemma-27B (0.482)** despite being **7× smaller and not domain-pretrained**. This is the cleanest demonstration in the paper that **task-aware self-distillation outperforms domain pre-adaptation** for the medical validation task — at least at this benchmark and model scale.

## Connections

- [[2507.03152-medval]] — the paper that benchmarks it.
- [[MedVAL4B]] — the smaller Qwen-based distilled model that beats it.
- [[google|Gemma]] — the base model family.
- [[gemini|Gemini]] — Google's frontier model lineage.
- [[MedVALBench]] — the benchmark on which it serves as a strong baseline.
- [[FineTuning]] — the prior-adaptation regime MedGemma instantiates and that MedVAL's task-aware distillation outperforms in this domain.
