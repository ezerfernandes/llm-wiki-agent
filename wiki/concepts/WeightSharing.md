---
title: "Weight Sharing"
type: concept
tags: [deep-learning, cnn, architectures, parameter-efficiency, mlsysbook]
sources: [mlsysbook-ch06-network-architectures]
last_updated: 2026-06-05
---

# Weight Sharing

Reusing the **same learned parameters across many positions** in a computation — applying one feature detector at every spatial location ([[CNN|CNNs]]) or one weight matrix at every time step ([[RNN|RNNs]]). It is the mechanism that decouples parameter count from input size and is the source of [[CNN|convolution]]'s and [[RNN|recurrence]]'s efficiency. Emphasized in [[mlsysbook-ch06-network-architectures]] (Reddi, *Machine Learning Systems* Vol 1, Ch 6) as the key innovation enabling CNNs to process high-resolution inputs within a single accelerator's memory budget.

## Why it matters (systems view)

- **Constant-parameter scaling.** A 3×3, 64-in/64-out conv layer needs ~37K parameters *regardless* of whether the image is 224×224 or 1024×1024; the equivalent fully-connected layer on a 224×224×64 input would need ~205M — a ~5,500× difference.
- **High [[ArithmeticIntensity|arithmetic intensity]].** A shared filter weight is reused across all 50,176 spatial positions of a 224×224 feature map, amortizing each weight load over many MACs — the reason CNNs are compute-bound rather than bandwidth-bound, and energy-efficient.
- **In RNNs**, weights are reused across every time step (high temporal locality), so the parameter count is independent of sequence length.
- It is also a form of [[InductiveBias|inductive bias]]: weight sharing encodes [[TranslationInvariance|translation equivariance]] — the same pattern means the same thing anywhere.

## Connections

- [[mlsysbook-ch06-network-architectures]] — frames weight sharing as the parameter-reduction innovation of CNNs.
- [[CNN]] / [[Convolution]] / [[TranslationInvariance]] — spatial weight sharing.
- [[RNN]] — temporal weight sharing (weight-tied across time).
- [[InductiveBias]] — weight sharing is a structural prior.
- [[ArithmeticIntensity]] — high weight reuse raises FLOP/byte, making the workload compute-bound.
