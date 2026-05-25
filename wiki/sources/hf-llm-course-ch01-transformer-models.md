---
title: "HuggingFace LLM Course — Ch 1: Transformer models"
type: source
tags: [hf-llm-course, course, transformers, nlp, llm]
date: 2026-05-23
source_file: raw/hf-llm-course/ch01-transformer-models.md
---

## Summary
Chapter 1 of the HuggingFace LLM Course introduces [[NLP]] and [[LanguageModel]]s, then surveys the [[Transformer]] architecture and its three variants: encoder-only ([[BERT]]-like), decoder-only ([[GPT]]-like), and encoder-decoder ([[T5]]-like). It teaches how to drive pretrained models via the `pipeline()` API for sentiment analysis, zero-shot classification, text generation, mask filling, NER, question answering, summarization, translation, image classification, and ASR. It closes with a deep-dive into LLM inference (prefill/decode phases, sampling strategies, KV cache) and a frank discussion of model bias and limitations.

## Key Claims
- The [[Transformer]] architecture was introduced in June 2017 with the paper "Attention Is All You Need" and was originally designed for translation.
- All major Transformer models ([[GPT]], [[BERT]], [[T5]]) are trained as [[LanguageModel]]s using [[SelfSupervisedLearning]] on raw text, then fine-tuned for specific tasks via [[TransferLearning]].
- Two main pretraining objectives dominate: [[MaskedLanguageModeling]] (used by encoder models like BERT) and [[CausalLanguageModeling]] (used by decoder models like GPT).
- Three architectural families map cleanly to task types: encoder-only for understanding (classification, NER, extractive QA), decoder-only for generation, encoder-decoder for sequence-to-sequence tasks (translation, summarization).
- [[Attention]] layers let the model selectively weight which input tokens matter when producing a representation; this is the core innovation that enables context-aware language modeling.
- Decoders use *masked self-attention* so they cannot attend to future tokens, enforcing the autoregressive property during training and inference.
- Modern LLMs follow a two-phase training recipe: large-scale pretraining on next-token prediction, then [[InstructionTuning]] to follow human instructions.
- The Hugging Face `pipeline()` function bundles preprocessing, model inference, and post-processing — letting users hit tasks like `sentiment-analysis`, `zero-shot-classification`, `fill-mask`, `ner`, `question-answering`, `summarization`, `translation`, `automatic-speech-recognition`, and `image-classification` with one call.
- The distinction between *architecture* (the layer skeleton), *checkpoint* (a specific set of trained weights, e.g. `bert-base-cased`), and *model* (umbrella term) is foundational vocabulary for the HF ecosystem.
- LLM inference splits into a compute-bound **prefill phase** (process the full prompt) and a memory-bound **decode phase** (autoregressively emit one token at a time), with [[KVCache]] as a key optimization to avoid recomputing past attention.
- Sampling strategies — temperature, top-p ([[NucleusSampling]]), top-k, [[BeamSearch]], plus presence/frequency penalties — give explicit control over the creativity/coherence tradeoff during decoding.
- Standard attention is O(n²) in sequence length; sparse variants like Longformer's local attention, Reformer's LSH attention, and axial positional encodings extend Transformers to long contexts.
- [[ViT]] applies the Transformer recipe to images by splitting a 224×224 image into 196 patches of 16×16 pixels, treating each as a "token," and using a learnable `[CLS]` token plus position embeddings — directly mirroring BERT.
- [[Whisper]] is an encoder-decoder Transformer pretrained on 680,000 hours of weakly supervised audio data, enabling zero-shot transcription and translation across many languages without task-specific fine-tuning.
- [[BERT]] is pretrained with two objectives — masked language modeling and next-sentence prediction — and uses `[CLS]` (for sequence-level outputs) and `[SEP]` (between sentences) special tokens with [[WordPiece]] tokenization.
- [[GPT-2]] uses [[BPE]] tokenization, adds positional encodings to token embeddings, and produces logits via a linear language-modeling head trained with cross-entropy against the right-shifted sequence.
- [[BART]] is pretrained by corrupting input (best strategy: text infilling with single mask spans) and reconstructing it; it adapts to translation by prepending a small randomly initialized source-language encoder to the pretrained model.
- LLMs reproduce biases from their training data; the chapter shows BERT's `fill-mask` returning gendered occupation stereotypes (e.g. "nurse/waitress/...prostitute" for "woman works as") even though BERT was trained on the relatively curated Wikipedia + BookCorpus — and fine-tuning does NOT remove intrinsic bias.
- Sharing pretrained weights via the Hugging Face Hub dramatically reduces the aggregate compute cost and carbon footprint of the ML community; tools like ML CO2 Impact and Code Carbon are integrated for footprint accounting.

