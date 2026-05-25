---
title: "HuggingFace LLM Course — Ch 2: Using 🤗 Transformers"
type: source
tags: [hf-llm-course, course, transformers, tokenization, inference]
date: 2026-05-23
source_file: raw/hf-llm-course/ch02-using-transformers.md
---

## Summary
Chapter 2 of the HuggingFace LLM Course unpacks the [[HuggingFaceTransformers]] library by decomposing the `pipeline()` function into its three steps: tokenizer preprocessing, model forward pass, and postprocessing of logits. It introduces the `Auto*` factory classes ([[AutoTokenizer]], [[AutoModel]], [[AutoModelForSequenceClassification]]), explains tokenization algorithms (word, character, subword via [[BPE]], [[WordPiece]], [[SentencePiece]]/[[Unigram]]), and walks through batching, [[Padding]], [[Truncation]], and [[AttentionMask]]s. The chapter closes with an "Optimized Inference Deployment" section covering production-grade LLM serving via [[TGI]], [[vLLM]], and [[LlamaCpp]], featuring techniques like [[FlashAttention]] (2), [[PagedAttention]], [[KVCache]] paging, [[ContinuousBatching]], and [[Quantization]] (GGUF).

## Key Claims
- The `pipeline()` function decomposes into three steps: tokenizer preprocessing -> model forward pass -> postprocessing (e.g. softmax over [[Logits]]).
- All 🤗 [[HuggingFaceTransformers]] models are PyTorch `nn.Module` classes, follow an "all-in-one-file" philosophy, and load via `from_pretrained(checkpoint)` from the [[HuggingFaceHub]].
- The default sentiment-analysis checkpoint is `distilbert-base-uncased-finetuned-sst-2-english`, a [[DistilBERT]] fine-tuned on [[SST-2]].
- A base [[AutoModel]] outputs hidden states of shape `(batch, seq_len, hidden_size)` — e.g. `(2, 16, 768)` for BERT-base; task heads (`*ForSequenceClassification`, `*ForCausalLM`, `*ForMaskedLM`, etc.) project those hidden states down to task-specific logits.
- Models output raw [[Logits]] (not probabilities) so loss functions can fuse the activation (e.g. softmax) with cross-entropy for training stability; `model.config.id2label` maps indices to labels.
- `bert-base-cased` has 12 layers, hidden size 768, and 12 attention heads; [[BERT]] adds special tokens `[CLS]` (start) and `[SEP]` (separator) that the tokenizer inserts automatically.
- [[Tokenizer]]s come in three families: word-based (huge vocab, many `[UNK]`), character-based (small vocab, long sequences, weak per-token semantics), and subword-based (best of both worlds).
- Subword tokenization keeps frequent words intact and decomposes rare words into meaningful sub-pieces (e.g. "annoyingly" -> "annoying" + "ly"); notable algorithms: byte-level [[BPE]] ([[GPT2]]), [[WordPiece]] ([[BERT]]), [[SentencePiece]]/[[Unigram]] (multilingual models).
- 🤗 Transformer models expect a batched 2-D input `(batch, seq_len)`; passing a 1-D tensor raises `IndexError: Dimension out of range`.
- [[Padding]] makes sequences in a batch rectangular using `tokenizer.pad_token_id`; without an [[AttentionMask]], attention layers contextualize padding tokens and produce different logits than the un-padded run — the mask (1=attend, 0=ignore) is required for correct batched inference.
- BERT-family models cap sequences at 512 tokens; long-context alternatives include [[Longformer]] and [[LED]]; otherwise truncate with `truncation=True` and `max_length`.
- The high-level `tokenizer(...)` call accepts `padding={True,"longest","max_length"}`, `truncation=True`, `max_length=N`, and `return_tensors={"pt","np"}` and returns a dict with `input_ids`, `attention_mask`, and optionally `token_type_ids`.
- [[TGI]] (Text Generation Inference) is HuggingFace's production server: [[FlashAttention]] 2, [[ContinuousBatching]], CPU/GPU offload, Kubernetes/Prometheus/Grafana integration, content filtering, rate limiting.
- [[vLLM]] uses [[PagedAttention]] (KV-cache split into fixed-size pages with a page table, allowing non-contiguous storage and prompt-cache sharing across parallel samples) achieving up to 24x higher throughput vs traditional methods.
- [[LlamaCpp]] is a C/C++ runtime targeting consumer hardware via [[Quantization]] (8/4/3/2-bit), [[GGUF]] tensor format, mixed precision, and CPU SIMD kernels (AVX2/AVX-512/NEON); supports CPU offload of layers via `--n-gpu-layers`.
- Generation sampling is controlled by [[Temperature]], [[TopPSampling]] (nucleus), [[TopKSampling]], [[RepetitionPenalty]], frequency/presence penalties, `no_repeat_ngram_size`, `min_new_tokens`/`max_new_tokens`, and `stop_sequences`.

