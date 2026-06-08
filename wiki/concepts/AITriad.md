---
title: "AI Triad"
type: concept
tags: [ml-systems, framework, mlsysbook, foundations]
sources: [mlsysbook-ch01-introduction]
last_updated: 2026-06-05
---

# AI Triad

The recognition that **Data, Algorithm, and Machine are three fundamentally interdependent elements** of every ML system — *Data* (the fuel), *Algorithm* (the blueprint), and *Machine* (the engine). Without any one, the others remain theoretical. Introduced in Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]) and operationalized as the [[DAMTaxonomy|D·A·M taxonomy]].

The triad is drawn with bidirectional arrows: the algorithm dictates the compute demand and the data volume required; the data's scale and complexity determine which machines and algorithms are feasible; the machine's capacity bounds both model scale and data throughput. **ML systems engineering is the discipline of keeping all three axes in balance** — optimizing one in isolation typically shifts the bottleneck rather than eliminating it.

## Connections

- [[DAMTaxonomy]] — the diagnostic form ("which axis is the bottleneck?").
- [[MachineLearningSystems]] — the systems the triad describes.
- [[IronLawOfMLSystems]] — quantifies the trade-offs among the axes.
- [[SamplesPerDollar]] — the economic constraint unifying the three axes.
- [[mlsysbook-ch01-introduction]] — source.
