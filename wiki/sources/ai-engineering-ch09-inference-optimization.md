---
title: "AI Engineering Ch 9 — Inference Optimization"
type: source
tags: [book, inference, optimization, latency, throughput, ai-engineering, oreilly, ai-engineering-book]
date: 2024-12-04
source_file: raw/papers/ai-engineering/ch09-inference-optimization.md
parent_source: ai-engineering-chip-huyen
---

# AI Engineering Ch 9 — Inference Optimization

## Summary

Chapter 9 of [[ChipHuyen|Chip Huyen]]'s *AI Engineering* ([[OReilly|O'Reilly Media]], December 2024) is the book's deep dive on **making models faster and cheaper to serve**. The chapter is organized around a three-level taxonomy — **model-level**, **hardware-level**, and **service-level** optimizations — pitched via an archery metaphor: model-level is "crafting better arrows," hardware-level is "training a stronger archer," service-level is "refining the entire shooting process." Hardware design is treated only as background; the technical core is model-level and service-level techniques. The chapter's central organizing distinction is between **compute-bound** and **memory bandwidth-bound** workloads (Williams et al. 2009, *Roofline*) — measured by **arithmetic intensity** (FLOPs per byte of memory access). Image generation (Stable Diffusion) is typically compute-bound; **autoregressive LLM inference is memory bandwidth-bound** under most conditions, and that single fact drives most of the chapter.

The **inference performance metrics** section formalizes the latency vocabulary [[ai-engineering-ch01-intro|Ch 1]] introduced. **TTFT** (time to first token) corresponds to [[Prefill|prefill]] and is dominated by input length; **TPOT** (time per output token) is steady-state decode speed; **TBT** (time between tokens, used by [[LinkedIn]]) and **ITL** (inter-token latency, used by [[NVIDIA]]) are variants on the same idea. Total latency = TTFT + TPOT × output length. A "very fast reader" can consume **120 ms/token (6–8 tokens/s)** — so anything faster than that during streaming is sufficient. Huyen flags that for **CoT** or agentic queries, the model's first token may be hidden plan/action steps, so user-observed TTFT differs from model-internal TTFT (some teams use **"time to publish"** to disambiguate). Because latency is a distribution, **p50/p90/p95/p99 percentiles** are more useful than averages. **Throughput** is tokens/s (TPS), often complemented by requests/second (RPS) or completed requests/minute (RPM). **Goodput** — borrowed from networking — is *requests/s that meet the SLO* (e.g. TTFT ≤ 200 ms ∧ TPOT ≤ 100 ms); the LinkedIn AI team reported it's "not uncommon to double or triple throughput if willing to sacrifice TTFT and TPOT."

The **utilization** subsection is one of the chapter's sharpest. `nvidia-smi`'s **GPU utilization** is the *percentage of time the GPU is doing anything* — which is misleading because a GPU "actively processing" one op/s on hardware capable of 100 op/s shows 100% utilization. **[[MFU|MFU]]** (Model FLOP/s Utilization, named in the [[PaLM]] paper, Chowdhery et al. 2022) and **[[MBU|MBU]]** (Model Bandwidth Utilization) are the metrics that actually matter. MBU = (parameter count × bytes/param × tokens/s) / theoretical bandwidth — e.g. a 7B model in FP16 at 100 tokens/s = 700 GB/s; on an A100-80GB at 2 TB/s that's 70% MBU. **MFU > 50% is considered good for training**; inference MFU during prefill > MFU during decode (compute-bound vs memory bandwidth-bound). Table 9-1 gives historical MFU values: GPT-3 21.3% (V100), Gopher 32.5% (TPU v3), Megatron-Turing NLG 30.2% (A100), PaLM 46.2% (TPU v4). Huyen calls out **"peak FLOP/s hacking"** — chip makers running benchmarks under sparsity / specific-shape conditions to inflate marketing numbers.

