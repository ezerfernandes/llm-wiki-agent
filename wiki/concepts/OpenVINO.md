---
title: "OpenVINO"
type: concept
tags: [mlops, optimization, inference-runtime, intel]
sources: [mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# OpenVINO

Intel's model optimization toolkit, targeting Intel CPUs, GPUs, VPUs, and FPGAs. It accepts ONNX, TensorFlow, PyTorch, Caffe, and MXNet source formats and applies model compression, async execution, and caching. In [[mlsysbook-ch14-ml-operations]]'s model-format-optimization comparison, OpenVINO optimizes for the Intel hardware ecosystem, occupying a middle ground between [[ONNXRuntime|ONNX Runtime]]'s broad hardware compatibility and [[TensorRT]]'s NVIDIA-only peak throughput.

## Connections
- [[ONNX]] — common interchange source format.
- [[TensorRT]] / [[CoreML]] / [[TensorFlowLite]] — sibling vendor-specific optimization frameworks.
- [[ONNXRuntime]] — broader-compatibility alternative.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
