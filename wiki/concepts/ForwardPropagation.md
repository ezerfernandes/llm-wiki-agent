---
title: "Forward Propagation"
type: concept
tags: [deep-learning, training, foundational]
sources: [d2l-multilayer-perceptrons]
last_updated: 2026-05-16
---

# Forward Propagation

The pass from input to output of a [[NeuralNetwork]] that *computes and caches* all intermediate variables along the [[ComputationalGraph]]. Counterpart to [[Backpropagation|backward propagation]]; both halves alternate to form the training loop ([[d2l-multilayer-perceptrons]] §Forward Propagation).

## Mechanics for a one-hidden-layer MLP

Input $\mathbf{x}\in\mathbb{R}^d$, hidden weights $\mathbf{W}^{(1)}\in\mathbb{R}^{h\times d}$, output weights $\mathbf{W}^{(2)}\in\mathbb{R}^{q\times h}$, activation $\phi$, loss $\ell$, $\ell_2$ regularizer $s$:

$$
\mathbf{z} = \mathbf{W}^{(1)}\mathbf{x}, \quad
\mathbf{h} = \phi(\mathbf{z}), \quad
\mathbf{o} = \mathbf{W}^{(2)}\mathbf{h}, \quad
L = \ell(\mathbf{o}, y), \quad
J = L + s.
$$

Every intermediate ($\mathbf{z}$, $\mathbf{h}$, $\mathbf{o}$) is **retained** because [[Backpropagation]] needs them in the reverse traversal.

## Memory cost

Caching all intermediates is the dominant memory cost of training. For a depth-$L$ network at batch $B$ and width $H$, forward-pass storage is $O(LBH)$ — proportional to depth × batch × width. Inference does *not* retain activations, which is why prediction needs far less memory than training. *Gradient checkpointing* trades compute for memory by re-running forward segments during backward.

## Why "forward" and "backward" can't be decoupled

[[d2l-multilayer-perceptrons]] §Training Neural Networks: "Forward propagation and backward propagation depend on each other." The regularization term during forward depends on current $\mathbf{W}^{(l)}$ — which were updated by the *previous* backward pass; the backward gradients depend on $\mathbf{h}$ — which came from the *current* forward pass.

## Connections

- [[d2l-multilayer-perceptrons]] — §Forward Propagation; §Computational Graph.
- [[Backpropagation]] — the reverse partner.
- [[ComputationalGraph]] — the DAG along which forward proceeds.
- [[NeuralNetwork]] / [[MultilayerPerceptron]] — what forward propagates through.
- [[Autograd]] — framework engines that build the graph during the forward pass.
- [[ChainRule]] — what backward applies to the cached forward variables.
