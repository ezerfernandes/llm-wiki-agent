---
title: "Web Scraping"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, data-acquisition]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Web Scraping

A [[DataAcquisition|data-acquisition]] strategy that builds datasets at scales manual curation cannot match (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]). [[ImageNet]] and OpenImages were built through systematic scraping; LLMs depend on web-scale text corpora; targeted scraping of code repositories built coding datasets.

Two failure surfaces bound its value:

- **Irreducible noise.** Scraping "traffic light" returns a 1914 manual-semaphore photo → a spurious correlation (traffic lights operated by uniformed officers). **No amount of additional scraped data removes the need for validation** that filters anachronistic/contextually-inappropriate content — the [[FourPillarsOfDataEngineering|quality pillar]] cannot be satisfied by scale alone.
- **Pipeline reliability + legal/ethical limits.** Website structure changes break extractors, rate limiting throttles throughput, dynamic content introduces inconsistencies; not all sites permit scraping, and ongoing litigation bounds training-data use. Teams must document provenance, respect terms of service/copyright, and anonymize user-generated content.

## Connections

- [[DataAcquisition]] — the parent strategy space.
- [[Crowdsourcing]] / [[SyntheticDataGeneration]] — sibling channels.
- [[ImageNet]] — built via scraping + crowdsourced labeling.
- [[DataQuality]] — why scale alone is insufficient.
- [[mlsysbook-ch04-data-engineering]] — source.
