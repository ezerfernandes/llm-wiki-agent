---
title: "MLPerf"
type: entity
tags: [benchmark, consortium, ml-systems, mlsysbook]
sources: [mlsysbook-ch01-introduction, mlsysbook-ch12-benchmarking]
last_updated: 2026-06-05
---

# MLPerf

The industry-standard benchmark suite for measuring ML training and inference performance, associated with [[VijayJanapaReddi|Vijay Janapa Reddi]]'s research lineage. In Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Ch 1]]), MLPerf scenarios are referenced as the basis for characterizing inference performance across deployment tiers (part of the Deployment Infrastructure pillar of the [[FivePillarFramework|five-pillar framework]]).

## Founding and structure

Founded **2018** by researchers from [[google|Google]], [[NVIDIA]], Intel, [[Harvard]], Stanford, and UC Berkeley (the name = "ML" + "Perf"), now governed by [[MLCommons]] (2020). [[mlsysbook-ch12-benchmarking|Ch 12]] details it as the synthesis of three decades of benchmark lessons (representative workloads + multi-objective metrics + full-system measurement), with founding leadership including [[DavidPatterson|Dave Patterson]]. The family is **tiered by deployment domain**:

- **MLPerf Training** — data center; metric: [[TimeToAccuracy|time-to-accuracy]], throughput (samples/s). Has outpaced Moore's Law (ResNet >30× over 5 years).
- **MLPerf Inference** — server/edge; QPS, latency percentiles, accuracy; defines the four [[MLPerfScenarios|execution scenarios]] (SingleStream/MultiStream/Server/Offline) + Interactive.
- **MLPerf Mobile / Client / Tiny** — on-device, consumer-hardware, and MCU/IoT (<1 MB, sub-50 mW) tiers.
- **MLPerf Power** — cross-cutting energy/efficiency measurement ([[MLPerfPower]]).

Its **Reference-vs-Submission accuracy guardrail** (e.g., 75.9% top-1 on ImageNet) is the chapter's defense against [[BenchmarkEngineering|benchmark engineering]]. A self-noted limitation: MLPerf benchmarks mostly **dense, unoptimized models**, while production runs compressed ones.

## Connections

- [[VijayJanapaReddi]] — associated researcher and Ch 12 author.
- [[MLCommons]] — the nonprofit consortium that governs MLPerf.
- [[DavidPatterson]] — founding leadership; the fallacy-of-peak-performance framing.
- [[MLPerfScenarios]] / [[MLPerfPower]] — the execution-scenario and power-measurement methodologies.
- [[TimeToAccuracy]] / [[ScalingEfficiency]] / [[TailLatency]] — the metrics MLPerf codifies.
- [[BenchmarkEngineering]] — the gaming the Reference-vs-Submission rule deters.
- [[mlsysbook-ch01-introduction]] — the chapter first referencing it.
- [[mlsysbook-ch12-benchmarking]] — the dedicated benchmarking chapter (capstone of the Optimize part).
- [[LighthouseModel]] — canonical workloads benchmarked across tiers.
- [[FivePillarFramework]] — benchmarking sits in the Deployment Infrastructure pillar.
