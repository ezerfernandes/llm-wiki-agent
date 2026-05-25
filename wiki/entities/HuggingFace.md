---
title: "Hugging Face"
type: entity
tags: [company, model-hub, nlp]
sources: [madewithml-mlops-training, madewithml-foundations-transformers, hands-on-llm-ch01-introduction-to-llms, hands-on-llm-ch02-tokens-and-embeddings, hands-on-llm-ch03-looking-inside-llms, hands-on-llm-ch04-text-classification, hands-on-llm-ch05-text-clustering-topic-modeling, ai-engineering-ch08-dataset-engineering, hands-on-llm-ch06-prompt-engineering, hands-on-llm-ch07-advanced-text-generation, hands-on-llm-ch09-multimodal-llms, hands-on-llm-ch11-fine-tuning-representation-models, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# Hugging Face

Model hub and `transformers` library. Provides the [[SciBERT]] tokenizer and pretrained checkpoint used throughout [[madewithml-mlops-training]] and [[madewithml-foundations-transformers]].

## From [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]]

Hugging Face is the **canonical model hub** in *[[HandsOnLLM|Hands-On Large Language Models]]* — every worked example in the book starts by downloading a model and tokenizer from the Hugging Face Hub.

> "The main source for finding and downloading LLMs is the Hugging Face Hub. Hugging Face is the organization behind the well-known Transformers package, which for years has driven the development of language models in general. As the name implies, the package was built on top of the transformers framework that we discussed in 'A Recent History of Language AI.'" — Ch 1

Concrete numbers from Ch 1:

- **800,000+ models** on the Hub at time of writing (2024).
- Models span LLMs, computer vision, audio, and tabular data — *"you can find almost any open source LLM."*

Ch 1's worked code uses two `transformers` constructs:

1. **`AutoModelForCausalLM.from_pretrained(...)` + `AutoTokenizer.from_pretrained(...)`** — load model + tokenizer with model ID, `device_map="cuda"`, `torch_dtype="auto"`, `trust_remote_code=True`.
2. **`pipeline("text-generation", model=model, tokenizer=tokenizer, ...)`** — high-level wrapper that encapsulates the model + tokenizer + generation logic into a single callable.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 deepens the `transformers` API surface used in the book:

- **`AutoTokenizer.from_pretrained(...)`** — paired with each surveyed model (BERT uncased/cased, GPT-2, Flan-T5, GPT-4, StarCoder2, Galactica, Phi-3). Tokenizers and models are loaded from the **same model ID** to ensure the tokenizer-model binding the chapter emphasizes.
- **`AutoModel.from_pretrained(...)`** (note: distinct from `AutoModelForCausalLM`) — loads an encoder for **contextualized embeddings** rather than generation. The chapter's [[deberta|DeBERTa v3]] worked example uses this to inspect the encoder output for `"Hello world"`.
- The chapter also introduces **`sentence-transformers`** as the canonical text-embedding library (also distributed via the [[HuggingFace|Hugging Face]] Hub); see [[SentenceTransformers]] and [[AllMPNetBaseV2]].

## From [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

Ch 3 uses Hugging Face Transformers as the platform for **dissecting the LLM internals**:

- **`print(model)`** — produces the PyTorch module tree visualization the chapter walks through for [[Phi3Mini|Phi-3-mini]] (32 `Phi3DecoderLayer` blocks, `qkv_proj`, `Phi3RotaryEmbedding`, `Phi3MLP` with `SiLU`, `Phi3RMSNorm`, `lm_head`).
- **`model.model(...)` then `model.lm_head(...)`** — splits the forward pass into the Transformer-block stack vs. the [[LMHead|LM head]] for inspecting intermediate `[1, 6, 3072]` hidden states.
- **`use_cache=True/False`** — toggles the [[KVCache|KV cache]] for the 4.5 s vs 21.8 s wall-clock measurement on Colab T4 / 100 tokens.

The chapter notes that `use_cache=True` is the **default in Hugging Face Transformers** — a quiet API choice that delivers ~5× decode-time speedup with no code change.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 uses Hugging Face's stack as the **substrate of all four pretrained-LLM classification regimes**:

- **`datasets` package** — `load_dataset("rotten_tomatoes")` loads the chapter's benchmark sentiment dataset (5,331 + 5,331 reviews, train/validation/test splits).
- **`transformers.pipeline("text-classification", ...)`** — wraps the [[TwitterRoBERTa|`cardiffnlp/twitter-roberta-base-sentiment-latest`]] task-specific model.
- **`transformers.pipeline("text2text-generation", ...)`** — wraps [[FLANT5|`google/flan-t5-small`]] for generative classification (encoder-decoder).
- **`transformers.pipelines.pt_utils.KeyDataset`** — adapter that lets pipelines iterate over a `datasets.Dataset` column without manual extraction.
- **The Hugging Face Hub itself** — Ch 4 reports **60,000+ text-classification models and 8,000+ embedding models** on the Hub at time of writing. Model-selection across this catalog is the chapter's opening problem.
- **The [[MTEB|MTEB leaderboard]]** (Hugging Face Space `mteb/leaderboard`) is the chapter's recommended starting point for **embedding-model selection**.

Ch 4 is the first chapter in *Hands-On LLMs* where the **Hugging Face `transformers.pipeline`** abstraction does the heavy lifting at *task* granularity (`text-classification`, `text2text-generation`) rather than at *generation* granularity (`text-generation`, as in Chs 1–3). This is a deliberate stylistic shift — the book's transition from *"open the LLM and look inside"* (Part I) to *"use the LLM as a service for a downstream task"* (Part II).

## Connections

- [[madewithml-mlops-training]] / [[madewithml-foundations-transformers]] — earlier wiki sources.
- [[HandsOnLLM]] / [[hands-on-llm-ch01-introduction-to-llms]] / [[hands-on-llm-ch02-tokens-and-embeddings]] — the canonical Hugging-Face-centered LLM book.
- [[Phi3Mini]] — the worked model in *Hands-On LLMs* Ch 1 (loaded from the Hub).
- [[deberta]] — Ch 2's contextualized-embedding worked model (from the Hub).
- [[SentenceTransformers]] — Ch 2's text-embedding library.
- [[OpenSourceLLM]] — the model category Hugging Face is the canonical distribution channel for.


## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

Ch 8 names Hugging Face as a top public-data source — "Hugging Face and Kaggle each host hundreds of thousands of datasets" — and as the canonical model hub for the [[Cosmopedia]] 25B-token synthetic corpus (HuggingFaceFW). Hugging Face's role in the chapter is as both **data marketplace and synthetic-data publisher** — the platform where [[AlpacaDataset|Alpaca]], [[UltraChat]], [[MetaMath]], and [[Cosmopedia]] are distributed for downstream finetuning use.

## From [[hands-on-llm-ch07-advanced-text-generation|*Hands-On LLMs* Ch 7]]

Ch 7 references the Hugging Face Hub as the **distribution channel for the [[GGUF]]-quantized [[Phi3Mini|Phi-3]] checkpoint** the chapter loads via [[LangChainLlamaCpp|`langchain.LlamaCpp`]] — `Phi-3-mini-4k-instruct-fp16.gguf`. Ch 7 also surfaces a structural distinction relative to Chs 1–6's `transformers.pipeline` usage: when loading the same model through [[LangChain]]'s `LlamaCpp` wrapper, the **chat template is NOT auto-applied** (unlike `transformers.pipeline`'s `apply_chat_template`) — a HuggingFace-vs-LangChain ergonomics gap the chapter reveals via the empty-output gotcha.

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 extends the `transformers` API surface into **vision-language** territory — the chapter's runnable code uses five Hugging Face classes the prior chapters did not touch:

- **`CLIPModel.from_pretrained("openai/clip-vit-base-patch32")`** — the multimodal embedding model; exposes `get_text_features(...)` and `get_image_features(...)` returning embeddings in the same 512-dim vector space.
- **`CLIPTokenizerFast.from_pretrained(...)`** — the CLIP text tokenizer, wraps with `<|startoftext|>` / `<|endoftext|>` (no `[CLS]` on the text side — *"in CLIP, the [CLS] token is actually used to represent the image embedding"*).
- **`CLIPProcessor.from_pretrained(...)`** — the CLIP image preprocessor (resizes to 224 × 224).
- **`Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b", torch_dtype=torch.float16)`** — the generative multimodal LLM; introspectable via `model.vision_model` (the frozen [[VisionTransformer|ViT]]) and `model.language_model` (the frozen OPT-2.7b LLM from [[meta]]).
- **`AutoProcessor.from_pretrained(...)`** — the BLIP-2 processor; *"can be compared to the tokenizer of language models"* — handles both image preprocessing and text tokenization in a single object.

The Hub also distributes the `Salesforce/blip2-opt-2.7b` checkpoint Ch 9 loads — making the chapter's **runnable end-to-end vision-language pipeline a Hugging-Face-native experience**.

## From [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]

Ch 11 is the wiki's **canonical worked example** of Hugging Face's fine-tuning stack — uses **seven** `transformers` classes that together implement four distinct fine-tuning regimes on the same `bert-base-cased` backbone:

| Class | Used by | Ch 11 regime |
|---|---|---|
| `AutoTokenizer` | All regimes | Common to all |
| `AutoModelForSequenceClassification` | Document classification | Regimes 1, 2 |
| `AutoModelForMaskedLM` | MLM continued pretraining | Regime 4 |
| `AutoModelForTokenClassification` | NER / token classification | Regime 5 |
| [[Trainer]] | All regimes | Common to all |
| [[TrainingArguments]] | All regimes | Common to all |
| [[DataCollatorWithPadding]] | Document classification | Regimes 1, 2 |
| [[DataCollatorForLanguageModeling]] | MLM continued pretraining | Regime 4 |
| `DataCollatorForWholeWordMask` | MLM (alternative) | Regime 4 (alt) |
| [[DataCollatorForTokenClassification]] | NER | Regime 5 |
| `pipeline("fill-mask")` | MLM qualitative eval | Regime 4 diagnostic |
| `pipeline("token-classification")` | NER inference | Regime 5 inference |
| `evaluate` (replaces deprecated `load_metric`) | F1 + [[seqeval]] | All regimes |

Ch 11 also uses **[[SetFit]]** (Tunstall et al. 2022, arXiv:2209.11055) — a separate `setfit` package, also distributed via Hugging Face, that wraps `sentence-transformers` for few-shot classification with its own `SetFitTrainer` / `SetFitTrainingArguments` mirroring the core `transformers` API.

The Ch 11 stack is the *"same `Trainer` + swap the model class + swap the collator"* pattern that makes Hugging Face's interface so powerful — it lets one chapter cover full FT, partial FT, MLM continued pretraining, and NER in ~1,300 lines of code on a Colab T4.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|*Hands-On LLMs* Ch 12]]

Ch 12 — the **book's final chapter** — extends the Hugging Face stack into **generative-LLM fine-tuning** with a four-package composition: [[transformers]] + [[peft|PEFT]] + [[bitsandbytes]] + [[trl|TRL]]. The chapter's Hugging Face surface:

| Class / API | Role |
|---|---|
| `AutoModelForCausalLM.from_pretrained(..., quantization_config=bnb_config)` | Load 4-bit-quantized [[TinyLlama]] base |
| `AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1BChat-v1.0")` | Borrow chat-variant tokenizer for `apply_chat_template` |
| `tokenizer.apply_chat_template(chat, tokenize=False)` | Format [[UltraChat]] examples into `<|user|>...<|assistant|>` chat format |
| [[BitsAndBytesConfig|`BitsAndBytesConfig`]] | 4-bit NF4 + double quantization + fp16 compute |
| [[LoraConfig|`peft.LoraConfig`]] | LoRA adapter: `r=64`, `α=32`, all 7 Llama-family projection layers |
| [[PrepareModelForKBitTraining|`peft.prepare_model_for_kbit_training`]] | Make quantized model trainable |
| [[TrainingArguments|`transformers.TrainingArguments`]] | `optim="paged_adamw_32bit"`, `lr_scheduler_type="cosine"`, `fp16=True`, `gradient_checkpointing=True` |
| [[SFTTrainer|`trl.SFTTrainer`]] | Supervised fine-tuning trainer |
| [[DPOConfig|`trl.DPOConfig`]] + [[DPOTrainer|`trl.DPOTrainer`]] | DPO preference-tuning trainer (`beta=0.1`) |
| [[AutoPeftModelForCausalLM|`peft.AutoPeftModelForCausalLM.from_pretrained(...).merge_and_unload()`]] | Reload base in 16-bit + merge LoRA delta |
| `transformers.pipeline("text-generation")` | Verify the fine-tuned model follows instructions |

Two Hugging Face datasets anchor the worked recipes:

- **[[UltraChat|`HuggingFaceH4/ultrachat_200k`]]** — 3,000 examples for the QLoRA-SFT stage.
- **[[DistilabelIntelOrcaDPOPairs|`argilla/distilabel-intel-orca-dpo-pairs`]]** — ~6,000 filtered triples for the DPO stage.

The Ch 12 stack is the *"swap the trainer + dataset on top of the same QLoRA substrate"* pattern — `SFTTrainer` for SFT, `DPOTrainer` for DPO — making Hugging Face's interface the canonical end-to-end post-training pipeline for the **GPU-poor** practitioner the book targets. **Completes the 12-chapter ingest of *Hands-On LLMs***.
