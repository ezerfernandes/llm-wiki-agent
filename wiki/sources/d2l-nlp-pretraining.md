---
title: "Dive into Deep Learning — Natural Language Processing: Pretraining"
type: source
tags: [textbook, d2l, nlp, word-embeddings, word2vec, glove, bert, pretraining, bpe]
date: 2026-05-16
source_file: raw/d2l-en/chapter_natural-language-processing-pretraining/
---

## Summary

[[AstonZhang|Zhang]], [[ZacharyLipton|Lipton]], [[MuLi|Li]] & [[AlexanderSmola|Smola]]'s ten-section *NLP Pretraining* chapter — D2L's pivot from architectures to **upstream text-representation pretraining**, the foundation that the entire Part 3 [[NLP|NLP-applications]] chapter consumes downstream. It builds two complementary stacks: (1) **static / context-independent word embeddings** — [[Word2Vec|word2vec]] ([[SkipGram|skip-gram]] + [[CBOW]]), trained efficiently with [[NegativeSampling|negative sampling]] or [[HierarchicalSoftmax|hierarchical softmax]]; [[GloVe]] as squared-loss co-occurrence factorization; and [[FastText|fastText]]'s character-$n$-gram [[SubwordEmbedding|subword embedding]] for morphology + OOV — and (2) [[BERT]] as the canonical **context-sensitive** Transformer-encoder pretraining recipe ([[MaskedLanguageModel|MLM]] + [[NextSentencePrediction|NSP]]) with [[WordPiece]] subwords on [[BookCorpus]] + [[EnglishWikipedia]]. The chapter operationalizes everything on a [[PTB|Penn Tree Bank]] toy corpus end-to-end (subsampling, center/context extraction, minibatching, similarity / analogy evaluation) and then re-builds the same pipeline at BERT scale. Closes by demonstrating semantic structure in pretrained [[GloVe]] vectors via [[WordSimilarity|cosine-similarity]] $k$-NN and the [[AnalogyTask|vec(c)+vec(b)−vec(a)]] analogy completion task.

## Key Claims