The **AI accelerators** section provides a quick taxonomy: [[NVIDIA]] GPUs dominate; alternatives include [[AMD]] GPUs, [[GoogleTPU]] (Tensor Processing Unit, Google), Intel Habana Gaudi, [[Graphcore]] IPU, [[Groq]] LPU, [[Cerebras]] Wafer-Scale QPU. Specialized **inference chips** include Apple Neural Engine, AWS [[Inferentia]], Meta MTIA; edge-inference chips include Google Edge TPU, NVIDIA Jetson Xavier. Chip selection comes down to **FLOP/s, memory size, memory bandwidth, power consumption**. The H100 SXM spec sheet (Table 9-2) is reproduced: TF32 989 TFLOP/s, BF16 1,979, FP16 1,979, FP8 3,958 (with sparsity). **CPU memory** has 25–50 GB/s bandwidth (16 GB–1 TB); **GPU HBM** has 256 GB/s to 1.5+ TB/s (24–80 GB); **on-chip [[SRAM]]** (L1/L2/L3 caches) exceeds 10 TB/s but is ≤ 40 MB. The two GPU programming languages mentioned by name are [[CUDA]] (NVIDIA) and [[Triton]] (OpenAI); AMD's open-source alternative is [[ROCm]]. **Power**: an H100 at peak draws ~7,000 kWh/year (a US household averages 10,000 kWh/year); **electricity is becoming a bottleneck to scaling compute**.

The **model-level optimization** section opens with **[[ModelCompression|model compression]]** — three families: [[Quantization|quantization]] (the dominant, easy-to-use lever — reducing FP32 → FP16 halves memory; "we're close to the limit — we can't go lower than 1 bit per value"), [[KnowledgeDistillation|distillation]], and **[[Pruning|pruning]]** (two senses: remove entire nodes — architectural change — or zero out unimportant parameters — sparsity). Frankle & Carbin (2019, lottery-ticket paper) showed pruning can remove > 90% of non-zero parameters without accuracy loss, but in practice pruning is less common because it's harder, the gains are usually smaller than quantization's, and not all hardware exploits sparsity.

The **autoregressive decoding bottleneck** subsection is where Chapter 9 is most distinctive. Across model APIs, an **output token costs 2–4× an input token**; Anyscale (Kadous et al. 2023) measured that **a single output token has the same latency impact as 100 input tokens**. Three families of techniques attack the decoding bottleneck: **[[SpeculativeDecoding|speculative decoding]]** (Chen et al. 2023 DeepMind — a 4B draft model proposed tokens for Chinchilla-70B, generating tokens 8× faster (1.8 ms vs 14.1 ms) and **halving response latency without quality loss**; 50 lines of PyTorch; integrated in vLLM, [[TensorRTLLM]], llama.cpp); **[[InferenceWithReference|inference with reference]]** (Yang et al. 2023 — copy draft tokens from input context rather than a draft model; **2× speedup** in retrieval / coding / multi-turn conversations); **[[ParallelDecoding|parallel decoding]]** ([[LookaheadDecoding|Lookahead decoding]] (Fu et al. 2024) uses the **[[JacobiAlgorithm|Jacobi method]]**; **[[MedusaDecoding|Medusa]]** (Cai et al. 2024) attaches multiple decoding heads + tree-based attention verification — NVIDIA reported **1.9× Llama 3.1 boost on HGX H200**).

The **attention-mechanism optimization** subsection groups techniques into three buckets: **redesign the attention mechanism**, **optimize the KV cache**, **write kernels**. The KV-cache size formula `2 × B × S × L × H × M` yields **54 GB** for LLama-2 13B with batch=32, seq=2048, FP16; the Pope et al. (2022) Google paper computed **3 TB** for a 500B+ MHA model with batch=512, ctx=2048 — three times the model weights. Attention redesigns include **[[LocalAttention|local windowed attention]]** (Longformer, Beltagy et al. 2020 — reduces effective seq length to a fixed window, cutting KV cache 10× when window=1000 vs avg-seq=10000), **[[CrossLayerAttention|cross-layer attention]]** (Brandon et al. 2024 — share K/V across adjacent layers), **[[multiqueryattention|multi-query attention]]** (Shazeer 2019 — share K/V across all query heads), and **[[GroupedQueryAttention|grouped-query attention]]** (Ainslie et al. 2023 — groups in between). Character.AI (2024) combined MQA + interleaved local/global + cross-layer attention to cut KV cache **> 20×**, removing it as a bottleneck for large batches. KV-cache optimizations include **[[PagedAttention|PagedAttention]]** (Kwon et al. 2023, vLLM), KV-cache quantization (Hooper et al. 2024; Kang et al. 2024), adaptive KV-cache compression (Ge et al. 2023), selective KV cache (Liu et al. 2024). Kernel-level work is exemplified by **[[FlashAttention|FlashAttention]]** (Dao et al. 2022, A100; FlashAttention-3 by Shah et al. 2024 for H100).

