---
title: "GPU Utilization"
type: concept
tags: [hardware, performance, monitoring, gpu]
sources: [leh-ch10-inference-pipeline-deployment, ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

## Definition
**GPU utilization** is the fraction of time a GPU is actively executing kernels, measured by NVIDIA's `nvidia-smi` or equivalent telemetry. As a metric it is the dominant signal for whether expensive accelerators are being used efficiently in production LLM serving.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] suggests GPU utilization as a candidate metric for [[TargetTrackingScaling]] when configuring [[ApplicationAutoScaling]] on the LLM Twin's [[AWSSageMakerInferenceEndpoint|SageMaker endpoint]] — specifically targeting ~70% to leave headroom for spikes while limiting idle cost. The 70% target reflects a common trade-off: pushing GPUs to 100% utilization saves cost but eliminates the buffer that absorbs brief traffic spikes; aiming lower keeps perceived latency stable.

## Key details
- ~70% target is a common autoscaling rule of thumb for LLM inference.
- Measured per device — multi-GPU instances need an aggregation strategy (mean, max).
- Distinguished from **memory utilization** (KV cache pressure) and **power utilization**.
- A GPU at 70% utilization but 95% memory may still be a bottleneck — autoscaling should consider both.
- Pairs with [[CooldownPeriod]] to avoid oscillation under bursty load.

## Connections
- [[GPU]] — the hardware whose use this metric measures.
- [[TargetTrackingScaling]] — the policy type that targets GPU utilization.
- [[ApplicationAutoScaling]] — the parent autoscaling stack.
- [[AmazonCloudWatch]] — host of the metric.
- [[InferenceOptimization]] — the discipline focused on raising effective throughput per GPU-second.
- [[KVCache]] — memory pressure complementary to GPU utilization.
- [[Monitoring]] / [[ModelMonitoring]] — the practice this metric serves.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

**Critical caveat: Ch 9 explicitly criticizes `nvidia-smi`'s GPU utilization as misleading**, and introduces [[MFU]] and [[MBU]] as the metrics that actually matter for efficiency.

### The critique

> *"A common but often misunderstood metric is GPU utilization, and NVIDIA is partially to blame for this misunderstanding. ... For example, if you run inference on a GPU cluster for 10 hours, and the GPUs are actively processing tasks for 5 of those hours, your GPU utilization would be 50%. However, actively processing tasks doesn't mean doing so efficiently. For simplicity, consider a tiny GPU capable of doing 100 operations per second. In nvidia-smi's definition of utilization, this GPU can report 100% utilization even if it's only doing one operation per second."* — Ch 9

### The diagnostic gap

`nvidia-smi`'s GPU utilization tells you whether the GPU is **busy**. It does NOT tell you whether the GPU is **efficient**. Use:

- **[[MFU]]** — what fraction of peak FLOP/s you're achieving.
- **[[MBU]]** — what fraction of peak memory bandwidth you're achieving.

For autoscaling purposes, GPU utilization can still be useful as a *capacity signal* — but it's not a proxy for "is my workload squeezing the chip optimally?"

### Higher utilization is NOT the goal

> *"Higher utilization rates for similar workloads on the same hardware generally mean that your services are becoming more efficient. However, the goal isn't to get the chips with the highest utilization. What you really care about is how to get your jobs done faster and cheaper. A higher utilization rate means nothing if the cost and latency both increase."* — Ch 9

A workload that hits 100% GPU utilization via aggressive batching but blows past TTFT/TPOT SLOs has **worse goodput** than one running at 70% utilization within SLOs.
