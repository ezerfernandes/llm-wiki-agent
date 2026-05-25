---
title: "Selenium"
type: entity
tags: [tool, library, browser-automation, web-scraping, open-source]
sources: [leh-ch03-data-engineering]
last_updated: 2026-05-22
---

## What it is
Selenium is the dominant browser-automation framework — a WebDriver protocol implementation that drives real browsers (Chrome, Firefox, Edge) for testing or scraping. The Python binding is `selenium`.

## In LLM Engineer's Handbook
Ch. 3 ([[leh-ch03-data-engineering]]) wraps Selenium in a reusable `BaseSeleniumCrawler` (extending `BaseCrawler`) that configures headless Chrome via `chromedriver_autoinstaller`, exposes `scroll_page()` for infinite-feed scraping, and hooks for `login()` and `set_extra_driver_options()`. The `MediumCrawler` and `LinkedInCrawler` subclass it to log in, scroll, and yield raw HTML, which is then parsed with [[BeautifulSoup]]. The chapter notes that ChromeDriver mismatches are the most common failure mode for these crawlers.

## Connections
- [[BeautifulSoup]] — pairs with Selenium for parsing.
- [[ChromeDriver]] — the binary Selenium drives.
- [[WebCrawling]] — domain.
- [[Scrapy]] / [[Crawl4AI]] — alternative crawlers.
- [[LinkedIn]] / [[Medium]] — sites the book scrapes with Selenium.
