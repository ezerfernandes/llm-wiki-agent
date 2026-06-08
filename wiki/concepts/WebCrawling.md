---
title: "Web Crawling"
type: concept
tags: [data-engineering, etl, scraping, fuzzing, testing, security]
sources: [leh-ch03-data-engineering, fuzzingbook-27-web-fuzzer, fuzzingbook-28-gui-fuzzer]
last_updated: 2026-06-06
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

## From The Fuzzing Book — Testing Web Applications
[[fuzzingbook-27-web-fuzzer|Ch 27]] uses crawling not for data collection but as a discovery step in [[WebApplicationFuzzing|Web-application fuzzing]]: a `crawl()` generator (with a `LinkHTMLParser` over the stdlib `html.parser.HTMLParser`) does a breadth-first walk of `<a href>` links from a start page, staying on the same host by default, capping at `max_pages`, and respecting `robots.txt` via `urllib.robotparser`. Each discovered page with a form is then fuzzed by a [[WebFormFuzzer|`WebFormFuzzer`]] — so the crawler turns a single seed URL into full-site automatic testing (and, with `SQLInjectionFuzzer`, full-site attack). It is a lightweight, raw-HTTP crawler (no browser automation), since the chapter's targets are static HTML forms.

## From The Fuzzing Book — Testing Graphical User Interfaces
[[fuzzingbook-28-gui-fuzzer|Ch 28]] crawls a site the *browser-automation* way: its [[GUIFuzzer|`GUICoverageFuzzer`]] explores a whole UI by following links and submitting forms through a real [[Selenium]] browser (`follow_link()` keeps it on-host), building a [[UINavigationModel|UI navigation model]] of pages and transitions ([[GUIFuzzing|GUI fuzzing]]). Unlike Ch 27's lightweight raw-HTTP `crawl()`, this regime renders JavaScript and explores *deep* states reachable only by filling forms — and it scales to nontrivial sites (the chapter crawls fuzzingbook.org), converging toward roughly one state per page.

## Connections
- [[GUIFuzzing]] / [[GUIFuzzer]] / [[UINavigationModel]] — Ch 28 crawls a UI through a browser to build a navigation model.
- [[WebApplicationFuzzing]] / [[WebFormFuzzer]] — Ch 27 crawls a site to discover and fuzz every form.
- [[WebCrawler]] / [[WebScraping]] — the crawler/scraper concepts this overlaps.
- [[ETL]] / [[DataCollectionPipeline]] — the pipeline web crawling participates in.
- [[Selenium]] / [[BeautifulSoup]] / [[ChromeDriver]] — the implementation stack.
- [[Scrapy]] / [[Crawl4AI]] — recommended production alternatives.
- [[BuilderPattern]] — used to wire per-platform crawlers into a dispatcher.
- [[LangChain]] — provides the `AsyncHtmlLoader` / `Html2TextTransformer` fallback.
- [[GitHub]] / [[LinkedIn]] / [[Medium]] / [[Substack]] — the four data sources crawled in the book.

## Sources
- [[leh-ch03-data-engineering]] — *LLM Engineer's Handbook* Ch 3, "Data Engineering" (production crawling pipeline).
- [[fuzzingbook-27-web-fuzzer]] — *The Fuzzing Book* Ch 27, "Testing Web Applications" (crawling to discover forms for fuzzing).
- [[fuzzingbook-28-gui-fuzzer]] — *The Fuzzing Book* Ch 28, "Testing Graphical User Interfaces" (browser-automation crawling to build a UI navigation model).
