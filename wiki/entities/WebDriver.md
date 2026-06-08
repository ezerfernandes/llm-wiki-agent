---
title: "WebDriver"
type: entity
tags: [tool, protocol, browser-automation, testing, web, selenium]
sources: [fuzzingbook-28-gui-fuzzer]
last_updated: 2026-06-06
---

# WebDriver

**WebDriver** is the W3C-standardized interface (and protocol) for programmatically controlling a Web browser: launching it, navigating, querying the live page for UI elements, reading their attributes, and dispatching interactions (typing, clicking). It is the mechanism behind [[Selenium]] — a Selenium *web driver* object is the handle a program uses to drive a browser — and browser-specific *driver servers* implement it (e.g. [[ChromeDriver|`chromedriver`]] for Chrome, `geckodriver` for Firefox).

## From The Fuzzing Book — Testing Graphical User Interfaces
[[fuzzingbook-28-gui-fuzzer|Ch 28]] builds its [[GUIFuzzing|GUI fuzzer]] entirely on a WebDriver. `start_webdriver(browser, headless, zoom)` returns a *GUI driver* — a [[Selenium]] `webdriver.Firefox`/`webdriver.Chrome` running **headless** — which the chapter uses to: navigate (`driver.get(url)`, `driver.back()`), take screenshots (`get_screenshot_as_png()`), query elements (`find_element(By.NAME, ...)`, `find_elements(By.TAG_NAME, "a")`), read attributes (`get_attribute('href')`), and interact (`element.send_keys(...)`, `element.click()`). Crucially, the WebDriver queries the *running* browser rather than parsing served HTML, so it sees elements created or changed by JavaScript — the property that lets the chapter generalize past the HTTP/HTML approach of [[fuzzingbook-27-web-fuzzer|Ch 27]]. The driver is cleaned up with `driver.quit()`. Selenium WebDriver also has variants for non-Web UIs (e.g. Android apps), so the same model generalizes beyond the browser.

## Connections
- [[Selenium]] — the framework that exposes WebDriver to Python; provides the driver objects.
- [[ChromeDriver]] — a concrete WebDriver server (Chrome); Firefox's is `geckodriver`.
- [[GUIFuzzing]] / [[GUIFuzzer]] — Ch 28 drives the UI fuzzer through a WebDriver.
- [[UINavigationModel]] — built by querying the WebDriver for each page's interactive elements.
- [[WebCrawling]] — following links via the WebDriver to explore a whole site.
- [[AndreasZeller]] / [[CISPA]] — author and publisher of the chapter using it.
- [[fuzzingbook-28-gui-fuzzer]] — the chapter that relies on it.

## Sources
- [[fuzzingbook-28-gui-fuzzer]] — *The Fuzzing Book* Ch 28, "Testing Graphical User Interfaces."
