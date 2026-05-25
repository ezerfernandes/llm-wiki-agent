---
title: "IIR Ch. 4: Index Construction"
type: source
tags: [iir, information-retrieval, textbook, index-construction, mapreduce, bsbi, spimi]
date: 2026-05-23
source_file: "https://nlp.stanford.edu/IR-book/html/htmledition/index-construction-1.html"
---

## Summary

Chapter 4 of Manning, Raghavan and Schütze's *Introduction to Information Retrieval* (Cambridge University Press, 2008) is the bridge between the conceptual [[InvertedIndex]] introduced in Chapter 1 and the scale at which real-world [[InformationRetrieval]] systems must build one. The chapter argues that **indexing algorithms are dictated by hardware**: spinning-disk seek latency dwarfs sequential transfer cost, RAM is finite, and processors are fast enough that I/O — not CPU — is the bottleneck. Four algorithms are presented in order of increasing scale and dynamism: **blocked sort-based indexing ([[BSBI]])** for collections that exceed memory, **single-pass in-memory indexing ([[SPIMI]])** which removes the term-to-termID dictionary from the critical path, **distributed indexing** with [[MapReduce]] for web-scale collections, and **dynamic indexing** with [[LogarithmicMerging]] for collections that change over time. The recurring case study is the [[ReutersRCV1]] news corpus (~800k documents, 100M tokens, ~1 GB of raw text). The chapter closes with a short tour of specialised index variants (security/ACL indexes, impact-ordered postings, positional and parametric indexes).

## Key Claims

- **Hardware is the boundary condition for index design.** A disk seek averages ~5 ms while reading one byte from disk costs ~0.02 µs; consequently the cost model of every indexing algorithm in the chapter is dominated by seeks and by the question "does this structure fit in memory?".
- **Sort-based indexing scales by externalising the sort.** [[BSBI]] partitions postings into in-memory blocks, sorts each block, writes a sorted run to disk, and finishes with a multi-way merge — total cost Θ(T log T) on T termID-docID pairs, but practical cost is dominated by parsing and merging, not by the sort itself.
- **The dictionary itself is the memory bottleneck.** [[SPIMI]] avoids holding a global term→termID map in RAM by using terms directly, writing one self-contained dictionary per block, and only sorting terms when the block is flushed. It runs in Θ(T) and processes substantially larger blocks than [[BSBI]].
- **Web-scale indexing is necessarily distributed.** [[MapReduce]] divides indexing into a *map* (parser) phase that emits term→docID key-value pairs and a *reduce* (inverter) phase that collects all pairs for a partition of the term space into postings lists. Google reportedly used five to ten chained MapReduce jobs to build its index circa 2004.
- **A growing collection needs an auxiliary index, not a rebuild on every change.** Maintaining a small in-memory index alongside the main on-disk index and merging periodically reduces seek cost; the deletion bit-vector handles removals. Naive auxiliary merging is Θ(T²/n), but [[LogarithmicMerging]] reduces this to Θ(T log(T/n)) at the cost of querying ~log(T/n) indexes instead of two.
- **Specialised use cases need specialised indexes.** ACL-based security, impact-ordered (rather than docID-ordered) postings for early termination in ranked retrieval, and positional/parametric indexes are all variants of the same core data structure.

## Section Notes

### 4.1 Hardware basics

The chapter opens with **Table 4.1**, a set of rule-of-thumb hardware constants for a typical 2007-era IR server:

| Parameter | Symbol/Value |
|---|---|
| Average disk seek time | ~5 × 10⁻³ s (5 ms) |
| Disk transfer time per byte | ~2 × 10⁻⁸ s (0.02 µs) |
| Processor clock rate | ~10⁹ Hz |
| Low-level operation time (e.g. compare-and-swap a word) | ~10⁻⁸ s (0.01 µs) |
| Server main memory | several GB |
| Server disk space | 1 TB or more |

From these constants the chapter derives a series of design guidelines:

- **Keep data in memory whenever it fits.** Memory access is roughly two orders of magnitude faster than disk transfer and five orders of magnitude faster than a disk seek, so frequently-used structures (the dictionary, posting heads) belong in RAM.
- **Read contiguously.** Reading 10 MB contiguously takes ~0.2 s; reading the same 10 MB scattered over 100 locations takes ~0.7 s because of repeated seeks. Indexing algorithms therefore prefer long sequential runs to many small writes.
- **Operate at block granularity.** "Reading a single byte from disk can take as much time as reading the entire block." Block sizes of 8–64 KB are typical, and inversion algorithms are designed around blocks rather than individual postings.
- **Overlap I/O with CPU.** Disk transfers use the system bus independently of the CPU; this asynchrony makes compression a net win — the time to read compressed bytes *and* decompress them is usually less than the time to read uncompressed bytes.

### 4.2 Blocked sort-based indexing ([[BSBI]])

