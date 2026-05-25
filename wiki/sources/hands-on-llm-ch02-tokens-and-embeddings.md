---
title: "Hands-On LLMs Ch 2 — Tokens and Embeddings"
type: source
tags: [book, hands-on-llm, oreilly, llm, tokenization, embeddings, word2vec]
date: 2024-01-01
source_file: raw/books/hands-on-llm/ch02-tokens-and-embeddings.md
book: "Hands-On Large Language Models"
book_isbn13: "9781098150969"
book_authors: ["Jay Alammar", "Maarten Grootendorst"]
book_publisher: "O'Reilly Media"
book_year: 2024
---

# Hands-On LLMs Ch 2 — Tokens and Embeddings

## Summary

The second chapter of [[JayAlammar|Jay Alammar]] and [[MaartenGrootendorst|Maarten Grootendorst]]'s *Hands-On Large Language Models* ([[OReilly|O'Reilly Media]], 2024, ISBN 978-1-098-15096-9) is the **deep-dive on the two layers that bookend every modern LLM call**: the [[Tokenizer|tokenizer]] that converts text into integer IDs, and the [[Embedding|embedding]] matrix that maps those IDs into the dense vector space the model actually computes on. The chapter contains three movements: (1) a **comparative tour of seven trained tokenizers** — [[bert|BERT]] uncased / [[bert|BERT]] cased / [[GPT2|GPT-2]] / [[FLANT5|Flan-T5]] / [[GPT4|GPT-4]] / [[StarCoder2]] / [[Galactica]] / [[Phi3Mini|Phi-3]] (Llama 2 tokenizer) — on a single contrived test string designed to expose how each handles capitalization, multilingual characters, emojis, Python code, whitespace, digits, and special tokens; (2) the [[TokenEmbedding|token-embedding]] / [[ContextualEmbedding|contextualized-word-embedding]] distinction, illustrated by running [[microsoft|Microsoft's]] [[deberta|DeBERTa v3]] on `"Hello world"` and inspecting the resulting `[1, 4, 384]` output tensor; and (3) **[[Word2Vec|word2vec]] as the conceptual ancestor** of all modern embeddings — the chapter walks the [[SkipGram|skip-gram]] + [[NegativeSampling|negative-sampling]] objective end-to-end, then re-applies the same algorithm to **music playlists** to build a [[Word2VecRecommender|song-recommendation system]] (Billie Jean → Kiss / Wanna Be Startin' Somethin' / The Way You Make Me Feel; Fade To Black → Little Guitars / Unchained / The Last in Line) demonstrating that **embeddings are useful far outside of NLP** — anywhere objects appear in sequences.

The chapter also introduces **[[TextEmbedding|text embeddings]] (sentence / document embeddings)** as a single vector per piece of text — the foundation of semantic search and RAG covered in Part II — and demonstrates them with the `sentence-transformers/all-mpnet-base-v2` model from the [[SentenceTransformers|sentence-transformers]] package (768-dim output). The chapter's organizing claim is that **three design choices determine tokenizer behavior**: (a) the tokenization **algorithm** ([[BPE]] / [[WordPiece]] / [[SentencePiece]] / character / byte), (b) the **parameters** (vocab size, special tokens, capitalization handling), and (c) the **training dataset domain** (English text vs code vs multilingual). Code-focused tokenizers ([[GPT4|GPT-4]], [[StarCoder2]], [[Galactica]]) assign single tokens to runs of whitespace; [[StarCoder2]] and [[Galactica]] give every digit its own token (hypothesizing better numeracy); [[Galactica]] adds `[START_REF]`, `[END_REF]`, and `<work>` for scientific citations and chain-of-thought.

## Key Claims

- **Tokenizers, not models, see text.** The model receives `input_ids` — a tensor of integer token IDs — not raw text. The tokenizer is paired with the model at training time; *"a pretrained language model is linked with its tokenizer and can't use a different tokenizer without training."* The decode method translates IDs back to text.
- **Three design factors dictate a tokenizer's behavior**: (1) the tokenization **method** (popular: [[BPE]] used by [[GPT|GPT]] family, [[WordPiece]] used by [[bert|BERT]], [[SentencePiece]] used by T5/Flan-T5); (2) **parameters** like vocabulary size (commonly 30K–50K, with newer models reaching 100K+) and which special tokens to include; (3) the **training dataset domain** — even with the same method and parameters, a tokenizer trained on English vs code vs multilingual text produces different vocabularies.
- **Four notable ways to tokenize**: **word**, **subword**, **character**, **byte**. Subword (full-and-partial-words) is the modern default because it both reduces vocabulary size for inflectional families (`apolog` + `-y`, `-ize`, `-etic`, `-ist`) and gracefully handles unseen words by falling back to character-level pieces. *"Subword tokens often average three characters per token"* — so a 1,024-token context fits ~3× more text than character-level tokenization.
- **Byte-level / tokenization-free encoding** (CANINE, ByT5 — named in passing) is a competitive alternative especially for multilingual settings. **Some subword tokenizers ([[GPT2|GPT-2]], RoBERTa) include bytes as fall-back tokens** for characters they can't otherwise represent — *"This doesn't make them tokenization-free byte-level tokenizers, because they don't use these bytes to represent everything, only a subset."*
- **Special tokens encode model-system protocol.** Common ones: beginning-of-text (`<s>` or `[CLS]`), end-of-text / end-of-generation (`</s>`, `<|endoftext|>`), padding (`[PAD]`, `<pad>`), unknown (`[UNK]`, `<unk>`), classification (`[CLS]`), separator (`[SEP]`), masking (`[MASK]`). Newer chat models add **turn-role tokens** (`<|user|>`, `<|assistant|>`, `<|system|>` — Phi-3 / Llama 2); code models add **fill-in-the-middle tokens** (`<|fim_prefix|>` / `<|fim_middle|>` / `<|fim_suffix|>` for [[GPT4|GPT-4]] and [[StarCoder2]]); [[StarCoder2]] additionally has `<filename>` / `<reponame>` / `<gh_stars>` to disambiguate cross-file code context; [[Galactica]] adds `[START_REF]` / `[END_REF]` for citations and the **`<work>` token for chain-of-thought reasoning**.
- **The comparative tokenizer tour (single 6-line test string)** highlights divergent behaviors. Selected numbers from the chapter:
  - **[[bert|BERT]] uncased (2018, WordPiece, 30,522 vocab)**: lowercases everything; loses newlines; replaces emoji and Chinese chars with `[UNK]`; uses `##` prefix for continuation pieces (`capital ##ization`).
  - **[[bert|BERT]] cased (2018, WordPiece, 28,996 vocab)**: preserves capitalization; *"CAPITALIZATION"* becomes 8 tokens (`CA ##PI ##TA ##L ##I ##Z ##AT ##ION`).
  - **[[GPT2|GPT-2]] (2019, BPE, 50,257 vocab)**: preserves newlines and capitalization; reconstructs 🎵 from 3 byte-level tokens (8582, 236, 113); 4 spaces = 3 tokens.
  - **[[FLANT5|Flan-T5]] (2022, SentencePiece, 32,100 vocab)**: no newline / whitespace tokens (bad for code); emoji + Chinese chars replaced with `<unk>`.
  - **[[GPT4|GPT-4]] (2023, BPE, ~100K vocab)**: assigns single tokens to runs of whitespace **up to 83 consecutive whitespaces**; gives Python keyword `elif` its own token; uses fewer tokens overall (`CAPITALIZATION` = 2 tokens vs GPT-2's 4).
  - **[[StarCoder2]] (2024, BPE, 49,152 vocab)**: code-focused; whitespace-run-as-single-token; **every digit its own token** (`600` → `6 0 0`) — hypothesis: better number / math representation. *"In GPT-2, for example, the number 870 is represented as a single token. But 871 is represented as two tokens (8 and 71)."*
  - **[[Galactica]] (Meta, 2022, BPE, 50K vocab)**: scientific-knowledge-focused; same digit-splitting and whitespace-run-tokens as StarCoder2; also assigns a single token to **two tabs (`\t\t`)** — the only one of the seven that does.
  - **[[Phi3Mini|Phi-3]] / [[Llama|Llama 2]] (BPE, 32,000 vocab)**: standard chat tokens (`<|user|>`, `<|assistant|>`, `<|system|>`); uses `<s>` to mark beginning of text.
- **Whitespace-token design affects code performance.** *"A model that uses a single token to represent four consecutive whitespace characters is more tuned to a Python code dataset. While a model can live with representing it as four different tokens, it does make the modeling more difficult as the model needs to keep track of the indentation level."*
- **Static vs contextualized token embeddings.** A pretrained language model **holds an embedding vector for each token in its tokenizer's vocabulary** — an `embedding matrix` of shape `vocab_size × embedding_dim`. These vectors are randomly initialized and trained jointly with the rest of the model. The model then transforms these **static input embeddings** into **[[ContextualEmbedding|contextualized embeddings]]** (one per input position, dependent on the surrounding sequence) — the actual representations consumed by downstream tasks like named-entity recognition, extractive summarization, and even AI image generation systems ([[DALLE]], [[Midjourney]], [[StableDiffusion]]).
- **DeBERTa v3** ([[deberta|DeBERTa]]) — *"at the time of writing one of the best-performing language models for token embeddings while being small and highly efficient"*. The worked example tokenizes `"Hello world"` and inspects the output: `torch.Size([1, 4, 384])` — batch × 4 tokens (`[CLS] Hello world [SEP]`) × 384-dim contextualized vectors.
- **Text embeddings = one vector per sentence/document.** *"While token embeddings are key to how LLMs operate, a number of LLM applications require operating on entire sentences, paragraphs, or even text documents."* One common production technique: **average the token embeddings**. Higher-quality models are trained specifically on text-embedding objectives ([[SentenceTransformers|Sentence-BERT]], Reimers & Gurevych 2019). The chapter demonstrates with `sentence-transformers/all-mpnet-base-v2` → 768-dim vector for `"Best movie ever!"`.
- **Word2vec is the conceptual ancestor.** A two-step training process: (1) generate (center-word, context-word) pairs via a **sliding window** ([[SkipGram|skip-gram]] — predict context words from center), (2) train a binary-classification neural network on the *(word, candidate-neighbor)* pairs to output 1 if they tend to co-occur and 0 if not. **[[NegativeSampling|Negative sampling]]** — adding randomly-paired words labeled 0 — is essential; without it, the model trivially outputs 1 always. *"It turns out that we don't have to be too scientific in how we choose the negative examples"* — random sampling works.
- **Embeddings work for any sequence-of-objects.** The chapter demonstrates by **embedding songs from human-curated playlists** via `gensim.models.Word2Vec` on a Cornell University dataset (Shuo Chen) of US radio-station playlists — treating songs as words and playlists as sentences. Hyperparameters: `vector_size=32, window=20, negative=50, min_count=1, workers=4`. Recommendation queries:
  - `Billie Jean` (Michael Jackson) → `Kiss` (Prince), `Wanna Be Startin' Somethin'` + `The Way You Make Me Feel` (Michael Jackson), `Holiday` (Madonna), `Don't Stop 'Til You Get Enough` (Michael Jackson).
  - `California Love` (2Pac) → `If I Ruled the World` (Nas), `I'll Be Missing You` (Puff Daddy), `Hate It or Love It` (The Game), `Hypnotize` (The Notorious B.I.G.), `Drop It Like It's Hot` (Snoop Dogg).
  - `Fade To Black` (Metallica) → `Little Guitars` + `Unchained` (Van Halen), `The Last in Line` (Dio), `Mr. Brownstone` (Guns N' Roses), `Breaking the Law` (Judas Priest).
- **Skip-gram + negative sampling is the prototype of contrastive training** — the same idea behind text-pair retrieval models (Ch 10) and multimodal models that match images and captions (Ch 9).
- **Forward references.** Ch 4 (classification), Ch 8 (semantic search + [[rag|RAG]]), Ch 9 (multimodal / image generation), Ch 10 (training custom embedding models), Ch 11 (fine-tuning representation models).

## Key Quotes

> "Tokens are the way in which the model sees its inputs. A text prompt sent to the model is first broken down into tokens." — Ch 2

> "This is how the tokenizer broke down our input prompt. ... Some tokens are complete words (e.g., Write, an, email). Some tokens are parts of words (e.g., apolog, izing, trag, ic). Punctuation characters are their own token." — Ch 2 (on subword behavior with Phi-3's Llama-2 tokenizer)

> "There are three major factors that dictate how a tokenizer breaks down an input prompt. First, at model design time, the creator of the model chooses a tokenization method. ... Second, after choosing the method, we need to make a number of tokenizer design choices like vocabulary size and what special tokens to use. ... Third, the tokenizer needs to be trained on a specific dataset to establish the best vocabulary it can use." — Ch 2

> "The GPT-4 tokenizer represents the four spaces as a single token. In fact, it has a specific token for every sequence of whitespaces up to a list of 83 whitespaces. The Python keyword elif has its own token in GPT-4. Both this and the previous point stem from the model's focus on code in addition to natural language." — Ch 2

> "A major difference here to everything we've seen so far is that each digit is assigned its own token (so 600 becomes 6 0 0). The hypothesis here is that this would lead to better representation of numbers and mathematics. In GPT-2, for example, the number 870 is represented as a single token. But 871 is represented as two tokens (8 and 71). You can intuitively see how that might be confusing to the model and how it represents numbers." — Ch 2 (on StarCoder2)

> "A pretrained language model is linked with its tokenizer and can't use a different tokenizer without training. ... The language model holds an embedding vector for each token in the tokenizer's vocabulary." — Ch 2

> "Instead of representing each token or word with a static vector, language models create contextualized word embeddings that represent a word with a different token based on its context." — Ch 2

> "If, however, we have a dataset of only a target value of 1, then a model can cheat and ace it by outputting 1 all the time. To get around this, we need to enrich our training dataset with examples of words that are not typically neighbors. These are called negative examples." — Ch 2 (introducing negative sampling)

> "This idea of a model that takes two vectors and predicts if they have a certain relation is one of the most powerful ideas in machine learning, and time after time has proven to work very well with language models." — Ch 2 (skip-gram-as-contrastive-prototype)

> "Imagine if we treated each song as we would a word or token, and we treated each playlist like a sentence. These embeddings can then be used to recommend similar songs that often appear together in playlists." — Ch 2 (recommendation embeddings reframing)

## Concepts Introduced or Engaged

- [[Tokenization]] / [[Tokenizer]] — *engaged*, the chapter's primary subject.
- [[SubwordEmbedding|Subword tokenization]] — *engaged*, the dominant modern scheme.
- [[BPE]] / [[WordPiece]] / [[SentencePiece]] — *engaged*, the three main subword algorithms.
- [[ByteLevelTokenization]] — *new*, the tokenization-free encoding direction (CANINE / ByT5 are named in passing in the chapter without dedicated wiki pages).
- [[WordTokenization]] — *new*, the older word-level scheme.
- [[CharacterTokenization]] — *new*, the character-level scheme.
- [[SpecialToken]] — *new*, the umbrella term for `[CLS]`, `[SEP]`, `[PAD]`, `[UNK]`, `[MASK]`, `<s>`, `</s>`, `<|endoftext|>`, etc.
- [[FillInTheMiddle]] — *new*, the GPT-4 / StarCoder2 code-completion training objective marked by `<|fim_prefix|>` / `<|fim_middle|>` / `<|fim_suffix|>` tokens.
- [[ChatTemplate]] — *engaged*, with new role-token vocabulary (`<|user|>` / `<|assistant|>` / `<|system|>`).
- [[ClassificationToken]] / [[ClsToken]] — *engaged*, `[CLS]` semantics.
- [[SepToken]] — *new*, the BERT segment-separator token.
- [[PadToken]] — *new*, the padding token used to align sequence lengths.
- [[UnkToken]] — *new*, the unknown / out-of-vocabulary fallback token.
- [[MaskToken]] — *new*, used during masked-language-model training.
- [[VocabularySize]] — *new*, the count of distinct tokens a tokenizer can produce.
- [[Embedding]] / [[WordEmbedding]] — *engaged*, the chapter's second-half subject.
- [[TokenEmbedding]] — *new*, the per-token vector in the embedding matrix; an LLM holds one per vocabulary entry.
- [[StaticEmbedding]] — *new*, the input-side embedding pre-context (word2vec-style).
- [[ContextualEmbedding]] — *engaged*, the post-context per-token output of the encoder.
- [[TextEmbedding]] — *new*, the single-vector-per-sentence/document representation.
- [[SentenceEmbedding]] — *new*, special case of text embedding for one sentence.
- [[Word2Vec]] / [[SkipGram]] / [[CBOW]] — *engaged*, the chapter's canonical static-embedding algorithm.
- [[NegativeSampling]] — *engaged*, the contrastive training mechanism.
- [[NoiseContrastiveEstimation]] — *engaged*, the principle negative sampling derives from.
- [[ContrastiveLearning]] — *engaged*, the broader class of which word2vec is an early example.
- [[Word2VecRecommender]] — *new*, the song-embedding-via-playlists pattern; the chapter's headline non-NLP application.
- [[RecommenderSystems]] — *engaged*, the broader application domain.
- [[GloVe]] — *engaged*, the chapter's named alternative to word2vec.
- [[FastText]] — *engaged*, the chapter's third static-embedding mention.
- Named-entity recognition (NER), extractive text summarization — *named in passing*, downstream applications of contextualized embeddings (no dedicated wiki pages yet).

## Entities Introduced or Engaged

- [[JayAlammar]] / [[MaartenGrootendorst]] — *engaged*, co-authors.
- [[HandsOnLLM]] — *engaged*, the book.
- [[bert|BERT]] (uncased + cased) — *engaged*, tokenizer comparison subject.
- [[GPT2]] — *engaged*, tokenizer comparison subject.
- [[FLANT5]] — *new*, the Flan-T5 family; uses SentencePiece.
- [[GPT4]] — *engaged*, tokenizer comparison subject.
- [[StarCoder2]] — *new*, code-focused 15B model with digit-per-token strategy and `<filename>` / `<reponame>` / `<gh_stars>` special tokens.
- [[Galactica]] — *engaged* (existing stub upgraded), scientific LM with `[START_REF]` / `[END_REF]` / `<work>` tokens.
- [[Phi3Mini]] — *engaged*, uses Llama 2 tokenizer with added chat tokens.
- [[Llama]] / Llama 2 — *engaged*, the tokenizer Phi-3 reuses.
- [[deberta|DeBERTa v3]] — *new*, the chapter's contextualized-embedding worked model.
- [[SentenceTransformers]] — *new*, the canonical text-embedding Python library; the `all-mpnet-base-v2` model is the chapter's worked example.
- [[AllMPNetBaseV2]] — *new*, the specific sentence-embedding model used (768-dim).
- [[HuggingFace]] — *engaged*, provider of the canonical `transformers` Python library used for the tokenizer + model calls throughout the chapter.
- [[Gensim]] — *new*, the Python NLP library used for word2vec + GloVe loading and song-embedding training.
- Rico Sennrich — *engaged in passing*, BPE author (no dedicated wiki page yet).
- [[NilsReimers]] — *new*, Sentence-BERT first author.
- [[IrynaGurevych]] — *new*, Sentence-BERT senior author.
- [[ShuoChen]] — *new*, Cornell author who collected the song-playlist dataset.
- [[CornellUniversity]] — *new*, source institution of the playlist dataset.
- [[FrankHerbert]] — *new*, Dune novelist quoted *"Thou shalt not make a machine in the likeness of a human mind"* as the word2vec example sentence.
- [[MichaelJackson]] — *new*, recommendation-example artist (Billie Jean → Kiss / Wanna Be Startin' Somethin' / The Way You Make Me Feel).
- [[Metallica]] — *new*, recommendation-example artist (Fade To Black → Van Halen / Dio / Guns N' Roses / Judas Priest).
- [[DALLE]] / [[Midjourney]] / [[StableDiffusion]] — *engaged*, named as downstream consumers of contextualized embeddings for AI image generation.
- [[microsoft|Microsoft]] — *engaged*, provider of DeBERTa and Phi-3.
- [[meta|Meta]] — *engaged*, provider of Galactica and Llama 2.

## Connections

- [[hands-on-llm-ch01-introduction-to-llms]] — the predecessor chapter; this chapter is the deep-dive on the two terms Ch 1 introduces (tokens, embeddings).
- [[JayAlammar]] / [[MaartenGrootendorst]] — co-authors.
- [[HandsOnLLM]] — the book.
- [[Tokenization]] / [[Tokenizer]] — the chapter's primary subject.
- [[BPE]] / [[WordPiece]] / [[SentencePiece]] — the three algorithmic schools.
- [[bert|BERT]] / [[GPT2]] / [[FLANT5]] / [[GPT4]] / [[StarCoder2]] / [[Galactica]] / [[Phi3Mini]] — the seven tokenizers contrasted.
- [[Embedding]] / [[WordEmbedding]] / [[TokenEmbedding]] / [[StaticEmbedding]] / [[ContextualEmbedding]] / [[TextEmbedding]] / [[SentenceEmbedding]] — the embedding taxonomy.
- [[Word2Vec]] / [[SkipGram]] / [[CBOW]] / [[NegativeSampling]] / [[NoiseContrastiveEstimation]] / [[ContrastiveLearning]] — the word2vec mechanism.
- [[Word2VecRecommender]] / [[RecommenderSystems]] — the non-NLP application.
- [[deberta|DeBERTa v3]] — the chapter's worked contextualized-embedding model.
- [[SentenceTransformers]] / [[AllMPNetBaseV2]] — the chapter's worked text-embedding model.
- [[rag|RAG]] / semantic search — forward-referenced applications of text embeddings (Part II of the book).
- [[ChatTemplate]] / [[FillInTheMiddle]] / [[SpecialToken]] — the special-token vocabulary newer tokenizers add.

## Contradictions

None directly conflicting with existing wiki content. **Soft tensions worth flagging** (do not constitute contradictions):

- **Vocabulary-size for [[bert|BERT]]-base.** The chapter reports BERT-base uncased at **30,522** and BERT-base cased at **28,996**. The existing [[wordpiece]] page says "30,000-token vocabulary" — these are consistent (rounded). No contradiction.
- **GPT-4 vocabulary size.** Chapter says *"a little over 100,000"*; existing [[Tokenization]] page (sourcing [[ai-engineering-ch01-intro|Huyen Ch 1]]) gives **100,256**. Consistent.
- **The word2vec method labels.** This chapter introduces only **skip-gram** by name (and refers to the alternative simply via the contrastive-classification reframing); the wiki's existing [[SkipGram]] and [[CBOW]] pages distinguish them more sharply. No contradiction — Ch 2 is the simplified pedagogical framing; the wiki's existing pages are the canonical detailed treatment.
- **NCE vs negative sampling.** The chapter cites *"Noise-contrastive estimation: A new estimation principle for unnormalized statistical models"* as the inspiration for negative sampling. The existing [[NoiseContrastiveEstimation]] page (citing [[d2l-nlp-pretraining]]) carries the more precise statement that **negative sampling is NCE with the noise-probability term dropped**. Consistent — Ch 2 says the pragmatic version; the wiki page carries the formal version.
- **Tokenizer-pair-with-model.** The chapter states *"a pretrained language model is linked with its tokenizer and can't use a different tokenizer without training."* This is consistent with the existing [[Tokenizer]] / [[TrainingServingSkew]] framing. No contradiction.
- **The 'subword tokens average three characters' heuristic.** The chapter quotes this as a rule of thumb; consistent with [[ai-engineering-ch01-intro|Huyen Ch 1]]'s *"100 tokens ≈ 75 words"* (≈ 3.75 chars/token for English). No contradiction.

## Position in the wiki

This is the **second chapter from *Hands-On Large Language Models*** ingested (after [[hands-on-llm-ch01-introduction-to-llms|Ch 1]]) and the **canonical wiki-level deep-dive on tokenizers and embeddings**. It substantially extends the wiki's tokenization coverage:

- **First seven-tokenizer side-by-side comparison.** The wiki previously held tokenizer information scattered across [[Tokenization]], [[BPE]], [[WordPiece]], [[SentencePiece]], [[bert]], [[GPT2]], [[t5]], and others; this chapter is the first source that runs all seven tokenizers on a single test string and tabulates the diffs. The tokenizer-comparison table now lives on the [[Tokenization]] page as a *"From Hands-On LLMs Ch 2"* section.
- **First wiki coverage of code-tokenizer design tradeoffs.** [[StarCoder2]] and [[Galactica]] are not previously well-documented; their per-digit-token + whitespace-run-token strategies are the first explicit treatment of code-domain tokenization choices in the wiki.
- **First wiki coverage of the [[FillInTheMiddle]] special tokens** used by [[GPT4]] and [[StarCoder2]].
- **First wiki worked example of [[SentenceTransformers]]** as a text-embedding library (citing Reimers & Gurevych 2019 Sentence-BERT), complementing the [[Embedding]] page's existing coverage of `sentence-transformers/all-MiniLM-L6-v2` from the LLM Engineer's Handbook.
- **First wiki worked example of word2vec for non-NLP recommendations** — the [[Word2VecRecommender]] pattern of treating songs as words and playlists as sentences. This grounds the long-standing [[Word2Vec]] / [[SkipGram]] / [[NegativeSampling]] line in a tangible non-language application.

The chapter complements rather than contradicts the existing wiki. Where [[d2l-nlp-pretraining|D2L NLP Pretraining]] is the **formal-math** treatment of word2vec / BPE / WordPiece / subword embedding, and [[ai-engineering-ch01-intro|Huyen Ch 1]] is the **practitioner-framing** of why tokenize-at-all, *Hands-On LLMs* Ch 2 is the **comparative empirical tour** — what each modern tokenizer actually does to a fixed test string.

Subsequent chapters (Ch 3: Looking Inside LLMs, Ch 4–11: applications, Ch 10: training custom embedding models, Ch 11: fine-tuning representation models) build on the token-and-embedding foundation this chapter lays down.
