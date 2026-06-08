---
title: "Cloud ML"
type: concept
tags: [ml-systems, cloud, deployment, mlsysbook]
sources: [mlsysbook-ch02-ml-systems]
last_updated: 2026-06-05
---

# Cloud ML

The deployment paradigm that **trades latency for elastic compute** by locating ML workloads in centralized data centers, decoupling computational capacity from the physical location of data sources and users. The high-compute, high-power end of the [[DeploymentSpectrum|deployment spectrum]] in [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]).

Cloud ML dominates the $R_{peak}$ term of the [[IronLawOfMLSystems|iron law]] — a single region can provision thousands of accelerators on demand (PFLOP/s–EFLOP/s) — but pays a 100–500 ms round-trip $L_{lat}$ penalty set by the [[SpeedOfLight|speed of light]] over continental distances, making it infeasible for sub-10-ms response. Operating regime: MW power (PUE 1.1–1.3), TB memory, >1000 TFLOP/s, >1000 GB/s bandwidth. The hardware anchor is the **TPU v4 Pod** (4,096 chips, >1 EFLOP/s, 131 TB HBM2).

It is the natural home of three of the four [[WorkloadArchetype|workload archetypes]]: Compute Beasts (ResNet training), Bandwidth Hogs (LLM inference), and Sparse Scatter ([[DLRM]] embedding tables). Training GPT-3 (~3,640 PFLOP-days, ~10,000 V100s, ~15 days, ~$4.6M) is the canonical "only a data center could do this" example.

**Constraints beyond latency:** the Data Gravity Invariant (moving data eventually costs more than moving compute), [[GDPR]]/[[HIPAA]] compliance, vendor lock-in, and [[TotalCostOfOwnership|TCO]] (sustained 24/7 serving often costs 2–3× more than amortized on-prem). The voice-assistant wall shows cloud-only is *physically impossible* at billion-device scale (~$500M/year + ~20 dedicated data centers + a backbone-saturating audio stream).

## Connections

- [[DeploymentSpectrum]] — the spectrum Cloud ML anchors at the high-compute end.
- [[EdgeML]] / [[MobileML]] / [[TinyML]] — the other three paradigms; cloud prioritizes elastic $R_{peak}$ at the cost of variable $L_{lat}$.
- [[IronLawOfMLSystems]] / [[BottleneckPrinciple]] — cloud training is compute-bound; cloud LLM inference is memory-bandwidth-bound.
- [[WorkloadArchetype]] — hosts Compute Beast, Bandwidth Hog, Sparse Scatter.
- [[SpeedOfLight]] — the source of the cloud latency penalty.
- [[GoogleTPU]] — the TPU v4 Pod hardware anchor.
- [[GDPR]] / [[HIPAA]] / [[TotalCostOfOwnership]] — the non-latency constraints pushing work to the edge.
- [[HybridML]] — cloud is the "train" tier of Train-Serve Split and the analytics tier of Hierarchical Processing.
- [[DLRM]] / [[Netflix]] / [[meta|Meta]] — cloud-only recommendation workloads.
- [[mlsysbook-ch02-ml-systems]] — source.
