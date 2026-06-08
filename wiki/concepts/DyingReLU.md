---
title: "Dying ReLU Problem"
type: concept
tags: [neural-networks, activation-functions, training, deep-learning]
sources: [mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Dying ReLU Problem

A failure mode of the [[ReLU]] activation where neurons permanently output zero and cease learning. If a neuron's weights evolve so that its preactivation `z = wᵀx + b` is consistently negative across *all* training examples, ReLU outputs 0 for every input — and since ReLU's gradient is also 0 for negative inputs, **no gradient flows back** through that neuron during [[Backpropagation|backpropagation]], so its weights can never update. The neuron stays dead.

Per [[mlsysbook-ch05-neural-computation|mlsysbook Vol 1 Ch 5]], this often results from **large learning rates** pushing weights into unfavorable regions, and in extreme cases **10–40% of a network's neurons can die** during training. From a systems view, dead neurons are *wasted capacity*: they consume memory and compute during inference but contribute nothing to the output.

## Mitigation

- Careful initialization (He init, He et al. 2015).
- Moderate [[LearningRate|learning rates]].
- Architectural choices: leaky ReLU variants, [[BatchNormalization|batch normalization]] (Ioffe & Szegedy 2015).

## Connections

- [[ReLU]] — the activation that exhibits the problem.
- [[ActivationFunction]] / [[GELU]] / [[SiLU]] — alternatives that avoid hard-zero gradients.
- [[Backpropagation]] / [[VanishingGradient]] — the gradient-flow context.
- [[BatchNormalization]] / [[LearningRate]] — mitigations.
- [[mlsysbook-ch05-neural-computation]] — source.
