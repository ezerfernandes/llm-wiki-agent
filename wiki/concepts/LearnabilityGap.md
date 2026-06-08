---
title: "Learnability Gap"
type: concept
tags: [deep-learning, theory, architectures, generalization, mlsysbook]
sources: [mlsysbook-ch06-network-architectures]
last_updated: 2026-06-05
---

# Learnability Gap

The gap between **what an architecture *can represent*** (representation capacity) and **what it *can learn*** with finite samples and compute (learnability). Introduced in [[mlsysbook-ch06-network-architectures]] (Reddi, *Machine Learning Systems* Vol 1, Ch 6) to resolve an apparent paradox: if [[MultilayerPerceptron|MLPs]] are universal approximators ([[UniversalApproximationTheorem]]), why has architectural innovation driven deep-learning progress?

## The three factors

1. **Sample complexity** — the UAT gives no bound on training examples. Sample complexity can scale as $\mathcal{O}(\exp(d_{\text{in}}))$ for an MLP but $\mathcal{O}(\text{poly}(d_{\text{in}}))$ for an architecture whose [[InductiveBias|inductive bias]] matches the data structure.
2. **Parameter efficiency** — required width can be exponential in input dimension (e.g. approximating $\sum_i \sin(x_i)$ may need $\mathcal{O}(\exp(d_{\text{in}}))$ MLP neurons vs $\mathcal{O}(d_{\text{in}})$ for a structure-matching architecture).
3. **Optimization difficulty** — even when optimal weights exist, gradient descent may not find them; specialized architectures introduce symmetries that constrain the search space.

## The canonical example (MNIST)

An MLP (784→4096→4096→10) uses **~20M parameters** for ~97–98% accuracy; a CNN uses **~420K** for ~99% — a **~47× parameter reduction with higher accuracy**, because the CNN's locality bias matches the spatial structure of images. The *manifold hypothesis* underwrites why learning is feasible at all: valid data occupies a low-dimensional surface within the full high-dimensional space.

## Connections

- [[mlsysbook-ch06-network-architectures]] — defines the learnability gap and the MNIST MLP-vs-CNN comparison.
- [[UniversalApproximationTheorem]] — guarantees representation but not learnability.
- [[InductiveBias]] — closing the gap is the act of matching bias to data structure.
- [[NoFreeLunchTheorem]] — the bias that aids one task hurts another.
- [[MultilayerPerceptron]] / [[CNN]] — the architectures contrasted.
- [[Generalization]] — the practical payoff of a smaller, well-matched hypothesis space.
