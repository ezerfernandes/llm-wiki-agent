---
title: "Christian Holler"
type: entity
tags: [person, author, researcher, fuzzing, security, javascript, langfuzz, mozilla, crash-management]
sources: [fuzzingbook-15-greybox-grammar-fuzzer, fuzzingbook-29-fuzzing-in-the-large]
last_updated: 2026-06-06
---

# Christian Holler

**Christian Holler** is a security researcher and engineer best known as the author of **[[LangFuzz]]**, the grammar-based [[FragmentBasedFuzzing|fragment-recombination]] fuzzer for JavaScript engines. He is a co-author of *The Fuzzing Book* (CISPA, 2024) alongside [[AndreasZeller|Andreas Zeller]], Rahul Gopinath, [[MarcelBohme|Marcel Böhme]], and Gordon Fraser, and first author of the paper *"Fuzzing with Code Fragments"* (Holler, Herzig & Zeller, USENIX Security 2012) that introduced the LangFuzz approach.

## Role in The Fuzzing Book
Holler's [[LangFuzz]] work is the direct inspiration for the [[FragmentBasedFuzzing|fragment-based mutation]] half of [[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] ("Greybox Fuzzing with Grammars"). The chapter recounts that in the first four weeks of running LangFuzz he netted **more than USD 50,000 in bug bounties**, and that LangFuzz has since found **more than 2,600 bugs** in the JavaScript engines of Firefox, Chrome, and Edge. It also credits his practice of [[SeedMining|seeding the fuzzer from JavaScript CVE reports]] — failure-inducing inputs republished after their bugs were fixed — as a source of further failures. The chapter notes wryly that "these are the same Holler and Zeller who are co-authors of this book," explaining why the book devotes several chapters to grammar-based fuzzing.

## From The Fuzzing Book — Fuzzing in the Large
Beyond LangFuzz, Holler is the author of **[[FuzzManager]]**, [[Mozilla]]'s open-source toolchain for managing large-scale fuzzing. [[fuzzingbook-29-fuzzing-in-the-large|Ch 29]] is built entirely on FuzzManager: it demonstrates collecting crashes from many fuzzers into a central server, grouping them into [[CrashDeduplication|buckets via crash signatures]], and visualizing per-fuzzer [[Coverage|coverage]]. This reflects his role on Mozilla Security, where FuzzManager underpins continuous browser fuzzing — the industrial counterpart to his academic LangFuzz work.

## Connections
- [[FuzzManager]] — Mozilla's crash-management toolchain he authored (subject of Ch 29).
- [[Mozilla]] — his employer; the org behind FuzzManager.
- [[CrashDeduplication]] / [[FuzzingAtScale]] — the crash-bucketing and large-scale management ideas FuzzManager embodies.
- [[LangFuzz]] — the fragment-recombination JavaScript fuzzer he authored.
- [[FragmentBasedFuzzing]] — the technique his "Fuzzing with Code Fragments" paper introduced.
- [[SeedMining]] — his practice of seeding from CVE-reported failure-inducing inputs.
- [[AndreasZeller]] / [[MarcelBohme]] — co-authors of *The Fuzzing Book* and (Zeller) co-author of the LangFuzz paper.
- [[GrammarAwareGreyboxFuzzing]] — the chapter built partly on his work.
- [[CISPA]] — publisher of *The Fuzzing Book* he co-authors.
- [[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] — the chapter inspired by his LangFuzz research.

## Sources
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — *The Fuzzing Book* Ch 15, "Greybox Fuzzing with Grammars."
- [[fuzzingbook-29-fuzzing-in-the-large]] — *The Fuzzing Book* Ch 29, "Fuzzing in the Large" (his FuzzManager toolchain for large-scale crash management).
