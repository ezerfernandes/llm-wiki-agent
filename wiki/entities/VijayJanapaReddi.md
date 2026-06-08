---
title: "Vijay Janapa Reddi"
type: entity
tags: [person, author, academia, ml-systems, mlsysbook]
sources: [mlsysbook-ch01-introduction, mlsysbook-ch02-ml-systems, mlsysbook-ch03-ml-workflow, mlsysbook-ch04-data-engineering, mlsysbook-ch05-neural-computation, mlsysbook-ch08-model-training, mlsysbook-ch09-data-selection, mlsysbook-ch10-model-compression, mlsysbook-ch11-hardware-acceleration, mlsysbook-ch12-benchmarking, mlsysbook-ch13-model-serving, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Vijay Janapa Reddi

Professor at **Harvard University** and author of the open-access textbook *Machine Learning Systems* (mlsysbook.ai), whose Volume 1 ("Foundations") is being ingested into this wiki ([[mlsysbook-ch01-introduction|Ch 1: Introduction]]). His work frames ML systems engineering as a distinct discipline grounded in the *physics of computation* — the [[IronLawOfMLSystems|iron law]], the energy tax, the [[DAMTaxonomy|D·A·M taxonomy]], and the [[MemoryWall|memory wall]] — rather than algorithmic intuition. He is closely associated with the [[MLPerf]] benchmarking effort.

## Connections

- [[mlsysbook-ch01-introduction]] / [[mlsysbook-ch02-ml-systems]] / [[mlsysbook-ch03-ml-workflow]] / [[mlsysbook-ch04-data-engineering]] / [[mlsysbook-ch05-neural-computation]] / [[mlsysbook-ch08-model-training]] / [[mlsysbook-ch09-data-selection]] — chapters he authored (Ch 2 develops the deployment-paradigm framework; Ch 3 the [[MLWorkflow|ML workflow]]; Ch 4 [[DataEngineering|data engineering]]; Ch 5 — opening Build-part chapter — treats [[NeuralNetwork|neural computation]] as the systems workload; Ch 8 — Build-part capstone — treats [[mlsysbook-ch08-model-training|model training]] as a systems problem via the [[IronLawOfTrainingPerformance|iron law of training]]; Ch 9 — opening the Optimize part — develops [[DataSelection|data selection]] and the [[InformationComputeRatio|ICR]] framework).
- [[Harvard]] — his institution / the book's host.
- [[MachineLearningSystems]] / [[MLSystemsEngineering]] — the discipline he defines.
- [[DeploymentSpectrum]] / [[CloudML]] / [[EdgeML]] / [[MobileML]] / [[TinyML]] — the four-paradigm framework he formalizes in Ch 2.
- [[MLPerf]] / [[MLCommons]] / [[mlsysbook-ch12-benchmarking]] — Reddi leads the MLPerf/MLCommons benchmarking effort; his Ch 12 (capstone of the Optimize part) is the authoritative in-book treatment of [[Benchmarking|benchmarking]].
- [[BitterLesson]] — the organizing principle he builds on.
- [[ModelCompression]] / [[mlsysbook-ch10-model-compression]] — his Ch 10 organizes compression into a three-dimension stack governed by the [[ConservationOfComplexity|conservation of complexity]] meta-law.
- [[mlsysbook-ch13-model-serving]] / [[ModelServing]] — his Ch 13 opens the Deploy part, formalizing the **serving inversion** (throughput→latency), [[QueuingTheory|queuing theory]], the [[LatencyBudget|latency budget]], and [[LLMServing|LLM serving]].
- [[mlsysbook-ch14-ml-operations]] — author/lead of *Introduction to Machine Learning Systems*; Ch 14 (ML Operations) frames the silent-failure thesis and the five MLOps principles.

