---
title: "HuggingFace LLM Course — Ch 6: The 🤗 Tokenizers library"
type: source
tags: [hf-llm-course, course, tokenization, bpe, wordpiece, unigram]
date: 2026-05-23
source_file: raw/hf-llm-course/ch06-tokenizers-library.md
---

## Summary

Chapter 6 of the HuggingFace LLM Course is a deep dive into the [[Tokenization]] pipeline as implemented by the 🤗 [[Tokenizers]] library (Rust, with Python bindings) that powers the "fast" tokenizers in 🤗 [[Transformers]]. It teaches how to (a) re-train an existing tokenizer on a new corpus with `AutoTokenizer.train_new_from_iterator()`, (b) exploit fast-tokenizer features such as [[OffsetMapping]] and `word_ids()` to reproduce the `token-classification` and `question-answering` pipelines by hand (including overflow/stride for long contexts), (c) understand the three dominant subword algorithms — [[BPE]], [[WordPiece]] (used by [[BERT]]), and [[Unigram]] (used with [[SentencePiece]] by [[T5]]/[[XLNet]]/[[ALBERT]]) — with full pedagogical implementations of each, and (d) assemble a tokenizer block-by-block from `normalizers`, `pre_tokenizers`, `models`, `trainers`, `post_processors`, and `decoders`, then wrap it in `PreTrainedTokenizerFast` for use in 🤗 Transformers. The chapter exposes the full tokenization stack from raw text to the `Encoding` object's `ids`, `type_ids`, `tokens`, `offsets`, `attention_mask`, `special_tokens_mask`, and `overflowing` fields.

## Key Claims

- Training a tokenizer is **deterministic** and statistical (identify best subwords); training a model is stochastic (SGD). Same algorithm + same corpus → same tokenizer.
- `AutoTokenizer.train_new_from_iterator()` keeps the original tokenizer's algorithm and special tokens — only the vocabulary changes — and **only works for fast tokenizers**.
- A new GPT-2 tokenizer trained on Python source code learns Python-specific tokens like `ĊĠĠĠ` (one indentation level) and `Ġ"""` (docstring opener), and correctly splits `LinearLayer` → `["ĠLinear","Layer"]`, producing ~25% fewer tokens than the stock GPT-2 tokenizer.
- Fast tokenizers' performance advantage manifests only when tokenizing many texts in parallel (`batched=True`); for a single sentence, fast can be **slower** than the Python version.
- Fast tokenizers return a `BatchEncoding` exposing `word_ids()`, `sentence_ids()`, `word_to_chars()`, `token_to_chars()`, `char_to_word()`, `char_to_token()` — and crucially `return_offsets_mapping=True` for character spans of every token.
- `word_ids()` generalizes the BERT-only `##` heuristic for "is this token at a word boundary?" to any fast tokenizer — enables clean NER/POS label propagation and whole-word masking.
- `(0, 0)` is reserved in offset mappings for special tokens like `[CLS]`/`[SEP]`.
- The standard QA setup tokenizes `[CLS] question [SEP] context [SEP]`, predicts independent start/end logits, masks non-context positions to `-10000` (preserving `[CLS]` for "no answer"), and uses `torch.triu(start_probs[:,None] * end_probs[None,:])` so that `start_index ≤ end_index`.
- Long-context QA uses `return_overflowing_tokens=True` with a `stride` (default 384/128 for the pipeline) to produce overlapping chunks; `overflow_to_sample_mapping` maps each chunk back to its source.
- Tokenization preprocessing has two steps before the model: **Normalization** (cleanup, NFC/NFKC/NFD/NFKD, lowercasing, accent stripping) and **[[PreTokenization]]** (splitting into pre-words; BERT splits on whitespace+punctuation, GPT-2 keeps spaces as `Ġ`, T5 SentencePiece uses `▁` and only splits on whitespace).
- [[SentencePiece]] treats input as a Unicode character stream including spaces (as `▁`), enabling **reversible tokenization** (concat + replace `▁`) and zero-pre-tokenization for languages without spaces (Chinese/Japanese). BERT's tokenizer is **not** reversible (collapses repeating spaces).
- [[BPE]] training: start from base alphabet, iteratively merge the most frequent adjacent token pair. Tokenization: apply merges in order. Used by GPT, GPT-2, RoBERTa, BART, DeBERTa.
- **[[ByteLevelBPE]]** (GPT-2/RoBERTa) tokenizes bytes (256 base) instead of characters → no `[UNK]` token possible; emojis and rare Unicode never become unknown.
- [[WordPiece]] training: same merge-rule approach as BPE but selects the pair with best **score = freq_pair / (freq_a × freq_b)**, prioritizing pairs whose parts are individually rare. Inner-word chars get the `##` prefix. Google never released the training implementation — described as "best guess".
- [[WordPiece]] tokenization saves **only the vocabulary** (no merges) — applies longest-prefix match. `"hugs"` → `["hug","##s"]`; BPE on the same vocab would give `["hu","##gs"]`. A word with any unmatchable suffix becomes a single `[UNK]` (unlike BPE which UNKs only the missing chars). 🤗 Tokenizers does **not** actually train WordPiece — it trains BPE and uses WordPiece tokenization at inference.
- [[Unigram]] inverts the loop: start from a **large** vocab, iteratively **remove** the bottom *p%* (10–20%) of tokens by loss-increase-when-removed; never remove base characters. Initial vocab can come from BPE-with-large-size or top substrings. Used with SentencePiece by AlBERT, T5, mBART, Big Bird, XLNet.
- [[Unigram]] tokenization treats tokens as independent (P(seg) = ∏ P(token)); the best segmentation is found via the **Viterbi algorithm** over a token graph. Fewer-token segmentations win because each factor divides by total frequency.
- SentencePiece uses an **Enhanced Suffix Array (ESA)** for initial-vocab construction and approximates the per-token loss-increase by replacing the removed token with its segmentation in the remaining vocab — so all scores compute in one pass.
- A tokenizer built via the 🤗 Tokenizers library is a `Tokenizer(model)` plus four pluggable stages: `normalizer`, `pre_tokenizer`, `post_processor` (e.g., `TemplateProcessing` with `$A`/`$B` and type-id colons), and `decoder`. Trainer must be told about special tokens explicitly (they are not in the corpus). Wrap with `PreTrainedTokenizerFast` or a specific `BertTokenizerFast`/`GPT2TokenizerFast`/`XLNetTokenizerFast` for 🤗 Transformers.

