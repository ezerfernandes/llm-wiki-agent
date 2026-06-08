---
title: "Inference Runtime"
type: concept
tags: [serving, inference, runtime, optimization, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# Inference Runtime

The **software layer that orchestrates tensor operations and manages hardware resources** during serving — and it can vary by an order of magnitude in performance for identical models ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]). Selection should start from the *binding constraint*, not the training framework:

- **Framework-native** ([[PyTorch]] eager, [[TensorFlow]]) — maximum compatibility, simplest pipeline, but training overhead and unexploited hardware optimizations. TorchScript / TF SavedModel add AOT graph optimization.
- **General-purpose** ([[ONNXRuntime|ONNX Runtime]]) — hardware-agnostic optimization via pluggable execution providers; one `.onnx` artifact across CPU/GPU/NPU, at a 5–15% throughput loss vs TensorRT for vision.
- **Specialized** ([[TensorRT]] for NVIDIA, [[OpenVINO]] for Intel) — aggressive [[LayerFusion|fusion]], kernel auto-tuning, hardware lock-in; 2–5× over framework-native.

ResNet-50/V100 batch-1 spread: PyTorch eager 8.5 ms (1×) → TorchScript 6.2 → ONNX 5.1 → TensorRT FP32 2.8 (3×) → FP16 1.4 (6×) → INT8 0.9 (~9×). The optimization-compatibility trade-off is inherent: more aggressive optimization yields more speed but more deployment complexity and potential numerical drift. JIT (e.g., `torch.compile`) vs AOT (`torch.export`, `trtexec`) governs whether compilation latency hits the first request or ships as a static artifact.

## Connections

- [[ONNXRuntime]] / [[TensorRT]] / [[OpenVINO]] / [[ONNX]] — the runtime/format ecosystem.
- [[LayerFusion]] / [[OperatorFusion]] — the graph optimizations specialized runtimes perform.
- [[Quantization]] — FP16/INT8 precision selection multiplies runtime gains.
- [[InferenceServer]] — invokes the runtime as its inference runner.
- [[CostPerInference]] — runtime + precision choice directly sets GPU count/cost.
- [[CUDA]] / [[SIMD]] / [[TensorCore]] — the hardware primitives runtimes target.
- [[mlsysbook-ch13-model-serving]] — source.
