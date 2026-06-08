---
title: "Mozilla"
type: entity
tags: [organization, company, browser, security, fuzzing, open-source]
sources: [fuzzingbook-29-fuzzing-in-the-large]
last_updated: 2026-06-06
---

# Mozilla

**Mozilla** is the organization behind the Firefox browser and a major practitioner of large-scale software security testing. Its security group (Mozilla Security) builds and runs fuzzing infrastructure to continuously test browser engines, which involve enormous, attack-exposed C++ codebases. Mozilla open-sources several of these tools, including **[[FuzzManager]]** (crash collection, bucketing, and coverage management) and `grcov` (a coverage-data aggregation tool).

## Role in The Fuzzing Book
[[fuzzingbook-29-fuzzing-in-the-large|Ch 29]] uses Mozilla's tooling as its case study for [[FuzzingAtScale|fuzzing in the large]]: the [[FuzzManager]] framework (authored by Mozilla's [[ChristianHoller|Christian Holler]], a co-author of the book) for collecting and deduplicating crashes, and Mozilla's `grcov` for capturing the per-fuzzer [[Coverage|coverage]] that FuzzManager's CovManager visualizes. The chapter cites the article *"Browser Fuzzing at Mozilla"* for how FuzzManager underpins Mozilla's continuous, massive browser fuzzing.

## Connections
- [[FuzzManager]] — Mozilla's crash-management toolchain demonstrated in the chapter.
- [[ChristianHoller]] — Mozilla Security engineer, FuzzManager author, and book co-author.
- [[ContinuousFuzzing]] / [[FuzzingAtScale]] — Mozilla runs browser fuzzing continuously at scale.
- [[Coverage]] — Mozilla's `grcov` collects the coverage data FuzzManager displays.
- [[fuzzingbook-29-fuzzing-in-the-large|Ch 29]] — the chapter that features Mozilla's tooling.

## Sources
- [[fuzzingbook-29-fuzzing-in-the-large]] — *The Fuzzing Book* Ch 29, "Fuzzing in the Large."
