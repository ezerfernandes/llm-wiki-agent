---
title: "QLoRA"
type: concept
tags: [peft, quantization, fine-tuning, adaptation, dspy]
sources: [2507.03152-medval, ai-engineering-ch07-finetuning, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-23
---

# QLoRA — Quantized Low-Rank Adaptation

**4-bit-quantized variant of [[lora|LoRA]]** for parameter-efficient fine-tuning. Combines:
1. **NF4 (NormalFloat-4) weight quantization** of the frozen pretrained base model — reduces memory ~4× vs FP16.
2. **Low-rank update** ($\Delta W = B A$, rank $r \ll \min(d, k)$) trained in higher precision (typically BF16) on top of the quantized base.
3. **Double quantization + paged optimizers** to avoid memory spikes during back-propagation.

Original paper: **Dettmers, Pagnoni, Holtzman & Zettlemoyer (NeurIPS 2023)**, ref [66] in [[2507.03152-medval]].

## Why it matters

Lets fine-tuning a multi-billion-parameter model fit on a single consumer-grade or workstation GPU (typically 24–48 GB VRAM) without giving up most of the accuracy that full-precision LoRA achieves. This is the bottleneck-relief that makes **distilled clinical validators trainable on a single A6000**.

## Use in MedVAL

[[2507.03152-medval]] §2.3.2 uses QLoRA as the PEFT method for fine-tuning open-source students < 8B parameters:
- 4-bit precision quantization via HuggingFace `BitsAndBytesConfig`.
- 5 epochs, Adam optimizer, lr $1\times 10^{-5}$ with linear decay, per-device batch size 1.
- Single **NVIDIA A6000** GPU.
- Applied to Llama-3.1-8B, Llama-3.2-3B, Qwen3-4B (the latter becomes [[MedVAL4B|MedVAL-4B]]).

As part of the paper's contribution, the authors **extend [[DSPy]]'s existing local parameter-efficient fine-tuning pipeline to support QLoRA** — via a [GitHub PR to `stanfordnlp/dspy`](https://github.com/stanfordnlp/dspy). This is the first wiki-corpus paper to add QLoRA as a first-class option inside `dspy.BootstrapFinetune`.

## Comparison to plain LoRA

| Aspect | [[lora|LoRA]] | QLoRA |
|---|---|---|
| Base model precision | FP16 / BF16 (frozen) | NF4 quantized (frozen) |
| Adapter precision | BF16 | BF16 |
| Memory vs full FT | ~3× reduction | ~12× reduction |
| Compute overhead | minimal | dequantization step on every forward |
| Typical hardware | A100 / H100 | consumer GPU (24 GB) feasible |

Trades a small amount of training-time compute for **dramatic memory savings**, opening up fine-tuning on hardware where LoRA wouldn't fit.

## Connections

- [[2507.03152-medval]] — the application paper.
- [[lora|LoRA]] — the parent low-rank-adaptation method.
- [[BootstrapFinetune]] — the DSPy optimizer that now ships with QLoRA support thanks to the MedVAL PR.
- [[DSPy]] — the framework into which the QLoRA pipeline was integrated.
- [[FineTuning]] — the parent regime.
- [[MedVAL]] / [[MedVAL4B]] — the validator pipeline / model that uses QLoRA end-to-end.
- [[2407.10930-better-together]] — a sibling DSPy paper that uses plain LoRA (rank 32 / alpha 64 / bfloat16) — the natural baseline for the QLoRA extension.

## From [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]]

[[ChipHuyen|Huyen]] frames QLoRA ([[TimDettmers|Dettmers]], Pagnoni, Holtzman & Zettlemoyer — NeurIPS 2023) as the quantized-LoRA work that **moved finetuning from datacenter-only to single-GPU-feasible**. Key points from Ch 7:

- **Why "reduce LoRA params more" misses the point**: per Ch 7's Table 7-6, a Llama-2 13B LoRA adapter (r=2 on query+key) is **6.55 MB** vs the 26 GB base model. Shrinking LoRA further yields negligible savings. The lever is the *base model's* memory, not the adapter's.
- **NF4 (NormalFloat-4)**: QLoRA's 4-bit format, designed around the empirical observation that "pre-trained weights usually follow a normal distribution with a median of zero." The quantization bins are distributed by quantiles of N(0, σ²), not uniformly.
- **Paged optimizers**: the second QLoRA innovation — auto-transfer optimizer states between CPU and GPU when GPU runs out of memory (especially with long sequence lengths).
- **End result**: a 65B-parameter model finetunable on a single 48 GB GPU. Compare to FP16 full FT of a 7B model (already at 56 GB).
- **[[Guanaco]] family**: the QLoRA paper's resulting models (Llama 7B → 65B finetuned in 4-bit). May 2023 GPT-4-as-judge Elo: GPT-4 1348, Guanaco 65B 1022, ChatGPT 966, Bard 902. Guanaco 65B was preferred to ChatGPT but didn't beat GPT-4.
- **The main cost of QLoRA**: NF4 quantization is computationally expensive. **QLoRA reduces memory but can *increase* training time** due to quantize/dequantize work in every forward+backward.
- **Sibling quantized-LoRA variants**: [[QALoRA]] (Xu et al. 2023), [[ModuLoRA]] (Yin et al. 2023), [[IRQLoRA|IR-QLoRA]] (Qin et al. 2024). "Many research labs have been working on quantized LoRA without publicly discussing it."

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* is the **first wiki source to walk a complete, runnable QLoRA recipe end-to-end** (vs Huyen Ch 7's abstract framing and MedVAL's domain-specific application). The chapter's framing:

### The three QLoRA innovations explained operationally

1. **[[BlockwiseQuantization|Blockwise quantization]]** — map *blocks* of higher-precision values with per-block quantization constants. Direct higher→lower mapping is lossy because multiple distinct higher-precision values collapse to the same lower-precision value; per-block quantization preserves the per-block dynamic range.
2. **[[NormalFloat4|NF4]] (NormalFloat-4)** — pre-trained weights are *"normally distributed between –1 and 1"*; NF4 bins original weights by **relative density** (more bins near zero, fewer in the tails). Prevents close-value collisions and reduces outlier impact.
3. **[[DoubleQuantization|Double quantization]] + [[PagedOptimizer|paged optimizers]]** — *"more elegant methods to further optimize this ... read about more in the QLoRA paper."*

> *"As a result, we can go from a 16-bit float representation to a measly 4-bit normalized float representation."* — Ch 12

### Worked recipe (TinyLlama + QLoRA SFT)

```python
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype="float16",
    bnb_4bit_use_double_quant=True,
)

peft_config = LoraConfig(
    lora_alpha=32, lora_dropout=0.1, r=64, bias="none",
    task_type="CAUSAL_LM",
    target_modules=["k_proj", "gate_proj", "v_proj", "up_proj",
                    "q_proj", "o_proj", "down_proj"],
)

# optim="paged_adamw_32bit" on the TrainingArguments side
```

### VRAM numbers from the chapter

> *"Loading the model now only uses ~1 GB VRAM compared to the ~4 GB of VRAM it would need without quantization."* — Ch 12 on loading [[TinyLlama|TinyLlama-1.1B]] in NF4

Single-epoch QLoRA SFT on a free Google Colab Tesla T4 ≈ **1 hour** for 3,000 UltraChat examples.

### Inference dividend

> *"Note that the quantization of LLMs in general is also helpful for inference as quantized LLMs are smaller in size and therefore require less VRAM."* — Ch 12

QLoRA's quantization step is not just a training-memory hack; the resulting 4-bit base remains usable at inference time, decoupling fine-tuning memory cost from inference memory cost.

### Both stages use QLoRA in Ch 12

The chapter applies the **same** QLoRA config to both:
- **SFT stage** ([[SFTTrainer]] + [[UltraChat]]).
- **DPO stage** ([[DPOTrainer]] + [[DistilabelIntelOrcaDPOPairs|orca-dpo-pairs]]).

This is the chapter's quiet structural point: QLoRA is the **memory-saving substrate**; the regime ([[SupervisedFinetuning|SFT]] vs [[DPO]]) is just a swap of the trainer + dataset on top.

### Parameterization-to-toggle-regimes

> *"This example demonstrates an efficient form of fine-tuning your model. If you want to perform full fine-tuning instead, you can remove the `quantization_config` parameter when loading the model and skip the creation of `peft_config`. By removing those, we would go from 'Instruction tuning with QLoRA' to 'full instruction tuning.'"* — Ch 12

The same training script flips between QLoRA and full FT by toggling two arguments.
