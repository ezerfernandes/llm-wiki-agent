---
title: "Keyword Spotting"
type: concept
tags: [tinyml, audio, edge, benchmark, mlsysbook]
sources: [mlsysbook-ch01-introduction, mlsysbook-ch02-ml-systems, mlsysbook-ch04-data-engineering, mlsysbook-ch06-network-architectures]
last_updated: 2026-06-05
---

# Keyword Spotting

Always-on detection of wake words / voice commands (e.g. "Alexa", "Hey Google") on tiny devices — used in Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]) as the **power-envelope [[LighthouseModel|Lighthouse Model]]** and the canonical [[TinyML]] workload. The question it poses is *"can I run always-on inference on milliwatts?"*

A keyword-spotting model must operate within a power budget often **below one milliwatt** to enable months of battery-powered operation, demanding *extreme* [[Quantization|quantization]] and specialized architectures. It is the workload behind the recurring Smart Doorbell mission (Wake Vision on a [[Microcontroller|microcontroller]] with a one-year-battery-life requirement).

[[mlsysbook-ch02-ml-systems|Ch 2]] uses KWS (a depthwise-separable-convolution net for MCUs) as the **Tiny Constraint** [[WorkloadArchetype|archetype]] anchor: ~10 µJ/inference (~100,000,000× more efficient than a cloud LLM query, the basis for years of coin-cell operation) and ~800 KB at FP32 in the book's lighthouse setup. It is also the canonical *hybrid*/[[WakeWordDetection|wake-word]] case — local always-on detection gates higher-power cloud NLP. The Smart Doorbell scorecard shows it passing a KB memory budget but *failing* a strict 50 ms latency target on an ESP32-S3 (101 ms baseline), motivating compression.

[[mlsysbook-ch04-data-engineering|Ch 4]] (Data Engineering) uses KWS as the **lighthouse running through the entire data-engineering lifecycle**: design-space targets (98% accuracy, <200 ms, <1 false wake/month, $150K budget, ≤64 KB always-on island); the false-positive math (1 false wake/month over 1-second windows ⇒ >99.9999% rejection, FPR ≈ 3.9×10⁻⁷, evaluated on False Accepts per Hour); multi-source acquisition (Speech Commands + MSWC's 23.4M samples / 50 languages + scraping + synthetic); audio processing into [[MFCC]]/[[Spectrogram|spectrogram]] features; automated [[ForcedAlignment|forced-alignment]] labeling (manual would take ~32 person-years); and a tiered storage budget (736 GB).

## Connections

- [[LighthouseModel]] — the power-envelope probe.
- [[MFCC]] / [[Spectrogram]] — the audio feature transforms in the KWS processing pipeline ([[mlsysbook-ch04-data-engineering|Ch 4]]).
- [[ForcedAlignment]] — the automated labeling that makes corpus-scale KWS feasible.
- [[WorkloadArchetype]] — KWS is the Tiny Constraint (energy-per-inference bound) archetype.
- [[WakeWordDetection]] — the always-on use case and hybrid-pipeline first stage.
- [[TinyML]] — the deployment regime.
- [[DepthwiseSeparableConvolution]] — the efficient operator KWS models use.
- [[Quantization]] / [[ModelCompression]] — the enabling techniques.
- [[Microcontroller]] — the hardware substrate.
- [[mlsysbook-ch01-introduction]] / [[mlsysbook-ch02-ml-systems]] — sources.
- [[mlsysbook-ch06-network-architectures]] — KWS (a DS-CNN) is the *power* [[LighthouseModel|Lighthouse Model]]: the extreme TinyML end, running always-on on microcontrollers with milliwatt budgets via [[DepthwiseSeparableConvolution|depthwise separable convolutions]] and extreme [[Quantization|INT8/INT4 quantization]] — "forcing engineers to count every byte and cycle."
