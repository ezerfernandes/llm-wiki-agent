---
title: "LoRA"
type: concept
tags: [peft, adaptation]
sources: [2407.10930-better-together, 2507.03152-medval, 2408.08849-ecg-chat, ai-engineering-ch07-finetuning, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-23
---

# LoRA — Low-Rank Adaptation

*Stub — referenced by other wiki pages but not yet ingested as a primary source.*

Hu et al. (2022, ICLR) — Low-Rank Adaptation of Large Language Models. LoRA freezes the pretrained weight matrix $W_0$ and adds a trainable low-rank update $\Delta W = B A$ with $B\in\mathbb{R}^{d\times r}, A\in\mathbb{R}^{r\times k}, r\ll\min(d,k)$. Used in [[2605.12966-agentic-ai-to-agi]] (§3.2) as empirical evidence for the central thesis: *specialized adapters are significantly more data-efficient than monolithic fine-tunes* — a low-dimensional, task-specific projection captures most of the gain.

Used in [[2407.10930-better-together|Soylu, Potts & Khattab (2024)]] as the [[BootstrapFinetune|BFT]] weight-update method inside [[BetterTogether]]: **rank 32, alpha 64, no dropout, bfloat16, lr 1e-5, 5 epochs, effective batch size 8**; targets the **query and key self-attention layers** only. The compact LoRA-only setup is what lets the paper fit all three 7-8B LMs into a 75-A100-GPU-hour Table-1 budget.

Two years later, [[2507.03152-medval|Aali et al. (MedVAL, 2026)]] extends [[DSPy]]'s local PEFT pipeline with **[[QLoRA|QLoRA]]** (4-bit-quantized LoRA) — letting < 8B-parameter clinical validators fine-tune on a single NVIDIA A6000 GPU. [[MedVAL4B|MedVAL-4B]] (Qwen3-4B base) is the resulting open-source artifact; the QLoRA support lands in `stanfordnlp/dspy` via the paper's GitHub PR.

A 2025 medical-MLLM data point: [[2408.08849-ecg-chat|ECG-Chat (Zhao et al. 2025)]] uses LoRA to specialize [[Vicuna13B|Vicuna-13B]] for ECG report generation under a constrained 8×V100 32GB budget — the [[ZeRO]] optimizer + LoRA combination is what lets a 13B-scale [[MultimodalLLM|adapter-MLLM]] fit at all, and the wiki's first record of LoRA applied to a **physiological-signal** modality.

## Connections
- [[2605.12966-agentic-ai-to-agi]]
- [[2407.10930-better-together]] — uses LoRA as the BFT weight-update method.
- [[2507.03152-medval]] — extends DSPy with [[QLoRA]] (4-bit LoRA) for clinical validators.
- [[QLoRA]] — quantized variant introduced by Dettmers et al. (NeurIPS 2023) and integrated into DSPy by MedVAL.
- [[BootstrapFinetune]] — the optimizer that applies LoRA (and now QLoRA).
- [[BetterTogether]] — the meta-optimizer that schedules the LoRA fine-tune between two prompt-opt steps.
- [[FineTuning]] — parent regime.
- [[MedVAL]] / [[MedVAL4B]] — the clinical-validator pipeline / model that uses QLoRA end-to-end.
- [[2408.08849-ecg-chat]] — LoRA applied to Vicuna-13B for ECG MLLM specialization (signal modality, not text).

## From [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]]

[[ChipHuyen|Huyen]]'s Ch 7 dedicates its longest single section to LoRA — the dominant [[PEFT]] technique by usage (per her analysis of 1,000+ `huggingface/peft` GitHub issues). The chapter's framing of LoRA:

### The math (Ch 7)

For a weight matrix W of dimension n × m, choose a rank r and construct A (n × r) and B (r × m). The LoRA update is:

$$W' = W + \frac{\alpha}{r} W_{AB}$$

During finetuning, only A and B are updated; W is frozen. The hyperparameter α controls how much the LoRA delta contributes during merging.

### Why LoRA solves the latency problem of [[adapterlayers|Houlsby 2019 adapters]]

The original Houlsby adapter inserts new layers into each transformer block, adding inference latency. LoRA's A·B product can be **merged back into W** at serving time, leaving inference unchanged. This is the architectural win that made LoRA dominate.

### LoRA configurations (Ch 7)

- **Where**: usually applied to the four self-attention matrices Wq, Wk, Wv, Wo. If budget-limited, the LoRA paper recommends **Wq and Wv** as the most impactful pair.
- **Rank**: typically 4–64; the LoRA paper finds that **applying LoRA to all four matrices with r=2 beats one matrix at r=8** given the same 18M-param budget on GPT-3 175B.
- **α : r ratio**: typically 1:8 to 8:1; experimentation needed.
- **Feed-forward LoRA**: [[Databricks]] (Sooriyarachchi 2023) reports the biggest performance bump from applying LoRA to all feedforward layers; Fomenko et al. (2024) — FF-LoRA is *complementary* to attention-LoRA.
- **Rank insensitivity**: most practitioners find r > 64 doesn't help and may overfit. [[SebastianRaschka|Raschka]] (2023) is the contrary data point with r=256 winning on his tasks.
- **Framework constraint**: Fireworks caps LoRA rank at 32, probably from memory constraints rather than performance evidence.

### Why LoRA works at all — the intrinsic-dimension hypothesis

The most theoretical part of Ch 7's LoRA section: [[Li2018IntrinsicDimension|Li et al. (2018)]], [[Aghajanyan2020IntrinsicDimension|Aghajanyan et al. (2020)]], and the LoRA paper itself argue that LLMs have very low [[IntrinsicDimension|intrinsic dimensions]] — and **larger models have lower intrinsic dimensions after pre-training**. "Pre-training acts as a compression framework for downstream tasks." This is why **0.0027% of GPT-3's parameters** (4.7M trainable LoRA params) can match full finetuning on multiple benchmarks.

### [[MultiLoraServing|Multi-LoRA serving]] — the under-discussed win

Two serving modes:
1. **Merged**: Compute W' = W + (α/r) W_AB ahead of inference. No latency overhead. Optimal for single-LoRA serving.
2. **Separate**: Keep W, A, B distinct; merge on-the-fly per request. Slight latency hit but **dramatic storage savings** when serving many LoRA adapters that share a base.

Worked example (Ch 7): one base model + 100 customer LoRAs (Llama-2-13B; rank=8 applied to query+key). Mode 1 = 1.68B parameters of storage; Mode 2 = 23.3M parameters. **72× reduction**. Mode 2 also makes per-tenant model switching (load just A,B) much faster than full-model swap.

### Why LoRA isn't used for *pre*-training

Open question Ch 7 surfaces: if low-rank works for adaptation, why not for pre-training? Attempts include [[ReLoRA]] (Lialin et al. 2023, works up to 1.3B) and [[GaLore]] (Zhao et al. 2024, competitive at 1B, promising at 7B). The conjectured answer: **full-rank pre-training is what compresses the intrinsic dimension** to the point where low-rank adaptation works — i.e., LoRA depends on a high-rank ancestor.

### Apple's on-device multi-LoRA

Apple (2024) used multiple LoRA adapters over a single 3B base, plus quantization (~3.5 bits/weight average), to ship multiple AI features in iPhone memory. This is Ch 7's canonical on-device LoRA case.

### Drawbacks Huyen names

- Doesn't match full-finetuning quality on every task.
- Harder to implement (needs model architecture knowledge) — though [[HuggingFacePEFT|HF PEFT]], [[Axolotl]], [[Unsloth]], [[LitGPT]] make this a non-issue for popular bases.
- The LoRA-rank tuning surface is real (rank + α + which matrices).

### LoRA variants ecosystem (Ch 7)

- **[[QLoRA]]** — 4-bit NF4 quantization of base + BF16 LoRA + paged optimizers; lets 65B finetune on one 48 GB GPU. The dominant variant in 2024–2025 application practice.
- **[[LongLoRA]]** — Chen et al. 2023; combines LoRA with attention modifications for context extension.
- **[[QALoRA]]** / **[[ModuLoRA]]** / **[[IRQLoRA|IR-QLoRA]]** — other quantized-LoRA work.
- **[[BitFit]]** — sibling adapter-based method (bias-only).
- **[[IA3]]** — sibling that scales activations rather than adding parameters; strong in multi-task batching.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

[[hands-on-llm-ch12-fine-tuning-generation-models|Ch 12]] is the wiki's first **runnable, GPU-poor LoRA recipe** — fine-tuning [[TinyLlama|TinyLlama-1.1B]] on a free Google Colab Tesla T4. The chapter's explanation of LoRA is the most pedagogical in the wiki, anchored in the *"two smaller matrices reconstruct one larger matrix"* intuition.

### The intuition Ch 12 builds

Decompose updates to a large weight matrix into two smaller matrices whose product reconstructs the update. A 10×10 matrix (100 weights) → two 10×1 matrices (20 weights). For GPT-3 175B's 12,288×12,288 matrices (150M parameters per block), **rank-8 LoRA = two 12,288×2 matrices = 197K parameters per block**.

> *"We can come up with two smaller matrices, which when multiplied, reconstruct a 10 × 10 matrix. This is a major efficiency win because instead of using 100 weights (10 times 10) we now only have 20 weights (10 plus 10)."* — Ch 12

### Theoretical justification

Ch 12 cites the same [[IntrinsicDimension|intrinsic-dimension]] result the wiki had via Huyen Ch 7 — Aghajanyan, Zettlemoyer & Gupta 2020 (arXiv:2012.13255). Language models *"have a very low intrinsic dimension. This means that we can find small ranks that approximate even the massive matrices of an LLM."*

### Worked `LoraConfig` in Ch 12

```python
peft_config = LoraConfig(
    lora_alpha=32, lora_dropout=0.1, r=64, bias="none",
    task_type="CAUSAL_LM",
    target_modules=["k_proj", "gate_proj", "v_proj", "up_proj",
                    "q_proj", "o_proj", "down_proj"],
)
```

- **`r=64`** — rank; *"Values typically range between 4 and 64."*
- **`lora_alpha=32`** — *"Controls the amount of change that is added to the original weights ... balances the knowledge of the original model with that of the new task. A rule of thumb is to choose a value twice the size of r."* (Note: the worked recipe's α=32 / r=64 = 0.5× contradicts its own inline rule.)
- **`target_modules`** — all seven LLaMA-family projections (attention Q/K/V/O + FFN up/gate/down). The chapter notes LoRA *"can choose to ignore specific layers"* as a speed/performance lever.

### LoRA + QLoRA together

Ch 12 uses LoRA stacked on a 4-bit-quantized base ([[QLoRA]]) for both the SFT and DPO stages. The chapter's structural point: the **same `LoraConfig`** works for both regimes — only the trainer (`SFTTrainer` vs `DPOTrainer`) and the dataset change.

### Merging

After training, the chapter uses `peft.AutoPeftModelForCausalLM.from_pretrained(...).merge_and_unload()` to fuse the LoRA delta back into the base weights. For the two-adapter SFT + DPO case, it merges iteratively: first the SFT adapter into the base, then the DPO adapter into the SFT-merged model.

### Adapter context

Ch 12 introduces LoRA as the **alternative to [[adapterlayers|Houlsby 2019 adapters]]** — both are PEFT methods that update only a small subset of parameters, but LoRA's low-rank factorization can merge back into base weights with zero inference latency, while Houlsby-style adapters add new layers that persist at inference. The chapter also mentions **[[adapterlayers#LLaMAAdapter|LLaMA-Adapter]]** (Zhang et al. 2023, arXiv:2303.16199) as the application of the adapter concept to generative Transformers with zero-init attention.