## Key Quotes

> "Training a tokenizer is a statistical process that tries to identify which subwords are the best to pick for a given corpus … It's deterministic, meaning you always get the same results when training with the same algorithm on the same corpus."

> "When tokenizing a single sentence, you won't always see a difference in speed between the slow and fast versions of the same tokenizer. In fact, the fast version might actually be slower!"

> "The key functionality of fast tokenizers is that they always keep track of the original span of texts the final tokens come from — a feature we call offset mapping."

> "SentencePiece … considers the text as a sequence of Unicode characters, and replaces spaces with a special character, `▁`. Used in conjunction with the Unigram algorithm, it doesn't even require a pre-tokenization step."

> "Google never open-sourced its implementation of the training algorithm of WordPiece, so what follows is our best guess based on the published literature."

> "Compared to BPE and WordPiece, Unigram works in the other direction: it starts from a big vocabulary and removes tokens from it until it reaches the desired vocabulary size."

> "🤗 Tokenizers does not implement WordPiece for the training (since we are not completely sure of its internals), but uses BPE instead."

## Code & Patterns

- **`train_new_from_iterator(corpus, vocab_size)`** — reuses an old fast tokenizer's algorithm/specials, retrains vocab on a new corpus (Python-generator pattern to avoid loading dataset into RAM).
- **`AutoTokenizer.from_pretrained()` + `is_fast` / `encoding.is_fast`** — verify a fast tokenizer is in use.
- **`encoding.tokens()` / `word_ids()` / `sequence_ids()` / `word_to_chars()` / `token_to_chars()` / `char_to_word()` / `char_to_token()`** — the BatchEncoding mapping API.
- **`return_offsets_mapping=True`** — get `(start_char, end_char)` per token; `(0,0)` for specials.
- **`return_overflowing_tokens=True, stride=…, max_length=…, truncation="only_second"`** — sliding-window chunking for long QA contexts; check `overflow_to_sample_mapping`.
- **Token-classification post-processing** — `aggregation_strategy ∈ {"simple","first","max","average"}`; IOB1 vs IOB2 label formats matter for B-/I- interpretation.
- **QA scoring** — mask non-context with `-10000`, softmax start/end, outer product, `torch.triu` to enforce `start ≤ end`, argmax, then offset lookup.
- **`tokenizer.backend_tokenizer.normalizer.normalize_str(...)` and `.pre_tokenizer.pre_tokenize_str(...)`** — peek inside the fast tokenizer.
- **BPE algorithm** — `compute_pair_freqs` + `merge_pair` loop; merges dict + appended vocab; byte-level avoids `[UNK]`.
- **WordPiece algorithm** — `score = pair_freq / (left_freq * right_freq)`; `encode_word` does longest-prefix-match with `##` prefixing on remainder.
- **Unigram algorithm** — initial vocab from `char_freqs ∪ top-N subwords`; store `-log(p)`; Viterbi `encode_word(word, model)` returning `(tokens, score)`; prune by `compute_scores` removing bottom 10%; never drop length-1 tokens.
- **Building from scratch** — `Tokenizer(models.WordPiece|BPE|Unigram(...))` + `.normalizer`/`.pre_tokenizer`/`.post_processor`/`.decoder`; trainers: `WordPieceTrainer` / `BpeTrainer` / `UnigramTrainer` (latter needs explicit `unk_token`, exposes `shrinking_factor`/`max_piece_length`).
- **Normalizers** — `BertNormalizer`, `NFD`/`NFKD`, `Lowercase`, `StripAccents`, `Replace` (with `Regex`), composed via `normalizers.Sequence`.
- **Pre-tokenizers** — `BertPreTokenizer`, `Whitespace` (splits on whitespace + non-word), `WhitespaceSplit` (whitespace only), `Punctuation`, `ByteLevel(add_prefix_space=...)`, `Metaspace` (for SentencePiece), composed via `pre_tokenizers.Sequence`.
- **Post-processors** — `TemplateProcessing(single="[CLS]:0 $A:0 [SEP]:0", pair="[CLS]:0 $A:0 [SEP]:0 $B:1 [SEP]:1", special_tokens=[...])`; `ByteLevel(trim_offsets=False)` to keep leading space in `Ġ` offsets.
- **Decoders** — `WordPiece(prefix="##")`, `ByteLevel()`, `Metaspace()`.
- **Persisting** — `tokenizer.save("tokenizer.json")` + `Tokenizer.from_file(...)`; wrap with `PreTrainedTokenizerFast(tokenizer_object=...)` and explicit special tokens (or use `BertTokenizerFast`/`GPT2TokenizerFast`/`XLNetTokenizerFast`); XLNet uses `padding_side="left"`.