BSBI is the workhorse external-sorting algorithm for inverted indexes. The chapter motivates it with the [[ReutersRCV1]] case study:

| Reuters-RCV1 statistic | Value |
|---|---|
| Documents N | 800,000 |
| Avg. tokens per document | 200 |
| Total tokens T | ~100,000,000 |
| Distinct terms M | ~400,000 |
| Bytes per token (with punctuation) | 6 |
| Bytes per token (no punctuation) | 4.5 |
| Bytes per term (string) | 7.5 |
| Raw collection size | ~1 GB |
| Storage for all termID–docID pairs | ~0.8 GB |

With ~10 million termID–docID pairs per memory block, BSBI processes RCV1 in **ten blocks** that then have to be merged.

The four phases are:

1. **Segment** the collection into chunks of equal size.
2. **Parse + accumulate** termID–docID pairs in memory until the block is full.
3. **Invert in memory**: sort the block's pairs by (termID, docID) and collect runs of identical termIDs into postings lists.
4. **Merge** all on-disk blocks simultaneously using a priority queue with one input buffer per block and one output buffer.

Cost is **Θ(T log T)** in the abstract; in practice the parser and the final merge dominate, not the in-memory sort. BSBI still requires a global term → termID dictionary that fits in memory, which is the constraint [[SPIMI]] is designed to remove.

```
BSBI-CONSTRUCT()
1  n <- 0
2  while (all documents have not been processed)
3    do n <- n + 1
4       block <- PARSENEXTBLOCK()
5       BSBI-INVERT(block)
6       WRITEBLOCKTODISK(block, f_n)
7  MERGEBLOCKS(f_1, ..., f_n; f_merged)
```

`PARSENEXTBLOCK` reads documents until the memory block is full, emitting termID–docID pairs. `BSBI-INVERT` sorts those pairs and produces postings lists. `MERGEBLOCKS` opens all block files concurrently, maintains small read buffers per block plus a write buffer, and at each step selects the smallest unprocessed termID across all input buffers (priority-queue style), appending its postings to the output.

### 4.3 Single-pass in-memory indexing ([[SPIMI]])

SPIMI's central idea is to **drop the global termID dictionary** and instead let each block keep its own local dictionary of term strings; blocks are merged at the end.

```
SPIMI-INVERT(token_stream)
 1  output_file <- NEWFILE()
 2  dictionary  <- NEWHASH()
 3  while (free memory available)
 4    do token <- next(token_stream)              # (term, docID) pair
 5       if term not in dictionary
 6         then postings_list <- ADDTODICTIONARY(dictionary, term)
 7         else postings_list <- GETPOSTINGSLIST(dictionary, term)
 8       if full(postings_list)
 9         then postings_list <- DOUBLEPOSTINGSLIST(dictionary, term)
10       ADDTOPOSTINGSLIST(postings_list, docID)
11  sorted_terms <- SORTTERMS(dictionary)
12  WRITEBLOCKTODISK(sorted_terms, dictionary, output_file)
13  return output_file
```

Compared to [[BSBI]], SPIMI:

- **eliminates the sort over (termID, docID) pairs**; postings are appended to the per-term list as they arrive, so the only sort is a single sort over the block's *terms* at flush time (line 11);
- **uses terms directly**, avoiding a global term→termID map that would itself consume memory;
- **grows postings lists dynamically** by doubling allocations (line 9), trading some wasted memory for amortised O(1) appends;
- **packs more documents into a block** because there is no separate dictionary table competing for RAM;
- **runs in Θ(T)** because all per-token operations are constant-time and the only super-linear step is the per-block term sort, which is small relative to T.

The chapter notes that both per-block dictionaries and postings can be compressed on disk, further increasing effective block size.

### 4.4 Distributed indexing ([[DistributedIndexing]] with [[MapReduce]])

For web-scale collections a single machine is inadequate; indexing must be distributed across a commodity-hardware cluster. The chapter uses [[MapReduce]] (Dean and Ghemawat, 2004) as its canonical example and notes that [[Google]] ran "five to ten" MapReduce passes to construct its index. [[Hadoop]] is cited as the open-source MapReduce implementation.

A master node assigns work to two classes of workers: **parsers** and **inverters**. Idle machines are reassigned in case of failure — fault tolerance is built into the scheduler.

- **Input splits.** The collection is broken into 16–64 MB splits, chosen large enough to be efficient sequential reads but small enough that the master can rebalance lost work cheaply.
- **Map phase (parsing).** Each parser reads its split and emits (term, docID) key-value pairs. Output is bucketed into **j term partitions** (e.g. *a–f*, *g–p*, *q–z*) and written to local **segment files** — one per (parser, partition) pair, so r parsers produce r × j segment files.
- **Shuffle.** Each inverter is assigned one term partition and pulls the r segment files for that partition from the parsers' local disks. Local writes + sequential reads minimise random network traffic.
- **Reduce phase (inversion).** The inverter sorts its incoming (term, docID) pairs by term and writes out the postings lists for its partition of the dictionary.

