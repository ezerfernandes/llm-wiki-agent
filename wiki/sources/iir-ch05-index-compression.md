---
title: "IIR Ch. 5: Index Compression"
type: source
tags: [iir, information-retrieval, textbook, compression, heaps-law, zipfs-law, gamma-codes]
date: 2026-05-23
source_file: "https://nlp.stanford.edu/IR-book/html/htmledition/index-compression-1.html"
---

## Summary

Chapter 5 of Manning, Raghavan and Schütze's *Introduction to Information Retrieval* (2008) develops the theory and engineering practice of compressing the two main data structures of an IR system: the **dictionary** (the lexicon mapping terms to postings) and the **postings file** (the per-term lists of document identifiers). The chapter is anchored by two empirical regularities — **Heaps' law**, which predicts how vocabulary grows with collection size, and **Zipf's law**, which predicts how skewed term frequencies are — and uses these to motivate a sequence of progressively more aggressive compression schemes. For the dictionary, the chapter walks from a naive fixed-width array, through a contiguous "dictionary-as-a-string" layout, to **blocked storage** with **front coding**. For postings, it introduces **gap encoding** between sorted docIDs and then two universal variable-length codes for those gaps: **variable byte (VB) codes** (bytewise) and **gamma codes** (bitwise), demonstrating that a Reuters-RCV1 postings file shrinks from ~400 MB uncompressed to 116 MB with VB and 101 MB with gamma. The recurring theme is that decompression speed matters more than compression speed: caching gains and faster I/O usually swamp the CPU cost of unpacking codes, so even relatively simple schemes give 1:4 ratios "essentially for free."

## Key Claims

- **Compression ratios of 1:4 are routinely achievable** on inverted indexes, cutting storage cost by ~75% with negligible impact on query performance.
- The primary benefit of compression is not raw disk savings but **better caching and faster disk-to-memory transfer**; with fast decoders, reading compressed bytes plus decoding can be faster than reading uncompressed bytes.
- Lossy preprocessing (case-folding ≈ −17% of distinct terms, stemming ≈ similar, stop-word removal ≈ −25–30% of nonpositional postings) and lossless encoding both contribute, but they compress different parts of the index.
- **Heaps' law**: M = k·T^b with 30 ≤ k ≤ 100 and b ≈ 0.5. Vocabulary keeps growing with collection size — there is no asymptotic ceiling — so the dictionary becomes the long-term scaling problem.
- **Zipf's law**: cf_i ∝ 1/i. A handful of terms dominate occurrences; the long tail is enormous. This heavy-tailed distribution is exactly what gap-encoded postings need: frequent-term lists have tiny gaps (often 1), so variable-length codes save dramatically.
- For Reuters-RCV1 (~800k docs, ~100M tokens, ~400k terms), a fixed-width dictionary of 19.2 MB compresses to 7.6 MB (string), 7.1 MB (blocked, k=4), and 5.9 MB (blocked + front-coded).
- Postings: ~400 MB uncompressed → **116 MB with VB** → **101 MB with gamma** on RCV1.
- **Gamma codes are universal**: within a factor of ≤ 2 + 1/H(P) ≤ 3 of the entropy bound for *any* gap distribution P, with no parameters to tune.
- **Variable byte codes** sacrifice some compression for byte-aligned, ~2× faster decoding — usually the right engineering choice in practice (Scholer et al., 2002).

## Section Notes

### 5.1 Statistical properties of terms in IR

The vocabulary of a large corpus is not bounded by a human dictionary. The OED has ~600k entries, but text collections accumulate proper nouns, identifiers, misspellings, and domain jargon without limit. Preprocessing choices materially change both M (vocabulary size) and the size of the postings file:

| Preprocessing | Effect on distinct terms | Effect on nonpositional postings |
|---|---|---|
| Case-folding | ~−17% | small |
| Stemming | ~−17% (similar) | modest |
| Stop-word removal (top 150) | tiny | −25% to −30% |

The "rule of 30" observation: the 30 most frequent words account for ~30% of all tokens in typical written English — the same heavy-tailed phenomenon Zipf's law formalizes.

The chapter distinguishes **lossless** compression (codes, blocked storage) from **lossy** preprocessing (case-folding, stemming, stop-word removal); both reduce index size but only the former is reversible.

### 5.1.1 Heaps' law — vocabulary growth

The model **M = k · T^b** linearizes in log–log space:

> log₁₀ M = b · log₁₀ T + log₁₀ k

For RCV1 the best fit is log₁₀ M ≈ 0.49 · log₁₀ T + 1.64, giving k ≈ 44, b ≈ 0.49. Plugging T = 1,000,020 in gives M ≈ 38,323; the actual vocabulary was 38,365 — strikingly accurate. The constants depend on preprocessing: numbers, capitalization, and spelling errors all push k upward. The two practical takeaways are:

