---
title: "DeBERTa"
type: entity
tags: [model, llm, encoder-only, transformer, microsoft]
sources: [hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# DeBERTa

**Decoding-enhanced BERT with Disentangled Attention** — [[microsoft|Microsoft Research's]] encoder-only language model line (He, Liu, Gao, Chen et al., 2020+). Improves on [[bert|BERT]] / [[RoBERTa]] via **disentangled attention** (separating content and position into two vectors per token) and an enhanced mask decoder. The latest mainline release is **DeBERTa v3** (*"DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing"*, He, Gao & Chen, 2021).

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

DeBERTa v3 is **the chapter's worked model for contextualized token embeddings**:

> "The model we're using here is called DeBERTa v3, which at the time of writing is one of the best-performing language models for token embeddings while being small and highly efficient." — Ch 2

The worked example loads `microsoft/deberta-v3-xsmall` from [[HuggingFace|Hugging Face]] and runs it on `"Hello world"`. The resulting output tensor has shape `torch.Size([1, 4, 384])` — interpreted as **4 tokens** (`[CLS] Hello world [SEP]`) × **384-dim contextualized embedding** per token (plus a leading batch dimension).

```python
from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-base")
model = AutoModel.from_pretrained("microsoft/deberta-v3-xsmall")

tokens = tokenizer('Hello world', return_tensors='pt')
output = model(**tokens)[0]
# output.shape -> torch.Size([1, 4, 384])
```

Note the chapter mixes `deberta-base` (for the tokenizer) with `deberta-v3-xsmall` (for the model) — this is the version of DeBERTa v3 with 384-dim hidden state used in the worked example.

## Why DeBERTa is a strong text-embedding base

- **Encoder-only** — like BERT, produces per-token contextualized vectors suitable for downstream feature extraction.
- **Disentangled position+content attention** — yields better representations per parameter than vanilla BERT.
- **Small variants available** (xsmall, small) — runs on consumer hardware.
- **Strong on GLUE / SuperGLUE** at parameter-count parity with much larger models.

## Connections

- [[bert]] — direct ancestor; DeBERTa improves on BERT's attention mechanism.
- [[microsoft]] — the publishing organization.
- [[HuggingFace]] — model hub host (`microsoft/deberta-base`, `microsoft/deberta-v3-xsmall`).
- [[ContextualEmbedding]] / [[TokenEmbedding]] — the type of embedding DeBERTa is used to produce.
- [[DeBERTaV3FactConsistency]] — wiki concept using DeBERTa v3 as an NLI-based fact-consistency model.
- [[HandsOnLLM]] / [[hands-on-llm-ch02-tokens-and-embeddings]] — Ch 2 worked example.
