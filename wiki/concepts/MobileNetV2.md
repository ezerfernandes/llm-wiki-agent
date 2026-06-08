---
title: "MobileNetV2"
type: concept
tags: [deep-learning, cnn, edge, efficient-architecture, mlsysbook]
sources: [mlsysbook-ch01-introduction, mlsysbook-ch02-ml-systems, mlsysbook-ch03-ml-workflow, mlsysbook-ch06-network-architectures, mlsysbook-ch10-model-compression, mlsysbook-ch12-benchmarking]
last_updated: 2026-06-05
---

# MobileNetV2

An efficient mobile/edge [[CNN]] used in Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]) as the **latency-and-power [[LighthouseModel|Lighthouse Model]]** — the question it poses is *"can I meet real-time constraints on battery?"* Its depthwise-separable, inverted-residual operator design exemplifies algorithmic efficiency (capability per FLOP) for the [[EdgeML|edge/mobile]] tier.

MobileNet sits on the algorithmic-efficiency trajectory the chapter charts from [[AlexNet]] (1×) through VGG, ResNet, and ShuffleNet to EfficientNet (~44.5×) over 2012–2019.

[[mlsysbook-ch02-ml-systems|Ch 2]] frames MobileNet as an *efficient Compute Beast*: its [[DepthwiseSeparableConvolution|depthwise separable convolutions]] perform the same image classification as ResNet but cut FLOPs by ~10× (~8–9× per layer), enabling real-time inference within a 2–5 W mobile thermal envelope. This is "not merely optimization but a qualitative shift in the arithmetic-intensity trade-off" — accepting lower peak throughput for sustainable operation under the [[PowerWall|power wall]].

## Connections

- [[CNN]] — parent family.
- [[LighthouseModel]] — the latency/power probe.
- [[WorkloadArchetype]] — the efficient Compute Beast archetype.
- [[DepthwiseSeparableConvolution]] — the operator that delivers its efficiency.
- [[EdgeML]] / [[MobileML]] / [[TinyML]] — its deployment tiers.
- [[EfficiencyFramework]] — algorithmic efficiency exemplar.
- [[ModelCompression]] — complementary compression techniques.
- [[mlsysbook-ch03-ml-workflow]] — [[mlsysbook-ch03-ml-workflow|Ch 3]] walks MobileNetV2 (~14 MB, ~300 MFLOPs) through all six lifecycle stages as a concrete example of how problem-definition constraints (size/FLOP budget) propagate to model-development choices.
- [[mlsysbook-ch01-introduction]] / [[mlsysbook-ch02-ml-systems]] / [[mlsysbook-ch03-ml-workflow]] — sources.
- [[mlsysbook-ch10-model-compression]] — Ch 10 Lighthouse Model for compression: a deployment-gap table entry (INT8 still ~7× over a TinyML envelope); its NAS-tuned successor [[MobileNetV3]] anchors the "4× MobileNet win" (8→35 FPS via INT8 [[Quantization]]).
- [[mlsysbook-ch06-network-architectures]] — MobileNet is the *edge-latency* [[LighthouseModel|Lighthouse Model]]: ~14× fewer FLOPs than [[ResNet|ResNet-50]] but, with moderate [[ArithmeticIntensity|arithmetic intensity]] (~21 FLOP/byte), can run *slower* on data-center GPUs ("FLOPs ≠ speed"); it's the selected architecture in Ch 6's worked wildlife-camera-trap case study (INT8, Cortex-A53, 2 W envelope).
- [[mlsysbook-ch12-benchmarking]] — MobileNetV2 is the **lighthouse example** running through the entire [[Benchmarking|benchmarking]] chapter: INT8 trade-off (14→3.5 MB, 120→35 ms on Pi 4, −0.9 pp top-1) but [[ExpectedCalibrationError|ECE]] 0.031→0.089 and edge-case accuracy −6.8 pp; EdgeTPU vs. Cortex-M7 validation (2 vs 15 ms, 7.5× but only ~3× end-to-end); and the ~5.4× INT8 inference-energy breakdown.
