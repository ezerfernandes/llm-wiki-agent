---
title: "Made With ML — Transformers"
type: source
tags: [foundations, made-with-ml, deep-learning, transformer, nlp]
date: 2026-05-15
source_file: raw/madewithml/foundations-transformers.md
---

## Summary
Capstone foundations lesson on the [[transformer]] architecture from *Attention Is All You Need* (Vaswani et al., 2017). Builds up the three core innovations — [[scaleddotproductattention]] `softmax(QK^T / √d_k) V`, [[multiheadattention]] running several attention heads in parallel and concatenating, and sinusoidal positional encoding to inject sequence order — and then uses a pretrained BERT encoder from [[HuggingFace]] (specifically `allenai/scibert_scivocab_uncased`) as a feature extractor for the same text-classification task used throughout the course. Closes with inference and an interpretability section that inspects which tokens contribute most to a prediction.

## Key Claims
- Transformers replace recurrence with stacked self-attention, enabling fully parallel computation over a sequence — overcoming the sequential bottleneck of [[RNN]]s.
- Scaled dot-product attention projects inputs into Query (Q), Key (K), and Value (V) matrices via learned weights, computes attention as `softmax(QK^T / √d_k) V`, and the `√d_k` scaling prevents softmax saturation for large key dimensions.
- Multi-head attention runs `h` independent attention heads in parallel on lower-dimensional projections, concatenates them, and re-projects — letting the model jointly attend to different representation subspaces.
- Self-attention is permutation-invariant; positional encoding (sinusoidal or learned) is added to token embeddings so the model can use order information.
- Sinusoidal positional encodings extrapolate to sequence lengths not seen during training, because they are a fixed deterministic function of position.
- Sub-word tokenization (WordPiece in the lesson's BERT-based tokenizer) is preferred over character-level: it captures meaningful morphemes (prefixes, suffixes, roots) while keeping vocabulary bounded.
- The lesson uses HuggingFace's pretrained BertModel as a frozen / fine-tunable feature extractor rather than training a transformer from scratch — pretraining solves the "needs huge data" disadvantage in practice.
- Transformers are compute-intensive (quadratic in sequence length) but unlike CNNs (filter-span limited) and RNNs (sequential), they can attend to any position in one step.

## Key Quotes
> "Transformers are a very popular architecture that leverage and extend the concept of self-attention to create very useful representations of our input data for a downstream task." — Overview

> "Better representation for our input tokens via contextual embeddings where the token representation is based on the specific neighboring tokens using self-attention." — Advantages

> "Attend (in parallel) to all the tokens in our input, as opposed to being limited by filter spans (CNNs) or memory issues from sequential processing (RNNs)." — Advantages

> "The most popular type of self-attention is scaled dot-product attention from the widely-cited Attention is all you need paper. This type of attention involves projecting our encoded input sequences onto three matrices, queries (Q), keys (K) and values (V), whose weights we learn."

## Connections
- [[MadeWithML]] — course this lesson belongs to
- [[GokuMohandas]] — author
- [[PyTorch]] — framework
- [[HuggingFace]] — provides the pretrained BertModel + tokenizer
- [[transformer]] — central architecture
- [[BERT]] — concrete pretrained model used (`allenai/scibert_scivocab_uncased`)
- [[SciBERT]] — specific BERT variant used
- [[Attention]] — predecessor concept
- [[selfattention]] — building block of every transformer layer
- [[scaleddotproductattention]] — the specific attention formulation
- [[multiheadattention]] — parallel attention heads
- [[PositionalEncoding]] — sinusoidal order injection
- [[wordpiece]] — sub-word tokenization used by BERT
- [[Tokenizer]] — preprocessing
- [[ContextualEmbedding]] — output of transformer encoder
- [[TransferLearning]] — pretrained encoder fine-tuned downstream
- [[FineTuning]] — downstream adaptation
- [[Interpretability]] — attention-based per-token attribution
- [[AttentionIsAllYouNeed]] — originating paper

## Contradictions
- None identified.