## Key Quotes
> "Attention Is All You Need" — title of the 2017 paper that introduced the Transformer architecture.
> "A large language model (LLM) is an AI model trained on massive amounts of text data that can understand and generate human-like text... without task-specific training." — Section 2 definition box.
> "Fine-tuning the model on your data won't make this intrinsic bias disappear." — Section 9, on the persistence of pretraining biases.
> "BERT is an architecture while `bert-base-cased`... is a checkpoint." — Section 4, on the architecture/checkpoint/model distinction.

## Code & Patterns
- `pipeline("<task>")` factory — covers `sentiment-analysis`, `zero-shot-classification` (with `candidate_labels=[...]`), `text-generation` (with `num_return_sequences`, `max_length`), `fill-mask` (with `top_k`), `ner` (with `grouped_entities=True`), `question-answering` (kwargs `question=`, `context=`), `summarization`, `translation`.
- Selecting a specific Hub checkpoint: `pipeline("text-generation", model="HuggingFaceTB/SmolLM2-360M")`; `pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")`.
- Vision pipeline: `pipeline(task="image-classification", model="google/vit-base-patch16-224")`; accepts URLs directly.
- Audio pipeline: `pipeline(task="automatic-speech-recognition", model="openai/whisper-large-v3")` and `openai/whisper-base.en` for fine-tuned ASR.
- Mask-token convention: BERT-style models use `[MASK]`; other models may use `<mask>` — must verify per checkpoint.
- NER post-processing: subword pieces (e.g. `S ##yl ##va ##in`) are regrouped into entity spans when `grouped_entities=True`.
- BERT fine-tuning patterns: attach task-specific heads (sequence-classification head, token-classification head, span-classification head for QA) on top of the pretrained encoder.

## Connections
- [[Transformer]] — primary subject of the chapter; the architecture and its three variants
- [[Attention]] — the core mechanism; "Attention Is All You Need"
- [[LanguageModel]] — the pretraining paradigm shared by all Transformer LLMs
- [[BERT]] — canonical encoder-only model, used throughout for classification/NER/QA examples
- [[GPT]] — original decoder-only Transformer
- [[GPT-2]] — used as the canonical decoder-only example for text generation
- [[T5]] — canonical encoder-decoder sequence-to-sequence model
- [[BART]] — encoder-decoder for summarization/translation, with text-infilling pretraining
- [[Llama]] — modern decoder-only LLM family from Meta
- [[Mistral]] — 7B model using grouped-query attention and sliding window attention
- [[Gemma]] — Google's lightweight open model family with interleaved local-global attention
- [[SmolLM]] — Hugging Face's small (135M–1.7B) decoder-only LLM series
- [[Whisper]] — encoder-decoder ASR model, OpenAI
- [[ViT]] — Vision Transformer; image classification via patch embeddings
- [[ConvNeXT]] — modern CNN baseline contrasted with ViT
- [[FineTuning]] — adapting a pretrained model to a specific task
- [[TransferLearning]] — the broader paradigm motivating fine-tuning
- [[MaskedLanguageModeling]] — BERT-style pretraining objective
- [[CausalLanguageModeling]] — GPT-style pretraining objective
- [[SelfSupervisedLearning]] — pretraining without human-labeled data
- [[InstructionTuning]] — second phase of modern LLM training
- [[BPE]] — byte pair encoding, used by GPT-2
- [[WordPiece]] — tokenization used by BERT
- [[Tokenizer]] — preprocessing step in every pipeline
- [[ClsToken]] — `[CLS]` representation for sequence-level outputs
- [[PositionalEncoding]] — added to token/patch embeddings
- [[BeamSearch]] — decoding strategy keeping multiple candidate sequences
- [[NucleusSampling]] — top-p sampling
- [[Temperature]] — controls sharpness of softmax during sampling
- [[KVCache]] — key-value caching, a critical inference optimization
- [[ContextWindow]] — the maximum input length a model can handle
- [[Hallucination]] — listed as a key LLM limitation
- [[Bias]] — Section 9 case study with BERT fill-mask
- [[ZeroShotLearning]] — performing tasks without task-specific fine-tuning
- [[FewShotLearning]] — in-context learning from a handful of examples
- [[HuggingFaceHub]] — the model/dataset distribution platform driving the ecosystem
- [[HuggingFaceTransformers]] — the library underlying the course
- [[Pipeline]] — the high-level API abstraction
- [[NamedEntityRecognition]] — example NLP task
- [[QuestionAnswering]] — example NLP task
- [[Summarization]] — example seq2seq task
- [[MachineTranslation]] — original Transformer motivation
- [[AutomaticSpeechRecognition]] — Whisper application
- [[Longformer]] — local attention for long sequences
- [[Reformer]] — LSH attention + axial positional encodings

## Contradictions
- none
