---
title: "Backpropagation"
type: concept
tags: [deep-learning, optimization, vector-calculus, foundational]
sources: [mml-ch05-vector-calculus, mml-book, d2l-preliminaries, d2l-multilayer-perceptrons, d2l-convolutional-neural-networks, ai-engineering-ch07-finetuning, mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Backpropagation

The chain-rule-based algorithm for computing gradients of a scalar loss with respect to every parameter in a computational graph, by propagating errors **backward** through the graph ([[mml-book]] §5.6).

For a composition $f = f_K\circ f_{K-1}\circ\cdots\circ f_1$, the chain rule gives:

$$\frac{df}{d\mathbf{x}} = \frac{df_K}{d f_{K-1}}\cdot\frac{df_{K-1}}{d f_{K-2}}\cdots\frac{df_1}{d\mathbf{x}}.$$

Backprop computes this product **right-to-left** (output ⇒ input), reusing intermediate [[Jacobian]] matrices. The key insight: each layer's local Jacobian is multiplied by the *accumulated* gradient from the layer above — so storage is $O(\text{depth})$, not $O(\text{depth}^2)$.

## Why it works for neural networks

Modern deep nets have $10^9$–$10^{12}$ parameters but a single scalar loss. Backprop is **reverse-mode** [[AutomaticDifferentiation]] — its cost is roughly constant in the number of parameters and *linear* in the depth of the graph. Forward-mode AD would cost $O(\text{params})$ per scalar loss derivative, which is impractical.

## The two pieces

1. **Forward pass**: compute $f_1(\mathbf{x}), f_2(f_1(\mathbf{x})), \dots, f_K\circ\cdots\circ f_1(\mathbf{x})$, *caching activations*.
2. **Backward pass**: compute $\nabla_{f_K}f = 1$, then iteratively $\nabla_{f_{k-1}}f = \nabla_{f_k}f \cdot \frac{df_k}{df_{k-1}}$ using cached activations.

The cached activations are what make backprop memory-hungry — every modern memory-saving technique ([[GradientCheckpointing|gradient checkpointing]], reversible nets, [[FlashAttention]]'s recomputation) targets this storage.

## Worked example: one-hidden-layer MLP with $\ell_2$

[[d2l-multilayer-perceptrons]] §Backpropagation works through the gradients for $\mathbf{z} = \mathbf{W}^{(1)}\mathbf{x}$, $\mathbf{h} = \phi(\mathbf{z})$, $\mathbf{o} = \mathbf{W}^{(2)}\mathbf{h}$, $J = L + s$ with $s = \tfrac{\lambda}{2}(\|\mathbf{W}^{(1)}\|_F^2 + \|\mathbf{W}^{(2)}\|_F^2)$:

$$
\frac{\partial J}{\partial \mathbf{W}^{(2)}} = \frac{\partial J}{\partial\mathbf{o}}\mathbf{h}^\top + \lambda\mathbf{W}^{(2)}, \quad
\frac{\partial J}{\partial \mathbf{z}} = \frac{\partial J}{\partial\mathbf{h}}\odot \phi'(\mathbf{z}),
$$

and so on — the canonical chain-rule + Hadamard-product walk used to motivate every framework's autograd implementation.

## From [[mml-ch05-vector-calculus|MML Ch 5]]

§5.6 is the canonical reference. MML motivates backprop by the impracticality of explicit symbolic gradients: for $f(x)=\sqrt{x^2+\exp(x^2)}+\cos(x^2+\exp(x^2))$ (Eq. 5.109) the analytic derivative (5.110) is a long, expensive expression — *"if we are not careful, the implementation of the gradient could be significantly more expensive than computing the function."* Backprop (citing Kelley 1960; Bryson 1961; Dreyfus 1962; Rumelhart et al. 1986) avoids this.

**§5.6.1 — gradients in a deep network.** A net is the composition $\mathbf{y}=(f_K\circ\cdots\circ f_1)(\mathbf{x})$ (Eq. 5.111), layers $\mathbf{f}_i=\sigma_i(\mathbf{A}_{i-1}\mathbf{f}_{i-1}+\mathbf{b}_{i-1})$ (Eq. 5.113), squared loss $L=\|\mathbf{y}-\mathbf{f}_K\|^2$ (Eq. 5.114). The chain rule for $\frac{\partial L}{\partial\boldsymbol\theta_i}$ (Eqs. 5.115–5.118) shows the recursion reuses upstream work: *"Assuming we have already computed the partial derivatives $\partial L/\partial\boldsymbol\theta_{i+1}$, then most of the computation can be reused to compute $\partial L/\partial\boldsymbol\theta_i$."* Orange terms = layer-output-w.r.t.-input; blue terms = layer-output-w.r.t.-parameters.

**§5.6.2 — backprop *is* [[ReverseModeAutodiff|reverse-mode]] [[AutomaticDifferentiation|automatic differentiation]].** MML's headline statement: *"backpropagation is a special case of a general technique... called automatic differentiation"* — a numeric-but-exact (up to machine precision) gradient, distinct from both symbolic differentiation and finite differences. Formalized over a [[ComputationalGraph|computation graph]]: set $\frac{\partial f}{\partial x_D}=1$ (Eq. 5.144), accumulate backward via $\frac{\partial f}{\partial x_i}=\sum_{x_j:\,x_i\in\mathrm{Pa}(x_j)}\frac{\partial f}{\partial x_j}\frac{\partial g_j}{\partial x_i}$ (Eq. 5.145). Reverse mode wins because *"the input dimensionality is often much higher than the dimensionality of the labels."* Deep insight (Example 5.14): **gradient cost ≈ function cost**, even when the symbolic derivative looks far worse.

## Combined with optimization

Backprop computes *gradients*; it does not update parameters. The downstream consumer is some variant of [[GradientDescent]] (vanilla, [[Momentum]], [[Adam]]). Together: **backprop + SGD = the entire training loop of every neural network in this wiki**.

## Failure modes

- **Vanishing gradient**: in deep stacks the Jacobian product shrinks exponentially → early layers see no signal. Fixes: ReLU, skip connections, batch norm, careful initialization.
- **[[ExplodingGradient|Exploding gradient]]**: the same product grows exponentially in the other direction. Fixes: gradient clipping, weight regularization, residual connections.

## Connections

- [[mml-book]] — §5.6 canonical reference.
- [[d2l-multilayer-perceptrons]] — worked one-hidden-layer-MLP example.
- [[ForwardPropagation]] — the cached-activation pass backward consumes.
- [[ChainRule]] — the calculus underneath.
- [[Jacobian]] — per-layer local linear approximation.
- [[AutomaticDifferentiation]] — backprop is reverse-mode AD.
- [[GradientDescent]] — what consumes backprop's output.
- [[Autograd]] — the [[PyTorch]] implementation.
- [[FlashAttention]] — recomputation strategy that saves backprop activations.
- [[CreditAssignment]] / [[ModelSize]] — the problem backprop solves and its training-memory consequence.
- [[mlsysbook-ch05-neural-computation]] — systems framing: 2× forward FLOPs, O(1)× cost, activation-storage memory gap.

## From [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]]

Ch 7 uses the **forward + backward pass decomposition** of backprop to motivate the [[MemoryBottleneck|memory bottleneck]] in finetuning — the chapter's central technical framing. [[ChipHuyen|Huyen]]'s simplified description:

- **Forward pass**: compute output from input (the inference path).
- **Backward pass**: compare prediction vs ground truth → compute [[Loss|loss]] → compute [[Gradient|gradient]] for each [[TrainableParameters|trainable parameter]] (derivative of loss w.r.t. each param) → use [[OptimizerState|optimizer]] (SGD / momentum / [[Adam]]) to convert gradient into a weight update.

This decomposition is what derives the [[TrainingMemoryFormula|training-memory formula]]:

> training memory = model weights + activations + gradients + optimizer states

Each trainable parameter requires **1 gradient + 0–2 optimizer-state values** depending on optimizer: vanilla SGD = 0; momentum = 1; Adam = 2. For a 13B model in FP16 with Adam, gradients + optimizer states alone = 13B × 3 × 2 bytes = **78 GB** (typically dwarfing the 26 GB weight footprint).

### Why training is harder than inference at low precision

Ch 7's footnote on this point: *"During training, the model's weights are updated via multiple steps. Small rounding changes can compound during the training process, making it difficult for the model to achieve the desirable performance. On top of that, loss values require precise computation. Small changes in the loss value can point parameter updates in the wrong direction."*

This is the **fundamental reason** [[QuantizationAwareTraining|QAT]] and [[MixedPrecisionTraining|mixed-precision]] training exist — you can't naively quantize during training the way you can for [[PostTrainingQuantization|PTQ]].

### Alternatives Ch 7 mentions

- **Evolutionary strategies** (Maheswaranathan et al.) — random search + surrogate gradients instead of real gradients.
- **Direct feedback alignment** (Arild Nøkland, 2016) — alternative credit-assignment scheme.

These remain experimental — backprop + variants of SGD remain "by far the most widely used" mechanism for transformer training.

## Systems framing (mlsysbook Ch 5)

[[mlsysbook-ch05-neural-computation|mlsysbook Vol 1 Ch 5]] defines backprop as "the efficient application of the chain rule to a [[ComputationalGraph|computational graph]], computing the gradient of the loss w.r.t. every parameter in a single backward traversal to solve the **[[CreditAssignment|credit assignment problem]]**" (illustrated with a factory-assembly-line analogy). Key quantitative claims:

- The backward pass costs **~2× the forward-pass FLOPs** and computes all P gradients in **one** pass — O(1)× the forward cost regardless of model size, vs numerical differentiation's O(P)× (P perturbed forward passes).
- The three per-layer gradient components: weight `∂L/∂W = A^(ℓ-1)ᵀ · ∂L/∂Z`, bias `∂L/∂b = 1ᵀ · ∂L/∂Z`, input `∂L/∂A^(ℓ-1) = ∂L/∂Z · W^(ℓ)ᵀ`.
- **Common pitfall**: backprop is *not* learning — it computes gradients; the optimizer performs the update. "Backpropagation determines the memory footprint; the optimizer determines the additional state overhead."
- For the MNIST MLP at batch 32, the stored-activation requirement makes **training ~4× the inference memory** — the structural driver behind [[GradientCheckpointing|gradient checkpointing]] and [[ModelParallelism|model parallelism]] (see [[ModelSize]]).
