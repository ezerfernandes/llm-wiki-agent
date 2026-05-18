---
title: "Streaming Processor (SP)"
type: concept
tags: [gpu, cuda, hardware, nvidia]
sources: [parproc-ch05-cuda-gpu-programming]
last_updated: 2026-05-17
---

# Streaming Processor (SP)

The **individual core** of a [[StreamingMultiprocessor|streaming multiprocessor]] (SM) on an [[NVIDIA]] GPU. Each SM contains a cluster of SPs; they execute the threads assigned to that SM. *"Each SM consists of a number of streaming processors (SPs), individual cores."* ([[parproc-ch05-cuda-gpu-programming]] §5.4.1).

## Position in the hierarchy

```
GPU                      (one device)
 └── SM × many           (streaming multiprocessors)
      └── SP × cluster   (streaming processors / cores)
```

The SP is the lowest hardware level. From the programmer's point of view, every CUDA thread eventually executes on some SP — but the **scheduling unit** is the [[Warp]] (32 threads), not the SP. Under [[SIMT]] all SPs in a warp's execution slot run the same instruction in lockstep.

## Word size

Tesla baseline: 32-bit. Double precision via 64-bit composite types like `float2`. *"Newer devices are capable of double precision."* (§5.4.1).

## See also

- [[StreamingMultiprocessor]] — parent SM container.
- [[Warp]] — the scheduling unit that drives SP execution.
- [[CUDA]] — programming model.
- [[NVIDIA]] — vendor.
- [[parproc-ch05-cuda-gpu-programming]] — §5.4.1.
