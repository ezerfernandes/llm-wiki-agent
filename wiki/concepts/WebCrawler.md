---
title: "Web Crawler"
type: concept
tags: [web-search, information-retrieval, distributed-systems]
sources: [iir-ch20-web-crawling-indexes, iir-ch19-web-search-basics]
last_updated: 2026-05-23
---

System that traverses the web by following hyperlinks, downloading pages, and feeding them to an indexing pipeline. The data-collection front end of any web search system.

**Hard requirements** ("must")
- **Politeness**: respect `robots.txt` ([[RobotsExclusionProtocol]]), rate-limit per-host requests so a single site doesn't get DOS'd.
- **Distributed operation**: a single machine cannot crawl the web in any reasonable freshness window.
- **Robustness**: handle malformed HTML, redirect loops, spider traps, crawler-targeted spam.

**Soft requirements** ("should")
- **Freshness**: revisit pages on a schedule proportional to their change rate.
- **Quality bias**: spend bandwidth on important pages (high [[PageRank]], high inlink count) first.
- **Extensibility**: handle new content types (PDF, JS-rendered pages, structured data feeds).

**Mercator-style architecture** ([[Mercator|Allan Heydon & Marc Najork, 2001]]):
- A **[[URLFrontier]]** stores discovered-but-not-yet-fetched URLs. Front queues prioritize by importance / freshness, back queues hold one host each so the politeness scheduler can pick the next fetch by least-recently-touched host (heap of next-fetch times).
- **DNS** is the surprise bottleneck — synchronous resolution serializes; production crawlers do async DNS with a heavy cache.
- **Fetchers** pull pages, **parsers** extract text + outlinks, **duplicate elimination** hashes content (Rabin fingerprints) to avoid indexing the same page twice across mirror sites.
- **Sitemaps** provide hint-driven crawling for sites that publish them.

Production crawler entities: [[Heritrix]] ([[InternetArchive]]'s open-source crawler), GoogleBot, BingBot, [[CommonCrawl]]'s ccBot. Full architecture in [[iir-ch20-web-crawling-indexes]].
