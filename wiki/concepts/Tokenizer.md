---
title: "Tokenizer"
type: concept
tags: [nlp, preprocessing]
sources: [madewithml-transformers, hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# Tokenizer

The component that implements [[Tokenization]] — mapping strings to integer IDs and back. Must be versioned with the model to avoid [[TrainingServingSkew]]; common implementations include [[sentencepiece]] and [[wordpiece]].

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 frames the tokenizer as **the protocol layer between application code and the model**: *"Looking at the code, we can see that the model does not in fact receive the text prompt. Instead, the tokenizers processed the input prompt, and returned the information the model needed in the variable `input_ids`."*

**Tokenizer-model binding** Ch 2 emphasizes:

> "A pretrained language model is linked with its tokenizer and can't use a different tokenizer without training." — Ch 2

Standard usage pattern (Ch 2 worked example):

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("microsoft/Phi-3-mini-4k-instruct", ...)
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")

input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to("cuda")
output = model.generate(input_ids=input_ids, max_new_tokens=20)
print(tokenizer.decode(output[0]))
```

The tokenizer is loaded **from the same model name** as the model — this is the canonical [[HuggingFace|Hugging Face]] `transformers` idiom that prevents accidental tokenizer-model mismatch. Ch 2 also demonstrates `tokenizer.decode(id)` for per-token inspection and `tokenizer.decode([id_1, id_2])` for joint decoding.

See the [[Tokenization]] page for Ch 2's comparative tour of seven actual tokenizers' behavior on a single test string.
