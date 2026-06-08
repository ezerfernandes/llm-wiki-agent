---
title: "Safetensors"
type: concept
tags: [serving, model-loading, cold-start, format, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# Safetensors

A model serialization format (Hugging Face, 2022) designed for **fast, safe loading**: it stores tensors as contiguous raw bytes with a minimal JSON header, enabling **zero-copy memory-mapped loading** — the raw bytes on disk map directly into the tensor's memory buffer ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]).

Vs PyTorch's default `torch.load` (Python `pickle`, which unpickles objects one by one with high CPU usage), safetensors loads **30–100× faster**: a 5 GB Stable Diffusion model loads in ~0.5 s (near-zero CPU) vs ~15 s. With `mmap`, loading speed becomes limited only by disk read speed (e.g., 3 GB/s NVMe) rather than CPU parsing. The "safe" also refers to security: unlike pickle, it cannot execute arbitrary code during deserialization. For autoscaling fleets this directly reduces [[ColdStart|cold start]] — the difference between a 15 s and 0.5 s model load determines whether new replicas absorb traffic spikes before SLOs break.

## Connections

- [[ColdStart]] — fast loading is a primary cold-start mitigation.
- [[Autoscaling]] / [[CapacityPlanning]] — faster replica spin-up under traffic spikes.
- [[PinnedMemory]] — complementary zero-copy/DMA loading optimization.
- [[HuggingFace]] — the creator.
- [[mlsysbook-ch13-model-serving]] — source.
