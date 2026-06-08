---
title: "Machine Learning Systems (mlsysbook Vol 1) — Ch 11: Hardware Acceleration"
type: source
tags: [book, ml-systems, mlsysbook, hardware, accelerators, gpu, tpu, npu, fpga, asic, systolic-array, memory-wall, roofline, dataflow, tensor-cores, hardware-software-codesign]
date: 2026-06-05
sources: []
source_file: raw/mlsysbook-vol1/mlsysbook-ch11-hardware-acceleration.qmd
last_updated: 2026-06-05
---

# Machine Learning Systems (mlsysbook Vol 1) — Ch 11: Hardware Acceleration

## Summary

Chapter 11 of [[VijayJanapaReddi|Vijay Janapa Reddi]]'s *Introduction to Machine Learning Systems* (Vol 1, [[Harvard]], mlsysbook.ai, 2026) is the **"M" (Machine) vertex of the [[DAMTaxonomy|D·A·M taxonomy]]** and the longest chapter in the book (~64k words). After Data was optimized (Ch 4) and the Algorithm compressed (Ch 10), this chapter explains how specialized silicon executes the surviving work. Its thesis is a single physical inversion: **arithmetic is nearly free while data movement is expensive** — fetching one value from DRAM costs ~100–1,000× the energy of a multiply-accumulate, and can exceed an INT8 op by >20,000×. Accelerators are therefore not primarily "faster at math"; they are architected to *hide, amortize, and minimize* data movement through deep memory hierarchies, massive parallelism, and specialized dataflows. The binding hardware-selection question is not "which chip is fastest?" but "which chip's memory system matches my model's access patterns?"

The chapter develops this level by level. It opens with **[[AmdahlsLaw|Amdahl's Law]] for AI** (the "acceleration wall": a 247× H100 advantage yields only ~5× speedup on memory-bound GPT-2 vs. ~18× on compute-bound ResNet-50) and the history of hardware specialization (Intel 8087 [[FPU]] → [[GPU|GPUs]] → [[DomainSpecificArchitecture|DSAs]]/[[GoogleTPU|TPUs]]) driven by the end of [[DennardScaling|Dennard scaling]] and the divergence of [[MooresLaw|Moore's Law]] from model demand (the "systems gap" widening ~3–4× per year). It then covers the **three [[ComputePrimitives|compute primitives]]** — vector (SIMD/SIMT), matrix ([[TensorCore|tensor cores]]/[[SystolicArray|systolic arrays]]), and [[SpecialFunctionUnit|special function units]] — plus N:M [[StructuredSparsity|structured sparsity]] and [[MixedPrecisionTraining|mixed precision]] numerics. The core of the chapter is the **AI [[MemoryWall|memory wall]]**: the Horowitz energy ladder (DRAM 640 pJ vs SRAM 5 pJ vs INT8-add 0.03 pJ), the bandwidth taper (HBM ≫ NVLink ≫ PCIe ≫ network), and the [[MemoryHierarchy|memory hierarchy]] (registers → SRAM → scratchpad → HBM → DRAM → flash). The **[[RooflineModel|Roofline Model]]** turns [[ArithmeticIntensity|arithmetic intensity]] into a diagnostic, and **[[HardwareMapping|hardware mapping]]** ([[WeightStationary|weight/output/input-stationary]] dataflow, [[KernelFusion|kernel fusion]], [[Tiling|tiling]], [[FlashAttention]]) into prescriptions. It closes with ML compilers ([[XLA]], [[TVM]], [[TensorRTLLM|TensorRT]], [[MLIR]]), multi-chip scaling, heterogeneous [[SystemOnChip|SoC]] design, fallacies/pitfalls, and a hardware-sustainability (carbon) argument.

## Key Claims

