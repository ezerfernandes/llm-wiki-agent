---
title: "Inference Performance Metrics"
type: concept
tags: [inference, metrics, latency, throughput, performance]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Inference Performance Metrics

**The metrics framework for evaluating inference services** — covered systematically in [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]. The metrics fall into three categories: **latency**, **throughput**, and **utilization**.

## The Ch 9 metrics tree

### Latency

- **[[TTFT|TTFT]]** — time to first token; dominated by [[Prefill|prefill]].
- **[[TPOT|TPOT]]** — time per output token; steady-state [[Decode|decode]] speed.
- **[[TBT|TBT]] / ITL** — time between tokens; streaming-cadence variant of TPOT (LinkedIn uses TBT, NVIDIA uses ITL).
- **Total latency** = TTFT + TPOT × number of output tokens.
- **[[TimeToPublish|Time to publish]]** — TTFT measured at user-visible token (not model-internal); useful for [[ChainOfThought|CoT]] / [[Agent|agentic]] workflows.

> *"Because latency is a distribution, the average can be misleading."* — Ch 9
>
> Report **p50, p90, p95, p99** percentiles, not averages.

### Throughput

- **TPS** — tokens per second (input or output; often refers to output).
- **RPS** — requests per second.
- **RPM** — completed requests per minute (used when individual requests take seconds — common for LLM workloads).
- **[[Goodput|Goodput]]** — requests/s satisfying the SLO; the metric you actually want to optimize because it captures the latency–throughput trade-off.

### Utilization

- **GPU utilization** (the [[GPUUtilization|`nvidia-smi` metric]]) — misleading; measures *time active*, not *FLOP/s achieved*.
- **[[MFU|MFU]]** — Model FLOP/s Utilization; from the [[PaLM]] paper.
- **[[MBU|MBU]]** — Model Bandwidth Utilization.

## The latency–throughput trade-off

> *"AI applications have the latency/throughput trade-off. Techniques like batching can improve throughput but reduce latency. According to the LinkedIn AI team, it's not uncommon to double or triple the throughput if you're willing to sacrifice TTFT and TPOT."* — Ch 9

Optimizing throughput-alone or latency-alone produces bad services. **Goodput** is the joint optimum.

## Cost as the synthesis

> *"Throughput is directly linked to compute cost. A higher throughput typically means lower cost. If your system costs $2/h in compute and its throughput is 100 tokens/s, it costs around $5.556 per 1M output tokens."*

The hierarchy: latency targets the SLO; throughput targets the cost; utilization diagnoses the bottleneck.

## Connections

- [[TTFT]] / [[TPOT]] / [[TBT]] / [[TimeToPublish]] — latency metrics.
- [[Goodput]] — SLO-aware throughput metric.
- [[MFU]] / [[MBU]] / [[GPUUtilization]] — utilization metrics.
- [[ComputeBound]] / [[MemoryBandwidthBound]] — what MFU/MBU diagnose.
- [[InferenceOptimization]] — what the metrics target.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
