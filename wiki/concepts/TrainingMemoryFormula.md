---
title: "Training Memory Formula"
type: concept
tags: [memory, training, finetuning, back-of-napkin]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Training Memory Formula

[[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]'s decomposition of the **GPU memory needed to train (or finetune) a model**:

$$M_{\text{train}} = M_{\text{weights}} + M_{\text{activations}} + M_{\text{gradients}} + M_{\text{optimizer\_states}}$$

The last two terms — gradients and optimizer states — scale with the **[[TrainableParameters|number of trainable parameters]]**, *not* the total parameter count. This is the entire motivation for [[PEFT|PEFT]].

## Per-trainable-parameter memory (Ch 7)

| Optimizer | Values per trainable param | Bytes at FP16 |
|---|---|---|
| Vanilla [[StochasticGradientDescent\|SGD]] | 1 (gradient only) | 2 |
| [[Momentum]] SGD | 2 (gradient + momentum) | 4 |
| **[[Adam]]** | **3** (gradient + 2 optimizer states) | **6** |

[[Adam]] is the de facto transformer optimizer, so **6 bytes per trainable parameter** is the typical case.

## Worked examples (Ch 7)

### 13B model, [[FullFinetuning|full finetuning]] with Adam in FP16

- Weights: 13B × 2 bytes = **26 GB**.
- Gradients + Adam states: 13B × 3 × 2 bytes = **78 GB**.
- Activations: typically 20%–200%+ of weight memory depending on context length.
- **Total**: easily **100+ GB** — beyond a single A100 80GB.

### 13B model, 1B [[TrainableParameters|trainable]] (PEFT)

- Weights (frozen): 13B × 2 bytes = 26 GB (no gradients, no optimizer states).
- Trainable: 1B × 3 × 2 bytes = **6 GB**.
- Activations: similar to full FT case.
- **Total**: ~32 GB + activations — fits a single A100 80GB.

### 7B model, full FT with Adam in FP16

- Weights: 7B × 2 = **14 GB**.
- Gradients + Adam states: 7B × 3 × 2 = **42 GB**.
- Total (excluding activations): **56 GB**.

That's already past most consumer GPUs.

## Activation memory caveat (Ch 7)

> "The activation memory can be much larger [than the model's weights]. If activations are stored for gradient computation, the memory needed for activations can dwarf the memory needed for the model's weights." — Ch 7, citing Korthikanti et al. (2022)

[[GradientCheckpointing|Gradient checkpointing]] (= activation recomputation) is the mitigation: recompute activations during the backward pass instead of caching them. Trades wall-clock time for memory.

## Connections

- [[MemoryBottleneck]] — what this formula quantifies.
- [[InferenceMemoryFormula]] — the corresponding inference formula.
- [[TrainableParameters]] / [[OptimizerState]] / [[Gradient]] / [[ActivationMemory]] — the components.
- [[Adam]] / [[StochasticGradientDescent]] / [[Momentum]] — optimizer-specific multipliers.
- [[PEFT]] / [[lora|LoRA]] / [[QLoRA]] — the techniques that collapse the trainable-parameter term.
- [[GradientCheckpointing]] / [[CPUOffloading]] / [[MixedPrecisionTraining]] — orthogonal mitigations.
- [[ai-engineering-ch07-finetuning]] — primary source.
