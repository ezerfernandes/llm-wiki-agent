---
title: "Forward Pass"
type: concept
tags: [neural-networks, training, inference]
sources: [hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
---

# Forward Pass

The propagation of inputs through a neural network from input layer to output layer to produce a prediction or representation. *"That's machine-learning speak for the inputs going into the neural network and flowing through the computations it needs to produce an output on the other end of the computation graph."* — [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

## In a Transformer LLM

For a Transformer LLM, **each token generation is one forward pass**: input tokens flow through the [[Tokenizer|tokenizer]] → embedding table → stack of [[transformer|Transformer blocks]] → [[LMHead|LM head]] → next-token probability distribution. The autoregressive generation loop runs forward pass after forward pass, appending each chosen token to the input.

## Distinction

- **Forward pass** vs **backward pass**: forward computes the output; backward (during training) computes gradients of the loss with respect to parameters via [[Backpropagation|backpropagation]].
- **Forward pass** vs **[[ForwardPropagation|forward propagation]]**: synonymous; the term *forward pass* is more common in LLM-internals literature.

## See also

- [[ForwardPropagation]] — synonymous term.
- [[Backpropagation]] — the gradient-computation counterpart during training.
- [[transformer]] — the architecture this concept is invoked across in modern LLMs.
- [[KVCache]] — the optimization that makes per-token decode-time forward passes much cheaper.
- [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]] — primary source.
