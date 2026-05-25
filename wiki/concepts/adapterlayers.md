---
title: "Adapter Layers"
type: concept
tags: [concept, fine-tuning, parameter-efficient]
sources: [1910.10683-t5, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# Adapter Layers

A parameter-efficient fine-tuning technique (Houlsby et al., 2019; Bapna et al., 2019) in which small dense-ReLU-dense bottleneck blocks are inserted after each pre-existing feed-forward sub-layer of a [[transformer]], and only those adapter parameters plus layer-norm parameters are updated during fine-tuning. The pre-trained backbone is frozen.

The bottleneck dimension `d` is the main hyperparameter — it trades parameter efficiency for capacity.

## T5's finding ([[1910.10683-t5]] Table 10)

- Low-resource tasks (SQuAD): small `d` (32) is competitive with full fine-tuning.
- High-resource tasks (concatenated GLUE/SuperGLUE): large `d` (2048) needed to approach full fine-tuning, but never quite matches it.
- Full fine-tuning beat adapters on every task in T5's setup, *but* adapters are attractive when many tasks must share one frozen backbone (no separate copy per task).

## See also

- [[1910.10683-t5]] — source paper studying this method.
- [[transformer]] — where adapters are inserted.
- [[gradualunfreezing]] — alternative parameter-efficient method T5 also evaluates.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* introduces adapters as the **first of two named [[PEFT]] families** (the other being [[lora|LoRA]]). The chapter's pedagogical anchor numbers:

- **Houlsby et al. (ICML 2019)**, *"Parameter-efficient transfer learning for NLP"* — fine-tuning **3.6% of BERT's parameters** reaches within **0.4% of full fine-tuning** on [[GLUE]].
- **Placement**: adapter modules are added *"after the attention layer and after the feedforward neural network"* inside each Transformer block — leaving the majority of model weights frozen.

### Two extensions Ch 12 names

1. **AdapterHub** (Pfeiffer et al. 2020, arXiv:2007.07779) — the central repository for sharing adapters. The chapter's framing: *"Practitioners can take adapters with specialized knowledge (e.g., medical text classification, NER) and use them on existing pretrained models without retraining the whole model."*
2. **LLaMA-Adapter** (Zhang et al. 2023, arXiv:2303.16199) — applies the adapter concept to text-generation Transformers with **zero-init attention**.

### Why LoRA replaced adapters as the dominant PEFT method (Ch 12 framing)

Ch 12 immediately pivots from adapters to LoRA as the worked-recipe choice: *"As an alternative to adapters, low-rank adaptation (LoRA) was introduced and is at the time of writing a widely used and effective technique for PEFT."* The implicit reason — consistent with Ch 7's framing — is LoRA's **merge-back-into-base-weights** capability, which eliminates the inference-latency overhead that persistent adapter layers introduce.
