---
title: "Martin Porter"
type: entity
tags: [person, researcher, information-retrieval, stemming]
sources: [iir-ch02-term-vocabulary-postings]
last_updated: 2026-05-23
---

British computer scientist; author of the **Porter stemming algorithm** (1980) — the most widely deployed stemmer for English IR systems. The algorithm uses cascading rule-based suffix stripping in five phases (e.g. `ies → y`, `sses → ss`, `ational → ate`, `eed → ee` only if the stem has at least one vowel-consonant pair); it is fast, has no lookup tables, and produces reasonable (though not linguistically perfect) conflations like `connect / connected / connecting / connection → connect`.

Successor work: the **Snowball** language (Porter, 2001) — a small domain-specific language for *writing* stemmers, plus the Snowball-implemented stemmers for ~25 languages (Porter2 / "English stemmer" for English, plus French, Spanish, German, Russian, Arabic, etc.). Snowball stemmers are bundled into Lucene / Elasticsearch / Solr and are the default stemmer for most production search systems.

The original 1980 paper *"An Algorithm for Suffix Stripping"* (Program 14(3)) is among the most-cited IR papers of all time. The Porter / Snowball line is contrasted with the [[Lovins]] stemmer (1968; longest-match single-pass) and the more aggressive [[PaiceHusk]] stemmer in [[iir-ch02-term-vocabulary-postings]] §2.2.4.
