---
title: "Crowdsourcing"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, data-acquisition, labeling]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Crowdsourcing

A [[DataAcquisition|data-acquisition]] and labeling strategy that distributes microtasks to a large pool of contributors (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]). It shifts the bottleneck from *finding enough examples* to *controlling the quality of many parallel judgments*.

Demonstrated at landmark scale by [[ImageNet]] ([[AmazonMechanicalTurk|Mechanical Turk]], millions of images into thousands of classes). Two systems advantages: **scalability** through parallel microtask distribution, and **diversity** from a global contributor pool's range of accents, cultural contexts, and linguistic variations — directly improving model generalization. The cost is that task design, validation, and iteration become part of the acquisition system. For KWS, crowdsourced wake-word audio still needs acoustic checks (SNR, duration, recording validity) before entering the training set.

## Connections

- [[DataAcquisition]] — the parent strategy space.
- [[AmazonMechanicalTurk]] — the canonical platform.
- [[WebScraping]] / [[SyntheticDataGeneration]] — sibling acquisition channels.
- [[DataLabeling]] — crowdsourcing as a labeling mode.
- [[mlsysbook-ch04-data-engineering]] — source.