1. **Vocabulary keeps growing**; there is no fixed dictionary you can pre-allocate.
2. **Dictionaries become large** for web-scale corpora, so dictionary compression is essential, not optional.

### 5.1.2 Zipf's law — term frequency distribution

If terms are ranked by collection frequency cf, then **cf_i ∝ 1/i**, or equivalently cf_i = c · i^k with k = −1. In log–log space: log cf_i = log c − log i. The second-most-common term occurs roughly half as often as the first, the third roughly one-third as often, etc. This is a power law with exponent −1 (see [[powerlaw]]). The empirical fit on RCV1 is "not particularly good, but good enough" — the law captures the *shape* (heavy tail, fast decay from the head) even when it misses the exact slope.

Why this matters for compression: the rank-frequency skew means that *most postings entries come from a small number of high-frequency terms whose lists are very dense*. Gap-encoding those dense lists yields gaps near 1, which variable-length codes encode in 1–2 bits/bytes — that is where most of the saving comes from.

### 5.2 Dictionary compression

The dictionary must support fast term lookup during query processing. The primary goal is to keep it (or most of it) **in main memory** so each query doesn't require a disk seek to find postings pointers. Constraints come from: multi-language enterprise indexes with huge vocabularies, mobile/embedded devices with tight RAM, and shared environments where the IR system co-exists with other memory-hungry processes ("the search system on your PC must get along with the memory-hogging word processing suite you are using at the same time").

#### 5.2.1 Dictionary as a string

A naive **fixed-width** dictionary allocates, per entry: 20 bytes for the term (Unicode), 4 bytes for document frequency, 4 bytes for the postings list pointer. For RCV1 (400k terms): 400,000 × 28 ≈ 11.2 MB just for the array; counting Unicode width assumptions can take it up toward 19.2 MB. The problem is twofold: average English term length is ~8 characters, so ~12 bytes per row are wasted padding; and terms longer than 20 characters cannot fit at all.

The **dictionary-as-a-string** layout concatenates all terms into one big character buffer and stores per-term records of:

- 4 bytes: document frequency
- 4 bytes: postings pointer
- 3 bytes: term pointer (≈22 bits suffices to address the ~3.2M-byte string)
- 8 bytes (avg): term characters in the shared string

Total ≈ 19 bytes/term → ~7.6 MB on RCV1. Binary search still works because record size is fixed; only the *string buffer* is variable-length.

#### 5.2.2 Blocked storage

Group terms into blocks of size k and store the term pointer **only at the start of each block**. Inside a block, each term is prefixed by 1 byte for its length. With k = 4, we drop 3 term pointers (9 bytes) and add 4 length bytes — a net saving of 5 bytes per block of 4 terms. On RCV1 this brings the dictionary to ~7.1 MB.

The tradeoff is lookup cost: binary search localizes a block (log₂(M/k) steps), then linear search within the block (k/2 steps on average). For k = 4 the expected lookup increases by roughly 25% versus pure binary search — usually acceptable.

#### Front coding

In a sorted dictionary, adjacent terms share long prefixes:

```
automata, automate, automatic, automation
        → 8automat*a1◇e2◇ic3◇ion
```

The common prefix `automat` is stored once with a marker; suffixes follow with their lengths. Front coding adds an inner-block decode step but cuts another ~2.4 MB on RCV1. Final dictionary footprint on RCV1: **5.9 MB**, down from a fixed-width ~19.2 MB — about a 3.25× compression for the lexicon alone.

### 5.3 Postings file compression

Uncompressed postings on RCV1: 800,000 documents × 100,000,000 postings × log₂(800,000) ≈ 20 bits per docID → ~250 MB lower bound, ~400 MB if stored as 32-bit words. The chapter develops two encodings, both of which operate on **gaps** between sorted docIDs rather than the docIDs themselves.

#### Gap encoding

A postings list `[283154, 283159, 283202, ...]` is rewritten as `[283154, 5, 43, ...]`. This is lossless because the list is sorted: the decoder reconstructs absolute docIDs by running sums. Crucially:

- **Frequent terms** (`the`, `for`) have postings densely packed — gaps cluster around 1.
- **Rare terms** (`arachnocentric`) have gaps that are essentially as big as the docIDs themselves (~20 bits).

A good code must therefore use *very few* bits for small gaps and gracefully scale up for large ones — a variable-length code.

#### 5.3.1 Variable byte (VB) codes

Each gap is split into 7-bit groups, written most-significant-group first. Each group occupies one byte; the top bit is a **continuation bit**: **1 = last byte, 0 = more bytes follow**.

