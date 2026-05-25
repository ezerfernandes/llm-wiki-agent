---
title: "IIR Ch. 2: The Term Vocabulary and Postings Lists"
type: source
tags: [iir, information-retrieval, textbook, tokenization, stemming, postings-list]
date: 2026-05-23
source_file: "https://nlp.stanford.edu/IR-book/html/htmledition/the-term-vocabulary-and-postings-lists-1.html"
---

## Summary
Chapter 2 of Manning, Raghavan and Schütze's *Introduction to Information Retrieval* (Cambridge University Press, 2008) details how raw document collections are transformed into the term vocabulary and postings lists that drive an inverted index. It walks through four construction steps — gathering documents, tokenization, linguistic preprocessing, and indexing — then examines the linguistic and engineering decisions at each stage: character-sequence decoding, document-unit selection, tokenization, stop-word removal, normalization/equivalence classing, stemming, and lemmatization. It then turns to postings-list optimizations: skip pointers for faster Boolean intersection (with the sqrt(P) placement heuristic), and three approaches to supporting phrase queries — biword indexes, positional indexes, and combination schemes. The chapter emphasizes that any preprocessing decision must be applied identically to both documents and queries, and that linguistic normalization gains vary dramatically by language (modest for English, large for morphologically rich languages such as Finnish, German, and Spanish).

