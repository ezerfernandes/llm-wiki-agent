---
title: "OpenVINO"
type: entity
tags: [intel, inference, runtime, cpu, serving, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# OpenVINO

Intel's specialized inference engine (Open Visual Inference and Neural network Optimization) that **bypasses framework abstractions to map computations directly onto proprietary hardware instructions** like AVX-512 and AMX ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]).

This direct targeting is "aggressive" because it abandons the portability framework-native runtimes must guarantee, allowing specialized kernels unsafe for general execution. The resulting **2–5× speedup over standard CPU execution** makes dedicated CPU serving economically viable for models under ~500M parameters — relevant because CPUs often outperform GPUs at batch-1 for small models (the GPU kernel-launch ~10 μs + ~50 μs data transfer exceeds tiny-layer compute time). Intel Extension for PyTorch (IPEX) plays a similar SIMD-mapping role.

## Connections

- [[InferenceRuntime]] — the specialized (Intel/CPU) end of the runtime spectrum.
- [[TensorRT]] / [[ONNXRuntime]] — the NVIDIA-specialized and portable alternatives.
- [[SIMD]] — the AVX-512/AMX vector units OpenVINO targets.
- [[CostPerInference]] — CPU serving economics for small models.
- [[Intel]] — the vendor.
- [[mlsysbook-ch13-model-serving]] — source.
