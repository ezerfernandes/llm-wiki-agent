---
title: "USPS Digit Recognition"
type: concept
tags: [case-study, neural-networks, deployment, ocr, ml-systems, history]
sources: [mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# USPS Digit Recognition

The early-1990s United States Postal Service handwritten ZIP-code reading system — one of the first large-scale, mission-critical neural-network deployments and the canonical end-to-end ML-systems case study in [[mlsysbook-ch05-neural-computation|mlsysbook Vol 1 Ch 5]]. Built on **[[LeNet]]** ([[YannLeCun|LeCun]] et al. 1989, 1998), the same convolutional lineage that produced the [[MNIST]] benchmark.

## By the numbers (LeNet deployment)

| Metric | Neural Network | Human Operators |
|---|---|---|
| Error rate | **1%** | 2.5% |
| Rejection rate | 9% | — |
| Throughput | 10–30 digits/sec | ~1 digit/sec |
| Parameters | ~10,000 | — |
| Training | 3 days / 23 epochs (Sun-4/260) | — |

The network beat human accuracy *and* ran 10–30× faster. The **9% rejection rate was the economically optimal trade-off** — uncertain digits routed to humans rather than risking misrouted mail. By the late 1990s, LeNet-style systems read millions of checks/day.

## Why it is the template

Success depended on the *whole pipeline* sharing one operating constraint (national-scale throughput, bounded error): robust **preprocessing** (lighting/size/orientation normalization, [[DataAugmentation|augmentation]]), neural **inference**, **postprocessing** (confidence thresholds, routing to human review), and physical sorting. This *capture → preprocess → infer → postprocess → act* architecture remains the template for production ML 30+ years later, and the modern "then vs now" comparison shows the **algorithm unchanged** while hardware improved orders of magnitude — validating algorithm–hardware co-design and the [[DAMTaxonomy|D·A·M]] alignment of Data, Algorithm, Machine.

## Connections

- [[LeNet]] / [[CNN]] / [[Convolution]] — the deployed architecture.
- [[YannLeCun]] — built LeNet, MNIST, the USPS recognizer.
- [[MNIST]] — the benchmark that grew out of this data-collection effort.
- [[DAMTaxonomy]] — the alignment principle the case study illustrates.
- [[Inference]] / [[DataAugmentation]] — pipeline stages.
- [[mlsysbook-ch05-neural-computation]] — source.
