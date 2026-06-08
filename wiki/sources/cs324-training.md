---
title: "CS324 — Training"
type: source
tags: [cs324, llm, course-lecture, training]
date: 2022-01-01
source_file: https://stanford-cs324.github.io/winter2022/lectures/training/
---

## Summary
This Stanford CS324 lecture covers how large language models are trained, organized around two themes: training objective functions and optimization algorithms. It contrasts the objectives of the three model families — autoregressive (decoder-only) maximum likelihood for [[GPT-3]], [[MaskedLanguageModeling]] plus next-sentence prediction for [[BERT]], and denoising span-corruption text-to-text objectives for [[BART]] and [[T5]] — then walks through optimizers ([[SGD]], [[Adam]], [[Adafactor]]), [[MixedPrecisionTraining]], and the practical machinery of training stability: [[LearningRateWarmup]], [[GradientClipping]], initialization scaling, and the full [[GPT-3]] training recipe.

## Key Claims
- An autoregressive (decoder-only) language model defines $p(x_{i+1}\mid x_{1:i}) = \text{softmax}(E\,\phi(x_{1:i})_i)$ and is trained by minimizing the negative log-likelihood, factorized as $\mathcal{O}(\theta)=\sum_{x_{1:L}\in\mathcal{D}}\sum_{i=1}^{L} -\log p_\theta(x_i\mid x_{1:i-1})$.
- Decoder-only models ([[GPT-3]]) produce unidirectional contextual embeddings; encoder-only models ([[BERT]]) give stronger bidirectional embeddings because they don't need to generate tokens.
- [[BERT]]-large is $\text{TransformerBlock}^{24}$ over token + position + sentence embeddings, with 24 layers, 16 attention heads, 1024-dim model, and 355M parameters; it adds [CLS] (classification) and [SEP] (sequence separator) special tokens.
- BERT's objective combines [[MaskedLanguageModeling]] and [[NextSentencePrediction]]; masking selects a random 15% of positions, replacing each with [MASK] 80% of the time, the original token 10%, and a random vocabulary word 10% — the 20% non-[MASK] replacement reduces train/test distribution shift since [MASK] never appears at test time.
- [[NextSentencePrediction]] is a binary task using the [CLS] embedding; training pairs sentence A with the true next sentence 50% of the time and a random sentence 50% of the time.
- [[RoBERTa]] improved on BERT by dropping next-sentence prediction, training on more data (16GB → 160GB) for longer, raising SQuAD from 81.8 to 89.4.
- Encoder-decoder models ([[BART]], [[T5]]) encode the input bidirectionally like [[BERT]] and decode autoregressively like [[GPT-2]]; [[BART]] (Lewis et al., 2019) uses a RoBERTa-style encoder, masks 30% of tokens, and permutes all sentences.
- [[T5]] (Raffel et al., 2020) is an 11B-parameter text-to-text encoder-decoder; its best unsupervised objective was "i.i.d. noise, replace spans," and unlike BERT it casts classification in natural-language space rather than via a [CLS] token.
- LLM optimization trades off three competing goals — speed, stability, and memory — and remains "fairly ad-hoc and poorly understood"; faster convergence and lower precision tend to reduce stability.
- [[Adam]] adds momentum and per-dimension adaptive step sizes via first/second moment estimates $m_t,v_t$ with bias correction, costing $4\times$ params of storage vs. $2\times$ for plain [[SGD]]; [[Adafactor]] (Shazeer & Stern, 2018) cuts memory from $O(mn)$ to $O(m+n)$ by storing row/column moment sums and dropping momentum, and was used to train [[T5]].
- [[MixedPrecisionTraining]] (Narang et al., 2018) keeps FP32 master weights, computes in FP16, and uses loss scaling because FP16 values below $2^{-24}$ underflow to 0 — halving memory.
- Transformers require [[LearningRateWarmup]] (increase LR initially, then decay); Huang et al. 2020 attribute the need to vanishing gradients from layer normalization destabilizing [[Adam]].
- Initialization is scaled: Xavier $W_{ij}\sim\mathcal{N}(0,1/n)$ with [[GPT-2]]/[[GPT-3]] adding a $1/\sqrt{N}$ factor (N = number of residual layers) and [[T5]] scaling attention matrices by $1/\sqrt{d}$.
- [[GPT-3]] training recipe: [[Adam]] with $\beta_1=0.9$, $\beta_2=0.95$, $\epsilon=10^{-8}$; batch size 3.2M tokens (~1500 sequences); [[GradientClipping]] to norm 1; linear warmup over the first 375M tokens then cosine decay to 10% of peak; gradually increasing batch size; weight decay 0.1.

## Key Quotes
> "i.i.d. noise, replace spans" — the T5 unsupervised objective the paper found worked well, among many that performed similarly

> "fairly ad-hoc and poorly understood" — characterizing the current state of large language model optimization

## Connections
- [[GPT-3]] — the canonical decoder-only autoregressive model; its full optimizer/learning-rate recipe closes the lecture.
- [[GPT-2]] — decoder-only model whose autoregressive decoding and $1/\sqrt{N}$ init scaling are referenced.
- [[BERT]] — canonical encoder-only model, defined here with its masked-LM + next-sentence-prediction objective.
- [[RoBERTa]] — the optimized BERT that drops next-sentence prediction and scales up data.
- [[BART]] — encoder-decoder denoising model masking 30% of tokens and permuting sentences.
- [[T5]] — the text-to-text encoder-decoder trained with Adafactor on a span-corruption objective.
- [[Transformer]] — the shared backbone architecture for all objectives discussed.
- [[MaskedLanguageModeling]] — BERT's core objective; reconstruct masked/corrupted tokens.
- [[NextSentencePrediction]] — BERT's auxiliary binary objective, later removed by RoBERTa.
- [[AutoregressiveLanguageModeling]] — the maximum-likelihood next-token objective for decoder-only models.
- [[Adam]] — adaptive-moment optimizer; the default for LLM training.
- [[Adafactor]] — memory-efficient optimizer storing factored moment statistics; used for T5.
- [[SGD]] — baseline optimizer contrasted with Adam on memory and convergence.
- [[MixedPrecisionTraining]] — FP16 computation with FP32 master weights and loss scaling.
- [[LearningRateWarmup]] — the warmup-then-decay schedule Transformers require.
- [[GradientClipping]] — clip gradient norm to stabilize training (used in GPT-3).
- [[AdamW]] — decoupled weight-decay variant referenced via Loshchilov & Hutter 2017.

## Contradictions
- None identified.
