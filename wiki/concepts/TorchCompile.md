---
title: "torch.compile"
type: concept
tags: [llm-engineering, frameworks, pytorch, compilation]
sources: [leh-ch08-inference-optimization, mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

## Definition
PyTorch graph capture and fusion tool producing optimized kernels.

## In LLM Engineer's Handbook
PyTorch 2.x graph-capture-and-fusion tool that traces Python model code into an FX graph and compiles into fused, optimized kernels (TorchInductor / Triton on GPU). For LLM inference the chief constraint is shape-stability, which is why pairing it with a [[StaticKVCache]] is necessary and yields up to 4x forward-pass speedup per [[leh-ch08-inference-optimization]].

## Three-stage pipeline ([[mlsysbook-ch07-ml-frameworks|mlsysbook Vol 1 Ch 7]])

Ch 7 frames `torch.compile` as **overhead amortization, not magic** — its goal is to fuse small element-wise ops (LayerNorm, GELU, Add) whose dispatch + launch overhead exceeds compute by 10–100×. The pipeline:

1. **[[TorchDynamo]]** (graph capture) — intercepts Python bytecode via CPython's PEP 523 frame-eval API; inserts *graph breaks* on unsupported code (`print`, arbitrary Python) rather than failing silently like `torch.jit.trace`.
2. **[[FXGraph|FX Graph]]** (IR) — PyTorch's LLVM-IR analog, separating frontend from backend.
3. **[[TorchInductor]]** (codegen) — emits [[Triton]] kernels (→[[PTX]]) for CUDA, C++/AVX for CPU; applies fusion, layout optimization, autotuning.

First call ~100 ms (small) to 5–10 min (GPT-3 scale); subsequent same-shape calls reuse cached code in microseconds. Modes: `default` (5–30 s, dev/training), `reduce-overhead` (CUDA graphs, +20–40% inference), `max-autotune` (+10–30%, long runs). Typical 1.3–2× on transformers, 2–5× on matrix ops. Per the [[DispatchOverhead|Dispatch Overhead Law]], small models benefit most. Backends include [[TorchInductor]] (default), [[ONNX]] Runtime, and [[TensorRTLLM|TensorRT]].

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — the three-stage pipeline and overhead-amortization framing.
- [[TorchDynamo]] / [[FXGraph]] / [[TorchInductor]] / [[Triton]] / [[PTX]] — the pipeline stages.
- [[JITCompilation]] / [[CompilationContinuum]] / [[DispatchOverhead]] — the when-to-compile principles.
- [[XLA]] — Google's framework-integrated compiler peer.
