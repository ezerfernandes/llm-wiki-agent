---
title: "Skip Connection"
type: concept
tags: [deep-learning, architecture, foundational, mlsysbook]
sources: [mlsysbook-ch06-network-architectures]
last_updated: 2026-06-05
---

# Skip Connection

A path that routes a layer's input *past* one or more intervening layers and recombines it with their output — the general family that includes the **[[ResidualConnection|residual connection]]** $\mathbf{y}=\mathcal{F}(\mathbf{x})+\mathbf{x}$ (addition) and U-Net-style long-range copies (concatenation). In [[mlsysbook-ch06-network-architectures]] (Reddi, *Machine Learning Systems* Vol 1, Ch 6), skip connections are presented as one of the **portable building blocks** that, though born in [[CNN|CNNs]] ([[ResNet]]), migrated to every modern architecture including [[Transformer|transformers]].

## Why it matters

- **Solves the depth problem.** [[Backpropagation|Backprop]] through many plain layers multiplies arbitrary Jacobians, causing [[VanishingGradient|vanishing]] or [[ExplodingGradient|exploding]] gradients. A residual block's Jacobian is $\mathbf{I}+\mathcal{F}'$, with eigenvalues clustered near 1 — a "gradient highway" that lets the signal flow unimpeded through 100+ layers *by construction* rather than by tuning.
- **Empirical contrast (ResNet/CIFAR-10):** a 56-layer *plain* net had worse error (~13.6%) than a 20-layer plain net (~8.8%) — the degradation problem — but a 56-layer *residual* net reached ~7.0%.
- **Depth needs architectural support:** <20 layers train fine without skips; 20–100 layers require them; >100 layers require skips **plus** careful normalization (pre-activation ResNet-v2).
- **Systems cost:** storing each block's input for the forward add and backprop adds ~20% activation memory and ~10% per-epoch compute on ResNet-50 — but total training time *drops* because the network actually converges.

## Connections

- [[mlsysbook-ch06-network-architectures]] — frames skip connections as a portable building block solving gradient flow.
- [[ResidualConnection]] / [[ResidualBlock]] / [[ResNet]] — the canonical additive form.
- [[VanishingGradient]] / [[ExplodingGradient]] / [[Backpropagation]] / [[ChainRule]] — the gradient-flow problem skips address.
- [[Transformer]] — wraps every sub-layer in a residual path; skips are a prerequisite for deep transformers.
- [[BatchNormalization]] / [[LayerNormalization]] — the complementary block: skips ensure gradients *reach* early layers, normalization ensures they have *stable magnitude*.
- [[CNN]] — the family skip connections were born in.