The chapter distinguishes **term-partitioned** (each machine owns a slice of the vocabulary) from **document-partitioned** (each machine owns a slice of the documents) indexes, observing that large web search engines tend to prefer document partitioning because it parallelises query evaluation more naturally — but that MapReduce indexing typically starts term-partitioned and then transforms the result.

```
# MapReduce indexing as schemas
schema of map:    input  -> list(k, v)
                  i.e.   document -> list(term, docID)
schema of reduce: (k, list(v)) -> output
                  i.e.   (term, list(docID)) -> postings_list(term)
```

### 4.5 Dynamic indexing ([[DynamicIndexing]])

Real collections are not static — documents are added, deleted, and modified. The naive strategy of editing the on-disk index for every change is infeasible because each affected term may live in a different block, costing up to one disk seek per update.

**Auxiliary-index strategy.** Maintain:
- a large **main index** on disk;
- a small **auxiliary index** in memory for new postings;
- an **invalidation bit-vector** marking deleted docIDs;
- a **merge policy** that periodically folds the auxiliary index into the main index.

Searches run against both indexes and merge results, filtering out invalidated docIDs. Each posting is rewritten ~T/n times over the lifetime of the index (where n is the auxiliary capacity), giving **Θ(T² / n)** total work.

**Logarithmic merging** ([[LogarithmicMerging]]). Maintain a hierarchy of indexes I₀, I₁, …, I_{log(T/n)}, where I_k has capacity 2^k · n:

- The in-memory index Z₀ holds up to n postings.
- When Z₀ fills, it is flushed to disk as I₀ (size n) if I₀ is empty, otherwise Z₀ ∪ I₀ is merged into I₁ (size 2n), and so on — cascading carries up the hierarchy like binary addition.
- Each posting is touched **once per level**, and there are log₂(T/n) levels.

Total work is therefore **Θ(T log(T/n))**, a substantial improvement over Θ(T²/n). The trade-off is query complexity: every query must consult ~log(T/n) indexes instead of two, and collection-wide statistics (e.g. document frequency) become harder to maintain. The chapter notes that some production systems give up on dynamic indexing entirely and simply rebuild the index from scratch on a schedule.

### 4.6 Other types of indexes

A short tour of variations:

- **Security / access-control indexes.** An inverted ACL maps each user to the documents they can see; query results are intersected with this list. Maintenance is hard (permissions change), users with broad access produce very long postings lists, and many systems prefer to consult the file system directly at query time.
- **Impact-ordered postings.** Standard inverted indexes order postings by docID, which is great for compression (gap encoding) and intersection. Ranked retrieval, however, benefits from ordering postings by **impact / weight**, so the highest-scoring documents are encountered first and scanning can stop once weights become negligible. Insertion is harder because a new document can land anywhere in the list.
- **Positional indexes** store token positions alongside docIDs (needed for phrase and proximity queries).
- **Parametric / zone indexes** are mentioned as further variants for fielded retrieval.

### 4.7 References and further reading

Key references the chapter points to:

- **External-sort-based indexing**: Witten, Moffat and Bell (1999) ch. 5; Moffat and Bell (1995) for in-situ construction; Lesk (1988) and Somogyi (1990) as early pioneers of sort-based indexing; Harman et al. (1992) and Fox and Lee (1991) on FAST-INV.
- **SPIMI**: Heinz and Zobel (2003); Zobel and Moffat (2006) for an updated survey.
- **Distributed indexing**: Dean and Ghemawat (2004) for [[MapReduce]]; Ribeiro-Neto et al. (1999) and Melnik et al. (2001) for alternative architectures; Baeza-Yates and Ribeiro-Neto (1999), Grossman and Frieder (2004), and Callan (2000) for introductions to distributed IR.
- **Dynamic indexing**: Lester et al. (2005), Büttcher and Clarke (2005a), Büttcher et al. (2006), Lester et al. (2006); Heinz et al. (2002) on vocabulary data structures.
- **Systems**: [[Hadoop]] (open-source MapReduce, lucene.apache.org/hadoop/); Lucene (lucene.apache.org); [[ReutersRCV1]] distributed by NIST.

## Algorithms & Formulas

### BSBI pseudocode

```
BSBI-CONSTRUCT()
1  n <- 0
2  while (collection not fully processed)
3    do n <- n + 1
4       block <- PARSENEXTBLOCK()        # fill memory with (termID, docID) pairs
5       BSBI-INVERT(block)               # sort pairs; build postings lists
6       WRITEBLOCKTODISK(block, f_n)
7  MERGEBLOCKS(f_1, ..., f_n; f_merged)  # k-way merge with priority queue

Complexity: Θ(T log T) where T = total number of termID-docID pairs.
For Reuters-RCV1: T ≈ 100M pairs, ~0.8 GB on disk, 10 blocks at 10M pairs/block.
```