## Key Quotes
> "The 🤗 Transformers library was created to solve this problem. Its goal is to provide a single API through which any Transformer model can be loaded, trained, and saved." — Section 1 (Introduction)

> "All 🤗 Transformers models output the logits, as the loss function for training will generally fuse the last activation function, such as SoftMax, with the actual loss function, such as cross entropy." — Section 2 (Behind the pipeline / Postprocessing)

> "The key feature of Transformer models is attention layers that contextualize each token. These will take into account the padding tokens since they attend to all of the tokens of a sequence." — Section 5 (Handling multiple sequences)

> "The PagedAttention approach can lead to up to 24x higher throughput compared to traditional methods, making it a game-changer for production LLM deployments." — Section 8 (Optimized Inference Deployment)

> "Flash Attention loads data once into SRAM and performs all calculations there, minimizing expensive memory transfers." — Section 8 (Optimized Inference Deployment)

## Code & Patterns
- **Auto classes**: `AutoTokenizer.from_pretrained(checkpoint)` and `AutoModel.from_pretrained(checkpoint)` (or task-specific `AutoModelForSequenceClassification`) dispatch to the correct architecture by checkpoint name.
- **Tokenizer call**: `tokenizer(text_or_list, padding=True, truncation=True, return_tensors="pt")` returns a dict with `input_ids`, `attention_mask`, and (for BERT-family) `token_type_ids`.
- **Manual tokenization pipeline**: `tokenizer.tokenize(seq)` -> list of subword strings; `tokenizer.convert_tokens_to_ids(tokens)` -> list of ints; `tokenizer.decode(ids)` -> reconstructed string (handles `##er`-style WordPiece continuations and special tokens).
- **Batch dimension**: always pass `torch.tensor([ids])` (shape `[1, L]`) — a 1-D tensor crashes the model.
- **Padding + mask**: `tokenizer.pad_token_id` for the pad value; attention mask `1`/`0` aligns 1:1 with `input_ids` and is required for correct batched logits.
- **Save/load**: `model.save_pretrained(dir)` writes `config.json` + `model.safetensors`; `model.push_to_hub("name")` (after `huggingface-cli login` or `notebook_login()`) shares to the [[HuggingFaceHub]].
- **TGI Docker launch**: `docker run --gpus all ghcr.io/huggingface/text-generation-inference:latest --model-id <repo>` exposes an OpenAI-compatible `/v1` endpoint; `InferenceClient` and `openai.OpenAI` both work as clients.
- **vLLM native API**: `LLM(model=...)` + `SamplingParams(temperature, top_p, top_k, max_tokens, presence_penalty, frequency_penalty, stop)` and `llm.generate(prompt, sampling_params)`.
- **llama.cpp**: build with `make`; serve a `.gguf` via `./server -m model.gguf -c <ctx> --n-gpu-layers N --cont-batching --mlock`; OpenAI-compatible API on `:8080/v1`.

## Connections
- [[HuggingFaceTransformers]] — the library whose surface API this chapter teaches.
- [[HuggingFaceHub]] — checkpoint storage that `from_pretrained()` and `push_to_hub()` target.
- [[AutoTokenizer]], [[AutoModel]], [[AutoModelForSequenceClassification]] — factory classes for dispatching to the right architecture.
- [[Tokenizer]], [[BPE]], [[WordPiece]], [[SentencePiece]], [[Unigram]] — tokenization algorithms surveyed.
- [[BERT]], [[DistilBERT]], [[GPT2]] — model families used as concrete examples.
- [[AttentionMask]], [[Padding]], [[Truncation]], [[Logits]], [[Softmax]] — preprocessing/postprocessing primitives.
- [[Longformer]], [[LED]] — long-context alternatives when 512/1024-token caps bind.
- [[TGI]], [[vLLM]], [[LlamaCpp]] — production inference servers contrasted on memory model, deployment, and integration.
- [[FlashAttention]], [[PagedAttention]], [[KVCache]], [[ContinuousBatching]], [[Quantization]], [[GGUF]] — optimization techniques powering those servers.
- [[Temperature]], [[TopPSampling]], [[TopKSampling]], [[RepetitionPenalty]] — decoding-time sampling controls.
- [[SmolLM2]] — example checkpoint family (`HuggingFaceTB/SmolLM2-360M-Instruct`, `SmolLM2-1.7B-Instruct-GGUF`) used in the deployment walkthroughs.
- [[PyTorch]] — backing tensor framework (`nn.Module`, `torch.tensor`).

## Contradictions
- None observed within this chapter. The chapter's claim that "most models handle sequences of up to 512 or 1024 tokens" reflects the BERT-era baseline and may understate context windows of modern LLMs documented elsewhere in the wiki; flag for the consolidator if a contradiction surfaces against later chapters.
