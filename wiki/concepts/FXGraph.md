---
title: "FX Graph"
type: concept
tags: [frameworks, pytorch, intermediate-representation, compilation]
sources: [mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# FX Graph

**FX Graph** is PyTorch's node-based directed acyclic graph [[IntermediateRepresentation|intermediate representation]], where each node represents an operation with explicit inputs and outputs. Operations captured by [[TorchDynamo]] are converted to FX format inside the [[TorchCompile|torch.compile]] pipeline. The FX graph serves as **PyTorch's analog to LLVM IR**: a standardized representation that separates the frontend (Python code capture) from the backend (hardware-specific code generation).

This decoupling lets different backends — [[TorchInductor]], [[ONNX]] Runtime, [[TensorRTLLM|TensorRT]] — all consume FX graphs, and enables optimization passes such as [[DeadCodeElimination|dead code elimination]], [[ConstantFolding|constant folding]], and pattern matching for [[KernelFusion|fusion]] opportunities.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — the IR stage of the torch.compile pipeline.
- [[TorchDynamo]] (produces it) / [[TorchInductor]] (consumes it) / [[TorchCompile]].
- [[IntermediateRepresentation]] — the general compiler pattern it instantiates.
- [[PyTorch]] — the framework.
