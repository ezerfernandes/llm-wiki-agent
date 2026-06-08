---
title: "TensorFlow Lite / TF Lite Micro"
type: concept
tags: [frameworks, edge, tinyml, deployment, tensorflow]
sources: [mlsysbook-ch07-ml-frameworks, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# TensorFlow Lite / TF Lite Micro

**TensorFlow Lite (TFLite)** and **TensorFlow Lite Micro (TFLM)** are the inference-only edge runtimes in the [[TensorFlow]] family, embodying the principle of *progressive constraint leading to progressive optimization*. As the target hardware shrinks, the runtime sheds capability to fit:

| | TensorFlow | TF Lite | TF Lite Micro |
|---|---|---|---|
| Training | Yes | No | No |
| Ops supported | ~1,400 | ~130 | ~50 |
| Needs an OS | Yes | Yes | No (bare metal) |
| Native quantization | No | Yes | Yes |
| Base binary | a few MB | tens–hundreds of KB | ~10 KB |
| Architectures | x86/GPU/TPU | Arm Cortex-A, x86 | Arm Cortex-M, DSPs, MCUs |

**TFLM** is the [[TinyML]] endpoint of the [[CompilationContinuum|compilation continuum]]: a tiny C/C++ interpreter over a flat model representation with a **fixed memory arena** (the application supplies a contiguous tensor arena; the runtime plans and reuses buffers without heap allocation after setup). A standard PyTorch runtime is ~500 MB and the Python interpreter ~20 MB — orders of magnitude larger than a 256 KB-RAM MCU. The "silicon contract" at this tier is strictly memory-bound: the model's working set (intermediate activations) must fit in the MCU's SRAM.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — TinyML micro-runtimes; framework selection by deployment target.
- [[TinyML]] — the deployment regime; [[CompilationContinuum]] — the AOT/static extreme.
- [[TensorFlow]] — the parent framework; [[ONNX]] — alternative interchange (TFLite uses its own conversion path).
- [[Quantization]] — INT8 native tooling enables the smallest footprints.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 lists TFLite as the mobile/Edge-TPU optimization framework (quantization, delegate support) in the format-optimization comparison.