- **The energy inversion is the whole game.** A DRAM access costs ~100× a MAC and, per Horowitz et al., over 20,000× an INT8 op; the energy ladder is INT8-add 0.03 pJ, FP32-add 0.9 pJ, FP32-mult 3.7 pJ, SRAM-read 5 pJ, **DRAM-read 640 pJ** (~128× the SRAM access). This is why accelerators prioritize data locality over raw FLOP/s; it is the AI-era form of the **Von Neumann bottleneck** (since 1945; see [[VonNeumannArchitecture]]).
- **Hardware acceleration trades programmability for compute density.** An [[NVIDIA]] A100 delivers ~312 TFLOP/s FP16/BF16 vs. ~1–2 TFLOP/s for a server CPU — a ~150–300× gap — by dedicating 80+ billion transistors to arithmetic units rather than branch predictors, out-of-order schedulers, and large caches. But CPUs reach only **5–10% utilization** on ML workloads.
- **[[AmdahlsLaw|Amdahl's Law]] caps the gain.** Acceleration only speeds the parallelizable fraction $p$ (typically 90–99% of an ML workload). At $p=0.9$, even an infinitely fast accelerator gives ≤10× total speedup. Concretely on H100 (247× matmul advantage): ResNet-50 ($p=0.95$) → ~18× actual; GPT-2 ($p=0.80$, KV-cache/sampling/Python overhead) → ~5×, with a hard ceiling of $1/(1-p)=5×$. This is *why* LLM inference optimization targets the serial fraction (batching, speculative decoding) over raw silicon speed.
- **The 2015 [[GoogleTPU|TPU]] efficiency shock ended the general-purpose era.** Google projected in 2013 that a few minutes/day of voice search would *double its data-center footprint*; it designed, verified, built, and deployed TPUv1 in 15 months. TPUv1 was 15–30× faster on inference and 30–80× better perf/watt than the [[NVIDIA]] K80 — by stripping caches/branch-prediction/OOO logic to fill the die with a 256×256 INT8 [[SystolicArray|systolic array]].
- **The "systems gap" cannot be closed by waiting for faster chips.** GPU supply ("Huang's Law") grows ~1.7× per year; model demand grows ~6× per year (AlexNet → Transformer → GPT-3 → GPT-4), widening the gap ~3–4× annually. [[DennardScaling|Dennard scaling]] ended ~2005, creating "dark silicon" (only ~30–50% of transistors powerable at advanced nodes), which *forces* specialization.
- **The dominant operation is multiply-accumulate (MAC), >95% of execution time.** Regardless of layer type (FC, conv, attention), networks multiply inputs by weights and accumulate. Three primitives exploit this: **vector ops** (SIMD/SIMT, element-wise activations/pooling/embedding lookups), **matrix ops** ([[TensorCore|tensor cores]] processing 16×16 tiles per instruction = 256 MACs; ~512× faster than scalar on a 2048-token QK^T), and **[[SpecialFunctionUnit|special function units]]** (ReLU/sigmoid in 1–2 cycles, exp/log via lookup+interpolation in 2–4, sqrt via fixed-iteration Newton-Raphson in 4–8).
- **[[SystolicArray|Systolic arrays]] win on energy by reuse.** Kung & Leiserson (1979); the name is from cardiac *systole* ("contraction") — data pulses through the grid like blood. A naive vector unit needs 4 DRAM accesses/MAC (~641 pJ); a 128×128 systolic array amortizes 2 loads across 128 ops (~6 pJ), a **~107× energy advantage** — but only when the matrix is large enough to fill the array (small/real-time-inference matrices collapse back toward the vector baseline). A 128×128 array does >16,000 MACs/cycle; this lets a TPU pack 100,000+ MAC units without melting.
- **The tiling principle bridges graph and silicon.** A 4096-wide layer on a 128-wide systolic array decomposes into 1,024 tiles, each staged HBM→SRAM→array, achieving 128× reuse per loaded byte. If a dimension is not a multiple of the tile size (e.g. width 129 on a 128 array) the system pays a **"fringe tax"** — 127 units idle while one finishes the remainder tile.
- **N:M [[StructuredSparsity|structured sparsity]] beats unstructured because of memory regularity.** NVIDIA Sparse Tensor Cores implement **2:4** (exactly 2 nonzero per 4-element block, 50% density), chosen at the accuracy-performance knee: 1:4 loses accuracy unrecoverably, 3:4 compresses too little. Metadata is just 4 index bits per 4-block; effect is 2× FLOP/byte → theoretical 2× speedup. The principle: "hardware achieves efficiency not by computing zeros faster, but by *never loading them*."
- **Reduced precision attacks both sides of the roofline at once.** FP32→FP16 halves memory traffic *and* lets tensor cores/systolic arrays pack 2× more MAC units in the same area. INT8 needs ~30× less energy than FP32 per op. [[NVIDIA]] precision support evolved: Volta (FP16) → Turing (+INT8/4/1) → Ampere (+TF32/BF16/FP64). Mixed precision = FP16/BF16 matmul with FP32 accumulation; INT8 inference with select activations kept higher.
- **The [[RooflineModel|Roofline]] makes "compute-bound vs memory-bound" quantitative.** Hardware ridge point $\text{AI}_{\text{ridge}} = R_{\text{peak}}/\text{BW}$ has risen sharply: V100 ~140, A100 ~153, H100 ~295, B200 ~281 FLOP/byte. High-end accelerators are "Bandwidth-Hungry" (ridge 150–300); TinyML MCUs are "Compute-Starved" (ridge <10) — so an architecture efficient in the cloud can be "a disaster at the edge."
- **Batch size is the most accessible roofline lever.** For a dense $(B×M)×(M×N)$ layer, AI ≈ $B$. At M=N=2048 FP16: batch-1 → AI≈1 (memory-bound); batch-32 → ≈31; batch-256 → ≈205 (compute-bound on A100). This is *why* serving systems batch — at the cost of queueing latency.
- **The GPT-2 batch-1 throughput ceiling: <1% utilization.** GPT-2 XL (1.5B params) must reload all ~3 GB of weights per token; AI ≈ 1 FLOP/byte ≪ A100 ridge (~153). Maximum throughput ≈ AI × bandwidth ≈ a few TFLOP/s, ~1% of the A100's ~312 TFLOP/s peak. A $15,000 GPU runs LLM inference at <1% efficiency — the "utilization gap" that drives KV-caching and quantization.
- **The bandwidth taper governs the single machine.** On an H100 node: HBM3 ~3.3 TB/s ≫ NVLink 4.0 ~900 GB/s ≫ PCIe Gen5 ~64 GB/s ≫ network (InfiniBand NDR) ~50 GB/s. The ~50× HBM/PCIe gap means any CPU transfer is "a catastrophic performance event"; [[NVLink]] is the only way to scale across 1–8 GPUs without hitting the "PCIe wall." [[DMA]] engines overlap transfer with compute (without it, throughput drops 20–40%).
- **[[KernelFusion|Kernel fusion]] and [[Tiling|tiling]] are the memory-bound prescriptions.** Fusing ReLU+BatchNorm+scale on a 1024×1024 FP32 tensor cuts the footprint 4× (16.8 MB → 4.2 MB) by keeping intermediates in registers; tiling cuts a naive $\mathcal{O}(N^3)$-access matmul to one fetch per tile (10–50× GEMM speedup). [[FlashAttention]] (Dao 2022) tiles attention along the sequence to avoid materializing the $S×S$ matrix in HBM. By intensity regime: very-low AI (<2, LayerNorm/activations) needs *mandatory* fusion (up to 10× via fused LayerNorm+GELU); high AI (>200) just maximizes tensor-core occupancy (90–95% of peak).
- **Architecture is hard-coded by the stationary-operand choice.** Weight-stationary (early [[GoogleTPU|TPUs]]) → CNNs with reused filters; output-stationary (partial sums in accumulators) → large-batch GEMM; input/row-stationary ([[Eyeriss]]) → general matmul reuse. "There is no 'perfect' accelerator." Per-workload memory profiles: MLP (large dense weights, low reuse, bandwidth-bound), CNN (small reused filters, high spatial reuse), Transformer (large weights + KV-cache, capacity+bandwidth-bound).
- **AI processor configurations diverge by deployment context.** A100: 1024-bit SIMD, 4×4×4 FP16 tensor cores, 108 SMs (training); TPUv4: 128-wide, 128×128 BF16 systolic array, 2 cores/chip (training); Intel Sapphire Rapids: 512-bit AVX + AMX 32×32 INT8/BF16, 56 cores (inference); [[Apple]] M1: 128-bit NEON, 16×16 FP16, 16 Neural Engine cores (mobile). H100 has >16,000 streaming processors and >500 tensor cores; [[Cerebras]] CS-2 has ~850,000 wafer-scale cores; [[Graphcore]] IPU has 1,472 tiles.
- **The Tensor Core is a "brittle contract."** On A100, tensor cores only trigger for FP16/BF16/TF32 with aligned tile shapes (multiples of 8/16); forcing unsupported FP32 accumulation falls back to CUDA cores at **1/16th throughput**. "Hardware features are brittle contracts."
- **[[FPGA|FPGAs]] and [[ASIC|ASICs]] sit at the flexibility extremes.** ASICs improve perf/watt by $10^3$–$10^5×$ (blockchain hashing, genomics) but are totally inflexible. FPGAs are reconfigurable after manufacture (good for evolving ML architectures) but require Verilog/VHDL and hours-long compiles. RISC-V's open ISA lets teams add custom ML instructions but lacks the cuDNN/TensorRT software stack.
- **[[CUDA]] is a software moat, not just silicon.** The cuBLAS/cuDNN/TensorRT ecosystem locks the training stack to NVIDIA; migrating requires rewriting thousands of optimized kernels — "this software lock-in, not raw silicon performance, is the primary reason NVIDIA dominates."
- **Heterogeneous [[SystemOnChip|SoC]] design is a coordination problem.** A mobile object-detection pipeline splits MobileNet backbone → NPU, NMS (irregular branching) → CPU, display overlay → GPU; the assignment shifts dynamically with battery, thermal state, and contention. NPUs give 10–100× energy efficiency *only* for supported operators — unsupported ops "fall back" and negate the advantage. Coordinated DVFS and thermal-throttling-via-migration manage the 3–7 W envelope; automotive ([[Qualcomm]] Snapdragon Ride) adds hard real-time + functional safety + V2X.
- **Sustainability is an engineering metric.** Specialized [[NeuralProcessingUnit|NPU]] silicon is far more energy-efficient per op than CPU inference; at fleet scale this compounds into substantial annual CO₂ reductions. "The same architectural principles that maximize performance per watt also minimize carbon per inference."

## Key Quotes

> "Arithmetic is nearly free while memory access is expensive. In the time it takes to fetch a single value from main memory, a processor could perform thousands of calculations." — Purpose, on the memory wall as a consequence of physics, not an engineering gap awaiting a fix

> "If data loading takes 10 percent of the time ($p=0.9$), even an *infinite speed* accelerator can only achieve a 10× total speedup." — on [[AmdahlsLaw|Amdahl's Law]] as the acceleration ceiling

> "Hardware acceleration becomes mandatory when a single workload crosses a fleet-level economic threshold." — the TPU "capacity cliff" war story (voice search would double Google's data centers)

> "Hardware achieves efficiency not by computing zeros faster, but by *never loading them in the first place*." — the 2:4 [[StructuredSparsity|structured-sparsity]] principle connecting sparsity to the memory wall

> "Data *cannot* be fetched from DRAM in a single cycle. It is physically impossible… The 'memory wall' is partially a *distance wall*." — the speed-of-light limit (20 mm at ~0.5c ≈ 130 ps vs. a 500 ps clock cycle)

> "Hardware features are brittle contracts. If the workload does not present supported data types and tile shapes, the accelerator falls back to generic execution." — the Tensor Core contract (FP32 fallback at 1/16th throughput)

> "This software lock-in, not raw silicon performance, is the primary reason NVIDIA dominates AI training infrastructure." — on the [[CUDA]] / cuBLAS / cuDNN / TensorRT moat

> "Effective hardware selection requires matching workload arithmetic intensity to architectural ridge points, not assuming specialization always wins." — Fallacy #1, against "more specialized hardware always wins"

> "Real-world performance equals Peak FLOP/s × Utilization." — Fallacy #3; an A100's ~312 TFLOP/s FP16 yields only ~120–180 (transformer training) or 10–30 (recsys) sustained

## Connections

- [[VijayJanapaReddi]] / [[Harvard]] — author and institution of *Introduction to Machine Learning Systems* (Vol 1, mlsysbook.ai); this is Ch 11, the "M" of the [[DAMTaxonomy|D·A·M taxonomy]] and the longest chapter.
- [[DAMTaxonomy]] — Ch 11 is the **Machine** vertex (Data = Ch 4, Algorithm/compression = Ch 10).
- [[IronLawOfMLSystems]] — acceleration raises $R_{\text{peak}}$, $\eta_{\text{hw}}$, and BW in the iron-law decomposition $T = D_{\text{vol}}/\text{BW} + O/(R_{\text{peak}}\eta_{\text{hw}}) + L_{\text{lat}}$.
- [[RooflineModel]] — the central diagnostic; ridge points V100 ~140, A100 ~153, H100 ~295, B200 ~281 FLOP/byte; optimization-by-intensity-regime; batch-size lever; GPT-2 <1% ceiling.
- [[ArithmeticIntensity]] — FLOP/byte; <10 = memory-bound (attention), >200 = compute-bound (high-reuse conv); AI ≈ batch size for dense layers.
- [[MemoryWall]] / [[VonNeumannArchitecture]] — the dominant constraint; Horowitz energy ladder; DRAM 640 pJ vs SRAM 5 pJ; "distance wall."
- [[MemoryHierarchy]] — registers → L1/L2 SRAM → scratchpad → HBM → DRAM → flash; each step ~10× latency for ~10× capacity; the "life of a tensor" KWS journey.
- [[HBM]] — high-bandwidth memory at 2–3 TB/s via 3D die stacking + TSVs; the dominant cost component of data-center accelerators; the bandwidth taper's top tier.
- [[SystolicArray]] — Kung & Leiserson 1979; TPUv4 128×128 BF16 array; ~107× energy advantage via operand reuse; the tiling/fringe-tax principle.
- [[TensorCore]] — 16×16 tile MMA per instruction; brittle-contract alignment (multiples of 8/16); sparse 2:4 variant; precision evolution Volta→Blackwell.
- [[GEMM]] — the workhorse primitive (90–95% of training time); cuBLAS/oneDNN reach 80–95% of peak; modern accelerators are "specialized GEMM engines."
- [[ComputePrimitives]] / [[VectorProcessor]] / [[SIMD]] / [[SIMT]] — vector (Cray-1 lineage), matrix, and special-function primitives; SIMD→SIMT evolution; warps, occupancy, divergence.
- [[SpecialFunctionUnit]] — dedicated ReLU/sigmoid/exp/sqrt circuits (1–8 cycle latencies) replacing pipeline-stalling software paths.
- [[StreamingMultiprocessor]] — the SIMT engine; occupancy determines whether the GPU is memory-bound or hits peak.
- [[CUDA]] — the SIMT programming model + ecosystem moat (cuBLAS/cuDNN/TensorRT).
- [[GPU]] — GeForce 256 (1999, hardware T&L) → AlexNet (2012, 2× GTX 580) → tensor-core era (~1,000× in a decade: K20X 3.9 TFLOP/s → H100 ~4,000 → B200 ~9,000).
- [[GoogleTPU]] — the canonical DSA; TPUv1 (2015) shock; TPUv4 128×128 systolic array, HBM2; "the secret to high performance" via BF16 + on-chip reuse.
- [[NeuralProcessingUnit]] — mobile inference blocks; 10–100× energy efficiency for supported ops; operator-fallback risk; Ethos-U micro-NPU at MCU scale.
- [[FPGA]] — reconfigurable (Verilog/VHDL); good for evolving architectures, hours-long compiles.
- [[ASIC]] — single-algorithm silicon; $10^3$–$10^5×$ perf/watt but inflexible (blockchain, genomics).
- [[DomainSpecificArchitecture]] — Hennessy/Patterson 2017 Turing Lecture; needs ≥10× efficiency to justify ecosystem cost.
- [[HardwareSoftwareCodesign]] — the chapter's recurring principle; INT8 pays off only because Tensor Cores were co-designed for it; a continuous feedback loop (FP16 → TF32/INT8 → 2:4 sparsity).
- [[FPU]] — the 8087/486DX floating-point coprocessor that began the recurring "specialize-then-integrate" cycle (FPU → GPUs → codecs → AI accelerators).
- [[DennardScaling]] / [[MooresLaw]] — their breakdown forced the shift to architecture; "systems gap" / "twin S-curves"; "dark silicon."
- [[AmdahlsLaw]] — the acceleration wall; ResNet ~18× vs GPT-2 ~5× on H100; also the multi-chip scaling ceiling (gradient-sync serial fraction).
- [[MixedPrecisionTraining]] / [[FP16]] / [[BF16]] / [[FP8]] / [[INT8]] / [[FloatingPoint]] — precision as a hardware design parameter; FP32 accumulation; FP4 on Blackwell.
- [[StructuredSparsity]] / [[Sparsity]] — N:M (2:4) pattern; CSR/BSR storage; why structure (not just zeros) enables hardware speedup.
- [[KernelFusion]] — eliminates intermediate HBM writes; 2–10× on memory-bound ops; register-pressure trade-off.
- [[Tiling]] / [[LoopTiling]] — spatial vs temporal vs hybrid; staging HBM→SRAM; tile-size/fringe-tax trade-offs.
- [[FlashAttention]] — the canonical fused, sequence-tiled attention kernel that avoids materializing the $S×S$ matrix in HBM.
- [[KVCache]] — the transformer memory-pressure driver; quadratic $S×S$ attention; activation-stationary mapping.
- [[HardwareMapping]] / [[WeightStationary]] / [[OutputStationary]] — binding the computation graph to hardware (placement, allocation, dataflow scheduling); the three stationary strategies; per-architecture (CNN/Transformer/MLP) priorities; hybrid mapping.
- [[NVLink]] / [[PCIe]] / [[DMA]] — the intra-node bandwidth taper; the "PCIe wall"; AllReduce/RDMA for multi-GPU scaling.
- [[SystemOnChip]] — heterogeneous mobile/automotive SoCs; CPU+GPU+DSP+NPU coordination; DVFS, thermal throttling, V2X.
- [[XLA]] / [[TVM]] / [[TensorRTLLM]] / [[MLIR]] — the ML compilers that automate mapping (graph optimization → kernel selection → memory planning → scheduling); ResNet-50 47 ms → 8 ms.
- [[Quantization]] — Ch 10's compression lever, here justified by hardware (4× memory-traffic cut transforms bandwidth-bound into compute-bound).
- [[NVIDIA]] — A100/H100/B200, Tensor Cores, K80, Volta→Blackwell, NVLink, the CUDA moat.
- [[Google]] — TPUv1–v4, XLA, the voice-search capacity cliff.
- [[Apple]] — M1 Neural Engine (16×16 FP16, 16 cores), mobile-inference priority.
- [[Intel]] — 8087/486DX FPU history, Sapphire Rapids AMX, IXP2800, Gaudi 2.
- [[AMD]] — MI300X/MI325X bandwidth (5.3–6 TB/s), RDNA SIMT, Infinity Fabric.
- [[Tesla]] — D1 processor (large local memory for autonomous-vehicle workloads).
- [[Cerebras]] — CS-2 wafer-scale (~850,000 cores).
- [[Graphcore]] — IPU (1,472 tiles, fine-grained parallelism, dynamic per-layer mapping).
- [[Eyeriss]] — pioneering row-stationary CNN dataflow accelerator (Chen 2016).
- [[Qualcomm]] — Snapdragon AI Engine (CPU/GPU/DSP/NPU heterogeneity); Snapdragon Ride automotive platform.

## Contradictions

- **No direct contradictions with sibling mlsysbook chapters.** Ch 11 extends and grounds concepts introduced earlier: [[RooflineModel]] and [[ArithmeticIntensity]] (Chs 2/5/6/8), [[SystolicArray]] (Ch 6), [[MemoryWall]] (Chs 1/2/5/7), [[GEMM]] (Chs 5/7), and the [[DAMTaxonomy]]. It is the deepest single treatment of hardware in the book and supersedes the brief earlier mentions in detail, not in claim.
- **"More specialized hardware always wins" is explicitly debunked.** The chapter's own Fallacy #1 pushes back on naive specialization rhetoric: an A100's ~312 TFLOP/s peak is irrelevant for a softmax at AI 2–5 (~3% utilization), and irregular/small-batch/dynamic-graph workloads can run better on flexible CPUs. Reconcile by treating "specialization wins" as **arithmetic-intensity-dependent**, gated by the [[RooflineModel|ridge point]].
- **Peak FLOP/s vs sustained throughput.** Vendor peak numbers (and some wiki [[GPU]]/[[NVIDIA]] pages) imply headline FLOP/s predicts performance; this chapter insists real performance = Peak × Utilization, with transformer training at 40–60% and recsys at 3–10% of A100 peak. Also flags the precision pitfall: quoting FP32 peak (~67 TFLOP/s H100) for a BF16 workload (~1,000 TFLOP/s) misclassifies kernels on the wrong roofline.
- **Batch-prediction economics vs. [[BatchInference]] framing elsewhere.** Where [[dmls-ch07-model-deployment|DMLS Ch 7]] frames batching as a serving-architecture choice, Ch 11 reframes it as a *roofline lever* — batch size directly sets arithmetic intensity (AI ≈ B), moving memory-bound dense layers into the compute-bound regime. Complementary, not conflicting: serving latency (queueing) is the cost the hardware view abstracts away.
