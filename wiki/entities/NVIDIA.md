---
title: "NVIDIA"
type: entity
tags: [company, hardware, gpu]
sources: [d2l-installation, d2l-builders-guide, 2205.14135-flashattention, d2l-computational-performance, parproc-ch05-cuda-gpu-programming, ai-engineering-ch01-intro, ai-engineering-ch02-foundation-models, ai-engineering-ch08-dataset-engineering, ai-engineering-ch09-inference-optimization, mlsysbook-ch07-ml-frameworks, mlsysbook-ch10-model-compression, mlsysbook-ch11-hardware-acceleration, mlsysbook-ch13-model-serving, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# NVIDIA

Santa Clara-headquartered semiconductor company; designer and vendor of essentially all GPUs that train modern deep-learning models. Its [[CUDA]] platform (released 2007) is the *de facto* GPU programming substrate for [[PyTorch]] / [[TensorFlow]] / [[JAX]] / [[MXNet]] and the kernels beneath [[FlashAttention]], [[BERT]] / [[1706.03762-attention-is-all-you-need|Transformers]], and every frontier LLM training run.

## In D2L

- **[[d2l-installation]]** — the install runbook tells readers to "download the NVIDIA driver and [[CUDA]]" before installing any GPU-enabled framework wheel; `nvidia-smi` queries driver / GPU state.
- **[[d2l-builders-guide]]** — `nvidia-smi` is the canonical "view graphics card information" command (`use-gpu.md`); `torch.device('cuda:i')` references NVIDIA cards specifically.
- **[[2205.14135-flashattention]]** — uses NVIDIA A100 / H100 SRAM-HBM hierarchy as the cost model ([[gpumemoryhierarchy]]).

## Hardware lineage relevant to DL

| Architecture | Card | Year | Highlight |
|---|---|---|---|
| Tesla (1st-gen unified-shader) | G80 / GT200 | 2006–2008 | First CUDA arch — Matloff's [[parproc-ch05-cuda-gpu-programming|Ch5]] baseline |
| Fermi | GF100 | 2010 | First true L1 cache ([[TrueCaching]]) |
| Kepler / Maxwell | GK / GM | 2012–2014 | Dynamic parallelism, 32-thread warp persists |
| Pascal | P100 | 2016 | Hardware-assisted [[UnifiedMemory]] via page tables |
| Volta | V100 | 2017 | First Tensor Cores |
| Ampere | A100 | 2020 | 40/80 GB HBM2e, bf16 |
| Hopper | H100 | 2022 | FP8, Transformer Engine |
| Blackwell | B200 / GB200 | 2024–2025 | NVLink fabric, FP4 |

## Ch5 ParProcBook coverage

[[parproc-ch05-cuda-gpu-programming]] is a chapter-length introduction to [[CUDA]] on NVIDIA hardware at the Tesla baseline: SM/SP hierarchy, [[Warp|32-thread warps]] under [[SIMT]] lockstep, the four-tier memory model ([[SharedMemory|shared]] / [[GlobalMemory|global]] / [[ConstantMemory|constant]] / [[TextureMemory|texture]]), [[ThreadDivergence|thread divergence]] as the within-warp performance killer, intra-block `__syncthreads()` vs inter-block atomic operations or host-roundtrip synchronization, [[MemoryCoalescing|coalescing]] of half-warp consecutive-word accesses, and pointers to [[CUBLAS]] / [[CUFFT]] / [[Thrust]].

## Connections

- [[CUDA]] — its parallel-computing platform.
- [[GPU]] — the hardware category it dominates.
- [[NvidiaTriton]] — NVIDIA's open-source inference server.
- [[gpumemoryhierarchy]] — NVIDIA A100 reference table.
- [[FlashAttention]] — exploits NVIDIA SRAM/HBM asymmetry.
- [[PyTorch]] / [[TensorFlow]] / [[JAX]] / [[MXNet]] — all ship CUDA-targeted wheels.
- [[d2l-builders-guide]] / [[d2l-installation]] — operational mentions.
- [[mlsysbook-ch14-ml-operations]] — Ch 14 lists NVIDIA's TensorRT (NVIDIA-only peak throughput) and Triton Inference Server among model-optimization and serving frameworks.


## From [[ai-engineering-ch01-intro|AI Engineering Ch 1]]

[[ChipHuyen|Chip Huyen]] in *AI Engineering* Ch 1 cites NVIDIA in two distinct roles:

- **CEO commentary on AI displacing programmers.** [[JensenHuang|Jensen Huang]] is quoted predicting AI will replace human software engineers and that *"we should stop saying kids should learn to code."* Ch 1 pairs this with [[MattGarman|Matt Garman's]] (AWS CEO) similar prediction.
- **3D-NPC demo partner.** NVIDIA's demos of [[Convai]] and [[Inworld]] are Ch 1's canonical industry references for AI-powered smart NPCs in games and immersive media — the 3D/embodied [[AIInterface|AI interface]] category.
- **GPU substrate for foundation models.** Implicit throughout — the *"there's more need for engineers who know how to work with GPUs and big clusters"* observation, and the Fortune-500 head-of-AI quote about teams that *"know how to work with 10 GPUs, but they don't know how to work with 1,000 GPUs"*, point at the NVIDIA-dominated infrastructure layer of the [[AIEngineeringStack|AI engineering stack]]. [[ChipHuyen]] previously worked at NVIDIA.

Huyen ([[ChipHuyen]]) previously worked at NVIDIA before turning to authoring.

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

Ch 2 supplies the **hardware/cost calibration** that anchors the chapter's compute-budgeting examples:

- **NVIDIA H100 NVL** delivers up to **60 TeraFLOP/s** = 6 × 10¹³ [[FLOPs|FLOPs]]/sec ≈ **5.2 × 10¹⁸ FLOPs/day** (measured in FP32).
- **H100 cloud pricing** at the time of writing: ≈$2–$5 per hour. *"As compute is getting rapidly cheaper, this number will get much lower."*
- **Worked GPT-3 training cost**: 256 H100s × 24h × 256 days / 70% utilization × $2/h ≈ **$4.14M and ≈236 days**.

Plus **[[BioNeMo]]** — NVIDIA's biomolecular foundation-model platform for drug discovery, one of three biomedical [[DomainSpecificModel|domain-specific FMs]] named in Ch 2.

## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

NVIDIA features in Ch 8 in two roles:

### 1. [[Nemotron4|Nemotron-4 340B]] — the chapter's headline synthetic-data case study

- **98% synthetic data** in instruction + preference finetuning (NVIDIA 2024).
- **Reverse-direction distillation**: teacher [[Mixtral8x7B|Mixtral-8x7B-Instruct-v0.1]] (~56B params MoE) trained student Nemotron-4-340B (340B dense) — and the student **exceeded the teacher**. Disproves the "teacher ≥ student" framing of [[knowledgedistillation|distillation]].
- Per Adler et al. 2024 (the Nemotron paper), NVIDIA engineered for **task diversity, topic diversity, and instruction diversity** as orthogonal axes — discussed under [[DataDiversity]].

### 2. The [[FirstPositionBias|first-position-bias]] mitigation for synthetic preference data

NVIDIA's preference-data pipeline:

> "NVIDIA researchers asked the AI judge twice, once with the response order swapped. They picked a valid (prompt, winning, losing) triplet only when the AI judge picked the same winner both times."

This is Ch 8's canonical example of how to mitigate AI-judge bias when curating synthetic preference data — applicable to any team using LLM-as-judge for preference labeling.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 features NVIDIA in multiple roles:

### As economic dominant

> *"The dominant type of AI accelerator is GPUs, and the biggest economic driver during the AI boom in the early 2020s is undoubtedly NVIDIA."*

### H100 SXM FLOP/s spec (Table 9-2)

| Precision | TFLOP/s (with sparsity) |
|---|---|
| TF32 Tensor Core | 989 |
| BFLOAT16 Tensor Core | 1,979 |
| FP16 Tensor Core | 1,979 |
| FP8 Tensor Core | **3,958** |

### nvidia-smi critique

Ch 9 calls out `nvidia-smi`'s GPU utilization metric as misleading and introduces [[MFU]] / [[MBU]] as the metrics that actually matter. See [[GPUUtilization]] for the full critique.

### Peak FLOP/s hacking

> *"Chip makers might also be doing what I call peak FLOP/s hacking. This might run experiments in certain conditions, such as using sparse matrices with specific shapes, to increase their peak FLOP/s."* — Ch 9

NVIDIA is the primary target of this critique — the "with sparsity" numbers in the H100 spec table are emblematic. See [[PeakFLOPSHacking]].

### Power consumption

- **H100 at peak: ~7,000 kWh/year**.
- Average US household: ~10,000 kWh/year.
- One H100 ≈ 70% of a household's electricity.

### ITL terminology

> *"Inter-token latency (ITL) is used by NVIDIA."* — Ch 9

The NVIDIA-side name for what LinkedIn calls [[TBT|TBT (time between tokens)]].

### Medusa on HGX H200

> *"NVIDIA claimed Medusa helped boost Llama 3.1 token generation by up to 1.9× on their HGX H200 GPUs (Eassa et al., 2024)."*

### Hardware lineage covered

- A100 (Ampere) — original [[FlashAttention]] target.
- H100 (Hopper) — FP8, FlashAttention-3 target.
- H200 — extended-memory H100 variant; Medusa Llama 3.1 benchmark.
- Blackwell (B200) — FP4 era.

### Inference-side hardware

- **Jetson Xavier** — named as an edge-inference chip example.

## From [[mlsysbook-ch07-ml-frameworks|mlsysbook Vol 1 Ch 7]]

Ch 7 anchors nearly every quantitative claim on the **A100** (312 TFLOP/s FP16, 2.04 TB/s HBM, 80 GiB, ~153 FLOP/byte ridge point). NVIDIA's software stack pervades the framework→hardware path: [[CUDA]] (2007) as the parallel-computing substrate (each `torch.matmul` traverses the dispatcher → [[CUBLAS|cuBLAS]] kernel → launch, costing 5–20 μs overhead), [[cuDNN]] for DL backward kernels, [[Triton]]→[[PTX]] as [[TorchInductor]]'s codegen target, [[TensorCore|Tensor Cores]] for FP16 [[MixedPrecisionTraining|mixed-precision]], [[NVLink]] (~600 GB/s, ~10× PCIe) for tensor parallelism, [[TensorRTLLM|TensorRT]] as the inference compiler (often 1.5–2× over TorchInductor), and Nsight Systems/Compute as the profilers.

## From [[mlsysbook-ch10-model-compression|mlsysbook Vol 1 Ch 10]]

Ch 10's compression hardware grounds in NVIDIA silicon: the **A100 (2020)** introduced **[[NMSparsity|2:4 structured sparsity]]** and the [[SparseTensorCore|Sparse Tensor Core]] path (up to 2× over dense when the pattern matches); INT8 Tensor Cores give ~2× peak throughput over FP16 (~624 TOPS vs ~312 TFLOP/s). cuSPARSE supports block-sparse storage, TensorRT's default calibration is the **Entropy** method, and Hopper FP8 units extend the energy-dividend story to even lower precision.

## From [[mlsysbook-ch11-hardware-acceleration|mlsysbook Vol 1 Ch 11]]

Ch 11 anchors the hardware-acceleration chapter on NVIDIA silicon and ecosystem: GPU performance rose ~1,000× in a decade (K20X 3.9 TFLOP/s FP32 → H100 ~4,000 → B200 ~9,000 TFLOP/s FP8); the precision evolution Volta(FP16)→Turing(+INT8/4/1)→Ampere(+TF32/BF16/FP64)→Hopper(FP8)→Blackwell(FP4); the [[TensorCore|Tensor Core]] "brittle contract" (FP32 fallback at 1/16th throughput); the [[NVLink]] vs PCIe bandwidth taper; and the **[[CUDA]] software moat** (cuBLAS/cuDNN/TensorRT) framed as "the primary reason NVIDIA dominates AI training infrastructure — not raw silicon performance." A100/H100/B200 supply the chapter's roofline and economics worked examples.

## From [[mlsysbook-ch13-model-serving|mlsysbook Vol 1 Ch 13]]

Ch 13 ([[ModelServing|Model Serving]]) leans on the NVIDIA serving stack: [[NVIDIATriton|Triton]] (multi-framework [[InferenceServer|inference server]]), [[TensorRT]] / [[TensorRTLLM|TensorRT-LLM]] ([[LayerFusion|fusion]], in-flight batching, INT8 — up to ~9× over PyTorch eager on ResNet-50), [[MIG]] (hardware GPU partitioning for multi-model SLO isolation), [[CUDAMPS|CUDA MPS]] (shared-context concurrency), and [[PinnedMemory|pinned memory]] for fast DMA. V100/A100/H100 supply the latency-budget, capacity-planning, and 8B Llama-3 worked examples; [[CUDA]] context creation (0.3–0.5 s) is a named [[ColdStart|cold-start]] component. See also [[mlsysbook-ch13-model-serving]].
