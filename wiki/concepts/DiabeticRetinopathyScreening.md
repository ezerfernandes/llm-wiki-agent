---
title: "Diabetic Retinopathy Screening"
type: concept
tags: [medical-ai, case-study, computer-vision, edge-ml, mlsysbook]
sources: [mlsysbook-ch03-ml-workflow]
last_updated: 2026-06-05
---

# Diabetic Retinopathy Screening

The **running case study** of Reddi's *Machine Learning Systems* ([[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]): an automated system that classifies retinal fundus images as healthy or showing diabetic retinopathy (DR), threading through all six [[MLSystemLifecycle|lifecycle]] stages. DR affects ~93–103M people worldwide and is a leading cause of *preventable* blindness; rural areas have ~1 ophthalmologist per 100,000+ people, making AI-assisted screening medically essential.

It was chosen because it looks simple (image classification) but reveals deep complexity from lab to field:

- **Research result**: AUC 0.99, [[Sensitivity|sensitivity]] 97.5%, [[Specificity|specificity]] 93.4% via [[TransferLearning|transfer learning]] on ~128K labeled images (Gulshan et al. 2016).
- **Deployment reality** (Beede et al. 2020, Thai clinics): 21% of images rejected for quality in the first six months; field sensitivity dropping to 78% on older cameras; bandwidth forcing [[NVIDIAJetson|edge]] deployment; FDA/SaMD regulatory validation; silent 8% sensitivity drop after a clinic upgraded cameras.

It demonstrates that **deployment constraints, not model metrics, are the binding bottleneck** — over 80% of healthcare AI projects with strong lab accuracy never reach clinical use.

## Connections

- [[mlsysbook-ch03-ml-workflow]] — source; the case study threads every stage.
- [[Sensitivity]] / [[Specificity]] / [[AUC]] / [[ModelCalibration]] — the metrics it foregrounds.
- [[TransferLearning]] — how it reached expert accuracy with ~128K images.
- [[NVIDIAJetson]] / [[EdgeML]] — the bandwidth-forced edge architecture.
- [[FederatedLearning]] — the privacy-driven training option.
- [[ConstraintPropagationPrinciple]] / [[DataCascade]] — patterns it illustrates repeatedly.
- [[FDA]] — the regulatory-validation pathway.
- [[mlsysbook-ch03-ml-workflow]] — source.
