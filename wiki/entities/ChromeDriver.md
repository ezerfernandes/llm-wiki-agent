---
title: "ChromeDriver"
type: entity
tags: [tool, browser-automation, web-scraping, google]
sources: [leh-ch03-data-engineering, fuzzingbook-28-gui-fuzzer]
last_updated: 2026-06-06
---

## What it is
ChromeDriver is the WebDriver server for Google Chrome that lets Selenium scripts drive the browser headlessly or interactively. The `chromedriver_autoinstaller` Python package downloads a ChromeDriver binary matching the host's Chrome version.

## In LLM Engineer's Handbook
Ch. 3 ([[leh-ch03-data-engineering]]) uses `chromedriver_autoinstaller.install()` inside `BaseSeleniumCrawler.__init__()` so the [[Selenium]]-driven Medium and LinkedIn crawlers work out of the box. The chapter flags ChromeDriver version mismatches as a common failure mode and offers a workaround: comment out Medium URLs in the YAML configs so the LangChain-based `CustomArticleCrawler` handles all article scraping instead.

## From The Fuzzing Book — Testing Graphical User Interfaces
[[fuzzingbook-28-gui-fuzzer|Ch 28]] uses ChromeDriver as one of two supported [[WebDriver|WebDriver]] servers (alongside Firefox's `geckodriver`) for its [[GUIFuzzing|GUI fuzzer]]. `start_webdriver(browser='chrome', headless=True)` constructs a `webdriver.Chrome` with `--headless=new`, asserting `chromedriver` is on the path; the chapter then drives the headless Chrome via [[Selenium]] to discover and activate UI elements and build a [[UINavigationModel|UI navigation model]].

## Connections
- [[Selenium]] — driver client.
- [[WebDriver]] — the interface ChromeDriver implements for Chrome.
- [[BeautifulSoup]] — pairs to parse Selenium's output.
- [[google]] — publisher of Chrome / ChromeDriver.
- [[GUIFuzzing]] / [[GUIFuzzer]] — Ch 28 drives headless Chrome via ChromeDriver.
- [[WebCrawling]] — domain.
- [[Docker]] — the chapter installs Chrome inside the Dockerfile for the same purpose.

## Sources
- [[leh-ch03-data-engineering]] — *LLM Engineer's Handbook* Ch 3 (ChromeDriver auto-install for crawlers).
- [[fuzzingbook-28-gui-fuzzer]] — *The Fuzzing Book* Ch 28, "Testing Graphical User Interfaces" (headless Chrome as a GUI-fuzzing driver).