### SPIMI-INVERT pseudocode

```
SPIMI-INVERT(token_stream)
 1  output_file <- NEWFILE()
 2  dictionary  <- NEWHASH()                       # per-block, term-keyed
 3  while (free memory available)
 4    do token <- next(token_stream)               # (term, docID)
 5       if term not in dictionary
 6         then postings_list <- ADDTODICTIONARY(dictionary, term)
 7         else postings_list <- GETPOSTINGSLIST(dictionary, term)
 8       if full(postings_list)
 9         then postings_list <- DOUBLEPOSTINGSLIST(dictionary, term)
10       ADDTOPOSTINGSLIST(postings_list, docID)
11  sorted_terms <- SORTTERMS(dictionary)          # sort terms at flush only
12  WRITEBLOCKTODISK(sorted_terms, dictionary, output_file)
13  return output_file

Complexity: Θ(T). No sort over (termID, docID) pairs; only a per-block term sort.
Memory advantage: no global term -> termID map; larger blocks than BSBI.
```

### MapReduce indexing phases

```
Map (parser):     document_split -> list((term, docID))
                  emits into j local segment files keyed by term partition
Shuffle:          inverter k pulls segment files for term partition k from all r parsers
Reduce (inverter):(term, list(docID)) -> postings_list(term)
                  one inverter per term partition

Cluster shape:    r parsers, j inverters; r * j segment files in total.
Splits:           16-64 MB each, large enough for sequential reads, small enough to rebalance.
Google (c. 2004): 5-10 chained MapReduce passes to build the production index.
```

### Logarithmic merging

```
Maintain indexes Z_0 (in memory, capacity n) and I_0, I_1, ... on disk
  where capacity(I_k) = 2^k * n.

ADD-POSTING(p):
  add p to Z_0
  if |Z_0| == n:
    merge Z_0 into I_0 (carrying up the hierarchy like binary addition)
    Z_0 <- empty

Number of levels: ~log_2(T / n)
Total work:       Θ(T log(T / n))         (vs. Θ(T^2 / n) for naive auxiliary merge)
Query cost:       must consult ~log(T / n) indexes per query (the cost of the speedup).
```

## Key Quotes

> "The design of indexing algorithms is governed by hardware constraints." — § 4 introduction.

> "Reading a single byte from disk can take as much time as reading the entire block." — § 4.1 Hardware basics, motivating block-granularity I/O.

> "SPIMI uses terms instead of termIDs, writes each block's dictionary to disk, and then starts a new dictionary for the next block." — § 4.3, the one-sentence definition of the algorithm.

> "Collections are often so large that we cannot perform index construction efficiently on a single machine." — § 4.4, motivating distributed indexing.

> "Each posting is processed only once on each of the log(T/n) levels." — § 4.5, the key insight behind logarithmic merging.

> "A low-level employee should not be able to find the salary roster of the corporation, but authorized managers need to be able to search for it." — § 4.6, motivating ACL-based security indexes.

## Connections

- [[InformationRetrieval]] — Chapter 4 is the construction-side companion to the conceptual IR pipeline introduced earlier in the book.
- [[InvertedIndex]] — every algorithm in this chapter is a different strategy for *building* an inverted index.
- [[BSBI]] — Blocked Sort-Based Indexing; external-sort baseline for collections larger than memory.
- [[SPIMI]] — Single-Pass In-Memory Indexing; removes the global termID dictionary and runs in Θ(T).
- [[MapReduce]] — programming model used to distribute index construction across a cluster; the chapter's worked example of distributed indexing.
- [[DistributedIndexing]] — the section-level concept of partitioning indexing work across many machines, with sub-concepts of term-partitioning vs. document-partitioning.
- [[DynamicIndexing]] — handling collections whose membership changes; auxiliary index + invalidation bit-vector.
- [[LogarithmicMerging]] — the Θ(T log(T/n)) merge strategy that makes dynamic indexing tractable.
- [[ReutersRCV1]] — the running case study (800k documents, 100M tokens, ~1 GB).
- [[Google]] — cited as the canonical operator of MapReduce-based web-scale indexing (5–10 chained jobs c. 2004).
- [[Hadoop]] — open-source MapReduce implementation referenced in the further-reading section.

## Contradictions

- None observed against existing wiki pages. The chapter is foundational and complementary to [[InvertedIndex]], [[InformationRetrieval]], [[MapReduce]], [[Hadoop]], and [[Google]] as they currently stand. If the wiki later acquires a source that argues against term-partitioned MapReduce indexing (e.g. systems that index directly into a document-partitioned layout), this page should be revisited.
