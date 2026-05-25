---
title: "Crawl4AI"
type: entity
tags: [tool, library, python, web-scraping, llm, open-source]
sources: [leh-ch03-data-engineering]
last_updated: 2026-05-22
---

## What it is
Crawl4AI is an open-source crawler purpose-built for feeding LLMs and RAG systems. It emits clean Markdown, supports JavaScript-rendered pages, and integrates with LLM-based extraction for structured output.

## In LLM Engineer's Handbook
Ch. 3 ([[leh-ch03-data-engineering]]) recommends Crawl4AI as the modern alternative for **LLM-targeted web crawling** when the book's custom Selenium + BeautifulSoup + LangChain-fallback would be insufficient — paired with [[Scrapy]] (for general scraping) as the two upgrade paths.

## Connections
- [[Scrapy]] — sibling recommendation.
- [[Selenium]] / [[BeautifulSoup]] — what the book uses at its scale.
- [[WebCrawling]] — domain.
- [[rag]] — typical downstream consumer of Crawl4AI's output.
