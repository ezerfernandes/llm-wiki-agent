---
title: "Mobile ML"
type: concept
tags: [ml-systems, mobile, deployment, mlsysbook, energy]
sources: [mlsysbook-ch02-ml-systems]
last_updated: 2026-06-05
---

# Mobile ML

The deployment paradigm **bounded by Thermal Design Power (TDP) and battery energy** — bringing ML to smartphones and tablets while balancing capability against a 2–5 W envelope. Sits between [[EdgeML|Edge ML]] and [[TinyML]] on the [[DeploymentSpectrum|deployment spectrum]] in [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]).

Unlike plugged-in edge servers, mobile devices move in the world on fixed energy budgets, so $\text{Energy} = \text{Power}\times T$ becomes a first-order design parameter alongside latency. Two distinct constraints bind:

- **The battery tax** (a *budget* problem): a 2 W always-on object detector drains a ~15 Wh phone in <8 hours (~320% of a full-day budget). Solvable by duty-cycling or compression.
- **The [[ThermalWall|thermal wall]]** (a *physics ceiling*): a passively-cooled SoC dissipates ~3 W max; a 12 W model hits the 80 °C thermal trip in ~60 s and [[ThermalThrottling|throttles]] regardless of remaining battery. No optimization raises it.

Operating regime: GB RAM, GB storage, tens of INT8 TOPS via [[NeuralProcessingUnit|NPUs]] (10–100× energy efficiency), 5–50 ms latency, LPDDR5 bandwidth limiting models to 10–100 MB. Mobile is an *efficient Compute Beast* paradigm: compute-heavy vision must be reshaped via [[DepthwiseSeparableConvolution|depthwise separable convolutions]] ([[MobileNetV2|MobileNet]], ~10× FLOP reduction). Applications: [[ComputationalPhotography|computational photography]] (10–15 models within ~200 ms shutter delay), voice ([[WakeWordDetection|wake word]] <1 mW → NPU speech recognition <10 ms), health monitoring, AR (sub-16 ms / 60 FPS). Apple's Face ID / Secure Enclave keeps biometric templates on-device (1:1,000,000 false acceptance).

## Connections

- [[DeploymentSpectrum]] — Mobile sits between Edge and TinyML.
- [[EdgeML]] — the stationary, plugged-in sibling; mobile adds the energy constraint.
- [[TinyML]] — the more constrained tier; mobile differs qualitatively (10,000× more memory).
- [[ThermalWall]] / [[ThermalThrottling]] / [[PowerWall]] — the physics ceiling distinct from the battery budget.
- [[NeuralProcessingUnit]] / [[SystemOnChip]] — the hardware delivering mobile efficiency.
- [[DepthwiseSeparableConvolution]] / [[MobileNetV2]] — the operator/model that fits compute-heavy vision into the budget.
- [[ComputationalPhotography]] — the canonical multi-model mobile pipeline.
- [[WorkloadArchetype]] / [[IronLawOfMLSystems]] — mobile binds on energy (implicit term).
- [[Apple]] — Face ID, Secure Enclave, Apple Watch (HIPAA-compliant on-device ECG).
- [[mlsysbook-ch02-ml-systems]] — source.
