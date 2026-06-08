---
title: "CS324 — Parallelism"
type: source
tags: [cs324, llm, course-lecture, systems]
date: 2022-01-01
source_file: https://stanford-cs324.github.io/winter2022/lectures/parallelism/
---

## Summary
This Stanford [[CS324]] (Winter 2022) lecture surveys distributed training of large language models along three orthogonal axes — [[DataParallelism]], [[ModelParallelism]] (tensor/intra-layer), and [[PipelineParallelism]] — and how they are composed into [[3DParallelism]] on modern GPU clusters. It frames every design choice around the memory/communication hierarchy (chip → box/[[NVLink]] → rack → datacenter) and the central tension between fitting the model in memory and minimizing communication. It grounds each strategy in landmark systems — [[Megatron]], [[GPipe]], [[TeraPipe]], and [[ZeRO]] — and a supplementary historical deck ("An Ancient Tale of Parallelism") motivates it via [[Hogwild]]-style asynchronous SGD and the statistical-vs-hardware-efficiency tradeoff.

## Key Claims
- The two questions that govern every distributed-training design are (1) **memory** — does the model + activations + optimizer state fit on a device? — and (2) **communication** — the network is "loose" (relatively slow) and gets slower at every level up the hierarchy (intra-chip ≫ intra-box [[NVLink]] ≫ inter-box ≫ inter-rack).
- A modern accelerator delivers on the order of ~125 TFLOP/s up to ~1 PFLOP/s (low precision) and packs multiple dies plus large high-bandwidth memory ([[HBM]]); the lecture contrasts this with whole supercomputers (~3.6 PF in Canada, ~44 PF in Germany, noting the figures are not directly comparable).
- Models and hardware are co-designed: a matrix multiply can hit ~80% of peak utilization, whereas irregular kernels like attention land near ~10–15% "out of the box," motivating heavy kernel/parallelism engineering.
- **[[DataParallelism]]** replicates the full model on each worker, shards the mini-batch, computes gradients in parallel, then all-reduces/averages them and re-broadcasts weights; utilization is high but communication scales with replicas × model size and it requires the whole model to fit on one device.
- **[[ModelParallelism]]** (tensor/intra-layer, the [[Megatron]] approach) splits weight matrices and their matmuls across devices so even a single oversized layer fits; it is communication-heavy *within each layer's* forward and backward pass and so is best confined to fast intra-box [[NVLink]] links.
- [[Megatron]]-LM (2019) trained an 8.3B-parameter Transformer on 512 GPUs at 15.1 PetaFLOP/s with 76% scaling efficiency, needs no compiler/library changes, and is orthogonal/complementary to pipeline parallelism (implemented with a few collectives in native [[PyTorch]]).
- **[[PipelineParallelism]]** splits the model by layer-stages across devices; a naive split creates a large idle **[[PipelineBubble]]** because each stage waits on the previous one, crushing utilization.
- **[[Microbatching]]** (the [[GPipe]] idea) splits each mini-batch into many micro-batches fed through the pipeline in staggered fashion (forward `F(i,j)` = stage `i`, micro-batch `j`); more micro-batches → more overlap → smaller bubble → higher efficiency (lecture sketches ~60–70% per-device utilization in practice).
- [[GPipe]] (NeurIPS 2018) adds batch-splitting micro-batch pipelining for near-linear speedup and uses **[[GradientCheckpointing]]** (re-materialization) to recompute activations in the backward pass, trading compute for memory; demos include a 557M AmoebaNet (84.4% ImageNet top-1) and a 6B-parameter, 128-layer multilingual NMT Transformer over 100+ languages.
- **[[TeraPipe]]** (ICML 2021) introduces token-level (sequence-dimension) pipeline parallelism, exploiting the Transformer autoregressive property to pipeline *within a single sequence*, giving a 5.0× training speedup on the 175B [[GPT-3]] model on 48 AWS p3.16xlarge instances vs. state-of-the-art model-parallel methods.
- **[[3DParallelism]]** composes all three: tensor parallelism within a box (fastest links), pipeline parallelism across boxes, data parallelism across the model-parallel groups — [[Megatron]]-LM at scale (SC 2021) trained up to 1T parameters on 3,072 GPUs at 502 PetaFLOP/s (~52% of peak per GPU), with an interleaved pipeline schedule giving 10%+ extra throughput.
- **[[ZeRO]]**-style sharding partitions optimizer state / gradients / parameters across data-parallel workers (rather than replicating them) as the memory-saving complement to compute parallelism, alongside **[[GradientAccumulation]]** to emulate large batches.
- Historical motivation ([[Hogwild]]): the core balance is **statistical efficiency** (how many steps) vs. **hardware efficiency** (how fast each step); classical locking makes SGD communication scale quadratically and *slow down* with more cores, while ignoring locks (Hogwild!) still converges at essentially the same rate — relaxing consistency to be architecture-aware is a large performance win.
- The supplementary deck's **DMGC** model classifies four number classes — Dataset, Model, Gradient, Communication — and quantizes each independently for low-precision training, warning that learning hyperparameters (momentum, delay) are coupled to those precision/hardware choices.

## Key Quotes
> "Keep it high level, give you a taste." — the lecturer's stated goal for surveying distributed training

> "We've co-designed models to extract performance." — on why matmul-heavy Transformers reach high hardware utilization

> "Statistical algorithms have relaxed notions of correctness." — "Ancient Tale" thesis enabling new algorithm/system/hardware tradeoffs

> "Ignore the locks!" / "go Hogwild!" — the asynchronous-SGD heresy that provably still converges (Niu, Recht, Ré, Wright, NIPS 2011)

> "Optimization is a leaky abstraction for deep learning." — closing reflection: worse optimization can mean better generalization

## Connections
- [[CS324]] — this is one lecture in Stanford's Winter 2022 Large Language Models course
- [[Megatron]] — anchors the tensor/model-parallelism section and the 3D-parallelism scaling results
- [[GPipe]] — the canonical micro-batch pipeline-parallelism system discussed
- [[TeraPipe]] — token-level pipeline parallelism extending the pipeline section
- [[ZeRO]] — optimizer-state/parameter sharding as the memory-saving complement to compute parallelism
- [[GPT-3]] — the 175B model used as the headline target for TeraPipe's 5× speedup
- [[PyTorch]] — Megatron's tensor parallelism is implemented with a few collectives in native PyTorch
- [[NVLink]] — the fast intra-box interconnect that determines where tensor parallelism is placed
- [[DataParallelism]] / [[ModelParallelism]] / [[PipelineParallelism]] / [[3DParallelism]] — the four core strategies taught
- [[Microbatching]] / [[PipelineBubble]] / [[GradientCheckpointing]] / [[GradientAccumulation]] — the mechanisms that make pipeline parallelism efficient
- [[Hogwild]] — historical asynchronous-SGD motivation from the supplementary deck
- [[HBM]] — high-bandwidth memory, the capacity constraint that forces model/pipeline parallelism
- [[cs324-training]] — companion lecture on the training procedure this parallelizes
- [[cs324-scaling-laws]] — companion lecture motivating why models grow large enough to need this

## Contradictions
- None identified. Complementary to [[cs324-training]] (single-model training) and [[cs324-scaling-laws]] (why models scale); this lecture supplies the systems machinery to train at that scale.
