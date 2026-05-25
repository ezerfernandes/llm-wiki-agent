---
title: "Medium"
type: entity
tags: [product, platform, publishing, blog]
sources: [leh-ch01-understanding-llm-twin-concept, leh-ch03-data-engineering]
last_updated: 2026-05-22
---

## What it is
Medium is a long-form online publishing platform for articles and newsletters. Many ML/AI practitioners publish technical writing there.

## In LLM Engineer's Handbook
Medium is one of the four crawled sources of the LLM Twin's data-collection pipeline. Ch. 1 ([[leh-ch01-understanding-llm-twin-concept]]) names it as one of the **articles** category sources (alongside Substack). Ch. 3 ([[leh-ch03-data-engineering]]) implements a `MediumCrawler` that inherits `BaseSeleniumCrawler`, drives a headless Chrome session via [[Selenium]], scrolls the article, then parses with [[BeautifulSoup]] (`h1.pw-post-title`, `h2.pw-subtitle-paragraph`).

## Connections
- [[Substack]] / [[LinkedIn]] / [[GitHub]] — peer crawled sources.
- [[Selenium]] / [[BeautifulSoup]] / [[ChromeDriver]] — tools used to crawl Medium.
- [[WebCrawling]] — domain.
- [[LLMTwin]] — running project whose corpus includes Medium articles.
