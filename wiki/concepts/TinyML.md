---
title: "TinyML"
type: concept
tags: [ml-systems, edge, embedded, mlsysbook, deployment]
sources: [mlsysbook-ch01-introduction, mlsysbook-ch02-ml-systems, mlsysbook-ch07-ml-frameworks, mlsysbook-ch10-model-compression, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# TinyML

Machine learning that runs on **microcontrollers and embedded devices under severe memory, compute, and energy constraints** — the extreme low end of the [[DeploymentSpectrum|deployment spectrum]] in Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]).

Representative archetype: an **ESP32-S3** with ~512 KB of RAM and a sub-watt (milliwatt) power budget. Smart-home wake-word detectors must recognize voice commands using less power than an LED bulb; battery sensors must run for months to years. The Smart Doorbell scenario (running [[KeywordSpotting]] / Wake Vision on a microcontroller with a "one-year battery life" mission) recurs throughout the book.

The cloud-to-TinyML gap spans **~10⁷× in compute and ~10⁶× in memory**, which is why a cloud model cannot simply be "shrunk" — each tier requires full [[DAMTaxonomy|D·A·M]] redesign. TinyML is made feasible by [[ModelCompression|model compression]]: aggressive [[Quantization|quantization]], [[Pruning|pruning]], and [[KnowledgeDistillation|distillation]], often reducing model size by over 90%.

[[mlsysbook-ch02-ml-systems|Ch 2]] argues TinyML is *qualitatively distinct*, not "scaled-down [[MobileML|mobile ML]]": it is the [[WorkloadArchetype|Tiny Constraint]] archetype where the objective shifts from minimizing latency to minimizing **energy per inference** (~10 µJ for keyword spotting, ~100,000,000× more efficient than a cloud LLM query). The **1 mW threshold** is the physical boundary where ambient [[EnergyHarvesting|energy harvesting]] flips deployment from "battery-limited" to "deploy-and-forget"; a CR2032 coin cell (~675 mWh) then powers a device for 1–10 years. Devices have only 32–512 KB of on-chip SRAM (no virtual memory/DRAM), forcing a memory-fit constraint ($M_{model} \le C_{mem}$) and an inference-only regime; FP32→INT8 quantization alone is insufficient below 64 KB, requiring full architectural redesign and 10K–100K-parameter models. Ecosystem fragmentation across ARM Cortex-M / RISC-V / Xtensa multiplies engineering cost.

## Framework view from [[mlsysbook-ch07-ml-frameworks|mlsysbook Vol 1 Ch 7]]

Ch 7 places TinyML at the extreme end of the [[CompilationContinuum|compilation continuum]]: MCUs with kilobytes of memory "cannot afford the overhead of a Python interpreter or a fully dynamic runtime." Micro-runtimes like [[TensorFlowLite|TF Lite Micro]] use a tiny C/C++ interpreter over a flat model with a **fixed memory arena** (the app supplies a contiguous tensor arena; no heap allocation after setup, since one `malloc()` failure on a 256 KB device is unrecoverable). A standard PyTorch runtime is ~500 MB; the Python interpreter alone ~20 MB — orders of magnitude larger than the device. The silicon contract here is strictly memory-bound: the working-set activations must fit in SRAM.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — TinyML micro-runtimes as the AOT/static extreme of the compilation continuum.
- [[TensorFlowLite]] / [[CompilationContinuum]] — the runtime and the principle.
- [[DeploymentSpectrum]] / [[SystemArchetype]] — TinyML is the lowest tier.
- [[EdgeML]] / [[MobileML]] — the adjacent (less constrained) tiers; TinyML differs qualitatively, not just in scale.
- [[WorkloadArchetype]] — TinyML serves the Tiny Constraint archetype (energy-per-inference bound).
- [[EnergyHarvesting]] — what the sub-1-mW budget enables.
- [[ModelCompression]] / [[Quantization]] / [[Pruning]] / [[KnowledgeDistillation]] — the enabling techniques.
- [[KeywordSpotting]] / [[WakeWordDetection]] — the canonical TinyML Lighthouse Model and use case.
- [[Microcontroller]] — the hardware substrate.
- [[mlsysbook-ch10-model-compression]] — Ch 10 makes compression *existential* for TinyML: a ~256 KB-SRAM microcontroller leaves ~100 KB for weights, so even INT8 isn't enough — the [[DSCNN]] keyword spotter + [[Binarization|INT4/binary]] quantization are required, and quantization here cuts both the iron-law $D_{vol}$ and compute terms (1-month → 4-month battery).
- [[mlsysbook-ch01-introduction]] / [[mlsysbook-ch02-ml-systems]] — sources.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 details TinyML edge operations: <1 MB / mW budgets, TFLite Micro/CMSIS-NN (no dynamic allocation), 90%+ sparsity, OTA updates, designed-in graceful degradation.