## Key Claims
- Inverted-index construction has four major steps: (1) collect the documents, (2) tokenize the text, (3) do linguistic preprocessing to produce a set of normalized index terms, and (4) index the documents by recording which terms occur in which.
- A **token** is an instance of a character sequence treated as a useful semantic unit; a **type** is the equivalence class of all tokens with the same character sequence; a **term** is a normalized type entered into the IR dictionary. In *to sleep perchance to dream* there are 5 tokens, 4 types, and (after stop-word removal) 3 terms.
- Decoding raw bytes into a character sequence may require encoding detection (UTF-8, vendor encodings) via machine learning, heuristics, metadata, or user selection, plus binary-format extraction (e.g. Word, zip) and markup/entity decoding (e.g. `&amp;` -> `&`).
- Non-linear writing systems such as Arabic complicate display but not storage: characters are still stored in linear logical order; bidirectional rendering and ligature shaping happen at display time.
- The choice of **document unit** is a granularity tradeoff: large units (whole books) inflate recall but cause spurious matches like "Chinese toys" hitting a book that mentions China in chapter 1 and toys in chapter N; very small units (sentence/paragraph) raise precision but fragment relevant evidence across multiple "documents."
- Proximity-based ranking and multi-level XML retrieval are partial mitigations for the granularity tradeoff; the right unit depends on collection, users, and queries.
- Tokenization must handle apostrophes (*O'Neill*, *aren't*), hyphens (vowel-separation *co-education*, compound names *Hewlett-Packard*, copyediting *hold-him-back-and-drag-him-away*), and multi-word units (*San Francisco*, *au fait*, phone numbers, dates) that may straddle whitespace.
- Language-specific tokenization issues include French elided articles (*l'ensemble*), German closed compounds (*Computerlinguistik*) that need a compound-splitter, and East-Asian scripts (Chinese, Japanese, Thai) that lack inter-word spacing and require word segmentation or character n-gram indexing.
- **Invariant:** queries and documents must be tokenized identically; otherwise a term that exists in the dictionary will never be found via the query path.
- **Stop words** are highly frequent, low-content terms (the IIR example list of 25 includes *a, an, and, are, as, at, be, by, for, from, in, is, it, of, on, that, the, to, was, were, will, with*) constructed by sorting terms by collection frequency and hand-filtering.
- Trends in stop-word usage have moved from 200-300-term stop lists toward minimal or empty lists, since phrase queries ("President of the United States"), titles, and semantically loaded prepositions ("flights *to* London") need them, and modern compression plus inverse-document-frequency weighting and impact-sorted indexes make keeping them cheap.
- **Normalization** creates equivalence classes among token variants so *USA* matches *U.S.A.* and *anti-discriminatory* matches *antidiscriminatory*; it can be done implicitly via mapping rules (which only delete characters reliably) or via explicit query-expansion / synonym lists (e.g. *car* <-> *automobile*), which are more flexible but more expensive.
- Asymmetric expansion lets a query *windows* match the OS sense while *window* matches the literal sense without matching the OS; symmetric equivalence classing cannot express this asymmetry.
- **Stemming** is a crude heuristic that chops off word endings (often also derivational affixes); **lemmatization** uses morphological analysis and a vocabulary to return the dictionary lemma, e.g. mapping *saw* to *see* or *saw* depending on context.
- **Porter's algorithm** is the dominant English stemmer; it applies 5 sequential phases of rewrite rules conditioned on the **measure** *m* (a rough syllable count) of the residual stem, e.g. `(m>1) EMENT ->` strips *-ement* from *replacement* but leaves *cement* untouched.
- Stemming raises recall but can harm precision: Porter conflates *operate, operating, operates, operation, operative, operatives, operational* all to *oper*, blurring queries like *operational and research*.
- Aggregate evidence shows stemming/lemmatization gives 0-5% gains for English but ~30% for Finnish and ~10% for Spanish; character 4-grams give 37% gains for Finnish and 27% for Swedish; diacritic removal alone can yield ~23% in Finnish/French/Swedish.
- **Skip pointers** accelerate postings-list intersection: standard merge is O(m+n), but adding skip pointers lets the algorithm jump over postings that cannot contribute to the AND result.
- The standard **sqrt(P) heuristic** places evenly-spaced skip pointers, sqrt(P) of them, in a postings list of length P, trading skip-comparison overhead against skip-span length.
- Skip pointers help conjunctive (AND) queries on static lists but give no benefit for OR queries, are degraded by index updates in dynamic indexes, and do not exist on intermediate query results.
- Phrase queries account for ~3-11.7% of web queries explicitly (with quotes) and many more implicitly (e.g. person names); supporting them requires structures beyond document-level postings.
- A **biword index** treats every adjacent token pair as a term: *Friends, Romans, Countrymen* yields biwords *friends romans* and *romans countrymen*. Longer phrases become AND-of-biwords, e.g. *stanford university palo alto* -> *stanford university* AND *university palo* AND *palo alto*; this can produce false positives without a post-filter.
- **Extended biwords** use part-of-speech tags to compress function-word sequences, indexing patterns of the form `NX*N` (Noun, then any number of function words/articles/prepositions, then Noun) so *renegotiation of the constitution* becomes a single biword-like unit.
- **Positional indexes** store, for each term, postings of the form `docID: <pos1, pos2, ...>` (typically with term frequency); they support arbitrary phrase queries and *within-k* proximity queries (e.g. *employment /3 place*) that biword indexes cannot.
- Phrase queries on positional indexes are answered by intersecting docIDs and then checking that positions of *t_{i+1}* are exactly one greater than positions of *t_i* (and so on for longer phrases).
- Positional indexes are substantially larger than non-positional indexes (rule of thumb: 2-4x), but are required for general phrase and proximity support.
- **Combination schemes** keep a positional index plus a phrase index of selected high-payoff phrases — phrases that are queried often *and* where component words are individually common but the phrase is rare (e.g. *The Who* speeds up ~1000x; *Britney Spears* ~3x).
- A "next-word" partial index — a hybrid between biword and positional — has been measured at ~25% of the query time of a positional-only system at ~26% extra storage, illustrating the broad design space.

## Section Notes

### 2.1 Document delineation and character sequence decoding
Frames the pre-tokenization problem: an indexer receives raw bytes and must produce a linear sequence of characters from a defined document. Two sub-problems follow — recovering characters and choosing what counts as a document.

### 2.1.1 Obtaining the character sequence in a document
Raw bytes must be decoded into characters; for ASCII English this is trivial, but real collections require detecting encodings (UTF-8, vendor-specific) via machine learning, heuristics, metadata, or user input, plus extracting text from binary formats (Word, zip) and decoding markup/entities (`&amp;` -> `&`). Non-linear scripts such as Arabic still store a linear character stream — bidirectional layout, right-to-left flow, and vowel diacritics are display-time concerns, not storage-time concerns. Commercial systems typically license format/encoding libraries rather than rolling their own.

### 2.1.2 Choosing a document unit
The indexer must decide what a "document" is: a whole mbox file vs. each message; a message vs. message-plus-attachments; a zipped archive vs. its members; a `latex2html`-split chapter vs. the reassembled book. Larger units inflate recall but produce semantic false positives ("Chinese toys" matching a book that mentions both terms chapters apart); smaller units (paragraphs, sentences) improve precision but split evidence. Proximity weighting and multi-level XML retrieval mitigate the tradeoff but do not eliminate it; the right unit depends on collection, users, and queries.

### 2.2 Determining the vocabulary of terms
Introduces the four-step pipeline (tokenize, drop stop words, normalize, stem/lemmatize) for going from a character stream to a set of index terms, and stresses that any decision applied to documents must also be applied to queries.

### 2.2.1 Tokenization
Defines tokenization as chopping the character stream into tokens (possibly discarding punctuation) and clarifies the *token/type/term* trichotomy. Surveys hard cases: apostrophes (*O'Neill*, *aren't*), hyphens with three different functions, multi-word names, dates, URLs, and email addresses. Discusses French elision, German compounding, and unsegmented East Asian scripts — for which character k-gram indexing is a common workaround.

### 2.2.2 Dropping common terms: stop words
Build a stop list by sorting terms by collection frequency and hand-filtering the head. Reduces postings drastically but breaks phrase queries ("President *of* the United States"), titles entirely composed of stop words, and any query where a "common" word is semantically load-bearing. Modern web engines trend toward keeping all words and using compression and weighting to manage cost.

### 2.2.3 Normalization (equivalence classing of terms)
Maps surface variants (*USA*/*U.S.A.*, *anti-discriminatory*/*antidiscriminatory*, accented vs. unaccented forms) to a single canonical term. Two implementation strategies: implicit equivalence classes built by deterministic mapping rules (which can only delete, not insert, characters) and explicit query-expansion lists (more flexible, allow asymmetric expansion such as *car* -> *automobile*, but more expensive). Warns against over-normalization (e.g. *C.A.T.* collapsing into *cat*) and notes that consistency between query and document processing matters more than the exact rules.

### 2.2.4 Stemming and lemmatization
Both aim to fold inflectional (and possibly derivational) variants onto a base form, but stemming is heuristic suffix-chopping while lemmatization performs dictionary-driven morphological analysis. Introduces Porter's algorithm with its 5 phases and the *m*-measure conditioning (e.g. `(m>1) EMENT ->` for *replacement* but not *cement*), and contrasts it with Lovins' and Paice-Husk stemmers. Empirically: little aggregate effect on English IR; substantial gains in morphologically rich languages.

### 2.3 Faster postings list intersection via skip pointers
Augments each postings list with skip pointers so intersection can jump over irrelevant runs. Gives the standard sqrt(P) placement heuristic and analyzes the tradeoff: more skips means shorter spans but more comparisons and storage. Notes that skip pointers help only AND-style queries on static, original postings.

### 2.4 Positional postings and phrase queries
Motivates phrase queries with examples like *Stanford University* (which must not match "the inventor Stanford Ovshinsky never went to university"). Roughly 10% of web queries are explicit phrases; many more are implicit. Sets up the three implementation strategies covered next.

### 2.4.1 Biword indexes
Index every adjacent token pair as if it were a term. Two-word phrase queries become a single dictionary lookup; longer phrases decompose into AND-of-biword queries (with possible false positives that need document verification). Extended biwords use POS tags to fold function-word interludes (`NX*N`), making *renegotiation of the constitution* indexable as one unit. The vocabulary blows up rapidly for phrase indexes of length >= 3, so exhaustive long-phrase indexes are impractical.

### 2.4.2 Positional indexes
Augment each posting with a list of in-document positions: `docID: <pos1, pos2, ...>`. Phrase queries intersect docIDs and then check positional offsets (1 for *t1 t2*, k for *t1 ... tk*). Also supports proximity operators like *employment /3 place*. Index size grows substantially (~2-4x) but expressivity is much higher than biwords.

### 2.4.3 Combination schemes
Hybrid: keep a positional index and add a small phrase index for high-value phrases. Best speedups arise when both component words are common but the phrase itself is rare (*The Who*: ~1000x; *Britney Spears*: ~3x). Williams et al.'s next-word partial index (a hybrid between biword and positional) achieves ~25% of positional-only query time at ~26% additional storage.

### 2.5 References and further reading
Cites work on Chinese segmentation and character bigram indexing, truecasing, computational morphology, n-gram-based language identification (written ID is easier than spoken), and cross-lingual stemming evaluations: Finnish stemming +30%, Spanish +10%, English 0-5%, diacritic removal +23%, Finnish 4-grams +37%, Swedish 4-grams +27%. Phrase-query prevalence in web logs is estimated at 3-11.7%.

## Algorithms & Formulas

### Skip-pointer-augmented postings intersection
Two postings lists *P1*, *P2* are walked with pointers *p1*, *p2*:

```
INTERSECT-WITH-SKIPS(P1, P2):
  answer <- []
  p1 <- head(P1); p2 <- head(P2)
  while p1 != nil and p2 != nil:
    if docID(p1) == docID(p2):
      append docID(p1) to answer
      p1 <- next(p1); p2 <- next(p2)
    else if docID(p1) < docID(p2):
      if hasSkip(p1) and docID(skip(p1)) <= docID(p2):
        while hasSkip(p1) and docID(skip(p1)) <= docID(p2):
          p1 <- skip(p1)
      else:
        p1 <- next(p1)
    else:
      if hasSkip(p2) and docID(skip(p2)) <= docID(p1):
        while hasSkip(p2) and docID(skip(p2)) <= docID(p1):
          p2 <- skip(p2)
      else:
        p2 <- next(p2)
  return answer
```

### sqrt(P) skip-pointer placement heuristic
For a postings list of length *P*, place sqrt(P) skip pointers at uniform intervals of approximately sqrt(P) postings. This balances the number of skips that may be taken (~ sqrt(P) of them, each saving ~ sqrt(P) steps) against the cost of storing and comparing the skip pointers themselves. Assumes a static index with a roughly uniform query distribution; index updates and non-uniform access patterns degrade the optimum.

### Positional phrase-query intersection (two-term phrase t1 t2)
For each docID *d* in `postings(t1) ∩ postings(t2)`:

```
POSITIONAL-INTERSECT(p1_positions, p2_positions, k=1):
  results <- []
  i <- 0; j <- 0
  while i < len(p1_positions) and j < len(p2_positions):
    diff <- p2_positions[j] - p1_positions[i]
    if diff == k:
      append (d, p1_positions[i], p2_positions[j]) to results
      i <- i + 1; j <- j + 1
    else if diff > k:
      i <- i + 1
    else:
      j <- j + 1
  return results
```

Generalizes to phrases of length *n* by iterative pairwise constraint application (positions of *t_{i+1}* must be exactly one greater than positions of *t_i*), or by collecting candidate positions per docID and checking that some consecutive subsequence of length *n* satisfies the per-step offset. Proximity queries `t1 /k t2` relax the equality to `|p2 - p1| <= k`.

### Porter's measure *m* (sketch)
Treating the residual stem as an alternating sequence of vowel-groups (V) and consonant-groups (C), *m* counts the number of `VC` transitions. Rewrite rules condition on *m*: e.g. `(m>1) EMENT ->` strips *-ement* only when the residual has at least two VC transitions, allowing *replacement -> replac* (m=2) but blocking *cement -> c* (m=1).

## Key Quotes
> "Tokenization is the task of chopping it up into pieces, called *tokens*, perhaps at the same time throwing away certain characters, such as punctuation."

> "Stop words are extremely common words which would appear to be of little value in helping select documents matching a user need."

> "Stemming usually refers to a crude heuristic process that chops off the ends of words ... whereas lemmatization usually refers to doing things properly with the use of a vocabulary and morphological analysis of words."

> "You always want to do the exact same tokenization of document and query words, generally by processing queries with the same tokenizer."

## Connections
- [[InformationRetrieval]] — chapter sits inside the IIR textbook's foundational chapters on building an inverted index.
- [[InvertedIndex]] — the artifact whose vocabulary and postings lists this chapter constructs.
- [[ClassBasedTFIDF]] — downstream weighting scheme that relies on the term vocabulary defined here.
- [[Tokenization]] — central topic of section 2.2.1; this source materially refines the existing concept page.
- [[PostingsList]] — the per-term list of docIDs (and optionally positions) whose intersection is optimized via skip pointers.
- [[TermVocabulary]] — the set of normalized index terms produced by the four-step pipeline.
- [[TokenTypeTerm]] — the *token / type / term* trichotomy used throughout IR.
- [[DocumentUnit]] — what an indexer treats as a "document," a key granularity decision.
- [[CharacterEncoding]] — UTF-8 and vendor encodings must be decoded before tokenization.
- [[StopWords]] — high-frequency, low-content terms historically removed from the vocabulary.
- [[EquivalenceClassing]] — collapsing surface variants onto canonical terms.
- [[QueryExpansion]] — explicit synonym/relation lists used as an alternative to equivalence classing.
- [[Stemming]] — heuristic suffix-stripping, increases recall, can hurt precision.
- [[Lemmatization]] — dictionary-driven reduction to base lemma form.
- [[PorterStemmer]] — the dominant English stemming algorithm, five phases, *m*-measure rules.
- [[LovinsStemmer]] — earlier single-pass English stemmer mentioned in IIR's further reading.
- [[PaiceHuskStemmer]] — alternative English stemmer mentioned in IIR's further reading.
- [[CharacterNgramIndex]] — common workaround for unsegmented scripts and morphologically rich languages.
- [[CompoundSplitting]] — needed for German-style closed compounds (e.g. *Computerlinguistik*).
- [[WordSegmentation]] — required for Chinese, Japanese, Thai indexing.
- [[Truecasing]] — restoring case information as preprocessing.
- [[LanguageIdentification]] — character-n-gram-based detection of the language of a document.
- [[SkipPointer]] — index-time-augmented pointers that accelerate Boolean AND.
- [[PostingsIntersection]] — the merge algorithm that skip pointers and positional structures extend.
- [[PositionalIndex]] — postings that include in-document token positions.
- [[BiwordIndex]] — adjacent-pair-as-term index for phrase queries.
- [[ExtendedBiwordIndex]] — POS-tag-conditioned biwords covering function-word interludes.
- [[PhraseQuery]] — multi-token queries that must match contiguous in-document sequences.
- [[ProximityQuery]] — queries that require terms to occur within k tokens, supported only by positional indexes.
- [[NextWordIndex]] — Williams et al.'s biword/positional hybrid.
- [[BooleanRetrieval]] — the query model these postings structures support.
- [[ReutersRCV1]] — the Reuters Corpus used for stop-word examples and other IIR statistics.
- [[ShakespeareCorpus]] — collection used elsewhere in IIR for tokenization examples (e.g. *to be or not to be*).
- [[ChristopherManning]] — co-author of IIR.
- [[PrabhakarRaghavan]] — co-author of IIR.
- [[HinrichSchutze]] — co-author of IIR.
- [[MartinPorter]] — author of the Porter stemming algorithm.
- [[CambridgeUniversityPress]] — publisher of IIR.
- [[StanfordNLPGroup]] — host of the IIR online edition.

## Contradictions
None identified against the current wiki.
