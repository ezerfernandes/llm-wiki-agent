---
title: "Model Parallelism"
type: concept
tags: [distributed-training, parallelism, multi-gpu, deep-learning]
sources: [d2l-computational-performance]
last_updated: 2026-05-16
---

# Model Parallelism

Splitting a single model's *parameters* (rather than its *data*) across multiple GPUs. Two flavors ([[d2l-computational-performance]] §`multiple-gpus`):

1. **Network partitioning (a.k.a. pipeline parallelism)** — assign distinct *layers* to distinct GPUs. GPU 0 runs layers 1–4, GPU 1 runs layers 5–8, etc. Activations flow GPU→GPU on the forward pass; gradients flow back on the backward pass.
2. **Layerwise / [[TensorParallelism|tensor]] partitioning** — split the units *within* a layer (e.g. compute 64 channels as 4×16 across 4 GPUs). The canonical historical example is the original [[AlexNet]] design ([[fig_alexnet_original]]) where dual GTX 580 GPUs with only 2 GB each forced [[AlexKrizhevsky|Krizhevsky]] to shard the conv channels.

## When it matters

The single use case: **the model doesn't fit on one GPU**. Modern Transformer LLMs at hundreds-of-billions of parameters are the canonical example — even an H100 (80 GB) can hold only ~40B FP16 parameters once you add gradients, optimizer state, and activations.

## Why it's hard

> *"The interface between layers (and thus GPUs) requires tight synchronization. […] The interface between layers also requires large amounts of data transfer, such as activations and gradients. This may overwhelm the bandwidth of the GPU buses."* — [[d2l-computational-performance]]

- Pipeline parallelism creates GPU **idle bubbles** at the start and end of each minibatch (GPU $k$ waits for activations from GPU $k{-}1$, GPU $0$ waits for gradients from GPU $k{-}1$). Solutions: GPipe, PipeDream, 1F1B scheduling.
- Tensor parallelism requires **synchronization at every layer** — bandwidth cost worse than pipeline parallelism on slow interconnects, but works on fast NVLink (Megatron-LM).
- Compute-intensive sequential ops are *nontrivial to partition*.

## Status

D2L's stance: **only recommended when there is excellent framework or OS support for chaining GPUs**. For 2026 LLM training, model parallelism is **mandatory** at frontier scale and is implemented in Megatron-LM, DeepSpeed-Inference, FSDP (param-sharded data parallelism, hybrid), and FairScale. For everything else, [[DataParallelism|data parallelism]] is preferred.

## See also
- [[DataParallelism]] — the strategy this contrasts with; recommended default.
- [[TensorParallelism]] — intra-layer model parallelism.
- [[PipelineParallelism]] — inter-layer model parallelism.
- [[AlexNet]] — the historical model-parallel example (2 × GTX 580 @ 2 GB).
- [[DistributedTraining]] — parent concept.
- [[d2l-computational-performance]] §`multiple-gpus`.