```text
VBENCODE-NUMBER(n):
  bytes = []
  while True:
    prepend (n mod 128) to bytes
    if n < 128: break
    n = n div 128
  set top bit of bytes[-1] to 1
  return bytes

VBDECODE(stream):
  n = 0
  while True:
    b = read_byte(stream)
    if (b & 128) == 0:
      n = 128*n + b
    else:
      n = 128*n + (b & 127)
      return n
```

Worked example from the book:

- docIDs `824, 829, 215406` → gaps `824, 5, 214577`
- gap 5 (7 bits): `1 0000101` → one byte
- gap 214577 spans 4 bytes: `0 0000110 0 1000101 0 0001101 1 0110001` (continuation bit cleared on first three, set on last)

On RCV1, VB shrinks the postings from ~400 MB to **116 MB** (~50%+ reduction). VB is byte-aligned, branch-light, and decodes near memory speed — that is why Scholer et al. (2002) found VB "two times faster" than bitwise alternatives at query time.

#### 5.3.2 Gamma (γ) codes

Gamma codes operate at the bit level. A positive integer G is encoded as:

1. Write G in binary: e.g. 13 → `1101`.
2. **Offset** = binary representation of G with the leading 1 stripped: `101` (length 3 bits).
3. **Length** = unary code for the offset's length: 3 → `1110` (three 1s then a terminating 0). See [[UnaryCode]].
4. Concatenate: `1110 101` → `1110101` (7 bits for G=13).

Decoding: scan the unary prefix to the first 0 — that count is L = the number of offset bits; read L bits, prepend the implicit leading 1, convert to integer.

Examples:

| G | binary | offset | length (unary) | γ(G) | bits |
|---|---|---|---|---|---|
| 1 | 1 | (empty) | 0 | `0` | 1 |
| 2 | 10 | 0 | 10 | `10 0` | 3 |
| 9 | 1001 | 001 | 1110 | `1110 001` | 7 |
| 13 | 1101 | 101 | 1110 | `1110 101` | 7 |
| 24 | 11000 | 1000 | 11110 | `11110 1000` | 9 |

Code length is **2·⌊log₂ G⌋ + 1 bits**, always odd. Important properties:

- **Prefix-free**: no γ code is a prefix of another, so γ-encoded streams need no separators.
- **Universal**: expected length E(L_γ) satisfies E(L_γ)/H(P) ≤ 2 + 1/H(P) ≤ 3 for any distribution P over positive integers. The optimal entropy lower bound is log₂ G bits; γ is within a factor of ~2 of it without knowing P in advance.
- **Parameter-free**: nothing to tune, robust to changing index distributions.

Compression on RCV1:

| Representation | Size |
|---|---|
| Uncompressed (32-bit) | ~400 MB |
| Variable byte | 116 MB |
| Gamma | **101 MB** |

The gamma-coded index is about 25% of the uncompressed size and well under 5% of the raw text corpus (960 MB of text / 3,600 MB with markup) — supporting the chapter's "1:4 or better" promise.

The tradeoff: gamma decoding requires bit shifts and masks, crosses machine-word boundaries, and so executes more slowly than VB on real CPUs. Choice between VB and γ is therefore an engineering decision driven by whether the bottleneck is *disk* (favor γ) or *CPU during query processing* (favor VB).

### 5.4 References and further reading

- **Heaps (1978)** — original empirical law on vocabulary growth.
- **Zipf (1949)** — rank-frequency law; **Witten & Bell (1990)** evaluated fit quality.
- **Elias (1975)** — introduced γ and δ codes; proved both are universal, δ asymptotically optimal for G > ~15.
- **Scholer et al. (2002)** — VB codes process queries ~2× faster than bitwise alternatives.
- **Anh & Moffat (2005, 2006a)**, **Zukowski et al. (2006)** — word-aligned binary codes for faster decoding.
- **Witten, Moffat & Bell (1999)** — *Managing Gigabytes*, the canonical reference on index compression.
- **Moffat & Zobel (1992)** — Golomb codes outperform γ on large web collections when distribution is well-modeled.
- **Moffat & Stuiver (1996)**, **Silvestri et al. (2004)** — docID assignment strategies amplify gap-coding wins.
- **Carmel et al. (2001)**, **Blanco & Barreiro (2007)** — lossy postings compression / pruning.
- **Zobel & Moffat (2006)** — survey covering term frequencies and position compression.
- **de Moura et al. (2000)** — compressed text that supports direct search without full decompression.

## Algorithms & Formulas

### Heaps' law

```
M  =  k · T^b           with 30 ≤ k ≤ 100,  b ≈ 0.5
log₁₀ M  =  b · log₁₀ T + log₁₀ k
RCV1 fit:  log₁₀ M ≈ 0.49 · log₁₀ T + 1.64    (k ≈ 44, b ≈ 0.49)
```

