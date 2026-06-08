---
title: "NVIDIA Jetson"
type: entity
tags: [hardware, edge-ml, nvidia, accelerator, mlsysbook]
sources: [mlsysbook-ch03-ml-workflow]
last_updated: 2026-06-05
---

# NVIDIA Jetson

[[NVIDIA]]'s family of compact GPU-accelerated **edge AI** modules, spanning a wide SKU spectrum: Jetson Orin Nano (7–15 W), Jetson Orin NX (10–25 W), and Jetson AGX Orin (15–60 W). In Reddi's *Machine Learning Systems* ([[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]) it is the canonical edge hardware for the [[DiabeticRetinopathyScreening|DR screening]] case study: an Orin Nano-class device (4–8 GB shared LPDDR5, 7–15 W) provides the integrated GPU compute to preprocess retinal images locally — necessary once the bandwidth analysis showed cloud-only upload would saturate a rural clinic's 2 Mbps uplink.

Its tight memory and power budget imposes the chapter's central [[EdgeML|edge]] trade-off: model complexity becomes a direct function of per-clinic hardware cost, forcing aggressive [[ModelCompression|model compression]]. The Ch 3 economics example assumes a Jetson-based edge deployment paying back its CapEx within a few years against cloud OpEx.

## Connections

- [[NVIDIA]] — manufacturer.
- [[EdgeML]] / [[DeploymentSpectrum]] — the deployment paradigm Jetson serves.
- [[DiabeticRetinopathyScreening]] — the case study that selects it.
- [[ModelCompression]] / [[Quantization]] — required to fit models in its memory budget.
- [[mlsysbook-ch03-ml-workflow]] — source.