## Connections

- [[Tokenization]] — chapter is a deep extension; ties together BPE/WordPiece/Unigram and the normalization → pre-tokenization → model → post-processing pipeline.
- [[Tokenizer]] — describes the architecture of the `Tokenizer` class and its building blocks.
- [[BPE]] — full training/tokenization walkthrough plus pedagogical implementation; clarifies byte-level BPE.
- [[ByteLevelTokenization]] — concrete byte-level BPE used by GPT-2/RoBERTa with no `[UNK]`.
- [[wordpiece]] — best-guess training algorithm with the `freq_pair/(freq_a·freq_b)` score; longest-prefix tokenization.
- [[sentencepiece]] — `▁` for spaces, reversible, language-agnostic; pairs with Unigram.
- [[SubwordEmbedding]] — context for why subword units matter.
- [[CharacterTokenization]] / [[WordTokenization]] — endpoints of the subword spectrum.
- [[BERT]] / [[DistilBERT]] / [[RoBERTa]] / [[GPT]] / [[GPT2]] / [[deberta]] / [[ALBERT]] / [[FLANT5]] — model-tokenizer correspondences (WordPiece for BERT-family; BPE for GPT/RoBERTa/BART/DeBERTa; Unigram+SentencePiece for AlBERT/T5/XLNet/mBART).
- [[HuggingFace]] — owner of the 🤗 Tokenizers + Transformers libraries.
- [[google]] — origin of WordPiece and BERT.
- [[openai]] — origin of BPE adoption for GPT.

## Contradictions

- The chapter notes 🤗 Tokenizers does **not** implement true WordPiece training (uses BPE under the hood and applies WordPiece encoding at inference). Any existing wiki claim that `WordPieceTrainer` faithfully reproduces Google's training is mistaken; the trainer is BPE-based, and exact-match retraining via `train_new_from_iterator()` is impossible for WordPiece-style tokenizers.
- The chapter explicitly says "Google never open-sourced" the WordPiece training implementation — if any concept page asserts the training algorithm definitively, it should be hedged as "best guess based on published literature".
- Fast tokenizers being "always faster than slow" is a common simplification — the chapter contradicts it for single-sentence cases.
