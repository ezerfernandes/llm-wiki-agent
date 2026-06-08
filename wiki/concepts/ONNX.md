---
title: "ONNX (Open Neural Network Exchange)"
type: concept
tags: [frameworks, interoperability, deployment, serialization]
sources: [mlsysbook-ch07-ml-frameworks, mlsysbook-ch13-model-serving, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# ONNX (Open Neural Network Exchange)

**ONNX** is a hardware-agnostic graph-representation format that enables model portability across frameworks and runtimes: train in [[PyTorch]], export through ONNX, and deploy through **ONNX Runtime** or a hardware-specific backend. It addresses the fragmentation that the best *training* framework (often PyTorch for research velocity) rarely matches the best *serving* runtime (often [[TensorRTLLM|TensorRT]] for latency, [[TensorFlowLite|TF Lite]] for mobile).

ONNX sits at the center of a **hub-and-spoke** interoperability model, accepting models from common training frameworks and dispatching them to ONNX Runtime and other compatible runtimes. It is also a [[TorchCompile|torch.compile]] backend (exporting the [[FXGraph|FX graph]] to ONNX for CPU/GPU/mobile/edge). The accepted trade-off: ONNX export can **lose framework-specific optimizations or custom operators**, requiring fallback implementations — so it reduces but does not eliminate compatibility testing and conversion work. (TensorFlow Lite uses its own conversion path rather than being a direct ONNX target in typical workflows.)

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — deployment targets and framework interoperability.
- [[PyTorch]] / [[TensorFlow]] — common ONNX export sources.
- [[TensorRTLLM]] / [[TVM]] / [[TensorFlowLite]] — specialized serving backends ONNX feeds.
- [[FXGraph]] — torch.compile's ONNX export path; [[IntermediateRepresentation]] — the general pattern.
- [[ONNXRuntime]] / [[InferenceRuntime]] / [[TensorRT]] — the runtime that executes ONNX models and the specialized engine it trades portability against ([[mlsysbook-ch13-model-serving|Ch 13]]: 5–15% throughput loss for cross-platform retargetability).
- [[mlsysbook-ch13-model-serving]] — Ch 13 places ONNX Runtime as the portable middle of the runtime-selection spectrum.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 presents ONNX as the standard interchange format in the format-optimization workflow (export → graph cleanup → fusion → quantize → validate numerical equivalence).