The **kernels and compilers** subsection names four common kernel-writing techniques: **vectorization** (process contiguous data elements simultaneously), **parallelization** (split arrays into independent chunks), **loop tiling** (reorder loop access for memory hierarchy; hardware-dependent), and **operator fusion** (combine multiple ops in one pass to reduce memory traffic). Compilers ("**lowering**" tools) bridge model scripts to hardware: standalone tools include Apache **[[TVM]]** and **[[MLIR]]**; framework-integrated include `torch.compile` (PyTorch), **[[XLA]]** (TensorFlow / OpenXLA), and TensorRT's built-in compiler. A PyTorch case study on Llama-7B (A100 80GB) showed throughput gains stacking: `torch.compile` → INT8 quant → INT4 quant → speculative decoding.

The **inference service optimization** section focuses on resource management *without* modifying the model. **[[Batching|Batching]]** has three flavors: **[[StaticBatching|static batching]]** (wait for N requests; first request blocked until last arrives — bad), **[[DynamicBatching|dynamic batching]]** (batch on N OR T-ms timeout, whichever first; LinkedIn-style), **[[ContinuousBatching|continuous batching]]** / **in-flight batching** (Orca, Yu et al. 2022 — evict completed responses and admit new ones mid-batch). **[[PrefillDecodeDisaggregation|Prefill-decode disaggregation]]** (DistServe, Zhong et al. 2024; "Inference Without Interference," Hu et al. 2024) assigns prefill and decode to *different* GPUs because they compete for resources when colocated; communication overhead is acceptable on NVLink-class fabrics. **Prefill:decode instance ratio** depends on workload — 2:1 to 4:1 for long inputs prioritizing TTFT; 1:2 to 1:1 for short inputs prioritizing TPOT (Meta talk on Llama inference). **[[PromptCaching|Prompt caching]]** (Gim et al. November 2023) caches system prompts / long documents / multi-turn conversation prefixes for reuse — Google Gemini gives **75% discount** on cached input tokens but charges **$1.00 per 1M tokens per hour** for cache storage; Anthropic promises **up to 90% cost savings and 75% latency reduction**. Table 9-3 (Anthropic 2024): chat with a 100K-token book = 11.5 s → 2.4 s (–79%, **–90% cost**); 10-turn convo with long system prompt = ~10 s → ~2.5 s (–75%, **–53% cost**).

The **parallelism** section covers **[[ReplicaParallelism|replica parallelism]]** (just copy the model — bin-packing problem for mixed sizes/GPUs), **[[TensorParallelism|tensor parallelism]]** / intra-operator parallelism (split tensors columnwise; "the most common model-parallelism approach for inference"), **[[PipelineParallelism|pipeline parallelism]]** (split layers across machines; **increases latency, so avoided for strict-latency inference; common in training**), and brief mentions of **[[ContextParallelism|context parallelism]]** (split input sequence across devices) and **[[SequenceParallelism|sequence parallelism]]** (split operators across devices for the entire input). The chapter's closing recommendation: across use cases, the **most impactful techniques are quantization, tensor parallelism, replica parallelism, and attention-mechanism optimization**.

## Key Claims

