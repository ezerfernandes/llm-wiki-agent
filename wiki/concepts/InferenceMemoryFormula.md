---
title: "Inference Memory Formula"
type: concept
tags: [memory, inference, finetuning, back-of-napkin]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Inference Memory Formula

[[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]'s back-of-napkin formula for **GPU memory needed to serve a model in inference**:

$$M_{\text{inference}} \approx N \cdot M \cdot 1.2$$

Where:
- **N** = number of model parameters.
- **M** = bytes per parameter (FP16 → 2; INT8 → 1; INT4 → 0.5).
- **1.2** = a 20% buffer for [[ActivationMemory|activations]] and KV-cache at typical sequence lengths.

## Worked examples (Ch 7)

| Model | Bytes/param | Weights only | With 20% buffer |
|---|---|---|---|
| 7B FP16 | 2 | 14 GB | 16.8 GB |
| 13B FP16 | 2 | 26 GB | 31.2 GB |
| 70B FP16 | 2 | 140 GB | 168 GB |
| 70B INT4 | 0.5 | 35 GB | 42 GB |

## Caveats

- **The 20% buffer breaks down at long sequence lengths.** [[ActivationMemory|Activation memory]] and KV-cache memory grow linearly with sequence length × batch size. For long-context workloads, you may need 50%+ for the activation buffer.
- **No optimizer-state term.** Inference doesn't need [[Gradient|gradients]] or [[OptimizerState|optimizer states]] — that's what makes inference cheaper than training (see [[TrainingMemoryFormula]]).
- **Per-GPU, not per-cluster.** If you're using tensor or pipeline parallelism, the per-GPU memory is roughly `M_inference / num_GPUs` plus overhead.

## Connections

- [[MemoryBottleneck]] — what this formula quantifies.
- [[TrainingMemoryFormula]] — the corresponding training formula (much larger).
- [[NumericalRepresentation]] — what `M` (bytes per param) depends on.
- [[ActivationMemory]] — the 20% buffer.
- [[Quantization]] — the lever that reduces `M`.
- [[ai-engineering-ch07-finetuning]] — primary source.
