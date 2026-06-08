---
title: "Machine Learning Systems (mlsysbook Vol 1) — Ch 8: Model Training"
type: source
tags: [book, ml-systems, mlsysbook, training, distributed-training, parallelism, mixed-precision, flash-attention, gradient-checkpointing, optimizers, gpu, roofline, harvard]
date: 2026-06-05
sources: []
source_file: raw/mlsysbook-vol1/mlsysbook-ch08-model-training.qmd
last_updated: 2026-06-05
---

# Machine Learning Systems (mlsysbook Vol 1) — Ch 8: Model Training

## Summary

Chapter 8 of [[VijayJanapaReddi|Vijay Janapa Reddi]]'s open-access *Machine Learning Systems* (Vol 1, Harvard, mlsysbook.ai, 2026) is the **capstone of the "Build" part** (Ch 5–8): it treats training as a *systems* problem rather than an optimization-theory problem. The framing question — *"Why does training a model cost millions while running it costs pennies?"* — yields the chapter's organizing fact: a **million-to-one cost asymmetry** between learning and inference, driven by the forward+backward+optimizer-step cost multiplied across billions of examples. Running GPT-2 once costs a fraction of a cent; training it cost ~$50,000 in 2019. Training GPT-4 cost an estimated $100M. The chapter's unifying lens is the **[[IronLawOfTrainingPerformance|iron law of training performance]]** — $T_{\text{train}} = O / (R_{\text{peak}} \times \eta_{\text{hw}})$ — a specialization of the general [[IronLawOfMLSystems|iron law]] that maps every optimization to one of three levers: total operations $O$, peak throughput $R_{\text{peak}}$, or hardware utilization $\eta_{\text{hw}}$ (GPT-3 hit $\eta_{\text{hw}}\approx0.45$; modern systems target $>0.55$).

The chapter proceeds in five stages. (1) **Mathematical foundations**: FLOP counting for [[GEMM]]-dominated transformer layers, the [[Adam]]-optimizer **6× training-memory multiplier** over FP16 inference weights, [[ActivationMemory|activation memory]] that dwarfs parameters, and [[ArithmeticIntensity|arithmetic intensity]] + the [[RooflineModel|Roofline Model]] to classify ops as compute- vs memory-bound. (2) **Pipeline architecture**: training as a *staged system pipeline* (storage → CPU preprocessing → PCIe → accelerator → NVLink gradient sync) where any throughput mismatch creates **[[AcceleratorBubble|accelerator bubbles]]** and the min-of-three rule governs throughput. (3) **Bottleneck diagnosis** via **[[MFU|Model FLOPs Utilization]]** and the **[[DAMTaxonomy|D·A·M taxonomy]]** (Data/Algorithm/Machine). (4) **Four single-machine optimizations** — [[DataPrefetching|data prefetching]], [[MixedPrecisionTraining|mixed-precision training]], [[FlashAttention]], and [[GradientAccumulation|gradient accumulation]]+[[GradientCheckpointing|checkpointing]] — composed via a profile→select→compose→reprofile loop and demonstrated end-to-end on a GPT-2 walkthrough (12× memory cut). (5) **Scaling beyond one machine** — [[DataParallelism|data]], [[ModelParallelism|model]], [[PipelineParallelism|pipeline]], and [[TensorParallelism|tensor]] parallelism, the **communication tax**, and the *physical-ceiling* decision rule for when to distribute.