- **Autoregressive LLM inference is fundamentally memory bandwidth-bound, not compute-bound.** Each decode step loads the full model weights to generate one token — meaning the bottleneck is HBM-to-compute data movement, not FLOPs. This single fact drives most of Chapter 9's techniques (KV-cache optimization, MQA/GQA, quantization for bandwidth not just memory, speculative decoding to convert decode to a prefill-shaped workload).
- **Prefill is compute-bound; decode is memory bandwidth-bound — and they should be physically separated on production inference servers.** Co-located prefill+decode causes resource contention degrading both TTFT and TPOT. [[DistServe]] (Zhong et al. 2024) shows disaggregation significantly improves request volume under latency SLOs; intermediate-state communication is acceptable on NVLink-class fabrics. The prefill-to-decode instance ratio is workload-dependent: **2:1–4:1 for long-input/TTFT-priority, 1:2–1:1 for short-input/TPOT-priority** (Meta Llama Inference talk).
- **`nvidia-smi`'s GPU utilization metric is misleading.** It measures *time spent actively processing* not *fraction of FLOP/s utilized*. **[[MFU]]** and **[[MBU]]** (introduced in the [[PaLM]] paper) are the metrics that matter. For training, MFU > 50% is good; Table 9-1: GPT-3 21.3% V100, PaLM 46.2% TPU v4.
- **An output token costs 2–4× an input token; a single output token = 100 input tokens in latency impact.** Anyscale (Kadous et al. 2023). This asymmetry is why the decoding bottleneck dominates all of Chapter 9's autoregressive-LLM work.
- **Speculative decoding can halve LLM response latency without changing quality.** DeepMind used a 4B draft model for Chinchilla-70B; draft model generated tokens 8× faster (1.8 ms vs 14.1 ms); overall response latency cut by > 50%. Implementable in **~50 lines of PyTorch**; integrated in vLLM, TensorRT-LLM, llama.cpp. Caveat: "if your MFU is already maxed out, speculative decoding makes less sense" — it works because decode has idle FLOPs available for free verification.
- **The KV cache can be larger than the model weights.** Pope et al. (2022): a 500B+ MHA model with batch=512, ctx=2048 has a 3 TB KV cache — **3× the model's weight size**. The KV cache scales linearly with sequence length × batch size × layers × model dim. This is the structural reason long-context LLMs are expensive to serve.
- **Character.AI cut KV cache > 20× via three stacked attention-mechanism redesigns.** MQA + interleaved local/global attention + cross-layer attention. The result: "memory is no longer a bottleneck for them for serving large batch sizes." Their average conversation has **180 messages** of dialogue history.
- **PagedAttention is the canonical KV-cache memory-management technique.** vLLM (Kwon et al. 2023) divides the KV cache into non-contiguous blocks, eliminating fragmentation and enabling cross-sequence memory sharing.
- **The four kernel-writing techniques are vectorization, parallelization, loop tiling, and operator fusion.** **[[FlashAttention]]** (Dao et al. 2022) was originally for A100; FlashAttention-3 (Shah et al. 2024) is Hopper-specific. **Kernels are tied to hardware** — new hardware needs new kernels.
- **Continuous batching (Orca, Yu et al. 2022) is the dominant batching strategy.** Static batching wastes the first request's latency on the last request's arrival; dynamic batching is better but still groups completion times; continuous (in-flight) batching admits new requests as old ones complete mid-batch.
- **Prompt caching delivers ~90% cost savings and ~75% latency savings on cacheable workloads.** Anthropic claims for 100K-token cached prompts: 11.5 s → 2.4 s TTFT (–79%, –90% cost). Google Gemini gives 75% discount on cached input tokens but charges $1/M tokens/hour for cache storage. Useful for: long system prompts, long-document chat, multi-turn conversations.
- **Pruning is the third compression family but rarely used in 2024.** Frankle & Carbin (2019) showed > 90% non-zero parameter reduction is sometimes possible without accuracy loss, but pruning is harder than quantization, gains are usually smaller, and not all hardware exploits sparsity.
- **Tensor parallelism is the most-impactful parallelism strategy for inference.** It reduces latency AND enables serving models too large for one GPU. Pipeline parallelism is generally avoided for strict-latency inference (extra inter-stage communication increases per-request latency); it's common in training for throughput. Replica parallelism is the easiest lever.
- **The most-impactful techniques across use cases: quantization, tensor parallelism, replica parallelism, attention-mechanism optimization.** Huyen's closing prescription. Choice depends on workload: long contexts → KV-cache management dominates; overlapping prompts / multi-turn → prompt caching dominates; latency-priority → replica parallelism scales out.
- **Inference cost can exceed training cost** (Desislavov et al. 2023) — inference accounts for **up to 90% of ML costs for deployed AI systems**. This is what justifies specialized inference accelerators (Apple Neural Engine, AWS Inferentia, Meta MTIA).
- **Electricity is becoming a bottleneck for scaling compute.** An H100 at peak draws ~7,000 kWh/year vs a US household's ~10,000 kWh/year. Data center locations are now constrained by electricity supply and geopolitics.

