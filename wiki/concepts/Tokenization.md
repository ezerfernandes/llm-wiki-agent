---
title: "Tokenization"
type: concept
tags: [nlp, preprocessing]
sources: [madewithml-preprocessing, madewithml-transformers, ai-engineering-ch01-intro, ai-engineering-ch02-foundation-models, hands-on-llm-ch01-introduction-to-llms, hands-on-llm-ch02-tokens-and-embeddings, ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Tokenization

Splitting text into discrete units (words, subwords, bytes) for model input. Modern systems use [[sentencepiece]] or [[wordpiece]] via a learned [[Tokenizer]] shared between training and inference.

## From [[ai-engineering-ch01-intro|AI Engineering Ch 1]]

[[ChipHuyen|Chip Huyen]] supplies the practitioner-level framing for *why* foundation models tokenize at all:

- **Tokens, not words or characters.** Three reasons, per Ch 1:
  1. Tokens decompose words into meaningful sub-components ("cooking" → "cook" + "ing").
  2. There are far fewer unique tokens than unique words → smaller vocabulary → more efficient model.
  3. Tokens gracefully handle unknown words ("chatgpting" → "chatgpt" + "ing").
- **Concrete numbers**: GPT-4 vocabulary = **100,256**; Mixtral 8x7B vocabulary = **32,000**; the average GPT-4 token is **~¾ the length of a word** (100 tokens ≈ 75 words).
- **Worked example**: GPT-4 splits *"I can't wait to build AI applications"* into 9 tokens; *"can't"* becomes two tokens, `can` and `'t`.
- **Tokenizer choice is the model developer's**: vocabulary size and tokenization method are decided at model-build time. Non-English languages may see a single Unicode character become multiple tokens.

Tokenization sits at the boundary between [[DatasetEngineering]] (during data preparation) and inference ([[InferenceOptimization]] — KV-cache and TPOT scale with token count).

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

Ch 2 introduces **the cross-language tokenization-efficiency asymmetry** — a major source of cost and latency disparity between languages:

Yennie Jun's benchmark on MASSIVE (1M short texts × 52 languages, [[GPT4|GPT-4]]):

| Language | Median tokens |
|---|---|
| English | **7** |
| Spanish | similar to English |
| Hindi | **32** |
| Burmese | **72** |

> "To convey the same meaning, languages like Burmese and Hindi require a lot more tokens than English or Spanish. ... GPT-4 takes approximately **10 times longer in Burmese than in English for the same content**. For APIs that charge by token usage, Burmese costs 10 times more than English."

This **compounds the [[LowResourceLanguage|under-representation problem]]**: low-resource languages are simultaneously (a) poorly represented in training data, (b) structurally harder to learn, and (c) 10× more expensive to use at inference time.

Ch 2 also reiterates [[ChipHuyen]]'s Ch 1 framing: tokenizer choice is the model developer's, vocabulary size and method are fixed at model-build time. Non-English languages may see a single Unicode character become multiple tokens.

## From [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]]

Ch 1 introduces tokenization as **the first step of the [[BagOfWords|bag-of-words]] pipeline** — the same operation that underlies every later LLM input pipeline:

> "Tokenization, the process of splitting up the sentences into individual words or subwords (tokens). The most common method for tokenization is by splitting on a whitespace to create individual words. However, this has its disadvantages as some languages, like Mandarin, do not have whitespaces around individual words." — Ch 1

The chapter motivates the subword-token approach by flagging the whitespace-splitting failure mode for Mandarin (and analogously, for compound-word languages where word boundaries are ambiguous). Ch 1 forward-references Ch 2 for the deep-dive on tokenization influence on language models.

Ch 1's worked code uses [[HuggingFace|Hugging Face]] `AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")` — the canonical pair-the-tokenizer-with-the-model pattern that every modern LLM `transformers` workflow uses.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 is the wiki's **canonical deep-dive on tokenization**, contributing:

**Three design factors** that determine how a tokenizer breaks down text:
1. **The tokenization method** — [[BPE]] (used by [[GPT|GPT]] family, [[Galactica]], [[StarCoder2]], [[Phi3Mini|Phi-3]]/[[Llama]] 2), [[WordPiece]] (used by [[bert|BERT]]), [[SentencePiece]] (used by [[FLANT5|Flan-T5]]/[[t5|T5]]), or [[ByteLevelTokenization|byte-level]] tokenization-free encoding (CANINE / ByT5).
2. **Tokenizer parameters** — [[VocabularySize|vocabulary size]] (30K–100K typically), which [[SpecialToken|special tokens]] to include (BOS, EOS, pad, unk, cls, sep, mask, chat-role, FIM, etc.), and capitalization treatment.
3. **The training dataset domain** — even with identical method + parameters, tokenizers trained on English text vs code vs multilingual text produce different vocabularies.

**Four notable tokenization granularities** (Ch 2's taxonomy):

| Granularity | Pros | Cons | Examples |
|---|---|---|---|
| [[WordTokenization\|Word]] | Simple, intuitive | Vocabulary bloat; OOV failures | [[Word2Vec\|word2vec]], [[BagOfWords\|bag-of-words]] |
| [[SubwordEmbedding\|Subword]] | Vocab efficiency, graceful OOV via fall-back to char pieces | Slightly more complex training | Modern default — [[BPE]], [[WordPiece]], [[SentencePiece]] |
| [[CharacterTokenization\|Character]] | No OOV ever | ~3× longer sequences than subword | Rare in production LLMs |
| [[ByteLevelTokenization\|Byte]] | Lossless multilingual coverage | Even longer sequences | CANINE, ByT5; partial: [[GPT2]] / RoBERTa byte-fallback |

**Seven-tokenizer comparative tour** on a single contrived test string (capitalization, multilingual chars, emoji, Python code, whitespace, digits, special tokens):

| Tokenizer | Year | Vocab | Method | Notable behavior |
|---|---|---|---|---|
| [[bert\|BERT-base uncased]] | 2018 | 30,522 | [[WordPiece]] | Lowercases; drops newlines; `[UNK]` for emoji/Chinese; `##` continuation |
| [[bert\|BERT-base cased]] | 2018 | 28,996 | [[WordPiece]] | Same as above but preserves case (`CAPITALIZATION` → 8 tokens) |
| [[GPT2]] | 2019 | 50,257 | [[BPE]] | Preserves newlines; byte-fallback reconstructs emoji (🎵 → 3 bytes) |
| [[FLANT5\|Flan-T5]] | 2022 | 32,100 | [[SentencePiece]] | No whitespace tokens (bad for code); `<unk>` for emoji/Chinese |
| [[Galactica]] | 2022 | 50,000 | [[BPE]] | `[START_REF]`/`<work>` scientific tokens; per-digit; whitespace runs; per-tab |
| [[GPT4]] | 2023 | ~100,000 | [[BPE]] | Whitespace runs up to 83; `elif` token; fewer tokens overall |
| [[StarCoder2]] | 2024 | 49,152 | [[BPE]] | Code-focused; per-digit tokens; `<filename>`/`<reponame>`/`<gh_stars>` |
| [[Phi3Mini\|Phi-3]]/[[Llama]] 2 | 2023–24 | 32,000 | [[BPE]] | Chat tokens `<\|user\|>`/`<\|assistant\|>`/`<\|system\|>` |

**Two empirical claims**:
- *"Subword tokens often average three characters per token"* — so a 1,024-token context fits ~3× more text via subwords vs character tokens.
- **Whitespace-token design affects code performance**: a model with a single token for four consecutive whitespaces is more tuned to Python; without it the model must track indentation as separate tokens (worse performance).

**Tokenizer-model binding**: *"a pretrained language model is linked with its tokenizer and can't use a different tokenizer without training."* Cannot swap tokenizers after pretraining.

Ch 2 forward-references the [[HuggingFace|Hugging Face]] *Summary of the tokenizers* page and the [[d2l-nlp-pretraining|D2L]] subword-embedding section for deeper algorithm-level treatment.

## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

Ch 8 puts tokenization at the **boundary between [[DatasetEngineering|dataset engineering]] and [[InferenceOptimization|inference]]**: it's both the last step of data formatting and the first step of every inference call. The chapter's contribution is operational rather than conceptual:

- Each model uses a specific tokenizer; data must be formatted to match the model's expectations.
- The tokenizer pairs with the model's [[ChatTemplate|chat template]] — together they define the wire format.
- Data inspection should include **token-distribution analysis** (see what tokens are common; check for unusual tokens; verify length distributions) before training.

Ch 8 also flags that token-level [[DataDeduplication|deduplication]] is one of several dedup granularities (alongside document, paragraph, sentence) — and that exact-token-match dedup is often too aggressive while fuzzy match via [[MinHashDeduplication|MinHash]] is the production default.
