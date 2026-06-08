---
title: "ResNet-50"
type: concept
tags: [deep-learning, cnn, architecture, benchmark, mlsysbook]
sources: [mlsysbook-ch01-introduction, mlsysbook-ch02-ml-systems, mlsysbook-ch03-ml-workflow, mlsysbook-ch10-model-compression, mlsysbook-ch12-benchmarking]
last_updated: 2026-06-05
---

# ResNet-50

A 50-layer residual [[CNN|convolutional network]] used in Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]) as the **compute-throughput [[LighthouseModel|Lighthouse Model]]**. It applies small weight filters across many spatial positions and (under batching) across many inputs, so weight *reuse* is high and the [[IronLawOfMLSystems|iron law]]'s compute term $O/(R_{peak}\cdot\eta_{hw})$ tends to dominate — the question it poses is *"is my hardware doing math or waiting for data?"*

The chapter's headline [[DAMTaxonomy|D·A·M]] worked example uses **batch-size-1** ResNet-50 on an A100 to show the opposite extreme: FP16 weights (~50 MB) loaded across ~2 TB/s HBM (~26 µs) exceed the ~8 GFLOP of arithmetic at ~312 TFLOP/s (~13 µs), so small-batch inference is *memory-bound* and sits below the A100 FP16 [[RooflineModel|roofline]] ridge point. The lesson: small-batch inference cannot be fixed by buying peak FLOP/s.

[[mlsysbook-ch02-ml-systems|Ch 2]] uses ResNet-50 (~4 GFLOP/inference, ~25.6M params, ~98 MB FP32) as the **Compute Beast** [[WorkloadArchetype|archetype]] anchor (cloud training, edge inference) and extends the batch-1 analysis to show *both* a cloud A100 and a mobile NPU are memory-bound — the bandwidth gap, not peak FLOP/s, drives the inference speedup, which is why [[Quantization|quantization]] beats faster hardware for deployment.

## Connections

- [[ResNet]] — the residual-network family.
- [[CNN]] — parent architecture.
- [[LighthouseModel]] — ResNet-50 is the compute-bound probe.
- [[WorkloadArchetype]] — the Compute Beast archetype.
- [[IronLawOfMLSystems]] / [[RooflineModel]] / [[ArithmeticIntensity]] — the analysis it anchors.
- [[GPUUtilization]] — the $\eta_{hw}$ it stresses.
- [[mlsysbook-ch03-ml-workflow]] — [[mlsysbook-ch03-ml-workflow|Ch 3]]'s "workflow variations" table shows the compute-bound ResNet-50 archetype optimizing each lifecycle stage for throughput (>80% GPU util, batch >128) vs. DLRM (latency) and keyword-spotting (energy).
- [[mlsysbook-ch01-introduction]] / [[mlsysbook-ch02-ml-systems]] / [[mlsysbook-ch03-ml-workflow]] — sources.
- [[mlsysbook-ch10-model-compression]] — Ch 10's recurring compression example: 25.6M params prune 90% at <2% loss (~10× overparameterization), and FP32→INT8 gives ~4× size / ~1.5–3× speedup (per the measured INT8 framework); the "50% prune + INT8 = 6× target, ~1.5× measured" theory-practice gap is told on ResNet-50.
- [[mlsysbook-ch12-benchmarking]] — the **de facto [[MLPerf]] Training reference model** (target 75.9% top-1 on ImageNet; moderate size + well-understood profile make it sensitive to hardware and software optimizations); the compute-bound [[RooflineModel|roofline]] exemplar (AI ≈300 → 85–90% A100 utilization) against which [[Benchmarking|benchmarks]] judge sustained vs. peak.