## Key Quotes

> "Computing the memory bandwidth being used for LLM inference is straightforward: parameter count × bytes/param × tokens/s." — Ch 9, the MBU formula

> "An experiment by Anyscale shows that 100 input tokens have approximately the same impact on the overall latency as a single output token." — Ch 9, footnote

> "Speculative decoding effectively turns the computation profile of decoding into that of prefilling." — Ch 9, on why speculative decoding works

> "We're close to the limit of quantization — we can't go lower than 1 bit per value." — Ch 9, on weight-only quantization

> "Across model API providers, an output token costs approximately two to four times an input token." — Ch 9

> "The KV cache size, on the other hand, grows linearly with sequence length." — Ch 9

> "[For a 500B+ MHA model with batch=512 and context=2048] the KV cache totals 3 TB. This is three times the size of that model's weights." — Ch 9, paraphrasing Pope et al. (2022)

> "It's like a bus that, after dropping off one passenger, can immediately pick up another passenger to maximize its occupancy rate." — Ch 9, on continuous batching

> "If your system prompt is 1,000 tokens, and your application generates one million model API calls daily, a prompt cache will save you from processing approximately one billion repetitive input tokens a day!" — Ch 9, on prompt caching

> "Across various use cases, the most impactful techniques are typically quantization (which generally works well across models), tensor parallelism (which both reduces latency and enables serving larger models), replica parallelism (which is relatively straightforward to implement), and attention mechanism optimization (which can significantly accelerate transformer models)." — Ch 9, closing prescription

## Concepts

### New (minted by this chapter)

