---
title: "Core ML"
type: concept
tags: [mlops, optimization, edge-ai, apple, inference-runtime]
sources: [mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Core ML

[[Apple]]'s model optimization and inference framework for on-device deployment across the Apple Neural Engine, GPU, and CPU. It accepts ONNX, TensorFlow, and PyTorch source formats and provides a unified format for Apple devices. In [[mlsysbook-ch14-ml-operations]]'s model-format-optimization table, Core ML is one of several target runtimes (alongside [[ONNXRuntime|ONNX Runtime]], [[TensorRT]], [[OpenVINO]], TF-TRT, [[TensorFlowLite|TFLite]]) that trade hardware breadth against peak performance — Core ML maximizes on-device inference within the Apple ecosystem.

## Connections
- [[ONNX]] — common interchange source format for Core ML.
- [[OpenVINO]] / [[TensorRT]] / [[TensorFlowLite]] — sibling optimization frameworks for other hardware.
- [[Apple]] — vendor.
- [[EdgeML]] / [[Quantization]] — on-device deployment context.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
