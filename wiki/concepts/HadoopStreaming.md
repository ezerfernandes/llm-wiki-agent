---
title: "HadoopStreaming"
type: concept
tags: [hadoop, mapreduce, interface, language-agnostic]
sources: [parproc-ch09-mapreduce-computation]
last_updated: 2026-05-17
---

# Hadoop Streaming

Hadoop's streaming interface makes the [[Hadoop]] [[MapReduce]] framework language-agnostic. While Hadoop is written in Java and natively targets Java or C++ programs, streaming allows mappers and reducers to be written in any language — R, Python, shell scripts, etc.

## Protocol

- Mapper reads its input chunk from **stdin**, one line at a time.
- For each line, the mapper emits zero or more `key \t data` pairs to **stdout** (tab-separated).
- The Hadoop framework collects all mapper output, groups lines by key (the shuffle/sort phase), and routes each key group to a reducer.
- The reducer reads its key group from **stdin** (presorted by key) and writes final output to **stdout**, which Hadoop redirects to [[HDFS]].

## Invocation

The streaming JAR is invoked at the command line:

```
bin/hadoop jar contrib/streaming/*.jar \
  -input <input-path-in-HDFS> \
  -output <output-path-in-HDFS> \
  -mapper ../wordmapper.R \
  -reducer ../wordreducer.R
```

A combiner may be specified via `-combiner` to pre-aggregate mapper output before the network hop, reducing shuffle traffic.

## Trade-offs

- **Universality:** Any language with stdin/stdout access can be used. [[WordCount]] in R is a worked example in [[parproc-ch09-mapreduce-computation]].
- **Performance cost:** Text serialization (string-to-number conversion) introduces overhead. Hadoop streaming is *"not designed for maximum efficiency."* (§9.1.1).
- **Combiner benefit:** Because all communication is one `(key, value)` pair per network message, many short messages create latency pressure. A combiner (often identical to the reducer) pre-reduces on the mapper node before shuffling.

## Connections

- [[Hadoop]] — the framework that provides streaming.
- [[MapReduce]] — the paradigm; streaming is the language-agnostic interface to it.
- [[HDFS]] — provides the input and output files.
- [[WordCount]] — the canonical streaming example implemented in R.
- [[parproc-ch09-mapreduce-computation]] — §9.1.1–§9.1.4 describe and demonstrate streaming.
