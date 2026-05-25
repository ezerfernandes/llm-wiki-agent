---
title: "Automatic Mixed Precision (AMP)"
type: concept
tags: [training, numerics, framework]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Automatic Mixed Precision (AMP)

A framework feature that **automatically decides which operations run in lower precision and which stay in higher precision** during training. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "The portions of the model that should be in lower precision can be set automatically using the automatic mixed precision (AMP) functionality offered by many ML frameworks."

## Implementations

| Framework | API |
|---|---|
| **[[PyTorch]]** | `torch.cuda.amp.autocast()` + `torch.cuda.amp.GradScaler()` |
| **[[TensorFlow]]** | `tf.keras.mixed_precision.set_global_policy('mixed_float16')` |
| **JAX** | `jax.lax.precision` + manual policy |

## What AMP does behind the scenes

- **Wraps the forward pass** so individual ops execute in lower precision (FP16 or BF16) where safe.
- **Keeps the master weight copy** in FP32.
- **Applies loss scaling** in FP16 paths to prevent gradient underflow (scale loss up by, e.g., 65,536 → unscale gradients before applying).
- **Maintains a per-op allowlist** for operations known to need higher precision (e.g., softmax, layer-norm, log-sum-exp, reductions).

## Why it matters

Mixed precision training without AMP is *possible* but error-prone — you have to know which ops are safe in which precision. AMP encodes that domain knowledge in the framework so the user just declares "train in mixed precision" and the framework handles the bookkeeping.

This is why **mixed precision became the default training mode** for foundation models: AMP removed the operational burden.

## Connections

- [[MixedPrecisionTraining]] — the manual / general form.
- [[FP16]] / [[BF16]] / [[FP32]] — the formats AMP mixes.
- [[Quantization]] — the broader umbrella.
- [[PyTorch]] / [[TensorFlow]] — framework implementations.
- [[ai-engineering-ch07-finetuning]] — primary source.