- [[ComputeBound]] — workload class whose time-to-complete is determined by computation
- [[MemoryBandwidthBound]] — workload class whose time-to-complete is determined by memory data-transfer rate
- [[ArithmeticIntensity]] — FLOPs per byte of memory access; the roofline classifier
- [[RooflineModel]] — Williams et al. 2009 cost model for compute-bound vs memory-bandwidth-bound classification
- [[Goodput]] — requests/s that meet the SLO (TTFT/TPOT constraints), borrowed from networking
- [[MFU]] — Model FLOP/s Utilization (from PaLM paper); observed-throughput ÷ peak-FLOP/s
- [[MBU]] — Model Bandwidth Utilization; observed bandwidth ÷ peak bandwidth
- [[TBT]] — Time Between Tokens; LinkedIn's name for inter-token latency during streaming
- [[TimeToPublish]] — TTFT measured at the user-visible token (not the model-internal first token), useful for CoT / agentic queries
- [[AIAccelerator]] — chip designed for AI workloads (GPUs, TPUs, IPUs, LPUs, MTIA, Inferentia, etc.)
- [[ModelCompression]] — umbrella for quantization, distillation, pruning, low-rank factorization
- [[Pruning]] — zero out unimportant parameters or remove nodes; produces sparsity
- [[Sparsity]] — fraction of zero parameters; only exploitable by hardware that supports it
- [[InferenceWithReference]] — speculative decoding variant where draft tokens come from the input context (Yang et al. 2023)
- [[ParallelDecoding]] — break sequential decoding dependency by generating multiple future tokens simultaneously
- [[LookaheadDecoding]] — parallel decoding via the Jacobi method (Fu et al. 2024)
- [[JacobiDecoding]] — family name for Jacobi-method-based parallel decoding
- [[MedusaDecoding]] — multiple decoding heads with tree-based attention verification (Cai et al. 2024)
- [[CrossLayerAttention]] — share K/V vectors across adjacent transformer layers (Brandon et al. 2024)
- [[PrefillDecodeDisaggregation]] — assign prefill and decode to different GPUs (DistServe, Zhong et al. 2024)
- [[DistServe]] — the prefill/decode disaggregation paper
- [[PromptCaching]] — cache overlapping prompt segments (system prompts, long docs, conversation prefix); a.k.a. context cache / prefix cache (Gim et al. November 2023)
- [[StaticBatching]] — wait for full batch before processing (first request blocked by last)
- [[DynamicBatching]] — N-or-T-ms whichever first
- [[Batching]] — umbrella for batching strategies in inference servers
- [[ReplicaParallelism]] — multiple full copies of a model (data parallelism's inference name)
- [[ContextParallelism]] — split input sequence across devices
- [[SequenceParallelism]] — split per-input operators across devices
- [[InferencePerformanceMetrics]] — latency/throughput/utilization umbrella for Ch 9's metrics framework
- [[OperatorFusion]] — combine multiple operators into a single kernel pass (vs. memory-bound separate kernels)
- [[LoopTiling]] — reorder loop accesses to match hardware memory hierarchy
- [[Lowering]] — process of converting a high-level model script to hardware-specific code
- [[Compiler]] — generic concept page for ML compilers (TVM, MLIR, XLA, TensorRT, torch.compile)
- [[Triton]] — OpenAI's GPU kernel language
- [[ROCm]] — AMD's open-source CUDA alternative
- [[TVM]] — Apache TVM, standalone ML compiler
- [[MLIR]] — Multi-Level Intermediate Representation (compiler infrastructure)
- [[XLA]] — Accelerated Linear Algebra; originally TensorFlow; OpenXLA
- [[GoogleTPU]] — Tensor Processing Unit; Google's AI accelerator
- [[Inferentia]] — AWS inference accelerator
- [[MTIA]] — Meta Training and Inference Accelerator
- [[AppleNeuralEngine]] — Apple on-device AI accelerator
- [[ThermalDesignPower]] — TDP; proxy for accelerator power consumption
- [[PeakFLOPSHacking]] — Huyen's term for chip-maker benchmark gaming via sparsity/specific-shape conditions
- [[LowRankFactorization]] — model compression via low-rank approximation of weight matrices

### Existing (updated by this chapter)

- [[InferenceOptimization]] — promoted from Ch 1 stub to full three-level taxonomy
- [[Prefill]] / [[Decode]] — confirmed compute-bound vs memory-bandwidth-bound asymmetry; disaggregation discussion
- [[TTFT]] / [[TPOT]] — formal definitions, percentile guidance, time-to-publish refinement
- [[KVCache]] — formula, 3 TB Pope et al. number, scaling-bottleneck framing
- [[PagedAttention]] — confirmed as Ch 9's canonical KV-cache management technique
- [[SpeculativeDecoding]] — Chinchilla-70B numbers, "50 lines of PyTorch," idle-FLOP rationale
- [[Medusa]] — multi-head + tree attention; HGX H200 1.9× Llama 3.1 number
- [[multiqueryattention]] / [[GroupedQueryAttention]] — KV-cache reduction framing
- [[LocalAttention]] — windowed-attention KV-cache math (10× cut at window=1000 vs seq=10000)
- [[FlashAttention]] / [[FlashAttention2]] — operator-fusion exemplar; A100 vs H100 (FlashAttention-3)
- [[Quantization]] — Ch 9 framing as #1 most impactful technique; 1-bit floor
- [[knowledgedistillation]] — model-compression role
- [[ContinuousBatching]] — Orca (Yu et al. 2022) origin
- [[TensorParallelism]] / [[PipelineParallelism]] — Ch 9 verdict on inference vs training trade-offs
- [[MultiLoraServing]] — Ch 9's brief routing-table mention (referenced via prompt caching context)
- [[BatchInference]] / [[OnlineInference]] — Ch 9 contrast for FM batch APIs vs traditional ML
- [[GPU]] / [[HBM]] / [[SRAM]] — memory-hierarchy numbers reiterated
- [[NVLink]] — high-bandwidth interconnect enabling cheap prefill-decode communication
- [[CUDA]] — chapter mentions; ROCm and Triton are added as alternatives
- [[Vectorization]] / [[kernelfusion]] — Ch 9 names them as 2 of 4 kernel-writing techniques
- [[GPUUtilization]] — Ch 9's critique that this `nvidia-smi` metric is misleading
- [[FP8]] / [[BF16]] / [[FP16]] / [[INT4]] / [[INT8]] — H100 spec table values
- [[JacobiAlgorithm]] — used in Lookahead decoding for parallel decoding verification

## Entities

### New
- [[GoogleTPU]] — referenced as a Google accelerator; TPU v3 / v4 from PaLM table
- [[AMD]] — referenced as GPU competitor + ROCm vendor + Habana Gaudi context
- [[Cerebras]] — Wafer-Scale QPU + the model-quality-variation experiment cited
- [[Groq]] — Language Processing Unit (LPU)
- [[Graphcore]] — Intelligent Processing Unit (IPU)
- [[Inferentia]] — also concept; AWS inference accelerator
- [[MTIA]] — also concept; Meta inference accelerator

### Existing (updated)
- [[NVIDIA]] — Hopper H100 (FP8), Ampere A100, Blackwell numbers; "peak FLOP/s hacking" critique
- [[Apple]] — Neural Engine; on-device AI accelerator role
- [[OReilly]] — publisher
- [[ChipHuyen]] — author
- [[Anthropic]] — prompt-caching pricing source (Table 9-3)
- [[google|Google]] — Gemini prompt-caching pricing; TPU; Pope et al. paper; Edge TPU
- [[meta|Meta]] — Llama inference talk on prefill:decode ratio; MTIA
- [[LinkedIn]] — TBT metric; throughput/latency trade-off claim
- [[CharacterAI]] — > 20× KV cache reduction case study
- [[Anyscale]] — 100-input-tokens ≈ 1-output-token latency claim
- [[Databricks]] — Llama 2-70B MBU chart
- [[googledeepmind|DeepMind]] — Chen et al. 2023 speculative decoding for Chinchilla-70B
- [[openai|OpenAI]] — Triton language; batch API pricing
- [[PyTorch]] — Llama-7B optimization case study
- [[TensorRTLLM]] / [[vLLM]] — inference engines hosting these optimizations
- [[NoamShazeer]] — MQA paper author
- [[TriDao]] — FlashAttention author

## Connections

- [[ai-engineering-chip-huyen]] — parent book.
- [[ai-engineering-ch01-intro]] — defines [[InferenceOptimization]] / [[TTFT]] / [[TPOT]] which Ch 9 deepens.
- [[ai-engineering-ch02-foundation-models]] — defines [[Prefill]] / [[Decode]] / [[transformer|transformer]] / [[Attention]] / [[KVCache]] which Ch 9 builds on.
- [[ai-engineering-ch07-finetuning]] — [[Quantization]] / [[FP16]] / [[BF16]] / [[INT4]] depth; PEFT-and-multi-LoRA-serving context.
- [[ai-engineering-ch08-dataset-engineering]] — [[knowledgedistillation]] depth; the *other* model-compression family.
- [[leh-ch08-inference-optimization]] — LLM Engineer's Handbook's parallel treatment ([[PagedAttention]], [[ContinuousBatching]], [[SpeculativeDecoding]], [[StaticKVCache]]); strong corroborator.
- [[hands-on-llm-ch03-looking-inside-llms]] — pedagogical-level treatment of [[multiqueryattention]] / [[GroupedQueryAttention]] / [[LocalAttention]] / [[FlashAttention]] / [[KVCache]].
- [[2205.14135-flashattention]] — primary source for FlashAttention.

## Contradictions

- **MFU as a universally-positive metric (some industry framing) vs. Huyen's nuance.** Huyen explicitly cautions: "A higher utilization rate means nothing if the cost and latency both increase." Higher MFU/MBU on the *wrong workload* (e.g. by over-batching) can hurt user-facing latency. The wiki page for [[GPUUtilization]] should reflect this.
- **`nvidia-smi`'s "GPU utilization" metric.** Huyen's framing — "actively processing tasks doesn't mean doing so efficiently" — is in direct tension with the common practice of reporting `nvidia-smi`'s number as if it represented hardware efficiency. Not a wiki contradiction per se but a vocabulary trap to flag on [[GPUUtilization]].
- **No direct contradictions with earlier chapters.** Ch 9 is a deepening rather than a revision of Ch 1's [[InferenceOptimization]] framing, Ch 2's [[Prefill]] / [[Decode]] framing, Ch 7's [[Quantization]] framing.
- **Minor terminological tension with [[Latency]] (existing concept).** The existing page (from parallel-processing book) defines latency as "time for one bit to travel from source to destination." Ch 9's *user-facing* latency (TTFT + TPOT × output length) is a *higher-level* latency. Not a contradiction — just two scales of the same word. Worth a cross-reference.
