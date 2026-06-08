---
title: "Web Application Fuzzing"
type: concept
tags: [fuzzing, testing, security, web, http, grammar-mining, crawling, python]
sources: [fuzzingbook-27-web-fuzzer, fuzzingbook-28-gui-fuzzer]
last_updated: 2026-06-06
---

# Web Application Fuzzing

**Web application fuzzing** is the testing of a Web application over HTTP by sending generated requests — typically by filling and submitting its **forms** — to provoke failures and security vulnerabilities. Unlike fuzzing a single function or file, the target is a *running server* with a network protocol (HTTP), a user-facing surface described in HTML, and usually a back-end database; the fuzzer interacts with it the way a browser would. It is the entry point to *The Fuzzing Book*'s treatment of user-interface testing and a direct precursor to generic [[fuzzingbook-28-gui-fuzzer|GUI fuzzing]].

## From The Fuzzing Book — Testing Web Applications
[[fuzzingbook-27-web-fuzzer|Ch 27]] sets up a deliberately *vulnerable* shop server (a Fuzzingbook "swag" order form on Python's `http.server`, backed by a `sqlite3` `orders` table) and fuzzes it three increasingly automatic ways:

1. **Hand-written grammar** — an `ORDER_GRAMMAR` of order URLs ([[HTTPFuzzing|CGI-encoded `GET` requests]]) fed to a [[GrammarFuzzer|`GrammarFuzzer`]]; a [[MutationBasedFuzzing|`MutationFuzzer`]] seeded from it quickly triggers an internal-server-error page, minimized with [[fuzzingbook-16-reducer|Ch 16]] delta debugging via a `WebRunner` oracle.
2. **Mined grammar** — `HTMLGrammarMiner`/`FormHTMLParser` parse the served HTML form and *automatically* derive a grammar of valid submissions, so [[WebFormFuzzer|`WebFormFuzzer`]] can fuzz any form given only its URL ([[GrammarMining|grammar mining]] from a UI).
3. **Crawl + fuzz** — a `crawl()` generator ([[WebCrawler|crawler]], `robots.txt`-aware) discovers every form on a site, and each is fuzzed in turn.

The chapter then shows the same machinery as an *attack* platform — [[HTMLInjection]], [[CrossSiteScripting|XSS]], and [[SQLInjection]] — culminating in a `SQLInjectionFuzzer` that empties the database fully automatically from nothing but a URL. The defenses (escaping output, parameterized SQL, suppressing error detail) are collected under [[InputSanitization|input sanitization]].

## From The Fuzzing Book — Testing Graphical User Interfaces
[[fuzzingbook-28-gui-fuzzer|Ch 28]] generalizes this HTTP/HTML approach into generic [[GUIFuzzing|GUI fuzzing]]. Where Ch 27 parses *served HTML* and speaks HTTP, Ch 28 drives a *real browser* with [[Selenium]] ([[WebDriver|WebDriver]]) and *queries the running UI* for its interactive elements — so it survives JavaScript (which can change a page without changing its URL) and generalizes to non-Web UIs. It models the application as a [[FiniteStateMachine|finite state machine]] of pages ([[UINavigationModel|UI navigation model]]) embedded in a [[Grammar|grammar]] ([[ModelBasedTesting|model-based testing]]), explores it with [[GUIFuzzer|`GUIFuzzer`]], and covers every transition via [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]]. The two chapters reuse the same vulnerable shop server; Ch 28 is the more general (but experimental) successor for dynamic UIs.

## Connections
- [[GUIFuzzing]] / [[GUIFuzzer]] — the Ch 28 browser-driven generalization for dynamic/JavaScript UIs.
- [[WebFormFuzzer]] — the concrete one-URL fuzzer that mines a form grammar and fuzzes it.
- [[HTTPFuzzing]] — the request layer: CGI-encoded `GET` URLs and the `WebRunner` HTTP oracle.
- [[SQLInjection]] / [[CrossSiteScripting]] / [[HTMLInjection]] — the security failures this fuzzing surfaces.
- [[CodeInjection]] — the unifying root cause of those attacks.
- [[GrammarMining]] — mining the submission grammar from served HTML.
- [[GrammarFuzzer]] / [[Grammar]] — the engine and data structure that generate requests.
- [[MutationBasedFuzzing]] — mutating valid order URLs to find generic failures.
- [[WebCrawler]] / [[WebCrawling]] — discovering forms across a whole site.
- [[InputSanitization]] — the cross-cutting defense.
- [[Fuzzing]] — the parent discipline.
- [[fuzzingbook-28-gui-fuzzer|Ch 28]] — generalizes from HTML/Web to arbitrary GUIs.

## Sources
- [[fuzzingbook-27-web-fuzzer]] — *The Fuzzing Book* Ch 27, "Testing Web Applications."
- [[fuzzingbook-28-gui-fuzzer]] — *The Fuzzing Book* Ch 28, "Testing Graphical User Interfaces" (the browser-driven, JavaScript-tolerant generalization).