- **One-hot vectors are a bad word representation** because their cosine similarity is identically 0 between any two distinct words — they cannot encode semantic similarity. This motivates dense embeddings.
- **Word embedding** is the technique of mapping words to fixed-length real vectors that better express similarity and analogy among words.
- **[[Word2Vec|word2vec]]** comprises two self-supervised shallow models: **[[SkipGram|skip-gram]]** (predict context words from a center word) and **[[CBOW|continuous bag of words]]** (predict the center word from averaged context-word vectors). Each word $w_i$ has two $d$-dim vectors $\mathbf{v}_i$ (as center) and $\mathbf{u}_i$ (as context); the conditional probability is a softmax over dot products $P(w_o\mid w_c)=\exp(\mathbf{u}_o^\top\mathbf{v}_c)/\sum_i\exp(\mathbf{u}_i^\top\mathbf{v}_c)$.
- **The softmax denominator is the bottleneck** — each gradient step sums over the entire vocabulary $|\mathcal{V}|$ (hundreds of thousands to millions of words), making exact training computationally infeasible.
- **[[NegativeSampling|Negative sampling]]** ([[NoiseContrastiveEstimation|NCE]] variant) rewrites the objective as a binary-classification game: maximize $\sigma(\mathbf{u}_o^\top\mathbf{v}_c)$ for positive (center, context) pairs and $\sigma(-\mathbf{u}_{h_k}^\top\mathbf{v}_c)$ for $K$ noise words sampled from a predefined distribution $P(w)$. Per-step cost drops from $\mathcal{O}(|\mathcal{V}|)$ to $\mathcal{O}(K)$.
- **[[HierarchicalSoftmax|Hierarchical softmax]]** replaces the flat softmax with a Huffman-style binary tree whose leaves are vocabulary words; each conditional probability factorizes along the root-to-leaf path as $\prod_j\sigma(\pm\mathbf{u}_{n(w_o,j)}^\top\mathbf{v}_c)$, reducing per-step cost to $\mathcal{O}(\log_2|\mathcal{V}|)$.
- **[[GloVe]]** ([[JeffreyPennington|Pennington]], [[RichardSocher|Socher]] & [[ChrisManning|Manning]] 2014) reinterprets skip-gram as cross-entropy against global co-occurrence statistics $x_{ij}$, but **swaps cross-entropy for a weighted squared loss** on $\log x_{ij}$: $\sum_{i,j}h(x_{ij})(\mathbf{u}_j^\top\mathbf{v}_i+b_i+c_j-\log x_{ij})^2$ with weight $h(x)=(x/c)^\alpha$ saturating at 1. Because $x_{ij}=x_{ji}$ is symmetric, GloVe's two vector matrices are mathematically equivalent and the final embedding sums them.
- **GloVe is justified by the ratio of co-occurrence probabilities** — $p_{ik}/p_{jk}$ is large when $w_k$ is related to $w_i$ but unrelated to $w_j$ (e.g. "solid" has $p(\cdot\mid\textrm{ice})/p(\cdot\mid\textrm{steam})\approx 8.9$); fitting this ratio via $f((\mathbf{u}_j-\mathbf{u}_k)^\top\mathbf{v}_i)$ recovers the GloVe loss.
- **[[FastText|fastText]]** ([[PiotrBojanowski|Bojanowski]], [[EdouardGrave|Grave]], [[ArmandJoulin|Joulin]] et al. 2017) represents each word as the sum of its character-$n$-gram vectors for $n\in[3,6]$ plus the whole-word token: $\mathbf{v}_w=\sum_{g\in\mathcal{G}_w}\mathbf{z}_g$. Shared subword parameters give better representations for rare and **out-of-vocabulary** words; everything else (skip-gram / CBOW) is unchanged.
- **[[BPE|Byte Pair Encoding]]** ([[RicoSennrich|Sennrich]], Haddow & Birch 2015) extracts variable-length subwords in a *fixed-size* vocabulary by iteratively merging the most frequent pair of consecutive symbols (greedy, frequency-based). BPE and variants underpin [[GPT2|GPT-2]] and [[RoBERTa]] tokenization.
- **[[AnalogyTask|Word analogies]]** — for $a:b::c:d$, find $d=\arg\max_w\cos(\textrm{vec}(w),\textrm{vec}(c)+\textrm{vec}(b)-\textrm{vec}(a))$ — recover both **semantic** structure (man:woman::son:daughter; beijing:china::tokyo:japan) and **syntactic** structure (bad:worst::big:biggest; do:did::go:went) directly from pretrained 50-dim GloVe vectors.
- **Static embeddings are context-independent** — [[Word2Vec|word2vec]] and [[GloVe]] assign the same vector to "bank" whether the sentence is *"deposit cash at the bank"* or *"sit down on the bank"*, fundamentally limiting them on polysemy. This motivates contextual representations ([[TagLM]] / [[CoVe]] / [[ELMo]] / [[GPT]] / [[BERT]]).
- **[[BERT]]** ([[JacobDevlin|Devlin]] et al. 2018) combines the best of [[ELMo]] (bidirectional context) and [[GPT]] (task-agnostic architecture): a [[Transformer|Transformer encoder]] pretrained on a large unlabeled corpus, then fine-tuned end-to-end with a tiny task-specific output head for a wide range of NLP tasks.
- **[[BERT]] input representation** sums three learned embeddings per position — **token** ([[WordPiece]] 30K vocab), **segment** ($\mathbf{e}_A$ / $\mathbf{e}_B$ for two-sequence inputs), and **learnable positional**. Each BERT input sequence is `[CLS] <text A> [SEP] (<text B> [SEP])`; the `[CLS]` final hidden state is the aggregate sequence vector used for sequence-level classification (e.g. NSP, sentiment).
- **[[MaskedLanguageModel|Masked Language Modeling]]** selects 15% of tokens for prediction. To mitigate the **pretrain / fine-tune mismatch** (the `[MASK]` token never appears at fine-tune time), each chosen position is replaced by `[MASK]` 80% of the time, by a random token 10%, and left **unchanged** 10%. Only the chosen positions contribute to the cross-entropy loss.
- **[[NextSentencePrediction|Next Sentence Prediction]]** is a binary classification head on the `[CLS]` embedding: 50% of training pairs are genuine consecutive sentences (`IsNext`), 50% are random (`NotNext`). Provides explicit inter-sentence signal for NLI / QA / paraphrase. The BERT loss is the linear sum of MLM and NSP losses; both labels are *free* — derivable from the corpus with no manual annotation.
- **Original BERT pretraining corpus**: concatenation of [[BookCorpus]] (800M words) + [[EnglishWikipedia]] (2.5B words) — **3.3B-word self-supervised corpus** with no labeling cost.

## Key Quotes

> "Since the cosine similarity between one-hot vectors of any two different words is 0, one-hot vectors cannot encode similarities among words." — the foundational motivation for distributed word representations (§word2vec).

> "Now the computational cost for gradients at each training step has nothing to do with the dictionary size, but linearly depends on $K$." — D2L on why negative sampling makes word2vec tractable (§approx-training).

