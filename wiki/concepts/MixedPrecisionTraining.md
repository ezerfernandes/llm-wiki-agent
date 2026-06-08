---
title: "Mixed Precision Training"
type: concept
tags: [training, numerics, gpu, finetuning]
sources: [ai-engineering-ch07-finetuning, mlsysbook-ch07-ml-frameworks, mlsysbook-ch08-model-training, mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# Mixed Precision Training

A training mode where **different tensors live in different numerical precisions** — typically a high-precision master copy plus lower-precision working copies for forward/backward computation. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "Training is more sensitive to numerical precision, so it's harder to train a model in lower precision. Training is typically done in mixed precision, with some operations done in higher precision (e.g., 32-bit) and some in lower precision (e.g., 16-bit or 8-bit)."

## The canonical recipe (Ch 7)

1. Keep an **FP32 master copy** of the weights.
2. Cast to **[[FP16]] or [[BF16]]** for the forward pass + backward pass + activations + gradients.
3. Accumulate gradients in **FP32** to avoid underflow.
4. Apply gradients to the **FP32 master copy**, then cast back to FP16/BF16 for the next forward pass.

Loss values are typically computed in FP32 even in mixed precision because small errors in loss can mis-direct parameter updates.

## Per-tensor / per-layer mixing

You can also have different *layers* in different precisions. Per Ch 7:

> "[[LLMQAT|LLM-QAT]] (Liu et al., 2023) quantizes weights and activations into 4 bits but keeps embeddings in 16 bits."

This pattern — less-sensitive layers in lower precision, more-sensitive layers in higher precision — generalizes across modern mixed-precision practice.

## [[AutomaticMixedPrecision|Automatic Mixed Precision (AMP)]]

Most ML frameworks ship an AMP utility that decides per-op what precision to use. Per Ch 7: *"The portions of the model that should be in lower precision can be set automatically using the automatic mixed precision (AMP) functionality offered by many ML frameworks."* Implementations:

- **PyTorch**: `torch.cuda.amp.autocast` + `GradScaler` for loss scaling.
- **TensorFlow**: `tf.keras.mixed_precision.set_global_policy('mixed_float16')`.

## Why mixed precision works

- **Forward/backward computation** doesn't need FP32 precision per-step; the result is bounded by activations + weights both in lower precision.
- **Gradient accumulation across many micro-batches** can underflow in FP16; FP32 accumulation prevents this.
- **Weight updates** are small relative to weight magnitudes; the FP32 master copy preserves these.

## When mixed precision isn't enough

- **Very long training runs** can compound rounding errors even in mixed precision. Solution: pure FP32 reference runs occasionally to sanity-check.
- **Models with extreme activation ranges** (e.g., very deep networks with no normalization) may need additional tricks (loss scaling, careful initialization).

## Cross-phase mixed precision

Ch 7 also notes: *"It's also possible to have different phases of training in different precision levels. For example, a model can be trained in higher precision but finetuned in lower precision. This is especially common with foundation models, where the team training a model from scratch might be an organization with sufficient compute for higher precision training. Once the model is published, developers with less compute access can finetune that model in lower precision."*

## Framework view from [[mlsysbook-ch07-ml-frameworks|mlsysbook Vol 1 Ch 7]]

Ch 7 frames mixed precision as the rare optimization that **improves two iron-law terms at once**: [[TensorCore|Tensor Cores]] run FP16 matmuls faster (raising $R_{\text{peak}}$, cutting the compute term) *and* FP16 activations halve the memory footprint (cutting $D_{\text{vol}}$). Frameworks auto-route matmuls/convs to FP16 while keeping softmax/layernorm in FP32. Key precision distinction: [[FP16]]'s 5-bit exponent underflows for gradients below ~6×10⁻⁵, requiring loss scaling (`GradScaler`); [[BF16]] (Google Brain ~2018) matches FP32's exponent range, **eliminating loss scaling** in most workloads — "BF16 is preferred when training stability matters, FP16 when numerical precision matters more."

## The six-step cycle and hardware ladder from [[mlsysbook-ch08-model-training|mlsysbook Ch 8]]

Ch 8 (the Build-part training capstone) gives the canonical six-step cycle — (1) FP32 master weights cast to FP16, (2) forward computes FP16 loss, (3) **[[LossScaling|loss is scaled]]** to prevent gradient underflow, (4) backprop computes scaled FP16 gradients, (5) gradients copied to FP32 and unscaled, (6) FP32 gradients update the master weights. The realized speedup is *smaller than the peak ratio*: A100 FP16/BF16 Tensor Cores hit ~16× FP32 *peak*, but end-to-end training gains ~2–2.5× once data movement, non-Tensor-Core kernels, communication, and optimizer work are counted. Cross-generation GPT-2 throughput: V100 18→45 samples/s (FP32→FP16, 2.5×), A100 165 (BF16), H100 380 ([[FP8]]) — ~21× over V100-FP32. Per-architecture defaults: V100 → FP16+loss-scaling, A100 → BF16 (transformers) / FP16 (CNNs), H100 → FP8 via TransformerEngine.

## Connections

- [[mlsysbook-ch08-model-training]] — the training-capstone treatment: six-step cycle, cross-generation throughput ladder, FP8 on Hopper.
- [[LossScaling]] — step 3 of the cycle; the FP16 underflow safeguard BF16 eliminates.
- [[mlsysbook-ch07-ml-frameworks]] — mixed precision as a dual iron-law win; FP16 vs BF16 loss-scaling distinction.
- [[TensorCore]] — the hardware mixed precision exploits.
- [[AutomaticMixedPrecision]] — the framework-level autopilot.
- [[NumericalRepresentation]] — the bit-allocation framework.
- [[FP16]] / [[BF16]] / [[FP8]] / [[FP32]] — the formats commonly mixed.
- [[Quantization]] / [[QuantizationAwareTraining]] — neighboring techniques.
- [[MemoryBottleneck]] — what mixed precision helps with.
- [[Backpropagation]] — the algorithm that requires precision care.
- [[ai-engineering-ch07-finetuning]] — primary source.
