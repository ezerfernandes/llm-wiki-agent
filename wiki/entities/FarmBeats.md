---
title: "FarmBeats"
type: entity
tags: [project, precision-agriculture, edge, deployment-case-study, mlsysbook]
sources: [mlsysbook-ch01-introduction]
last_updated: 2026-06-05
---

# FarmBeats

Microsoft's precision-agriculture platform that deploys ML to farms with limited connectivity. In Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Ch 1]]) FarmBeats is the **resource-constrained edge** deployment case study: models **under 500 KB** run inference on low-power devices over **TV white-space bandwidth measured in kilobits per second**.

Its lesson: the binding constraint for edge ML is often **network bandwidth, not compute or model quality**. Even a 500 KB model update takes minutes to deliver, so **model freshness** (not accuracy) becomes the dominant failure mode. Crop-disease detection also faces [[DataDrift|drift]] across growing seasons — the same phenomenon as Waymo's weather drift, with a different engineering response dictated by machine constraints.

## Connections

- [[mlsysbook-ch01-introduction]] — the case-study source.
- [[Waymo]] / [[AlphaFold]] — the other two case studies.
- [[EdgeML]] / [[DeploymentSpectrum]] — its constrained-edge pattern.
- [[ModelCompression]] — needed to hit the <500 KB budget.
- [[microsoft|Microsoft]] — parent.
