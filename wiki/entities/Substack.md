---
title: "Substack"
type: entity
tags: [product, platform, newsletter, publishing]
sources: [leh-ch01-understanding-llm-twin-concept, leh-ch03-data-engineering]
last_updated: 2026-05-22
---

## What it is
Substack is a newsletter and online-publishing platform with paid-subscription support. Many tech writers run technical newsletters there.

## In LLM Engineer's Handbook
Substack is one of the four crawled sources for the LLM Twin's data-collection pipeline. Ch. 1 ([[leh-ch01-understanding-llm-twin-concept]]) names it among the **articles** category sources alongside Medium. Ch. 3 ([[leh-ch03-data-engineering]]) does not implement a dedicated Selenium crawler for Substack; instead Substack URLs fall through to the `CustomArticleCrawler` fallback that uses [[LangChain]]'s `AsyncHtmlLoader` + `Html2TextTransformer`.

## Connections
- [[Medium]] / [[LinkedIn]] / [[GitHub]] — peer crawled sources.
- [[LangChain]] — the loaders used to crawl Substack via `CustomArticleCrawler`.
- [[WebCrawling]] — domain.
- [[LLMTwin]] — running project whose corpus includes Substack articles.
