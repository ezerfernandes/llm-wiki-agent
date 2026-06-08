---
title: "Quantization"
type: concept
tags: [inference, optimization, model-compression, serving]
sources: [ai-engineering-ch01-intro, ai-engineering-ch07-finetuning, ai-engineering-ch09-inference-optimization, hands-on-llm-ch07-advanced-text-generation, hands-on-llm-ch12-fine-tuning-generation-models, mlsysbook-ch02-ml-systems, mlsysbook-ch10-model-compression, mlsysbook-ch11-hardware-acceleration, mlsysbook-ch12-benchmarking, mlsysbook-ch13-model-serving, mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Quantization

**Reducing the numerical precision of model weights (and sometimes activations) — e.g., from FP16 to INT8, INT4, FP8, or FP4 — to lower memory footprint and accelerate inference.** Per [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]], one of three [[InferenceOptimization|inference-optimization]] techniques explicitly named (alongside [[KnowledgeDistillation|distillation]] and parallelism); Chapter 9 of the book covers all three in depth.

## Quantization is not training

Ch 1 makes a small but important distinction:

> *"Training always involves changing model weights, but not all changes to model weights constitute training. For example, quantization, the process of reducing the precision of model weights, technically changes the model's weight values but isn't considered training."*

Quantization moves weight values to a lower-precision representation; it does not adjust them via a loss-and-gradient process. Different conceptual category.

## Why it works

- **Foundation models are big**: 70B+ parameters at FP16 = 140+ GB just to load.
- **Hardware supports low precision**: NVIDIA Hopper (FP8), Blackwell (FP4), Ampere (INT8). Lower precision = more parallel MAC operations per cycle.
- **LLMs are surprisingly robust** to weight quantization, especially with calibration or per-channel scaling.

Quantization typically delivers the largest **TPOT/TTFT** improvement per engineering hour at the model-development layer.

## Common variants (Chapter 9)

- **Post-training quantization (PTQ)** — quantize after training; no further training needed.
- **Quantization-aware training (QAT)** — train with quantization simulation in the loop.
- **GPTQ / AWQ / SmoothQuant / GGUF** — specific weight-quantization techniques common in 2024.
- **KV-cache quantization** — reduce KV-cache precision rather than weights.

## Connections

- [[InferenceOptimization]] — the discipline this technique serves.
- [[TTFT]] / [[TPOT]] — the latency metrics quantization improves.
- [[AIEngineeringStack]] — model-development-layer responsibility.
- [[knowledgedistillation]] — the other major compression lever.
- [[ai-engineering-ch01-intro]] — primary source.

## From [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]]

Ch 7 is the book's most thorough quantization treatment, framed as the **most effective memory lever** in finetuning. [[ChipHuyen|Huyen]]'s key points:

### Terminology rule

> "Strictly speaking, it's quantization only if the target format is integer. However, in practice, quantization is used to refer to all techniques that convert values to a lower-precision format. In this book, I use quantization to refer to precision reduction, to keep it consistent with the literature."

This wiki follows the same convention.

### What and when to quantize (Ch 7)

| Decision | Common choice | Why |
|---|---|---|
| **What** | Weights (more than activations) | Weight quantization has more stable impact on performance with less accuracy loss. |
| **When** | [[PostTrainingQuantization\|PTQ]] | Most common; doesn't require retraining; supported by [[PyTorch]] / [[TensorFlow]] / [[HuggingFace]] transformers out-of-the-box. |
| **Training-time** | [[QuantizationAwareTraining\|QAT]] or direct low-precision training | Higher upfront cost, better low-precision quality. [[CharacterAI]] (2024) trained entirely in INT8. |

### The format spectrum

Per Ch 7, "Once you get to 8 bits and under, numerical representations get more tricky":

- **Float family**: [[FP32]] (single-precision, default in [[NumPy]] / [[pandas]]) → [[FP16]] (half-precision) → [[BF16]] (Google's TPU-optimized; more range, less precision than FP16) → [[TF32]] ([[NVIDIA]]'s GPU-optimized; 19 actual bits) → [[FP8]] → [[FP4]] (smallest IEEE-compliant float).
- **Integer family**: [[INT8]] / [[INT4]] (also called fixed-point).
- **Specialized**: [[NormalFloat4|NF4]] (QLoRA, designed for normal-distribution weights) → 1.58-bit [[BitNetB158|BitNet b1.58]] (Microsoft, 2024) → 1-bit [[BinaryConnect]] / [[XnorNet]] / [[BitNet]].