### Zipf's law

```
cf_i  ∝  1/i                            (rank i, collection frequency cf_i)
cf_i  =  c · i^k        with k = −1
log cf_i  =  log c − log i
```

### Variable byte encoding

```
VBENCODE-NUMBER(n):
  bytes ← empty
  while True:
    bytes ← (n mod 128) ⧺ bytes
    if n < 128: break
    n ← n div 128
  bytes[-1] ← bytes[-1] OR 128       # set continuation bit on final byte
  return bytes

VBENCODE(numbers):
  return concat(VBENCODE-NUMBER(n) for n in numbers)

VBDECODE(byte_stream):
  numbers ← []
  n ← 0
  for b in byte_stream:
    if (b AND 128) == 0:
      n ← 128·n + b                 # continuation: keep accumulating
    else:
      n ← 128·n + (b AND 127)       # terminator: finish number
      append n to numbers; n ← 0
  return numbers
```

### Gamma codes (unary length + binary offset)

```
γ(G):
  bin   ← binary(G)                 # e.g. G = 13 → "1101"
  off   ← bin[1:]                   # strip leading 1 → "101"
  L     ← length(off)               # 3
  ulen  ← "1" repeated L, then "0"  # unary(L) = "1110"
  return ulen ⧺ off                 # "1110" + "101" = "1110101"

γ⁻¹(stream):
  L ← count of leading 1-bits in stream until first 0
  consume that prefix (L ones + the 0)
  off ← read next L bits
  return integer("1" ⧺ off)

Length:   |γ(G)|  =  2 · ⌊log₂ G⌋ + 1   bits
Universal bound:  E(L_γ) / H(P)  ≤  2 + 1/H(P)  ≤  3
```

### RCV1 compression scorecard

| Structure | Bytes |
|---|---|
| Dictionary, fixed-width | ~19.2 MB |
| Dictionary, as-string | ~7.6 MB |
| Dictionary, blocked (k=4) | ~7.1 MB |
| Dictionary, blocked + front-coded | **~5.9 MB** |
| Postings, uncompressed (32-bit) | ~400 MB |
| Postings, variable byte | 116 MB |
| Postings, gamma | **101 MB** |

## Key Quotes

> "Compression ratios of 1:4 are easy to achieve, potentially cutting the cost of storing the index by 75%." — §5

> "The main goal of compressing the dictionary is to fit it in main memory, or at least a large portion of it, to support high query throughput." — §5.2

> "The search system on your PC must get along with the memory-hogging word processing suite you are using at the same time." — §5.2

> "Typical values for the parameters k and b are: 30 ≤ k ≤ 100 and b ≈ 0.5." — §5.1.1 (Heaps' law)

> "If t₁ is the most common term in the collection, t₂ is the next most common, and so on, then the collection frequency cf_i of the ith most common term is proportional to 1/i." — §5.1.2 (Zipf's law)

> "The postings for frequent terms are close together." — §5.3, motivating gap encoding

> "No gamma code is the prefix of another, so they form a prefix-free code." — §5.3.2

## Connections

- [[InformationRetrieval]] — Chapter 5 sits in the index-engineering thread of the IIR textbook; compression is what makes large-scale retrieval feasible in RAM-bounded systems.
- [[InvertedIndex]] — the chapter compresses exactly this structure: dictionary + postings lists.
- [[HeapsLaw]] — empirical law for vocabulary growth, justifies dictionary compression because M never saturates.
- [[ZipfsLaw]] — rank-frequency power law, justifies gap encoding because frequent terms produce tiny gaps.
- [[powerlaw]] — Zipf is the canonical power-law example in NLP/IR; the heavy tail drives the asymmetric distribution that variable-length codes exploit.
- [[DictionaryCompression]] — overall family of techniques (string layout, blocking, front coding).
- [[FrontCoding]] — prefix-sharing inside dictionary blocks; uses alphabetical ordering to fold redundancy.
- [[PostingsCompression]] — gap encoding + variable-length codes on docID differences.
- [[VariableByteCode]] — byte-aligned, continuation-bit code; favored when decoding speed matters more than ratio.
- [[GammaCode]] — bitwise universal code, ~2× better compression than VB at the cost of bit-fiddling.
- [[UnaryCode]] — the length-prefix used inside gamma codes; n is encoded as n ones plus a 0.

## Contradictions

- None identified against existing wiki content. The chapter's "1:4 compression with negligible accuracy loss" is consistent with later IIR chapters and general IR literature. If a future ingest covers learned/neural index compression (e.g., quantized embeddings for dense retrieval), watch for tension with the lossless framing here — gamma/VB are lossless on docIDs, whereas modern ANN indexes routinely sacrifice precision for footprint.
