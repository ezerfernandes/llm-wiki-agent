---
title: "Google"
type: entity
tags: [company, lab]
sources: [1409.3215-seq2seq, 1706.03762-attention-is-all-you-need, 1810.04805-bert, 1910.10683-t5, 2312.11805-gemini]
last_updated: 2026-05-10
---

# Google

Google's research arms — **Google Brain**, **Google Research**, and **Google AI Language** (now consolidated into **Google DeepMind**) — produced the four foundational sequence-modeling and pretraining papers in this wiki: [[1409.3215-seq2seq]] (Sutskever, Vinyals, Le — 2014), [[1706.03762-attention-is-all-you-need]] (Vaswani et al. — 2017), [[1810.04805-bert]] (Devlin, Chang, Lee, Toutanova — 2018), and [[1910.10683-t5]] (Raffel, Shazeer, Roberts et al. — 2020).

## Sequence-to-sequence learning (2014)

[[1409.3215-seq2seq]] introduces the encoder-decoder framing that powers all subsequent neural MT and language modeling. Authors:
- Ilya Sutskever — later co-founded [[OpenAI]].
- Oriol Vinyals — now leads research at Google DeepMind.
- Quoc V. Le — led Google Brain's AutoML and continued sequence-modeling work.

## Attention Is All You Need (2017)

Authors of that paper, all affiliated with Google at submission (with one exception):
- Ashish Vaswani (Google Brain)
- Noam Shazeer (Google Brain)
- Niki Parmar (Google Research)
- Jakob Uszkoreit (Google Research)
- Llion Jones (Google Research)
- Aidan N. Gomez (University of Toronto; work performed while at Google Brain)
- Łukasz Kaiser (Google Brain)
- Illia Polosukhin (work performed while at Google Research)

The paper's tensor2tensor codebase was open-sourced at https://github.com/tensorflow/tensor2tensor.

## BERT (2018)

[[1810.04805-bert]] introduces [[BERT]] — a deep bidirectional Transformer encoder pre-trained with [[MaskedLanguageModel]] + [[NextSentencePrediction]] objectives — and the pretrain-then-finetune transfer-learning recipe that dominates NLP from 2018 onward. Google AI Language authors:
- Jacob Devlin
- Ming-Wei Chang
- Kenton Lee
- Kristina Toutanova

Code and pre-trained checkpoints at https://github.com/google-research/bert.

## T5 (2020)

[[1910.10683-t5]] introduces **[[t5]]** — the Text-to-Text Transfer Transformer — an encoder-decoder Transformer + [[spancorruption]] denoising + the [[c4]] corpus + the unified [[texttotextframework]]. Frames the most thorough controlled ablation of transfer-learning choices in NLP to date; T5-11B achieves state-of-the-art on 18 of 24 benchmarks (GLUE 90.3, SuperGLUE 88.9 — within 0.9 of human). Authors:
- Colin Raffel (Google Brain)
- Noam Shazeer (Google Brain; also co-author of [[1706.03762-attention-is-all-you-need]])
- Adam Roberts
- Katherine Lee
- Sharan Narang
- Michael Matena
- Yanqi Zhou
- Wei Li
- Peter J. Liu

Code and checkpoints at https://github.com/google-research/text-to-text-transfer-transformer; C4 via TensorFlow Datasets.

## Gemini (2023)

[[2312.11805-gemini]] introduces the **[[Gemini]] 1.0** family of natively-multimodal foundation models (Ultra, Pro, Nano), authored under the [[GoogleDeepMind]] banner — the 2023 merger of Google Brain, the ML arm of Google Research, and DeepMind. Gemini Ultra is the first model to exceed human-expert performance on MMLU (90.04%) and sets state-of-the-art on 30 of 32 reported benchmarks. Predecessor: PaLM 2 (see [[PaLM2]]); consumer rebrand: [[Bard]] → Gemini / Gemini Advanced.

## Role in the wiki

Google is the architectural origin of every modern large language model in this wiki. The 2014 [[SeqToSeq]] paper established the encoder-decoder framing; the 2017 [[Transformer]] paper replaced its recurrent backbone with self-attention; the 2018 [[BERT]] paper supplied the pretrain-then-finetune transfer-learning recipe; and the 2023 [[Gemini]] family supplies the frontier-multimodal-deployment template. Every subsequent LLM in the AI/LLM corpus inherits this substrate.