### Hardware co-evolution (Ch 7)

- [[NVIDIA]] Blackwell announced 4-bit float inference (2024).
- [[Apple]] ships on-device models averaging **3.5 bits per weight** via a 2/4-bit mixture (2024).
- TensorFlow Lite / PyTorch Mobile bundle PTQ for edge inference.
- "Some edge devices only support quantized inference."

### Quantization in finetuning vs inference

- **Inference**: standard practice — train in high precision, quantize for serve. Memory + latency win.
- **Finetuning**: harder because backprop is precision-sensitive. Solution → **[[MixedPrecisionTraining|mixed precision]]**: keep an FP32 master copy of weights, run forward+backward in lower precision (FP16/BF16/FP8), aggregate gradients in FP32. Managed via [[AutomaticMixedPrecision|AMP]] in PyTorch / TF.
- **[[QLoRA]]** is the canonical training-with-quantization example: base in NF4 (frozen), LoRA adapter in BF16, optimizer states paged.

### The 1.58-bit moment

Ma et al. (Microsoft, 2024) introduced [[BitNetB158|BitNet b1.58]] — a transformer LLM at 1.58 bits/parameter that matches 16-bit Llama 2 up to 3.9B params. Ch 7 cites this as evidence we're "entering the era of 1-bit LLMs."

### Why low precision often makes things *faster*, not just smaller

- Larger batch sizes fit in memory.
- Bit-level addition takes ~`t × bits` nanoseconds — half the bits, half the time (in principle; format-conversion overhead can offset this).

### Cautionary tale: the BF16/FP16 confusion

Ch 7's quoted lesson: Llama 2 was released in BF16. Many teams loaded it in FP16 (same bit count!) and reported "much worse than advertised" quality. BF16 has more range bits, fewer precision bits; values like 1234.56789 round to **1232.0 in BF16 vs 1235.0 in FP16** — different errors. **Always load a model in the format it was trained for.**

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 frames quantization as the **#1 most impactful inference-optimization technique** across use cases:

> *"Across various use cases, the most impactful techniques are typically quantization (which generally works well across models), tensor parallelism, replica parallelism, and attention mechanism optimization."*

### The 1-bit floor

> *"Weight-only quantization is by far the most popular approach since it's easy to use, works out of the box for many models, and is extremely effective. Reducing a model's precision from 32 bits to 16 bits reduces its memory footprint by half. However, we're close to the limit of quantization — we can't go lower than 1 bit per value."*

The theoretical floor is being approached — see [[BitNetB158]] (Microsoft 2024) for the 1.58-bit work.

### Quantization and MBU

Quantization is the dominant lever for [[MBU|Model Bandwidth Utilization]]:

> *"This underscores the importance of quantization (discussed in Chapter 7). Fewer bytes per parameter mean your model consumes less valuable bandwidth."* — Ch 9 (in the context of the MBU formula)

For [[MemoryBandwidthBound|memory-bandwidth-bound]] [[Decode|decode]], halving bytes-per-parameter (FP16 → INT8) doubles effective bandwidth headroom and roughly doubles tokens/s.

### PyTorch case study

Ch 9's Llama-7B optimization stack on A100 80GB showed throughput stacking:
1. `torch.compile` → 2. INT8 weights → 3. INT4 weights → 4. speculative decoding.

