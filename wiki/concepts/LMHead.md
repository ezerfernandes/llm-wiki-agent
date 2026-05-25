---
title: "Language Modeling Head (LM Head)"
type: concept
tags: [transformer, architecture, decoding]
sources: [hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
---

# Language Modeling Head (LM Head)

The final layer of a Transformer LLM — *"a simple neural network layer ... [that] translates the output of the stack into probability scores for what the most likely next token is"* ([[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]).

## Mechanism

The LM head is a single linear layer mapping the final-block hidden state (`d_model` = 3,072 for [[Phi3Mini|Phi-3-mini]]) to a logit vector of size **|vocabulary|** (32,064 for Phi-3-mini). In the Phi-3 PyTorch print-out from Ch 3 it appears as:

```
(lm_head): Linear(in_features=3072, out_features=32064, bias=False)
```

Only the **last token stream's** output is fed to the LM head — the model uses all prior streams' intermediate outputs in the attention sub-layers but only the final-position output for the next-token prediction.

Worked example from Ch 3:

```python
model_output = model.model(input_ids)            # [1, 6, 3072]
lm_head_output = model.lm_head(model_output[0])  # [1, 6, 32064]
token_id = lm_head_output[0, -1].argmax(-1)
tokenizer.decode(token_id)                       # → "Paris"
```

for the prompt `"The capital of France is"`.

## Heads are interchangeable

> "The lm_head ... is one of multiple possible 'heads' to attach to a stack of Transformer blocks to build different kinds of systems. Other kinds of Transformer heads include sequence classification heads and token classification heads." — Ch 3

This is the architectural payoff of separating tokenizer → Transformer blocks → head: the same backbone can be repurposed by swapping the head — generation (vocab-sized logits), sequence classification (class-sized logits), token classification (per-position class logits), etc.

## See also

- [[transformer]] — the Transformer blocks the LM head sits on top of.
- [[DecodingStrategy]] — what to do with the LM head's output probability distribution.
- [[Softmax]] — the operation that turns LM-head logits into probabilities.
- [[GreedyDecoding]] / [[Sampling]] — the two main decoding regimes.
- [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]] — primary source.
