---
title: "ChromeDriver"
type: entity
tags: [tool, browser-automation, web-scraping, google]
sources: [leh-ch03-data-engineering]
last_updated: 2026-05-22
---

## What it is
ChromeDriver is the WebDriver server for Google Chrome that lets Selenium scripts drive the browser headlessly or interactively. The `chromedriver_autoinstaller` Python package downloads a ChromeDriver binary matching the host's Chrome version.

## In LLM Engineer's Handbook
Ch. 3 ([[leh-ch03-data-engineering]]) uses `chromedriver_autoinstaller.install()` inside `BaseSeleniumCrawler.__init__()` so the [[Selenium]]-driven Medium and LinkedIn crawlers work out of the box. The chapter flags ChromeDriver version mismatches as a common failure mode and offers a workaround: comment out Medium URLs in the YAML configs so the LangChain-based `CustomArticleCrawler` handles all article scraping instead.

## Connections
- [[Selenium]] — driver client.
- [[BeautifulSoup]] — pairs to parse Selenium's output.
- [[google]] — publisher of Chrome / ChromeDriver.
- [[WebCrawling]] — domain.
- [[Docker]] — the chapter installs Chrome inside the Dockerfile for the same purpose.
