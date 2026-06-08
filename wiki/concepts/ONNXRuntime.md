---
title: "ONNX Runtime"
type: concept
tags: [serving, inference, runtime, cross-platform, mlsysbook]
sources: [mlsysbook-ch13-model-serving, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# ONNX Runtime

Microsoft's **hardware-agnostic inference engine**: a model exports to [[ONNX]] format, then ONNX Runtime applies framework-agnostic graph optimizations (constant folding, redundant-node elimination, [[OperatorFusion|operator fusion]]) and selects **execution providers** for the target hardware — CPU, NVIDIA/AMD GPU, or custom accelerators ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]).

Its value is portability: a single `.onnx` artifact retargets across CPU/GPU/NPU without recompilation, avoiding separate per-hardware optimization pipelines. The trade-off is a 5–15% throughput loss vs [[TensorRT]] for vision models, offset by the flexibility premium that matters most in heterogeneous device fleets (recompiling per target is measured in engineer-days). In the ResNet-50/V100 runtime ladder it sits between TorchScript and TensorRT (~5.1 ms, ~1.7×).

## Connections

- [[InferenceRuntime]] — the broader runtime-selection spectrum (portability vs raw speed).
- [[ONNX]] — the interchange format ONNX Runtime executes.
- [[TensorRT]] / [[OpenVINO]] — the specialized engines it trades portability against.
- [[OperatorFusion]] — among the graph optimizations it applies.
- [[mlsysbook-ch13-model-serving]] — source.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 positions ONNX Runtime as the broad-hardware-compatibility optimization framework (vs TensorRT's NVIDIA-only peak throughput).

