---
title: "Web Crawling"
type: concept
tags: [data-engineering, etl, scraping]
sources: [leh-ch03-data-engineering]
last_updated: 2026-05-22
---

## Definition
**Web crawling** is the practice of programmatically fetching pages from websites and extracting their content for downstream processing — the *extract* stage of an ETL pipeline when the data source is the public web. Techniques range from raw HTTP GETs through HTML-parsed extraction to full browser automation that drives a real Chromium instance to render JavaScript-heavy pages.

## In LLM Engineer's Handbook
[[leh-ch03-data-engineering]] is a worked example of LLM-training-data web crawling. The chapter builds a `CrawlerDispatcher` (via the [[BuilderPattern|Builder pattern]]) that routes URLs to per-platform crawler subclasses of `BaseCrawler` (an ABC). Four concrete crawlers are implemented: `GithubCrawler` shells out to `git clone` in a temp directory; `MediumCrawler` and `LinkedInCrawler` use [[Selenium]]-driven headless Chrome with [[BeautifulSoup]] HTML parsing and an infinite-scroll helper; `CustomArticleCrawler` falls back to LangChain's `AsyncHtmlLoader` + `Html2TextTransformer` for arbitrary blogs/Substack. The chapter recommends [[Scrapy]] for production-grade general scraping and [[Crawl4AI]] for LLM-targeted crawling.

## Key details
- Three crawling regimes: raw HTTP (fast, fragile for JS-heavy sites), HTML-parsed (BeautifulSoup over rendered HTML, faster than browser but limited), full browser automation (Selenium / Playwright, slowest but handles modern SPAs).
- Login-gated sites (LinkedIn) require browser automation that simulates real user sessions.
- Infinite-feed scraping needs scroll automation with explicit termination (scroll-limit or scroll-height stability).
- Production stack alternatives: Scrapy (general), Crawl4AI (LLM-friendly), Playwright (modern browser automation).
- The book's architecture reduces crawled content to three platform-agnostic categories (article, post, repository) so new sources only require a new crawler.

## Connections
- [[ETL]] / [[DataCollectionPipeline]] — the pipeline web crawling participates in.
- [[Selenium]] / [[BeautifulSoup]] / [[ChromeDriver]] — the implementation stack.
- [[Scrapy]] / [[Crawl4AI]] — recommended production alternatives.
- [[BuilderPattern]] — used to wire per-platform crawlers into a dispatcher.
- [[LangChain]] — provides the `AsyncHtmlLoader` / `Html2TextTransformer` fallback.
- [[GitHub]] / [[LinkedIn]] / [[Medium]] / [[Substack]] — the four data sources crawled in the book.
