---
title: "Google"
type: entity
tags: [company, lab]
sources: [1409.3215-seq2seq, 1706.03762-attention-is-all-you-need, 1810.04805-bert, 1910.10683-t5, 2312.11805-gemini, ai-engineering-ch01-intro, ai-engineering-ch02-foundation-models, hands-on-llm-ch01-introduction-to-llms, ai-engineering-ch05-prompt-engineering, hands-on-llm-ch04-text-classification, hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
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

## From [[ai-engineering-ch01-intro|AI Engineering Ch 1]]

[[ChipHuyen|Chip Huyen]] in *AI Engineering* Ch 1 cites Google in several roles:

- **One of the "big corporations" building foundation models** alongside [[meta|Meta]], [[microsoft|Microsoft]], Baidu, and Tencent — the entity tier that can afford to develop FMs from scratch.
- **[[gemini|Gemini]] launch (Dec 2023)** — Ch 1's canonical anecdote on prompt-format dependence: Google claimed Gemini Ultra beat ChatGPT on [[MMLU]] using CoT@32 prompting (90.04% vs. 86.4%), but with 5-shot only, [[GPT4|GPT-4]] outperformed Gemini Pro (78.4% vs. 71.8%). Ch 1 uses this to argue that *"different prompts can cause models to perform very differently."*
- **Google Photos** — a worked example of [[DataOrganization|AI-driven data organization]]: Google Photos uses AI to surface images matching natural-language search queries.
- **Google Image Search** — extended example: generates images when no existing match is found.
- **Google Docs / Gmail** — example consumers of AI writing assistants ([[Grammarly]] integrates via browser extension).
- **Google Assistant** — voice-assistant interface category (alongside Siri, Alexa); cited as an example of conversational AI that predates the ChatGPT moment.
- **Google Maps** — example of a [[ReactiveOrProactive|proactive]] AI feature (traffic alerts).

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

Ch 2 supplies several additional Google-specific data points:

1. **[[GoogleGNMT|GNMT (Google Neural Machine Translation)]] 2016** — first major production use of the [[Attention|attention]] mechanism (introduced by Bahdanau et al. 2014, three years before the Transformer paper). Google's GNMT was attention-with-seq2seq; the Transformer paper later showed attention works without RNNs at all.
2. **[[c4|C4 (Colossal Clean Crawled Corpus)]]** — Google's heuristically-filtered subset of [[CommonCrawl|Common Crawl]] that dominates pretraining data for many LLMs.
3. **[[MedPaLM2|Med-PaLM 2]]** — Google's medical-domain LLM; one of three biomedical [[DomainSpecificModel|domain-specific models]] named in Ch 2.
4. **PaLM-2 training**: 10²² [[FLOPs|FLOPs]] for the largest variant (Chowdhery et al. 2022).
5. **[[gemini|Gemini]] MMLU 32-vote**: Ch 2's marquee [[selfconsistency|self-consistency]] data point — Google sampled 32 outputs per question and majority-voted to lift Gemini's reported [[mmlu|MMLU]] score above what a single-output evaluation would have produced.
6. **[[transformer|Transformer]] hardware lineage** — *"The transformer was originally designed by Google to run fast on Tensor Processing Units (TPUs), and was only later optimized on GPUs."* Footnote 12 of Ch 2.

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

Google appears in Ch 5 in **four roles**:

1. **[[PaLM2|PaLM 2]] documentation defines "context"** in a way Ch 5 flags as ambiguous: *"the description that shapes 'how the model responds throughout the conversation. For example, you can use context to specify words the model can or cannot use, topics to focus on or avoid, or the response format or style.'"* This is the same as the **task description** in Ch 5's terminology — adding to the prompt-vs-context vocabulary confusion.
2. **[[gemini|Gemini]] 1.5 Pro's 2M-token context** — the endpoint of Ch 5's 2,000× context-length growth chart (GPT-2's 1K → Gemini 1.5 Pro's 2M in five years).
3. **[[Dotprompt|Firebase Dotprompt]]** — Google's `.prompt` file format, used as the canonical example in Ch 5's organize-your-prompts section.
4. **"Eat rocks" AI Overviews brand-risk anecdote** (2024) — cited as a current-day example of brand-risk failures from generative-AI-in-production.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 uses **`google/flan-t5-small`** ([[FLANT5|Flan-T5]]) as the open-source [[GenerativeClassification|generative-classification]] demo — F1 = 0.84 on [[RottenTomatoes|Rotten Tomatoes]]. Two underlying Google contributions are surfaced:

- **[[t5|T5]] (Raffel et al., 2020)** — the encoder-decoder Transformer Flan-T5 is built on; Ch 4 introduces it via *"its architecture is similar to the original Transformer where 12 decoders and 12 encoders are stacked together."*
- **Flan-T5 (Chung et al., 2022)** — the **1,800+ task instruction-tuning** recipe that turns the base T5 into an instruction-following classifier without further fine-tuning. *"This resulted in the Flan-T5 family of models that benefit from this large variety of tasks."*

These are the chapter's main demonstration that **Google's open-source generative LLMs are competitive with closed-source alternatives** for downstream classification — Flan-T5-small reaches F1 = 0.84 vs ChatGPT's F1 = 0.91 at zero API cost.
