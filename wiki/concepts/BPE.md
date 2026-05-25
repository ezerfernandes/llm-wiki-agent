---
title: "Byte Pair Encoding (BPE)"
type: concept
tags: [nlp, tokenization, subword, compression]
sources: [d2l-nlp-pretraining, hands-on-llm-ch02-tokens-and-embeddings, hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# Byte Pair Encoding (BPE)

A statistical subword-tokenization algorithm adapted to NLP by [[RicoSennrich|Sennrich]], Haddow & Birch (2015) from a 1994 data-compression algorithm. Learns a **fixed-size vocabulary** of variable-length subword units by **greedy frequency-based merging**:

1. Initialize the vocabulary with all individual characters (plus a special end-of-word marker — D2L uses `'_'` — and `[UNK]`).
2. Tokenize the training corpus as space-separated single characters within each word; do not consider pairs that cross word boundaries.
3. Find the most frequent pair of consecutive symbols across the corpus; concatenate it into a new symbol and add it to the vocabulary.
4. Replace every occurrence of that pair with the merged symbol.
5. Repeat steps 3–4 for a target number of merges (which sets the final vocab size).

Result: common substrings ("fast", "tall", "er_") become single tokens while rare/novel words decompose into their longest learnable subword pieces (e.g. "tallest_" → "tall est_" using the merges learned on "fast/tall" data). To get a vocabulary of size $m$ from an initial alphabet of size $n$, perform $m-n$ merges.

BPE underpins the tokenization of [[GPT2|GPT-2]], [[GPT3|GPT-3]], [[RoBERTa]], and most decoder-only LLMs; [[WordPiece]] (used by [[BERT]]) is a closely-related variant that picks the merge that **maximizes unigram likelihood** rather than raw frequency. [[FastText]]'s character-$n$-gram approach is the alternative non-merge-based subword scheme.

See [[d2l-nlp-pretraining]] §subword-embedding §Byte-Pair-Encoding.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 names BPE as **the most popular tokenization method**, used across the [[GPT|GPT]] family, [[Galactica]], [[StarCoder2]], and [[Phi3Mini|Phi-3]] / [[Llama]] 2. The chapter's comparative tokenizer tour highlights two BPE-specific behaviors:

- **Byte-level fallback** ([[GPT2]] / [[RoBERTa]]) — the vocabulary includes the 256 individual bytes as fall-back tokens, so any Unicode character can be encoded losslessly. *"This doesn't make them tokenization-free byte-level tokenizers, because they don't use these bytes to represent everything, only a subset."* In Ch 2's demo, [[GPT2|GPT-2]] decomposes the 🎵 emoji into 3 byte tokens (IDs 8582, 236, 113) that round-trip correctly through `decode`.
- **Domain-tuned BPE vocabularies** can include sequences of consecutive whitespaces as single tokens — *"the GPT-4 tokenizer represents the four spaces as a single token. In fact, it has a specific token for every sequence of whitespaces up to a list of 83 whitespaces"* — improving Python-code encoding efficiency at the cost of vocabulary slots.

The chapter also notes that newer BPE vocabularies trend **larger** (GPT-4 at ~100K, vs GPT-2's 50,257), prioritizing fewer tokens per text over a smaller embedding matrix.

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 records BPE in a **multimodal** setting via the [[BLIP2|BLIP-2]] `Blip2Processor`, whose `.tokenizer` is a `GPT2TokenizerFast` (the GPT-2-family BPE byte-level encoder) because the BLIP-2 LLM backbone is OPT-2.7b ([[meta|Meta]]) — which uses the same BPE byte-level tokenizer family as GPT-2 / RoBERTa. Inspection reports `vocab_size=50265`, BOS/EOS/UNK = `</s>`, PAD = `<pad>`. Worked tokenization of *"Her vocalization was remarkably melodic"* → `['</s>', 'Her', 'Ġvocal', 'ization', 'Ġwas', 'Ġremarkably', 'Ġmel', 'odic']`.

Ch 9 also codifies the **`Ġ`-as-space byte-level convention** the BPE-byte-level family uses: *"this is actually supposed to be a space. However, an internal function takes characters in certain code points and moves them up by 256 to make them printable. As a result, the space (code point 32) becomes Ġ (code point 288)."* This is the wiki's first explicit narration of the code-point-shift mechanism — see [[ByteLevelTokenization]].
