---
title: "CS324 — Modeling"
type: source
tags: [cs324, llm, course-lecture, architecture]
date: 2022-01-01
source_file: https://stanford-cs324.github.io/winter2022/lectures/modeling/
---

## Summary
This Stanford CS324 lecture opens the black box of large language models by covering two pillars of model construction: [[Tokenization]] and model architecture. It walks through tokenization schemes ([[BPE]] and the [[UnigramLanguageModel]]/SentencePiece approach), the move from static to [[ContextualEmbeddings]], the three architectural families (encoder-only, decoder-only, encoder-decoder), and builds the [[Transformer]] from primitives — [[Attention]], [[SelfAttention]], multi-headed attention, feedforward layers, residual connections, layer normalization, and positional embeddings — culminating in the full [[GPT-3]] specification.

## Key Claims
- A tokenizer maps raw text to a sequence of tokens from a vocabulary $\mathcal{V}$; good tokenization balances three competing concerns — sequence length, parameter sharing across related words (vital for morphologically rich languages like Arabic and Turkish), and per-token meaningfulness.
- Naive space-splitting fails: Chinese has no spaces, German has long compounds, and English has hyphenated words and contractions (the Penn Treebank splits *don't* into *do* + *n't*).
- [[BPE]] ([[SennrichEtAl2015]]) starts with a character vocabulary and iteratively merges the most frequent adjacent pair, emitting an ordered merge list; [[GPT-2]] and [[GPT-3]] use BPE with a 50K vocabulary, and [[WangEtAl2019]] apply BPE at the byte level (there are 144,697 Unicode characters) for multilingual coverage.
- The [[UnigramLanguageModel]] (SentencePiece, [[KudoRichardson2018]]) defines a likelihood objective $p(x_{1:L}) = \prod_{(i,j)\in T} p(x_{i:j})$, trains via EM, and prunes tokens by their loss contribution (keeping the top 80%); it is used by [[T5]] and [[Gopher]].
- Tokenizer choice has real efficiency impact: [[Jurassic]] (SentencePiece, 256K vocab) needs 28% fewer tokens than GPT-3 (≈1.4× faster) and fits 39% more text into the same 2048-token context.
- The central modeling abstraction is the embedding function $\phi: \mathcal{V}^L \to \mathbb{R}^{d\times L}$ producing [[ContextualEmbeddings]] — embeddings whose values depend on the surrounding context, unlike static word embeddings.
- There are three model families: encoder-only ([[BERT]], [[RoBERTa]]) gives bidirectional embeddings for classification but cannot generate and needs masked-LM objectives; decoder-only ([[GPT-2]], [[GPT-3]]) is autoregressive with unidirectional context and simple maximum-likelihood training; encoder-decoder ([[BART]], [[T5]]) combines bidirectional input encoding with autoregressive generation.
- [[RecurrentNeuralNetwork]] sequence models compute $h_i = \text{RNN}(h_{i-1}, x_i)$ left-to-right; the SimpleRNN ([[Elman1990]]) computes $\sigma(Uh + Vx + b)$ but suffers from vanishing gradients, addressed by LSTM/GRU variants, with bidirectional variants used by [[ELMo]] and [[ULMFiT]].
- [[Attention]] ([[VaswaniEtAl2017]]) is a soft lookup: scores $= x^\top W_\text{key}^\top W_\text{query}\, y$, weights $\alpha = \text{softmax}(\text{score}/\sqrt{d})$, output $= \sum_i \alpha_i (W_\text{value}\, x_i)$; [[SelfAttention]] uses each token as its own query so every token attends to every other, and multi-headed attention runs several heads to capture different syntactic/semantic relations.
- The [[Transformer]] block stacks AddNorm(FeedForward, AddNorm(SelfAttention, x)), where AddNorm wraps each sublayer with a residual connection $x + f(x)$ (inspired by ResNets) and [[LayerNormalization]] to keep activation magnitudes stable.
- Because token embeddings carry no position information, sinusoidal [[PositionalEmbeddings]] are added: $P_{i,2j}=\sin(i/10000^{2j/d_\text{model}})$ and $P_{i,2j+1}=\cos(i/10000^{2j/d_\text{model}})$.
- [[GPT-3]] is $\text{TransformerBlock}^{96}(\text{EmbedTokenWithPosition}(x_{1:L}))$ with $d_\text{model}=12{,}288$, $d_\text{ff}=4d_\text{model}$, $n_\text{heads}=96$, context $L=2{,}048$, 96 layers, and 175 billion parameters.
- These design choices are not necessarily optimal: [[LevineEtAl2020]] argue GPT-3 is too deep, motivating the deeper-but-wider [[Jurassic]] architecture; other variants include post-norm vs. pre-norm layer-norm placement, dropout, and the sparse Transformer GPT-3 uses to reduce parameters by interleaving sparse and dense layers.

## Key Quotes
> "These decisions are not necessarily optimal. Levine et al. 2020 provide some theoretical justification, showing that the GPT-3 is too deep, which motivated the training of a deeper but wider Jurassic architecture." — on GPT-3's depth and the design rationale for Jurassic

> "GPT-3 uses a sparse Transformer to reduce the number of parameters, interleaving it with dense layers." — on architectural variants beyond the vanilla Transformer

## Connections
- [[Transformer]] — the lecture builds this architecture from primitives (attention, feedforward, residuals, layer norm, positional embeddings).
- [[Attention]] — defined here as a soft, query/key/value lookup, the core operation of the Transformer.
- [[SelfAttention]] — uses each token as a query so all tokens attend to one another; the contextualizing layer in a Transformer block.
- [[Tokenization]] — one of the lecture's two main themes; converting raw text into token sequences.
- [[BPE]] — the byte-pair-encoding tokenizer used by GPT-2/GPT-3, introduced for NLP by Sennrich et al.
- [[UnigramLanguageModel]] — the likelihood-based SentencePiece tokenizer used by T5 and Gopher.
- [[ContextualEmbeddings]] — the central representation that distinguishes neural LMs from static word vectors.
- [[GPT-3]] — the worked example whose full architecture (175B params, 96 layers) closes the lecture.
- [[BERT]] — canonical encoder-only model for bidirectional classification embeddings.
- [[T5]] — canonical encoder-decoder text-to-text model.
- [[BART]] — encoder-decoder denoising sequence-to-sequence model.
- [[RecurrentNeuralNetwork]] — the pre-Transformer sequence model contrasted against attention.
- [[Jurassic]] — AI21's deeper-but-wider model with a 256K SentencePiece vocabulary, used to contrast tokenizer/architecture choices.
- [[VaswaniEtAl2017]] — "Attention is All You Need," the foundational Transformer paper cited throughout.
- [[PositionalEmbeddings]] — sinusoidal scheme injecting order into otherwise position-agnostic token embeddings.
- [[LayerNormalization]] — stabilization technique inside the AddNorm adapter.

## Contradictions
- None identified.
