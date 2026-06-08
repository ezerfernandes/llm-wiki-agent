---
title: "Autoscaling"
type: concept
tags: [infrastructure, mlops, serving, mlsysbook]
sources: [mlsysbook-ch13-model-serving, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Autoscaling

Automatic adjustment of compute resources (nodes, replicas, GPUs) in response to load signals like queue depth or request latency. Essential for cost-efficient [[BatchInference]] and online serving on platforms like [[AnyscaleServices]], [[KNative]], and [[Kubeflow]].

## In mlsysbook (Ch 13)

[[mlsysbook-ch13-model-serving|mlsysbook Ch 13]] positions autoscaling as the response to the [[QueuingTheory|tail-latency explosion]]: spin up replicas *before* utilization hits the ~70% "knee," not after. Its hard constraint is **[[ColdStart|cold start]]** — GPU instances take 2–5 min to become useful (driver init + model load + warmup) vs 30–60 s for CPU. This asymmetry drives strategy: **predictive scaling for GPU** (provision ahead of anticipated demand), **reactive scaling for CPU**, and **hybrid** (always-on GPU baseline + CPU overflow for spikes). [[Safetensors]] zero-copy loading and precompiled [[TensorRT]] engines shrink the cold-start window so new replicas absorb spikes before SLOs break.

## Connections

- [[ColdStart]] — the startup latency that bounds how fast autoscaling adds capacity.
- [[CapacityPlanning]] — peak load + ~30% headroom, scaling down off-peak.
- [[QueuingTheory]] / [[AdmissionControl]] — scale before the knee; shed load if scaling can't keep up.
- [[CostPerInference]] — autoscaling reduces idle-hardware waste.
- [[mlsysbook-ch13-model-serving]] — source.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 covers ML autoscaling: scale 1→dozens of replicas in <60s (35–50% cost savings) but must account for model cold-start and GPU memory fragmentation.

