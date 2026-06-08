---
title: "Depthwise Separable Convolution"
type: concept
tags: [deep-learning, cnn, efficient-architecture, mobile, mlsysbook]
sources: [mlsysbook-ch02-ml-systems, mlsysbook-ch03-ml-workflow, mlsysbook-ch06-network-architectures, mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

# Depthwise Separable Convolution

An architectural factorization that **splits a standard convolution into a depthwise spatial filter (one filter per input channel) and a pointwise (1×1) channel mixer**, reducing FLOPs by ~8–9× for typical layer configurations. The key efficiency operator behind [[MobileNetV2|MobileNet]] in [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]).

[[mlsysbook-ch02-ml-systems|Ch 2]] frames it as a *prerequisite*, not a mere optimization: MobileNet performs the same image classification as [[ResNet|ResNet]] but cuts total FLOPs ~10×, enabling real-time vision within a 2–5 W [[MobileML|mobile]] [[PowerWall|power-wall]] envelope. This is "a qualitative shift in the arithmetic-intensity trade-off" — accepting lower peak throughput for sustainable operation. The same operator is used by [[KeywordSpotting|keyword-spotting]] [[TinyML]] models (e.g. DS-CNN) on microcontrollers.

## Connections

- [[MobileNetV2]] — the model built on this operator.
- [[CNN]] — the parent operation it factorizes.
- [[KeywordSpotting]] — TinyML DS-CNN models reuse it.
- [[MobileML]] / [[TinyML]] — the tiers it makes feasible.
- [[ArithmeticIntensity]] / [[PowerWall]] — the efficiency trade-off it embodies.
- [[ModelCompression]] — the broader efficiency discipline.
- [[mlsysbook-ch03-ml-workflow]] — uses [[MobileNetV2]] (~14 MB, ~300 MFLOPs) as a worked workflow example: depthwise separable convolutions are the model-development choice that meets the FLOP budget set at problem definition (without them the same accuracy would need 2–3× the device's compute ceiling).
- [[mlsysbook-ch02-ml-systems]] / [[mlsysbook-ch03-ml-workflow]] — sources.
- [[mlsysbook-ch10-model-compression]] — Ch 10's computation-reduction principle: 5–10× FLOP reduction; MobileNetV2 takes a 4-point ImageNet drop for **13.7× fewer ops vs ResNet-50**; underpins [[MobileNetV3]] and the [[DSCNN]] keyword spotter.
- [[mlsysbook-ch06-network-architectures]] — Ch 6 factorizes standard convolution (cost $\mathcal{O}(N K^2 C_{\text{in}} C_{\text{out}})$) into depthwise ($K{\times}K{\times}C_{\text{in}}$) + pointwise ($1{\times}1{\times}C_{\text{in}}{\times}C_{\text{out}}$), cutting cost by ≈ $1/C_{\text{out}}+1/K^2$ (≈ $1/K^2$, i.e. 8–9× for 3×3); the operator powers both [[MobileNetV2|MobileNet]] (edge latency Lighthouse) and [[KeywordSpotting|KWS DS-CNN]] (TinyML power Lighthouse).
