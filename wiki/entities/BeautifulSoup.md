---
title: "BeautifulSoup"
type: entity
tags: [tool, library, python, web-scraping, html, open-source]
sources: [leh-ch03-data-engineering]
last_updated: 2026-05-22
---

## What it is
BeautifulSoup (`bs4`) is a Python library for parsing HTML and XML documents into a navigable tree, with selectors that mirror DOM access patterns. It is the de-facto standard for HTML scraping in Python alongside `lxml`.

## In LLM Engineer's Handbook
Ch. 3 ([[leh-ch03-data-engineering]]) uses BeautifulSoup inside the `MediumCrawler` (which inherits `BaseSeleniumCrawler`) to parse `self.driver.page_source` after [[Selenium]] finishes scrolling: `BeautifulSoup(page_source, "html.parser")`, then `soup.find_all("h1", class_="pw-post-title")` and `soup.find_all("h2", class_="pw-subtitle-paragraph")` extract Medium article titles and subtitles.

## Connections
- [[Selenium]] — produces the raw HTML BeautifulSoup parses.
- [[WebCrawling]] — domain BeautifulSoup serves.
- [[ChromeDriver]] — driver Selenium uses to fetch the page.
- [[Scrapy]] / [[Crawl4AI]] — alternative production crawlers the authors recommend.
- [[Python]] — language.