(The exact gains are visualized in Figure 9-14; book doesn't quantify how each step impacts model quality.)

### Quantization as compression family

Ch 9 lists quantization as one of four [[ModelCompression|model-compression]] families alongside [[knowledgedistillation|distillation]], [[Pruning|pruning]], and [[LowRankFactorization|low-rank factorization]] — and the only one Huyen explicitly says "is extremely effective" out of the box.

## From [[hands-on-llm-ch07-advanced-text-generation|Hands-On LLMs Ch 7]]

[[hands-on-llm-ch07-advanced-text-generation|Ch 7]] of *Hands-On LLMs* introduces quantization briefly to motivate the [[GGUF]]-quantized [[Phi3Mini|Phi-3]] used throughout the chapter. The chapter defers the deep treatment to **Ch 12** but commits four operational points:

- **Definition**: *"Quantization reduces the number of bits required to represent the parameters of an LLM while attempting to maintain most of the original information."*
- **The clock analogy**: *"If asked what the time is, you might say '14:16,' which is correct but not a fully precise answer. You could have said it is '14:16 and 12 seconds' instead, which would have been more accurate. However, mentioning seconds is seldom helpful and we often simply put that in discrete numbers, namely full minutes. Quantization is a similar process that reduces the precision of a value (e.g., removing seconds) without removing vital information (e.g., retaining hours and minutes)."*
- **The trade-off**: *"This comes with some loss in precision but often makes up for it as the model is much faster to run, requires less VRAM, and is often almost as accurate as the original."*
- **The 4-bit rule of thumb**: *"As a rule of thumb, look for at least 4-bit quantized models. These models have a good balance between compression and accuracy. Although it is possible to use 3-bit or even 2-bit quantized models, the performance degradation becomes noticeable and it would instead be preferable to choose a smaller model with a higher precision."*

Ch 7 uses an **8-bit Phi-3 variant** (vs the 16-bit fp16 original), *"cutting the memory requirements almost in half."* This consistent with Huyen Ch 7's *"weights more than activations"* + *"PTQ as default"* framing — Ch 7 of *Hands-On LLMs* is doing PTQ-served inference with no fine-tuning involved.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 is the **runnable quantization deep-dive** the book's earlier Ch 7 deferred to *"Ch 12 for the complete and highly visual guide."* The chapter motivates quantization via the precision-vs-memory trade visualizing π in float32 vs float16:

> *"If we lower the amount of bits to represent a value, we get a less accurate result. However, if we lower the number of bits we also lower the memory requirements of that model."* — Ch 12

### The naive-mapping problem

Ch 12 makes the wiki's clearest articulation of why direct higher→lower-precision quantization is lossy:

> *"When directly mapping higher precision values to lower precision values, multiple higher precision values might end up being represented by the same lower precision values."* — Ch 12

The fix is **[[BlockwiseQuantization|blockwise quantization]]** + **[[NormalFloat4|distribution-aware binning]]**:

1. **[[BlockwiseQuantization|Blockwise]]**: per-block quantization constants let each block of weights cluster around its own dynamic range without crushing fine differences.
2. **Distribution-aware (NF4)**: *"A nice property of neural networks is that their values are generally normally distributed between –1 and 1."* This lets binning happen by **relative density** — more bins near zero, fewer in the tails — reducing the same-quantized-value collision problem.

### The QLoRA stack

Ch 12 introduces quantization specifically as the **Q in [[QLoRA]]** — the chapter does not cover quantization-for-inference-only as a separate concern, because Ch 7 already did. Its position: quantization is **the memory-saving substrate** that makes LoRA fine-tuning viable on consumer GPUs.

> *"As a result, we can go from a 16-bit float representation to a measly 4-bit normalized float representation. A 4-bit representation significantly reduces the memory requirements of the LLM during training. Note that the quantization of LLMs in general is also helpful for inference as quantized LLMs are smaller in size and therefore require less VRAM."* — Ch 12

The chapter's explicit pedagogy points to a separate blog post for the *"complete and highly visual guide to quantization."*

## In ML-systems deployment ([[mlsysbook-ch02-ml-systems|mlsysbook Ch 2]])

Reddi frames quantization as the deployment lever that "often beats faster hardware" because batch-1 inference is [[MemoryWall|memory-bandwidth]]-bound on both cloud and mobile hardware: cutting bytes ([[ArithmeticIntensity|FP32→INT8]]) reduces the iron law's $D_{vol}/\text{BW}$ term that dominates wall-clock. Across the [[DeploymentSpectrum|deployment spectrum]] it is necessary but bounded by physics — FP32→INT8 cuts mobile power ~4× (still ~3 W from a 12 W baseline, hitting the [[ThermalWall|thermal wall]]), and is *insufficient* below the [[TinyML]] 64 KB memory-fit constraint, forcing full architectural redesign.

## The precision dimension in [[mlsysbook-ch10-model-compression|mlsysbook Ch 10]]

Ch 10 calls quantization *"the single most impactful optimization technique for deployment, especially for LLMs,"* and is the wiki's deepest treatment of its mechanics and physics:

- **Bits are energy.** Normalized to an INT8 add (1×): FP32 add ≈ 30×; a single 32-bit DRAM read > 10,000×. FP32→INT8 saves 4× memory but up to **~20× energy/inference** — the **"Energy Dividend"** (pay 4× in bits, get ~30× back in arithmetic energy). Memory-access energy, not arithmetic, dominates.
- **The "Free Lunch / Cliff":** accuracy holds flat FP32→INT8 (<1%), then collapses at the 3–4-bit cliff. INT8 ≈ <1% drop, INT4 ≈ 1–3% — *not universal* (validate per-model; vision tolerates better than language generation).
- **Affine math:** $q=\text{round}(x/s)$; $s=(\beta-\alpha)/(2^b-1)$, $z=\text{round}(-\alpha/s)$. Governed by [[Calibration|calibration]] (Max/Entropy/Percentile) and granularity (layerwise → groupwise → **channelwise standard** → sub-channelwise).
- **Speedup is bottleneck-dependent:** SIMD packing gives up to 4× on compute-bound layers; [[ActivationAwareWeightQuantization|AWQ]] INT4 weights dominate [[MemoryWall|bandwidth-bound]] LLM decode. A100: ~2× INT8-vs-FP16 peak compute.
- **[[Binarization|Extreme quantization]]** (binary/ternary, 16–32× size) lives in the [[TinyML]] regime.

See [[PostTrainingQuantization|PTQ]] / [[QuantizationAwareTraining|QAT]] for the precision-reduction strategy ladder and [[StraightThroughEstimator|STE]] for the QAT gradient trick. [[mlsysbook-ch10-model-compression]]

## Benchmarking quantization ([[mlsysbook-ch12-benchmarking|mlsysbook Ch 12]])

Ch 12 is the validation counterweight to the "INT8 is near-free" framing. INT8 quarters memory (4×) and accelerates 2–4×, and the **energy story** is decomposed precisely: register→DRAM costs ~16,000× per byte while a MAC drops FP32 1× → INT8 0.05× (~20× cheaper, transistor count ∝ bit-width²), so for MobileNetV2 INT8 attacks model-load energy (4×) *and* compute (~20×) for a **~5.4× total inference-energy reduction**. But quantization needs a **representative calibration dataset** (else non-reproducible; accuracy preservation 95–99% depends on calibration-data similarity to deployment), and aggregate accuracy hides damage: INT8 MobileNet holds top-1 (−0.9 pp) while [[ExpectedCalibrationError|ECE]] degrades 0.031→0.089 and edge-case accuracy drops 6.8 pp — a [[Benchmarking|multi-dimensional benchmark]] (accuracy + calibration + edge cases, on a [[ParetoFrontier|Pareto frontier]]) is mandatory. Quantization is also the canonical [[BenchmarkEngineering|benchmark-gaming]] vector (silent FP32→BF16 during a run), which MLPerf's accuracy guardrail disqualifies.

## Precision selection for serving ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]])

Ch 13 frames precision as **a direct infrastructure-economics lever**: theoretical INT8/FP32 throughput = 32/8 = 4× (achieved 2.5–3.5× due to [[TensorCore|Tensor Core]] alignment effects), so an INT8 workload needs **~1/3 the GPUs** of FP32 (a 30-GPU FP32 fleet → 10 at INT8). ResNet-50/V100: FP16 is a near-free 2× (no accuracy loss); INT8 PTQ is ~3× at <0.4 pp accuracy loss; INT8 QAT recovers most accuracy via retraining. **Layer sensitivity** ($\epsilon_{\text{quant}} \propto \alpha \cdot \|W\|_2 \cdot 2^{-b}$): keep first conv + final classification layers at FP16, INT8 the stable middle. The chapter elevates the calibration-data pitfall to a named fallacy — ImageNet-calibrated INT8 dropped 3.2 pp on out-of-distribution wildlife images. For LLM decode, weight-only INT4 (AWQ) beats activation quantization. See [[InferenceRuntime]], [[CostPerInference]], [[mlsysbook-ch13-model-serving]].

## Efficiency-as-responsibility ([[mlsysbook-ch15-responsible-engineering|mlsysbook Ch 15]])

Ch 15 recasts quantization (~2–4× compression) as an instrument of *responsibility*, not just performance: a 20% inference-latency reduction via quantization is shown to save ~$300K [[TotalCostOfOwnership|TCO]] and a few tonnes of CO₂ ([[CarbonFootprint|carbon]]) over a system's life, since inference dominates training ~40:1. It also widens accessibility by fitting models onto cheaper/edge hardware. See [[Sustainability]], [[GreenAI]], [[mlsysbook-ch15-responsible-engineering]].
