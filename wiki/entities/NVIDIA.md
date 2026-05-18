---
title: "NVIDIA"
type: entity
tags: [company, hardware, gpu]
sources: [d2l-installation, d2l-builders-guide, 2205.14135-flashattention, d2l-computational-performance, parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
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