GPT-2 (1.5B) is the recurring **Lighthouse Model** ("large enough to need distributed training and memory tricks, small enough to reason about"), with [[ResNet|ResNet-50]] (compute-bound vision) and [[DLRM]] (memory-bandwidth-bound recommendation) as foils. The thesis throughout is **hardware-software co-design**: matrix-multiply patterns drove [[TensorCore|Tensor Cores]], which frameworks exposed via [[AutomaticMixedPrecision|AMP]] APIs, enabling FP16 training that shaped next-gen hardware — and **IO-aware algorithm design** (FlashAttention's tiling) delivers order-of-magnitude wins that no hardware scaling alone could.

## Key Claims

- **The million-to-one cost asymmetry is the gatekeeper of AI.** Each example needs a forward pass + a backward pass (~2× the forward cost) + an optimizer step touching every parameter; repeat across billions of examples × epochs × hyperparameter configs. A single GPT-2 forward pass is ~3×10⁹ FLOPs; full training ~10¹⁹ FLOPs. A lab that trains in 3 days iterates 10× faster than one taking a month — and compounding iteration speed dominates any single architectural insight.
- **The [[IronLawOfTrainingPerformance|iron law of training]]** $T_{\text{train}} = O/(R_{\text{peak}}\cdot\eta_{\text{hw}})$ holds when the pipeline is correctly staged (data movement overlapped via prefetch, communication absorbed by gradient overlap), leaving $\eta_{\text{hw}}$ the dominant lever. The theory-to-practice gap is typically **2–3×**. $\eta_{\text{hw}}$ is *not* fixed by hardware — memory-bandwidth saturation, kernel-launch overhead, and sync barriers each erode it independently, so diagnosis requires profiling not spec sheets.
- **[[Adam]] imposes a 6× training-memory multiplier.** A 7B-param model needs 14 GB (FP16 weights) + 14 GB (FP16 gradients) + 56 GB (FP32 Adam first+second moments) = **84 GB** before activations. This is *the* reason a model that infers on one GPU needs many GPUs to train. The optimizer-state escalation runs SGD (1×) → Momentum (2×) → RMSProp (2×) → Adam (3× param+state). **[[AdamW]]** decouples weight decay for better generalization at *zero* extra memory — the default for large transformers.
- **Adam buys convergence with memory.** GPT-2 XL converges in ~50K steps vs ~150K+ with SGD+Momentum — saving weeks despite higher per-step cost. Standard config: β₁=0.9, β₂=0.999, LR warmed 0→2.5e-4 over 500 steps then cosine decay, weight decay 0.01, global-norm gradient clipping at 1.0.
- **OOM, not slow compute, is the most common training failure.** Activation tensors from all $N_L$ layers accumulate during the forward pass and must coexist in GPU memory; they OOM *before the first gradient is computed*. GPT-2 needs >40 GB of activations at batch 8, exceeding a 32 GB V100. GPT-2's FP32 static state alone (~24 GB) nearly fills a V100 before activations.
- **The most common training failure is *misdiagnosed* — data-bound jobs look like hardware problems.** A 40% MFU run with idle GPU gaps is usually a serialized input pipeline (the "GIL-locked GPU"), not a slow GPU. Random-access data shuffling delivers only ~10% of sequential storage bandwidth ($F_{\text{access}}\approx0.1$).
- **[[ArithmeticIntensity|Arithmetic intensity]] (FLOPs/byte) classifies every op.** Dense [[GEMM]] is $\mathcal{O}(n)$ FLOP/byte (compute-bound); activation functions ~0.5, attention softmax ~5, LayerNorm ~10 FLOP/byte (all memory-bound). A100 ridge point ≈156 FLOP/byte (FP16), H100 higher. Materialized GPT-2-Small attention has intensity $d_{\text{head}}/2 = 32$ → memory-bound. **Optimizing activation compute yields near-zero wall-clock gain** because memory transfer, not arithmetic, dominates.
- **[[ReLU]] vs [[Sigmoid]] differ ~2–3× despite vastly different complexity** — both are memory-bandwidth-bound. ReLU runs at 95%+ of peak FLOP/s (single comparison, ~50% zeros enable sparsity), sigmoid only 30–40%. GPT-2's [[GELU]] is ~2–4× ReLU cost (erf), adding 10–20% to forward time; frameworks use the tanh approximation (~1.5× ReLU).
- **Batch size physics: bigger batches raise arithmetic intensity, moving ops from memory- to compute-bound.** Batch ≥256 hits >90% utilization; batch 16–32 only 60–70%. ResNet-50 critical batch ≈8,192; the **linear LR scaling rule** ($\eta \propto B$) holds only up to the critical batch. **[[WaveQuantization|Wave quantization]]**: an NVIDIA GPU executes 32-thread warps, so batch 33 launches a second 3%-utilized warp that takes as long as the first — batch 32 is faster than 33, and 64 is as fast as 33. Always use multiples of 32/64.
- **[[MFU|Model FLOPs Utilization]]** = useful model FLOPs / (peak rate × step time), counting only convergence-advancing FLOPs (excludes recomputation/padding). PaLM 540B reported **46.2% MFU** on 6,144 TPU v4 chips. Production runs hit 30–50%; the practical ceiling is 55–65% (achievable only with FlashAttention + tuned batch sizes). 100% MFU is impossible (weights must still load from DRAM).
- **The [[DAMTaxonomy|D·A·M taxonomy]] maps bottlenecks to fixes.** Compute-bound (Algorithm; util >90%) → FlashAttention/mixed precision/faster hardware. Memory-bound (Machine; util 50–80%, high bandwidth use) → operator fusion/memory-efficient attention/reduced precision. Data-bound (Data; periodic util→0, CPU busy) → prefetching/pipeline overlap/faster storage/DataLoader parallelism.
- **[[MixedPrecisionTraining|Mixed precision]] cuts memory ~50% and accelerates compute 2–3×.** Six-step cycle: FP32 master weights → cast FP16 → forward (FP16 loss) → scale loss → backprop (scaled FP16 grads) → copy to FP32 + unscale → update master. **[[LossScaling|Loss scaling]]** (2⁸–2¹⁴) prevents FP16 gradient underflow (FP16 floor 6.1×10⁻⁵; subnormals flush to zero). **[[BF16]]** matches FP32's 8-bit exponent range, eliminating loss scaling — the default for transformers (gradients span 10⁻¹⁰ to 10³). FP32 ops still required for loss accumulation, softmax denominators, normalization variance, optimizer state.
- **[[TensorCore|Tensor Cores]] do a 4×4 FP16 matmul-accumulate per cycle with an FP32 accumulator** (prevents catastrophic cancellation), 8–16× CUDA-core throughput — but inputs must align to multiples of 8/16 or most of the advantage is silently forfeited. A100 FP16/BF16 ≈ 16× FP32 peak. **[[FP8]]** (H100 Hopper) doubles again: E4M3 (precision, fwd weights/acts) + E5M2 (range, bwd grads), ~2× FP16. Cross-generation GPT-2 throughput: V100 18 samples/s (FP32) → 45 (FP16, 2.5×); A100 165 (BF16); H100 380 (FP8) ≈ 21× over V100-FP32.
- **[[FlashAttention]] is IO-aware, not compute-clever.** Standard attention materializes the $S{\times}S$ score matrix in HBM (4096-len, 16 heads = 4.0 GB just for scores); attention spends 70–80% of time waiting on memory. FlashAttention tiles Q/K/V into SRAM blocks (20+ TB/s, 10× HBM), uses **online softmax**, never materializes the full matrix → $\mathcal{O}(S^2)\to\mathcal{O}(S)$ memory, same $\mathcal{O}(S^2 d)$ FLOPs, **2–4× speedup**, and shifts attention from memory- to compute-bound on the roofline. [[FlashAttention2]] reaches 50–73% of A100 peak; FlashAttention-3 ~740 TFLOP/s (~75% peak) on H100 via FP8. Default above 512 tokens, mandatory above 2,048.
- **[[GradientAccumulation|Gradient accumulation]] simulates large batches by summing gradients over $k$ micro-batches before one optimizer step** — mathematically equivalent (gradients are additive). GPT-2 reaches effective batch 512 on 8 V100s (micro-batch 16 × 4 steps) instead of 32 GPUs; saves 75% of cluster cost. `no_sync()` fires AllReduce once per effective batch, cutting communication 75%. BERT-Large hit 99.5% of full-batch performance at effective batch 256 over 8 steps. Cost: ~8–15% wall-clock overhead from micro-batch serialization.
- **[[GradientCheckpointing|Activation checkpointing]]** stores activations at only $\sqrt{N_L}$ layers and recomputes the rest in the backward pass: $\mathcal{O}(N_L)\to\mathcal{O}(\sqrt{N_L})$ memory. GPT-2 (48 layers): ~7 checkpoints, peak ~14×A (vs 48×A), **71% memory savings for ~33% extra compute**. Selective checkpointing (checkpoint attention, skip cheap FFN/LayerNorm) hits 60–80% savings at 20–25% overhead. GPT-3 scales 1.3B→3.7B on V100s via checkpointing.
- **The GPT-2 walkthrough composes everything: 12× memory reduction** (FP32 baseline → AMP → checkpointing), bringing 1.5B params within a single V100. Cluster-level on 32 V100s: ~40% training-time reduction, ~40% energy reduction, proportional carbon cut. The "administrative tax" (gradients + optimizer state) is **4–6× model weights**; activations add another 10–50×.
- **Distributed training trades compute bottlenecks for communication bottlenecks (the "communication tax").** [[DataParallelism|Data parallelism]] replicates the model, splits the batch, syncs gradients via [[AllReduce]] (Ring AllReduce moves $2(N-1)/N$ × gradient per worker — nearly GPU-count-independent). [[ModelParallelism|Model parallelism]] partitions the model (needed when it exceeds GPU memory) but suffers 25–50% utilization from **pipeline bubbles**. [[PipelineParallelism]] (GPipe/PipeDream) microbatches to recover 70–90% utilization. [[TensorParallelism]] (Megatron-LM) splits individual matmuls/attention heads across GPUs. **Hybrid**: tensor parallel within a node (NVLink), pipeline across nodes in a rack, data parallel across racks.
- **[[NVLink]] is 10–50× faster than PCIe and inter-node Ethernet/InfiniBand** (NVLink up to ~900 GB/s on H100 vs 1.25–12.5 GB/s inter-node). The network becomes a wall when $t_{\text{comm}} > t_{\text{compute}}$; a 7B model on 8 GPUs incurs an AllReduce of ~1.75×14 GB. GPT-3 training across 1,024 V100s spent ~30–40% of wall-clock on inter-GPU communication.
- **Scale only when a single device hits one of three physical ceilings:** (1) memory exhaustion (70B FP16 weights ≈140 GB > A100/H100-SXM 80 GB), (2) wall-clock time (10²⁴ FLOPs ≈32 years on one H100 at perfect utilization), or (3) dataset scale (petabyte streaming exceeds single-node IO). Exhaust mixed precision → accumulation → checkpointing → pipeline optimization *first*.
- **The PaLM loss-spike war story**: the 540B run spiked ~20× despite gradient clipping; the fix was operational — restart from a checkpoint ~100 steps before the spike and skip ~200–500 batches. Large-scale stability is an operational problem (checkpoint cadence, loss-spike detection, BF16), not just an optimizer-theory one.

## Key Quotes

> "Why does training a model cost millions while running it costs pennies?" — chapter Purpose; the million-to-one asymmetry that "governs who can participate at all."

> "The most common training failure is out-of-memory (OOM) error, which is a memory management problem... the activation tensors from all $N_L$ layers accumulate during the forward pass and must coexist in GPU memory simultaneously, causing OOM before the first gradient is computed." — Training-systems definition, common pitfall

> "A frequent misconception is that $\eta_{\text{hw}}$ is fixed by hardware. System efficiency is a pipeline property... diagnosing which factor dominates requires profiling rather than reading hardware specs." — iron-law definition

> "An algorithm's runtime is determined not by FLOP count but by memory traffic." — the IO-aware algorithm design principle that FlashAttention exemplifies

> "Always choose batch sizes and hidden dimensions that are powers of two or multiples of 8/32/64 to avoid this 'quantization tax.' A batch of 32 is often faster than 33, and a batch of 64 is often just as fast as 33." — wave-quantization engineering rule

> "PaLM's 540-billion-parameter run reported 46.2 percent MFU on 6,144 TPU v4 chips—meaning over half the theoretical compute was lost to memory stalls, communication, and pipeline bubbles." — on MFU

> "Use data parallelism when the model fits in memory but training is too slow. Use model parallelism when the model is too big to fit in a single GPU's memory." — the data-vs-model-parallelism selection rule

> "This diagnostic discipline distinguishes engineers who solve problems from those who throw hardware at symptoms." — Summary, on internalizing the iron law

## Connections

- [[VijayJanapaReddi]] — author; Harvard, mlsysbook.ai Vol 1.
- [[mlsysbook-ch01-introduction]] — source of the general [[IronLawOfMLSystems|iron law]] this chapter specializes into the [[IronLawOfTrainingPerformance|iron law of training]].
- [[mlsysbook-ch05-neural-computation]] — established *what* neural ops compute; Ch 8 asks *what they cost*. Shares [[Backpropagation]], [[GradientDescent]], [[Adam]], activation functions.
- [[mlsysbook-ch06-network-architectures]] — the [[GEMM]]/convolution/attention computational primitives whose training cost Ch 8 quantifies.
- [[mlsysbook-ch07-ml-frameworks]] — the execution substrate (computational graphs, autodiff, hardware abstraction); the [[MemoryWall]] and [[DAMTaxonomy]] are inherited; reuses the same A100 reference GPU and Lighthouse Models.
- [[mlsysbook-ch04-data-engineering]] — the upstream data pipeline (Parquet/TFRecord/Arrow, partitioning, locality) whose throughput Ch 8's staged pipeline depends on.
- [[IronLawOfTrainingPerformance]] — the chapter's central organizing equation $T=O/(R_{\text{peak}}\cdot\eta_{\text{hw}})$.
- [[IronLawOfMLSystems]] — the parent law; this is its training specialization.
- [[MFU]] — the $\eta_{\text{hw}}$ term made concrete; PaLM benchmark.
- [[DAMTaxonomy]] — Data/Algorithm/Machine bottleneck classification applied to training.
- [[RooflineModel]] / [[ArithmeticIntensity]] — the diagnostic that classifies ops compute- vs memory-bound; ridge point shifts with precision.
- [[GEMM]] — the dominant training operation; Tensor Cores, cuBLAS, Strassen crossover.
- [[Adam]] / [[AdamW]] / [[SGD]] / [[StochasticGradientDescent]] / [[Momentum]] / [[RMSProp]] / [[GradientDescent]] / [[MiniBatchGradientDescent]] — the optimizer progression and its memory escalation.
- [[OptimizerState]] — the per-parameter moment tensors that triple memory.
- [[Backpropagation]] — the gradient-computation cost driver; reverse-mode AD (Linnainmaa, not textbook chain rule).
- [[ActivationMemory]] / [[ActivationCheckpointing]] / [[GradientCheckpointing]] — the activation-storage problem and its $\sqrt{N_L}$ rematerialization fix.
- [[MixedPrecisionTraining]] / [[AutomaticMixedPrecision]] / [[LossScaling]] — the precision optimization and its underflow safeguard.
- [[BF16]] / [[FP16]] / [[FP32]] / [[FP8]] — the numerical-format tiers; BF16 = transformer default, FP8 = Hopper.
- [[TensorCore]] — the hardware behind FP16/BF16/FP8 speedups; 4×4 MAC, alignment requirement.
- [[FlashAttention]] / [[FlashAttention2]] — IO-aware tiled attention; online softmax; the chapter's exemplar of memory-bound→compute-bound shifting.
- [[GradientAccumulation]] — large effective batches without large memory; cuts communication via `no_sync()`.
- [[DataPrefetching]] — overlapping data movement with compute to eliminate accelerator bubbles.
- [[AcceleratorBubble]] — idle silicon from pipeline-stage throughput mismatch.
- [[WaveQuantization]] — the 32-thread warp tail-effect "quantization tax."
- [[Warp]] — the GPU lockstep-execution unit underlying wave quantization.
- [[DataParallelism]] / [[ModelParallelism]] / [[PipelineParallelism]] / [[TensorParallelism]] / [[3DParallelism]] — the scaling strategies; "what do we replicate vs partition?"
- [[AllReduce]] / [[RingAllReduce]] — gradient synchronization; bandwidth-optimal $2(N-1)/N$ scaling.
- [[ZeRO]] — parameter/gradient/optimizer-state sharding (FSDP/ZeRO) for models that don't fit (referenced as the alternative to single-GPU INT4).
- [[DistributedTraining]] — the multi-node regime and its communication tax.
- [[NVLink]] / [[Infiniband]] — the interconnects whose bandwidth ratio determines parallelism feasibility.
- [[HBM]] / [[SRAM]] / [[MemoryHierarchy]] / [[MemoryWall]] — the bandwidth hierarchy FlashAttention and prefetching exploit.
- [[BatchSize]] / [[LearningRate]] / [[LearningRateScheduler]] / [[LearningRateWarmup]] — batch-size physics and the linear LR scaling rule.
- [[GELU]] / [[ReLU]] / [[Sigmoid]] / [[Softmax]] — activation systems trade-offs.
- [[Convexity]] — (loss-landscape framing: saddle points dominate over local minima at scale).
- [[GPT2]] — the recurring 1.5B-param Lighthouse Model.
- [[GPT3]] — 3.14×10²³ FLOPs; $\eta_{\text{hw}}\approx0.45$; checkpointing case.
- [[ResNet]] / [[DLRM]] — compute-bound vision vs memory-bandwidth-bound recommendation foils.
- [[GPU]] / [[GPUUtilization]] / [[CUBLAS]] / [[cuDNN]] — the dominant training hardware and its kernel libraries; A100 = reference GPU.
- [[NVIDIA]] — Tensor Cores, Volta/Ampere/Hopper, NVLink, Nsight profilers, DALI.
- [[GeoffreyHinton]] — RMSProp (Coursera Lecture 6e, never peer-reviewed).
- [[Horovod]] — overlapping computation with communication for gradient sync.
- [[GPipe]] / [[MegatronLM]] — pipeline-parallel and tensor-parallel pioneers.
- [[ai-engineering-ch09-inference-optimization]] — the inference-side sibling; shares MFU, mixed precision, the compute/memory-bound roofline framing (training vs inference cost asymmetry).
- [[dmls-ch07-model-deployment]] — the deployment-side counterpart (this chapter's trained artifact is what gets deployed/compressed there).

## Contradictions

- **No direct contradictions with prior mlsysbook chapters.** Ch 8 is a deepening: the [[IronLawOfMLSystems|iron law]] specializes Ch 1's, the [[DAMTaxonomy]] and [[MemoryWall]] reuse Ch 7's vocabulary, [[GEMM]]/attention primitives reuse Ch 6, and the GPT-2/ResNet/DLRM Lighthouse Models recur identically.
- **MFU definition reconciles with the [[MFU]] page.** The wiki's [[MFU]] page (from [[ai-engineering-ch09-inference-optimization|*AI Engineering*]]) defines MFU as a *throughput-ratio* for **inference** (observed tokens/s ÷ peak tokens/s). Ch 8 defines it for **training** as a *FLOP-ratio* (useful model FLOPs ÷ peak-rate FLOP budget, excluding recomputation/padding). Same PaLM provenance, same intent ($\eta_{\text{hw}}$ made concrete); treat MFU as a single metric with a training/inference framing split rather than two metrics.
- **Tensor Core peak speedup is an upper bound, not an end-to-end promise.** The 16× A100 FP16:FP32 *peak* ratio and "2–8×" Tensor-Core throughput figures are hardware ceilings; realized training speedup is smaller (~2–2.5× on V100) once data movement, non-Tensor-Core kernels, communication, loss scaling, and optimizer work are counted. Any wiki page citing a fixed mixed-precision speedup should treat it as workload-conditional.
- **FlashAttention benchmark numbers in the chapter are illustrative.** The chapter's per-call timing/memory table is explicitly "representative chapter numbers, not values reported verbatim by Dao et al." — the *systems pattern* (OOM→fits, 2–4× speedup, larger backward-pass gains) is the load-bearing claim, not the exact ms/GB figures.
