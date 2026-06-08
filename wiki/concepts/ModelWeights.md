---
title: "Model Weights"
type: concept
tags: [ml-systems, neural-networks, mlsysbook, foundations]
sources: [mlsysbook-ch01-introduction]
last_updated: 2026-06-05
---

# Model Weights

The **learned numerical parameters of a neural network** — one value per connection between units. In the [[Software2|Software 2.0]] framing of Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]), the weights are the *binary executable* "compiled" from training data by the [[StochasticGradientDescent|SGD]] training loop.

Weight count is the single largest determinant of both memory footprint ($D_{vol}$) and serving cost, because **every inference request must load the weights through the memory hierarchy.** A GPT-3-scale model stores ~175 billion such values, consuming ~350 GB in FP16. This is why weight loading makes large language model decode [[MemoryBandwidth|bandwidth-bound]].

## Connections

- [[Software2]] — weights as the "executable."
- [[StochasticGradientDescent]] — the "compiler" that produces them.
- [[MemoryBandwidth]] / [[IronLawOfMLSystems]] — why loading weights dominates the data term.
- [[GPT3]] — the 350 GB footprint exemplar.
- [[Quantization]] — reduces weight precision to shrink the footprint.
- [[mlsysbook-ch01-introduction]] — source.
