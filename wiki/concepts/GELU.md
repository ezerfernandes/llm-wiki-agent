---
title: "GELU"
type: concept
tags: [activation-function, transformer]
sources: [d2l-attention-and-transformers]
last_updated: 2026-05-16
---

# GELU (Gaussian Error Linear Unit)

An [[ActivationFunction|activation function]] introduced by [[Hendrycks.Gimpel.2016|Hendrycks & Gimpel 2016]]:

$$\textrm{GELU}(x) = x \cdot \Phi(x)$$

where $\Phi$ is the standard Gaussian CDF. Approximation:

$$\textrm{GELU}(x) \approx 0.5 x \left(1 + \tanh\!\left[\sqrt{2/\pi}\,(x + 0.044715 x^3)\right]\right).$$

A "smoother version of [[ReLU]]" — its derivative is everywhere nonzero (no dead-neuron problem at $x = 0$) and saturates more gracefully on the negative side.

## Where it's used

- **[[VisionTransformer|ViT]]** MLP sublayer (instead of ReLU).
- **[[BERT]]**, [[GPT-2]], [[GPT-3]] — and essentially every modern Transformer-based LLM.
- **Most pre-LLaMA decoder-only Transformers**; some recent ones use SiLU/Swish or SwiGLU instead.

## See also

- [[ActivationFunction]] · [[ReLU]] · [[FeedForwardNetwork]] · [[VisionTransformer]] · [[Transformer]]