> "Unlike word2vec that fits the asymmetric conditional probability $p_{ij}$, GloVe fits the symmetric $\log x_{ij}$. Therefore, the center word vector and the context word vector of any word are mathematically equivalent in the GloVe model." — the structural distinction GloVe vs. skip-gram (§glove).

> "Thanks to shared parameters from subwords among words with similar structures, rare words and even out-of-vocabulary words may obtain better vector representations in fastText." — the OOV motivation for subword embeddings (§subword-embedding).

> "ELMo encodes context bidirectionally but uses task-specific architectures; while GPT is task-agnostic but encodes context left-to-right. Combining the best of both worlds, BERT (Bidirectional Encoder Representations from Transformers) encodes context bidirectionally and requires minimal architecture changes for a wide range of natural language processing tasks." — D2L's one-paragraph summary of the 2018 pretraining-architecture trilemma (§bert).

> "It is noteworthy that all the labels in both the aforementioned pretraining tasks can be trivially obtained from the pretraining corpus without manual labeling effort. The original BERT has been pretrained on the concatenation of BookCorpus and English Wikipedia. These two text corpora are huge: they have 800 million words and 2.5 billion words, respectively." — D2L on the **self-supervised scaling** that makes BERT possible (§bert).

## Connections

### Entities
- [[AstonZhang]], [[ZacharyLipton]], [[MuLi]], [[AlexanderSmola]] — chapter authors (D2L team).
- [[TomasMikolov]] — first author of the [[Word2Vec|word2vec]] skip-gram and CBOW papers (2013) cited throughout §word2vec / §approx-training.
- [[JeffreyPennington]], [[RichardSocher]], [[ChrisManning]] — [[StanfordUniversity|Stanford NLP]] authors of [[GloVe]] (2014).
- [[PiotrBojanowski]], [[EdouardGrave]], [[ArmandJoulin]] — [[fair|Facebook AI Research]] authors of [[FastText]] (2017).
- [[RicoSennrich]] — first author of [[BPE]] for neural machine translation (2015).
- [[JacobDevlin]] — first author of [[BERT]] (2018; cited via [[1810.04805-bert]]).

### Concepts
- [[WordEmbedding]] — the umbrella concept this whole chapter operationalizes.
- [[Word2Vec]], [[SkipGram]], [[CBOW]] — D2L's first family of embedding models.
- [[NegativeSampling]], [[NoiseContrastiveEstimation]], [[HierarchicalSoftmax]] — approximate-training tricks that make softmax over a million-word vocabulary tractable.
- [[GloVe]] — squared-loss co-occurrence factorization.
- [[FastText]], [[SubwordEmbedding]], [[BPE]], [[WordPiece]] — the subword-tokenization lineage.
- [[AnalogyTask]], [[WordSimilarity]] — downstream intrinsic-evaluation tasks for static embeddings.
- [[BERT]], [[MaskedLanguageModel]], [[NextSentencePrediction]], [[ClassificationToken]] — context-sensitive Transformer-encoder pretraining.
- [[ContextualEmbedding]], [[ELMo]], [[GPT]] — the 2018 pretraining-architecture lineage BERT sits inside.
- [[Transformer]], [[TransformerEncoder]], [[SelfSupervisedLearning]] — architectural and paradigmatic prerequisites built up in [[d2l-attention-and-transformers]].

### Cross-corpus
- [[1810.04805-bert]] — Devlin et al.'s original BERT paper; this D2L chapter is its **textbook companion** and ports the recipe to an executable PyTorch / MXNet pipeline.
- [[1706.03762-attention-is-all-you-need]] — the Transformer encoder BERT reuses.
- [[d2l-attention-and-transformers]] — the chapter that builds the Transformer encoder D2L's `BERTEncoder` subclasses.
- [[d2l-recurrent-neural-networks]] / [[d2l-recurrent-modern]] — the immediately preceding sequence-modeling layer.
- [[d2l-preliminaries]], [[d2l-linear-regression]] — the gradient + SGD + softmax / cross-entropy machinery underneath every model in this chapter.

## Contradictions

- None with the existing wiki. Reinforces [[1810.04805-bert]] (same MLM + NSP recipe) and complements [[bert]]'s concept page with a from-scratch PyTorch / MXNet implementation path. Adds finer mechanical detail on [[NegativeSampling]] / [[HierarchicalSoftmax]] / [[BPE]] than any existing wiki page; flags the static-vs-contextual ("bank" example) limitation that [[BERT]] resolves — consistent with [[bert]] and [[1810.04805-bert]]'s framing.
