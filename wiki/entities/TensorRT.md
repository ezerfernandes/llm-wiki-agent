---
title: "TensorRT"
type: entity
tags: [nvidia, inference, runtime, gpu, serving, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# TensorRT

NVIDIA's **specialized inference engine** for NVIDIA GPUs. It abandons framework portability by requiring a build phase that recompiles the model for a specific target GPU architecture (e.g., H100), and this hardware lock-in enables aggressive, irreversible optimizations — [[LayerFusion|layer fusion]], kernel auto-tuning, constant folding — that framework-native runtimes cannot safely perform ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]).

The resulting non-portable engine delivers **2–5× lower latency** than framework-native serving (ResNet-50/V100 batch-1: 8.5 ms PyTorch eager → 2.8 ms FP32 → 1.4 ms FP16 → 0.9 ms INT8, ~9× at INT8), directly reducing the GPU count needed to meet a throughput target. Auto-fusion drops a typical ResNet-50 from ~50 kernels to ~15. Ships post-training quantization out of the box. Its sibling [[TensorRTLLM]] (in-flight batching) extends these techniques to LLM serving. Trade-off: TensorRT compilation is the dominant 15–30 s phase of [[ColdStart|cold start]] (precompile and cache the engine to avoid it).

## Connections

- [[InferenceRuntime]] — the specialized end of the runtime-selection spectrum.
- [[LayerFusion]] / [[OperatorFusion]] — the graph optimizations TensorRT performs.
- [[ONNXRuntime]] / [[OpenVINO]] — the portability and Intel-hardware alternatives.
- [[TensorRTLLM]] — the LLM-serving sibling.
- [[Quantization]] / [[TensorCore]] — FP16/INT8 precision paths on Tensor Cores.
- [[ColdStart]] — TensorRT compilation dominates first-deploy startup.
- [[NVIDIA]] — the vendor.
- [[mlsysbook-ch13-model-serving]] — source.
