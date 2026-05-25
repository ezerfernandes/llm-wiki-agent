---
title: "PyTorch"
type: entity
tags: [tool, deep-learning, framework]
sources: [madewithml-mlops-training, madewithml-foundations-pytorch, d2l-preliminaries, d2l-builders-guide, ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# PyTorch

Deep-learning framework underlying every foundations DL lesson and the training pipeline in [[madewithml-mlops-training]]. Bridges from [[NumPy]] semantics to GPU-accelerated [[Tensor]] ops with [[Autograd]]; wrapped by [[RayTrain]] for distributed training.

[[d2l-builders-guide]] is the chapter that explains *how* PyTorch is structured: every layer / sub-network / model is a `nn.Module` subclass exposing a `forward` method; [[StateDict|`state_dict()`]] saves parameters (not architecture); `nn.LazyLinear` defers shape inference; `nn.Parameter` wraps a tensor as a tracked weight; `net.to(device)` migrates the model across CPU/[[GPU]] boundaries with explicit operand-locality rules.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 features PyTorch in multiple roles:

### Compiler

`torch.compile` is one of three framework-integrated ML compilers Ch 9 names (alongside [[XLA]] and TensorRT). See [[TorchCompile]].

### The Llama-7B optimization case study

Ch 9's Figure 9-14 reproduces a PyTorch team experiment on **Llama-7B on A100 80GB**, stacking four optimizations:

1. `torch.compile` — efficient kernel emission.
2. INT8 weights — first quantization step.
3. INT4 weights — further quantization.
4. Speculative decoding — final layer.

Each step multiplies throughput; the chapter doesn't quantify quality impact.

### Speculative decoding implementation

> *"This approach has gained traction because it's relatively easy to implement and doesn't change a model's quality. For example, it's possible to do so in 50 lines of code in PyTorch."* — Ch 9 on speculative decoding

### Limitation noted

> *"Popular frameworks such as PyTorch and TensorFlow don't yet allow fine-grained control of memory access. This has led many AI researchers and engineers to become interested in GPU programming languages such as CUDA, OpenAI's Triton, and ROCm."* — Ch 9

PyTorch is positioned as the high-level framework; kernel-level work happens below it in [[CUDA]] / [[Triton]] / [[ROCm]].
