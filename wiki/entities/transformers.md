---
title: "transformers (Hugging Face)"
type: entity
tags: [tool, library, hugging-face, open-source, llm-tooling]
sources: [hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# transformers (Hugging Face library)

**Hugging Face `transformers`** — the canonical open-source Python library for loading, training, and serving pretrained Transformer models. Provides `AutoTokenizer`, `AutoModelForCausalLM`, `AutoModelForSequenceClassification`, `AutoModelForTokenClassification`, `AutoModelForMaskedLM`, the `Trainer` API, and the `pipeline()` high-level inference wrapper. Sits underneath every Hugging Face training and inference workflow in the wiki — paired with [[peft|PEFT]], [[trl|TRL]], [[bitsandbytes]] and other libraries to compose end-to-end fine-tuning + serving stacks.

## Summary

The library [[HandsOnLLM|*Hands-On LLMs*]] treats as **the canonical first interface** to working with LLMs ([[hands-on-llm-ch01-introduction-to-llms|Ch 1]] declares it the book's primary tooling commitment). Every chapter from Ch 1 through Ch 12 uses `transformers` for at least one of: tokenizer loading (`AutoTokenizer.from_pretrained`), model loading (`AutoModelForCausalLM` / `AutoModelForSequenceClassification` / `AutoModelForTokenClassification` / `AutoModelForMaskedLM`), `Trainer`-based fine-tuning, or `pipeline()` inference.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 uses `transformers` as the **base library** of the chapter's four-package fine-tuning stack: `transformers` + [[peft|PEFT]] + [[bitsandbytes]] + [[trl|TRL]]. Specifically:

- **Model loading**: `AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T", quantization_config=bnb_config, ...)` — passes the [[BitsAndBytesConfig]] through `transformers`'s `quantization_config` argument, which delegates to [[bitsandbytes]].
- **Tokenizer**: `AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1BChat-v1.0")` — used to apply the [[ChatTemplate|chat template]] (`<|user|>...<|assistant|>`) to the [[UltraChat]] examples before training.
- **Training arguments**: `transformers.TrainingArguments` (with `optim="paged_adamw_32bit"`, `lr_scheduler_type="cosine"`, `fp16=True`, `gradient_checkpointing=True`) — consumed by [[trl|TRL]]'s `SFTTrainer` and `DPOTrainer`.
- **Inference**: `transformers.pipeline("text-generation", model=merged_model, tokenizer=tokenizer)` — used to verify the fine-tuned TinyLlama follows instructions (e.g., *"Tell me something about Large Language Models."*).

The chapter's structural point: `transformers` is the **substrate**; [[peft|PEFT]] / [[bitsandbytes]] / [[trl|TRL]] are **adapters on top** that hook into specific `transformers` extension points (`quantization_config`, custom `Trainer` subclasses, model-modification utilities).

## Connections

- [[HuggingFace]] — the publisher / company behind the library.
- [[peft]] / [[trl]] / [[bitsandbytes]] — the three companion libraries Ch 12 uses on top of `transformers`.
- [[Trainer]] — the canonical `transformers.Trainer` training loop (used in [[hands-on-llm-ch11-fine-tuning-representation-models|Ch 11]]; [[trl|TRL]]'s `SFTTrainer` / `DPOTrainer` subclass it in Ch 12).
- [[TrainingArguments]] — `transformers.TrainingArguments`, the configuration dataclass.
- [[ChatTemplate]] — the per-tokenizer `apply_chat_template` formatter.
- [[hands-on-llm-ch12-fine-tuning-generation-models]] — primary source.
