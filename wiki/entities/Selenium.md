---
title: "Selenium"
type: entity
tags: [tool, library, browser-automation, web-scraping, open-source]
sources: [leh-ch03-data-engineering, fuzzingbook-28-gui-fuzzer, fuzzingbook-29-fuzzing-in-the-large]
last_updated: 2026-06-06
---

## What it is
Selenium is the dominant browser-automation framework — a WebDriver protocol implementation that drives real browsers (Chrome, Firefox, Edge) for testing or scraping. The Python binding is `selenium`.

## In LLM Engineer's Handbook
Ch. 3 ([[leh-ch03-data-engineering]]) wraps Selenium in a reusable `BaseSeleniumCrawler` (extending `BaseCrawler`) that configures headless Chrome via `chromedriver_autoinstaller`, exposes `scroll_page()` for infinite-feed scraping, and hooks for `login()` and `set_extra_driver_options()`. The `MediumCrawler` and `LinkedInCrawler` subclass it to log in, scroll, and yield raw HTML, which is then parsed with [[BeautifulSoup]]. The chapter notes that ChromeDriver mismatches are the most common failure mode for these crawlers.

## From The Fuzzing Book — Testing Graphical User Interfaces
[[fuzzingbook-28-gui-fuzzer|Ch 28]] uses Selenium as the foundation of generic [[GUIFuzzing|GUI fuzzing]]: `start_webdriver()` launches a *headless* Firefox (`geckodriver`) or Chrome ([[ChromeDriver|`chromedriver`]]) and returns a Selenium [[WebDriver|web driver]] the fuzzer drives. The chapter highlights that Selenium queries the *running* browser for its interactive elements (`find_element(By.NAME, ...)`, `find_elements(By.TAG_NAME, "a")`, `send_keys()`, `click()`) rather than parsing served HTML, so it survives JavaScript — and that Selenium has variants (e.g. Android) that generalize the approach to mobile apps. A [[Runner|`GUIRunner`]] executes the fuzzer's `fill`/`check`/`submit`/`click` action strings via Selenium, and a [[GUIFuzzer|`GUIGrammarMiner`]] mines a [[UINavigationModel|UI navigation model]] from what Selenium reports. The chapter also shows hand-written *Selenium tests* (the manual baseline its fuzzer automates).

## From The Fuzzing Book — Fuzzing in the Large
[[fuzzingbook-29-fuzzing-in-the-large|Ch 29]] reuses Ch 28's `start_webdriver()` to drive [[FuzzManager]]'s **Web UI** programmatically inside the notebook — logging in as `demo` (`find_element(By.NAME, "username")`/`send_keys`/`click`), navigating the crashes list, creating a [[CrashDeduplication|crash bucket]], and viewing coverage pages — so the crash-management workflow can be demonstrated end-to-end without manual clicking.

## Connections
- [[FuzzManager]] — Ch 29 drives its Web UI via Selenium to demonstrate crash bucketing/coverage.
- [[BeautifulSoup]] — pairs with Selenium for parsing.
- [[ChromeDriver]] — the binary Selenium drives.
- [[WebDriver]] — the interface/protocol Selenium implements to control the browser.
- [[GUIFuzzing]] / [[GUIFuzzer]] — Ch 28 builds its GUI fuzzer on Selenium.
- [[UINavigationModel]] / [[ModelBasedTesting]] — the UI model mined via Selenium queries.
- [[WebCrawling]] — domain.
- [[Scrapy]] / [[Crawl4AI]] — alternative crawlers.
- [[LinkedIn]] / [[Medium]] — sites the book scrapes with Selenium.

## Sources
- [[leh-ch03-data-engineering]] — *LLM Engineer's Handbook* Ch 3 (Selenium for crawling/scraping).
- [[fuzzingbook-28-gui-fuzzer]] — *The Fuzzing Book* Ch 28, "Testing Graphical User Interfaces" (Selenium as the GUI-fuzzing driver).
- [[fuzzingbook-29-fuzzing-in-the-large]] — *The Fuzzing Book* Ch 29, "Fuzzing in the Large" (Selenium drives the FuzzManager Web UI to demonstrate crash submission, bucketing, and coverage).
