# Stanford CS324 (Winter 2022) — Modeling
Source: https://stanford-cs324.github.io/winter2022/lectures/modeling/
Fetched for wiki ingest.

---

## Overview

This lecture examines how large language models are constructed, moving from treating language models as black boxes to understanding their internal mechanisms. It focuses on two core topics: **tokenization** and **model architecture**.

---

## Tokenization

### Definition and Purpose

A **tokenizer** converts raw text strings into sequences of tokens drawn from a vocabulary $\mathcal{V}$:

$$\text{the mouse ate the cheese} \Rightarrow [\text{the}, \text{mouse}, \text{ate}, \text{the}, \text{cheese}]$$

Language models operate on token sequences, not raw characters.

### Challenges with Simple Splitting

Splitting by spaces is inadequate because:

- Languages like Chinese lack spaces between words.
- German has long compound words (e.g., *Abwasserbehandlungsanlange*).
- English has hyphenated words (*father-in-law*) and contractions (*don't*).
- The Penn Treebank splits *don't* into *do* and *n't*.

### Design Principles for Good Tokenization

An effective tokenizer balances three concerns:

1. **Sequence length** — Too many tokens (the extreme being characters/bytes) makes sequences hard to model.
2. **Parameter sharing** — Too few tokens prevents sharing between related words; critical for morphologically rich languages (Arabic, Turkish).
3. **Meaningfulness** — Each token should represent a linguistically or statistically meaningful unit.

### Byte Pair Encoding (BPE)

[Sennrich et al. 2015] adapted the byte pair encoding algorithm from data compression for NLP tokenization.

**Learning phase**:

- Initialize the vocabulary $\mathcal{V}$ with all characters.
- Iteratively:
  - Find the most frequently co-occurring pair $(x, x') \in \mathcal{V}$.
  - Replace all occurrences with a new symbol $xx'$.
  - Add $xx'$ to $\mathcal{V}$.

**Example progression** (each merge applied to the three strings "the car", "the cat", "the rat"):

```
[t, h, e, ␣, c, a, r], [t, h, e, ␣, c, a, t], [t, h, e, ␣, r, a, t]
→ [th, e, ␣, c, a, r], [th, e, ␣, c, a, t], [th, e, ␣, r, a, t]   (th occurs 3×)
→ [the, ␣, c, a, r], [the, ␣, c, a, t], [the, ␣, r, a, t]          (the occurs 3×)
→ [the, ␣, ca, r], [the, ␣, ca, t], [the, ␣, r, a, t]              (ca occurs 2×)
```

**Output**: an updated vocabulary plus an ordered list of merge operations.

**Applying the tokenizer**: apply the learned merges sequentially to new strings.

**Unicode handling**:

- There are 144,697 Unicode characters, which creates sparsity issues.
- [Wang et al. 2019] applies BPE to bytes instead of characters for multilingual models.
- Example: Chinese *今天* [gloss: *today*] → `[x62, x11, 4e, ca]`.

**BPE adoption**: GPT-2 and GPT-3 use BPE with a 50K vocabulary size.

### Unigram Model (SentencePiece)

A more principled approach that defines an explicit objective function for tokenization quality.

Given a sequence $x_{1:L}$ and a tokenization $T$ (a set of span indices):

$$p(x_{1:L}) = \prod_{(i,j) \in T} p(x_{i:j})$$

**Example**:

- String: *ababc*
- Tokenization $T = \{(1,2), (3,4), (5,5)\}$ with vocabulary $\{\text{ab}, \text{c}\}$
- Likelihood: $p(x_{1:L}) = \frac{2}{3} \cdot \frac{2}{3} \cdot \frac{1}{3} = \frac{4}{9}$

**Algorithm**:

1. Start with a reasonably large seed vocabulary $\mathcal{V}$.
2. Repeat:
   - Optimize $p(x)$ and $T$ using the EM algorithm.
   - Compute $\text{loss}(x)$ for each token (the reduction in likelihood if it were removed).
   - Retain the top 80% of tokens by loss.

**Adoption**: used by the SentencePiece tool ([Kudo & Richardson 2018]), T5, and Gopher.

### Tokenizer Comparison

**GPT-3 vs. Jurassic**:

- GPT-3: BPE, 50K vocabulary.
- Jurassic: SentencePiece, 256K vocabulary.

**Impact**:

- Jurassic requires 28% fewer tokens than GPT-3 (1.4× faster).
- With the same 2048-token context length, Jurassic prompts can fit 39% more text.

**Example tokenizations** for "Abraham Lincoln lived at the White House.":

- GPT-3: `[Ab, raham, ␣Lincoln, ␣lived, ␣at, ␣the, ␣White, ␣House, .]`
- Jurassic: `[Abraham␣Lincoln, ␣lived, ␣at␣the␣White␣House, .]`

---

## Model Architecture

### Contextual Embeddings

The key development beyond treating language models as black boxes is mapping token sequences to **contextual embeddings**:

$$[\text{the}, \text{mouse}, \text{ate}, \text{the}, \text{cheese}] \xrightarrow{\phi} \left[\binom{1}{0.1}, \binom{0}{1}, \binom{1}{1}, \binom{1}{-0.1}, \binom{0}{-1}\right]$$

- Contextual embeddings depend on the surrounding context (unlike static word embeddings).
- Notation: $\phi: \mathcal{V}^L \to \mathbb{R}^{d \times L}$ (the embedding function).

### Three Types of Language Models

#### Encoder-Only (BERT, RoBERTa)

$$x_{1:L} \Rightarrow \phi(x_{1:L})$$

Produces contextual embeddings for classification tasks.

**Examples**:

- Sentiment: `[CLS] the movie was great` → positive
- Natural language inference: `[CLS] all animals breathe [SEP] cats breathe` → entailment

**Pros**: embeddings depend **bidirectionally** on both left and right context.

**Cons**:

- Cannot naturally **generate** completions.
- Requires non-standard training objectives (masked language modeling).

#### Decoder-Only (GPT-2, GPT-3)

$$x_{1:i} \Rightarrow \phi(x_{1:i}),\ p(x_{i+1} \mid x_{1:i})$$

Standard autoregressive language models for generation.

**Example** (text autocomplete): `the movie was` → `great`

**Pros**:

- Can naturally **generate** completions.
- Simple training objective (maximum likelihood).

**Cons**: embeddings depend only **unidirectionally** on left context.

#### Encoder-Decoder (BART, T5)

$$x_{1:L} \Rightarrow \phi(x_{1:L}),\ p(y_{1:L} \mid \phi(x_{1:L}))$$

Bidirectional input encoding combined with autoregressive output generation.

**Example** (table-to-text): `[name: Clowns | eatType: coffee shop]` → `Clowns is a coffee shop`

**Pros**: bidirectional input processing plus natural generation capability.

**Cons**: requires specialized training objectives.

---

## Building Blocks for Model Architecture

### EmbedToken

Converts token sequences to vectors via an embedding matrix $E \in \mathbb{R}^{|\mathcal{V}| \times d}$:

```
def EmbedToken(x: V^L) → R^(d×L):
    Return [E_{x_1}, ..., E_{x_L}]
```

These are context-independent word embeddings.

### SequenceModel (Abstract)

```
def SequenceModel(x: R^(d×L)) → R^(d×L):
    Process each element x_i with respect to the others
    [abstract implementation]
```

Maps context-independent embeddings to contextual embeddings.

### FeedForwardSequenceModel

A fixed-length context model (n-gram style):

```
def FeedForwardSequenceModel(x: R^(d×L)) → R^(d×L):
    For i = 1, ..., L:
        Compute h_i = FeedForward(x_{i-n+1}, ..., x_i)
    Return [h_1, ..., h_L]
```

---

## Recurrent Neural Networks (RNNs)

### Basic RNN Architecture

```
def SequenceRNN(x: R^(d×L)) → R^(d×L):
    For i = 1, ..., L:
        Compute h_i = RNN(h_{i-1}, x_i)
    Return [h_1, ..., h_L]
```

Processes sequences left-to-right, maintaining a hidden state $h$.

### RNN Implementations

**SimpleRNN** [Elman 1990]:

```
def SimpleRNN(h: R^d, x: R^d) → R^d:
    Return σ(Uh + Vx + b)
```

where $\sigma$ is a nonlinearity (logistic or ReLU).

**Issues**:

- Difficult to train due to vanishing gradients.
- Long-range dependencies are unlikely to be captured crisply.

**Improvements**: LSTM and GRU variants address the vanishing-gradient problem.

### Bidirectional RNNs

```
def BidirectionalSequenceRNN(x: R^(d×L)) → R^(2d×L):
    Compute left-to-right:  [h_1^→, ..., h_L^→] ← SequenceRNN(x_1, ..., x_L)
    Compute right-to-left:  [h_L^←, ..., h_1^←] ← SequenceRNN(x_L, ..., x_1)
    Return [h_1^→ h_1^←, ..., h_L^→ h_L^←]
```

Used by ELMo and ULMFiT for bidirectional context.

---

## Transformers

The breakthrough architecture enabling large language models ([Vaswani et al. 2017], "Attention is All You Need").

### Attention Mechanism

Attention is a "soft" lookup table comparing a query $y$ against key-value pairs derived from a sequence $x_{1:L}$:

$$[\text{score}_1, ..., \text{score}_L] = \mathbf{x}^\top W_\text{key}^\top W_\text{query}\, y$$

$$[\alpha_1, ..., \alpha_L] = \text{softmax}\left(\frac{[\text{score}_1, ..., \text{score}_L]}{\sqrt{d}}\right)$$

Output is a weighted sum over values:

$$\sum_{i=1}^L \alpha_i (W_\text{value}\, x_i)$$

**Pseudocode**:

```
def Attention(x: R^(d×L), y: R^d) → R^d:
    Return W_value · x · softmax(x^T W_key^T W_query y / √d)
```

### Multi-Headed Attention

Multiple attention heads capture different aspects (syntax, semantics, etc.):

```
def MultiHeadedAttention(x: R^(d×L), y: R^d) → R^d:
    Return W_output [Attention(x, y), ..., Attention(x, y)]
                     (n_heads times)
```

### Self-Attention Layer

Substitute each $x_i$ as the query:

```
def SelfAttention(x: R^(d×L)) → R^(d×L):
    Return [Attention(x, x_1), ..., Attention(x, x_L)]
```

This allows all tokens to attend to all other tokens.

### Feedforward Layer

Token-wise processing (independent of other tokens):

```
def FeedForward(x: R^(d×L)) → R^(d×L):
    For i = 1, ..., L:
        Compute y_i = W_2 max(W_1 x_i + b_1, 0) + b_2
    Return [y_1, ..., y_L]
```

### Training Stability Techniques

#### Residual Connections

Skip connections that allow gradients to flow through identities when the function's own gradients vanish:

$$x + f(x)$$

Inspired by ResNets in computer vision.

#### Layer Normalization

```
def LayerNorm(x: R^(d×L)) → R^(d×L):
    Normalize each x_i to prevent magnitude explosion
```

#### AddNorm Adapter

```
def AddNorm(f: (R^(d×L) → R^(d×L)), x: R^(d×L)) → R^(d×L):
    Return LayerNorm(x + f(x))
```

### Transformer Block

Combines self-attention and feedforward with the stability techniques:

```
def TransformerBlock(x: R^(d×L)) → R^(d×L):
    Return AddNorm(FeedForward, AddNorm(SelfAttention, x))
```

### Positional Embeddings

Problem: token embeddings don't encode position, so identical words at different positions get identical embeddings.

**Solution**: add positional information via sinusoidal embeddings:

```
def EmbedTokenWithPosition(x: R^(d×L)):
    Even dimensions: P_{i,2j}   = sin(i / 10000^(2j/d_model))
    Odd dimensions:  P_{i,2j+1} = cos(i / 10000^(2j/d_model))
    Return [x_1 + P_1, ..., x_L + P_L]
```

---

## GPT-3 Architecture

With all components in place, GPT-3 stacks Transformer blocks:

$$\text{GPT-3}(x_{1:L}) = \text{TransformerBlock}^{96}(\text{EmbedTokenWithPosition}(x_{1:L}))$$

### Architectural Specifications

| Parameter | Value |
|-----------|-------|
| Hidden state dimension | $d_\text{model} = 12{,}288$ |
| Feedforward intermediate dimension | $d_\text{ff} = 4 \, d_\text{model}$ |
| Number of attention heads | $n_\text{heads} = 96$ |
| Context length | $L = 2{,}048$ |
| Total parameters | 175 billion |
| Depth | 96 layers |

**Design critique**: [Levine et al. 2020] argue that GPT-3 is too deep, which motivated the development of the deeper-but-wider Jurassic architecture. ("These decisions are not necessarily optimal. Levine et al. 2020 provide some theoretical justification, showing that the GPT-3 is too deep, which motivated the training of a deeper but wider Jurassic architecture.")

### Important Architectural Variants

- **Layer normalization position** — post-norm (the original Transformers paper) vs. pre-norm (GPT-2), affecting training stability ([Davis et al. 2021]).
- **Dropout** — applied throughout to prevent overfitting.
- **Sparse Transformers** — "GPT-3 uses a sparse Transformer to reduce the number of parameters, interleaving it with dense layers."
- **Masking** — different patterns are used for encoder-only, decoder-only, and encoder-decoder models.

> Note: This lecture does **not** cover mixture-of-experts (MoE) or retrieval-augmented models (e.g., RETRO, kNN-LM). It focuses on foundational Transformer architecture; sparse Transformers are mentioned only in passing.

---

## Further Reading

### Tokenization
- Mielke et al. 2021: "Between words and characters: A Brief History of Open-Vocabulary Modeling and Tokenization in NLP" — comprehensive survey.
- Sennrich et al. 2015 (ACL): "Neural Machine Translation of Rare Words with Subword Units" — introduces BPE to NLP.
- Wu et al. 2016: "Google's Neural Machine Translation System" — introduces WordPiece (used by BERT).
- Kudo & Richardson 2018 (EMNLP): "SentencePiece: A simple and language independent subword tokenizer and detokenizer."

### Core Transformer Literature
- Vaswani et al. 2017 (NIPS): "Attention is All You Need" — original Transformers paper.
- Bahdanau et al. 2017: early attention mechanism for machine translation.
- The Illustrated Transformer (https://jalammar.github.io/illustrated-transformer/) and The Illustrated GPT-2 (https://jalammar.github.io/illustrated-gpt2/) — visual explanations.

### Decoder-Only Models
- Radford et al. 2019: "Language Models are Unsupervised Multitask Learners" — GPT-2.
- Brown et al. 2020 (NeurIPS): "Language Models are Few-Shot Learners" — GPT-3.
- Rae et al. 2021: "Scaling Language Models: Methods, Analysis & Insights from Training Gopher" — Gopher (DeepMind).
- Lieber et al. 2021: "Jurassic-1: Technical details and evaluation" — AI21 Labs.

### Encoder-Only Models
- Devlin et al. 2019 (NAACL): "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding."
- Liu et al. 2019: "RoBERTa: A Robustly Optimized BERT Pretraining Approach" — Facebook.

### Encoder-Decoder Models
- Lewis et al. 2019 (ACL): "BART: Denoising Sequence-to-Sequence Pre-training" — Facebook.
- Raffel et al. 2019: "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer" — T5.

### Efficient Variants
- Press et al. 2021: "Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation" — ALiBi embeddings.
- Dai et al. 2019 (ACL): "Transformer-XL" — recurrence and relative position encoding.
- Child et al. 2019: "Generating Long Sequences with Sparse Transformers."
- Wang et al. 2020: "Linformer: Self-Attention with Linear Complexity."
- Choromanski et al. 2020 (ICLR): "Rethinking Attention with Performers."
- Tay et al. 2020: "Efficient Transformers: A Survey."
