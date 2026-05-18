---
title: "WordCount"
type: concept
tags: [mapreduce, example, hadoop, snowdoop]
sources: [parproc-ch09-mapreduce-computation]
last_updated: 2026-05-17
---

# WordCount

The canonical "Hello World" example for [[MapReduce]] systems. Given a text file, compute the frequency count of each distinct word. It illustrates the full map/shuffle/reduce pipeline with minimal domain-specific complexity.

## Hadoop Streaming Implementation (R)

**Mapper (`wordmapper.R`):** reads stdin line by line; for each word in a line, emits `word \t 1` via `cat(w, "\t 1\n")`.

**Reducer (`wordreducer.R`):** reads presorted `word \t count` pairs from stdin; accumulates counts while the word stays the same; emits `word \t total` on word change. The count field may be greater than 1 if a combiner pre-aggregated the mapper output.

**Combiner:** often identical to the reducer. Runs on each mapper's local output before the shuffle phase, reducing the number of `(word, 1)` pairs sent over the network.

**Run command:**
```
bin/hadoop fs -put ../rnyt rnyt
bin/hadoop jar contrib/streaming/*.jar \
  -input rnyt -output wordcountsnyt \
  -mapper ../wordmapper.R -reducer ../wordreducer.R
```

Output lands in HDFS under `wordcountsnyt/part-00000`, etc.

## Snowdoop Implementation (R)

In [[Snowdoop]], the file is pre-chunked into distributed mini-files. Each worker calls `wordcensus(basename, ndigs)` which reads its chunk with `scan` and calls `tapply(words, words, length)` to get per-chunk counts. The manager uses `clusterCall(cls, wordcensus, ...)` then reduces with `addlists` (element-wise list sum) and `Reduce`. No Java, no configuration.

## Connections

- [[MapReduce]] — the paradigm WordCount exemplifies.
- [[Hadoop]] — the platform for the streaming implementation.
- [[HadoopStreaming]] — the stdin/stdout interface used.
- [[HDFS]] — storage for input and output.
- [[Snowdoop]] — provides an alternative pure-R implementation.
- [[parproc-ch09-mapreduce-computation]] — §9.1.2 and §9.4.1 give both implementations.
