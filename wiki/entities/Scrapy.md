---
title: "Scrapy"
type: entity
tags: [tool, library, python, web-scraping, open-source]
sources: [leh-ch03-data-engineering]
last_updated: 2026-05-22
---

## What it is
Scrapy is an open-source Python framework for large-scale web crawling and scraping. It provides spiders, request scheduling, item pipelines, middleware, and built-in support for politeness rules, retries, and storage backends.

## In LLM Engineer's Handbook
Ch. 3 ([[leh-ch03-data-engineering]]) recommends Scrapy as the modern alternative for **production-grade general web scraping**, when the book's hand-rolled [[Selenium]]+[[BeautifulSoup]]+[[LangChain]]-fallback approach would not scale. Scrapy is paired with [[Crawl4AI]] as the two recommended crawler upgrades.

## Connections
- [[Crawl4AI]] — sibling recommendation for LLM-targeted crawling.
- [[Selenium]] / [[BeautifulSoup]] — what the book uses instead at its scale.
- [[WebCrawling]] — domain.
- [[Python]] — language.
