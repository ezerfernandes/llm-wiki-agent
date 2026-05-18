---
title: "RegNet"
type: concept
tags: [deep-learning, cnn, architecture, design-space]
sources: [d2l-convolutional-modern]
last_updated: 2026-05-16
---

# RegNet

A family of CNN architectures by [[IliaRadosavovic|Radosavovic]] et al. (2020) at [[fair|FAIR]] — the output of a **design-space optimization** approach that rejects the "find the single best network" framing of [[NeuralArchitectureSearch|NAS]] in favor of optimizing *distributions* of networks. RegNetX and RegNetY are the resulting model families, derived from a constrained AnyNet design space with explicit, interpretable design rules ([[d2l-convolutional-modern]] §cnn-design).

## AnyNet — the parent design space

A generic CNN template: **stem → body → head**, where the body has 4 stages of [[ResNeXt]] blocks. Hyperparameters per stage $i$:

- $d_i$ — depth (number of blocks)
- $c_i$ — block width (channels)
- $k_i$ — bottleneck ratio
- $g_i$ — group width (for grouped conv)

Plus $c_0$ for the stem. Total: 17 hyperparameters → $2^{17}$ configurations at coarse resolution — infeasible to enumerate.

## The design-space methodology

Radosavovic et al. proceed via empirical CDFs of error across *uniformly sampled* networks. If the CDF for a constrained sub-space matches/exceeds that of the parent space, the constraint loses nothing. Progressive constraints (AnyNetA → B → C → D → E):

1. **Tie bottleneck ratios:** $k_i = k$ ∀ $i$. **No accuracy loss.** Loses 3 hyperparameters.
2. **Tie group widths:** $g_i = g$ ∀ $i$. **No accuracy loss.** Loses 3 hyperparameters.
3. **Increase channels across stages:** $c_i \leq c_{i+1}$. **Improves performance.**
4. **Increase depth across stages:** $d_i \leq d_{i+1}$. **Improves performance.**

The final $\textrm{AnyNet}_E$ space is dramatically smaller than the original AnyNet, but contains only competitive networks.

## RegNet design principles

Examining the best-performing networks within $\textrm{AnyNet}_E$:

- **Linear width growth.** Channel count per *block index* (not just per stage) follows $c_j \approx c_0 + c_a j$. The piecewise-constant per-stage allocation is engineered to match this dependence.
- **No bottleneck.** Bottleneck ratio $k=1$ performs best. (RegNet skips bottlenecks despite using ResNeXt blocks.)

These design rules generalize across compute budgets — small RegNets and large RegNets follow the same principles.

## RegNetX vs. RegNetY

- **RegNetX**: plain ResNeXt blocks.
- **RegNetY**: adds **Squeeze-and-Excitation (SE)** modules (Hu, Shen & Sun 2018) — per-channel global attention that "allows for efficient information transfer between locations." Modest accuracy gain.

## RegNetX-32 (D2L's worked example)

`stem_channels=32, groups=16, bot_mul=1, arch=((4,32,16,1),(6,80,16,1))`:

- Stem: $3\times3$ conv to 32 channels, stride 2 + BN + ReLU.
- Stage 1: 4 ResNeXt blocks, 32 channels, 16 groups, no bottleneck. First block strides 2.
- Stage 2: 6 ResNeXt blocks, 80 channels, 16 groups, no bottleneck.
- Head: global avg pool + FC.

(The D2L example uses 2 stages for tractability; full RegNet has 4.)

## Significance

The design-space approach is positioned by [[d2l-convolutional-modern]] as a third path between:

- **Pure manual design** (AlexNet → ResNet) — slow, depends on human ingenuity, no guarantee of optimality.
- **NAS** (zoph2016neural, EfficientNet) — enormous compute cost; outputs a single network with limited transferability.
- **Design spaces** — moderate compute, outputs both a family of networks *and* interpretable design principles that transfer.

> "Identifying a distribution over networks can be a sensible strategy. In other words, we assume that there are many good needles in the haystack." — [[d2l-convolutional-modern]] §cnn-design

## Connections

- [[d2l-convolutional-modern]] — canonical reference.
- [[ResNeXt]] — the building block of AnyNet/RegNet.
- [[NeuralArchitectureSearch]] — the alternative methodology RegNet is positioned against.
- [[ResNet]] / [[CNN]] — broader family.
- [[fair]] / [[meta]] — institutional home.
- [[GroupedConvolution]] — primitive carried over from ResNeXt.
- [[Stem]] / [[NetworkHead]] — the stem/body/head template AnyNet formalizes.
