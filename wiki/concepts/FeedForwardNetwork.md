---
title: "Feed-Forward Network (positionwise FFN)"
type: concept
tags: [transformer, architecture]
sources: [d2l-attention-and-transformers, 1706.03762-attention-is-all-you-need, hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
---

# Feed-Forward Network (positionwise FFN)

The two-layer MLP applied to **every position independently** inside each [[Transformer]] encoder / decoder block, providing the non-attention nonlinearity that lets a Transformer block represent arbitrary functions of its self-attention output.

$$\textrm{FFN}(\mathbf{x}) = \max(0, \mathbf{x}\mathbf{W}_1 + \mathbf{b}_1)\,\mathbf{W}_2 + \mathbf{b}_2$$

— two linear layers with a [[ReLU]] (or [[GELU]] in [[VisionTransformer|ViT]] and modern LLMs) activation in between. The same parameters are applied **identically at each sequence position** — hence "positionwise."

## Why "positionwise"

Each token's representation passes through the same MLP independently — there is no mixing across positions inside the FFN. Cross-position mixing happens only in the [[SelfAttention|self-attention]] sublayer. Equivalent to two pointwise (kernel-size-1) convolutions over the sequence axis.

## Dimensions (vanilla Transformer)

- Input / output dimension: $d_{\textrm{model}} = 512$.
- Hidden dimension: $d_{\textrm{ff}} = 2048$ (4× expansion).
- Approximately two-thirds of the total parameter count of a Transformer block.

## In context

The FFN is the second sublayer of every encoder block (after self-attention) and the third sublayer of every decoder block (after self-attention + encoder–decoder attention). Each sublayer is wrapped in a [[ResidualConnection|residual connection]] and [[LayerNormalization|LayerNorm]].

## See also

- [[Transformer]] · [[MultiHeadAttention]] · [[ResidualConnection]] · [[LayerNormalization]] · [[ReLU]] · [[GELU]] · [[PreNorm]]
- [[SwiGLU]] / [[SiLU]] — the modern gated-activation variants replacing ReLU in 2024-era LLMs.
- [[RMSNorm]] — the modern normalization typically wrapping the FFN sublayer.

## From [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

Ch 3 makes a substantive **functional claim** about what the FFN does:

> "The feedforward neural network (collectively in all the model layers) is the source of [factual] information. ... When the model was successfully trained to model a massive text archive ... it learned and stored the information (and behaviors) that make it succeed at this task." — Ch 3

> "For an LLM to be successfully trained, it needs to memorize a lot of information. But it is not simply a large database. Memorization is only one ingredient in the recipe of impressive text generation. The model is able to use this same machinery to interpolate between data points and more complex patterns to be able to generalize." — Ch 3

The chapter's "*The Shawshank ___*" → `Redemption` example illustrates: completing this requires the model to have memorized the title from training data. The FFN is presented as the **locus of memorization and interpolation**, while [[selfattention|self-attention]] handles **context incorporation** (Ch 3's "*The dog chased the squirrel because it ___*" example). The chapter is consistent with the mechanistic-interpretability literature (Geva et al. 2020, *"Transformer Feed-Forward Layers Are Key-Value Memories"*) but does not cite it directly.

### Modern FFN: gated variant

For [[Phi3Mini|Phi-3-mini]] (Ch 3 PyTorch print-out):

```
Phi3MLP(
  (gate_up_proj): Linear(in=3072, out=16384)
  (down_proj): Linear(in=8192, out=3072)
  (activation_fn): SiLU()
)
```

The `gate_up_proj` fuses the gate and up-projection matrices (3072 → 8192 each, concatenated to 3072 → 16384). The [[SiLU|SiLU]] activation gates one stream against the other ([[SwiGLU|SwiGLU]]-style), then `down_proj` projects back to model dimension. The 8,192 inner dimension is ~2.67× expansion of the 3,072 model dim — typical for SwiGLU-style FFNs which use a smaller expansion than the original Transformer's 4× because of the gated structure's extra parameters.
