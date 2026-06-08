---
title: "The Fuzzing Book Ch 27 — Testing Web Applications"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, web, http, sql-injection, xss, grammar-mining, crawling]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-27-web-fuzzer.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# Testing Web Applications

## Summary
Chapter 27 opens the book's domain-specific Part V move toward *user interfaces* by targeting **Web applications over HTTP** ([[WebApplicationFuzzing|Web-application fuzzing]]). It builds a small, deliberately *vulnerable* shop server on Python's `http.server` (a "Fuzzingbook Swag" order form backed by a `sqlite3` `orders` database), then drives it three ways: with a hand-written [[Grammar|`Grammar`]] of order URLs, with a [[MutationBasedFuzzing|mutation fuzzer]] that quickly triggers an internal server error (minimized via [[fuzzingbook-16-reducer|Ch 16]] delta debugging), and — the chapter's central technique — with a grammar **mined automatically from the served HTML form** ([[WebFormFuzzer|`WebFormFuzzer`]] / `HTMLGrammarMiner`). The same machinery is then weaponized: by injecting HTML, JavaScript, and SQL into form fields it demonstrates [[HTMLInjection|HTML injection]], [[CrossSiteScripting|cross-site scripting (XSS)]], and [[SQLInjection|SQL injection]], and a `SQLInjectionFuzzer` performs the attack *fully automatically* from nothing but a URL. It reuses the grammar machinery of [[fuzzingbook-09-grammars|Ch 9]]/[[fuzzingbook-10-grammar-fuzzer|Ch 10]] and the grammar-mining idea of [[fuzzingbook-18-grammar-miner|Ch 18]], and leads directly into generic [[fuzzingbook-28-gui-fuzzer|GUI fuzzing (Ch 28)]].

## Key Concepts
- **A vulnerable Web server (`SimpleHTTPRequestHandler`)** — a `BaseHTTPRequestHandler` subclass whose `do_GET()` routes `/` to an order form, `/order?...` to order handling, `/terms` to terms, and everything else to a `Page Not Found`. Orders are stored by string-formatting field values into an `INSERT INTO orders VALUES ('{item}', '{name}', ...)` SQL command and running it with `db.executescript()` — the root cause of every vulnerability in the chapter. It runs in a separate process (`multiprocess`) and ships log messages back over an `HTTPD_MESSAGE_QUEUE`.
- **HTTP request grammar / CGI encoding** ([[HTTPFuzzing]]) — form submissions are `GET` requests of the form `<action>?field_1=value_1&field_2=value_2`, with values **CGI-encoded** (spaces → `+`, other non-alphanumerics → `%nn`). `cgi_encode()` (counterpart to `cgi_decode()` from [[fuzzingbook-04-coverage|Ch 4]]) lets the grammar embed arbitrary strings into URLs, with a `do_not_encode` parameter to preserve grammar metacharacters.
- **Hand-written `ORDER_GRAMMAR`** — a [[Grammar|`Grammar`]] producing valid order URLs (items, sample names/emails/cities, 5-digit zips), fed to a [[GrammarFuzzer|`GrammarFuzzer`]]. A [[MutationBasedFuzzing|`MutationFuzzer`]] seeded from it perturbs field values, names, and URL structure until an internal-server-error page appears; a `WebRunner` (subclass of `Runner`) maps HTTP status to `PASS`/`FAIL`/`UNRESOLVED` so the [[fuzzingbook-16-reducer|`DeltaDebuggingReducer`]] can minimize the failing path (missing required fields).
- **`HTMLGrammarMiner` / `FormHTMLParser`** ([[WebFormFuzzer]]) — parses served HTML with the stdlib `html.parser.HTMLParser`, collecting the form's `action` and a `fields` map (input name → HTML type, or `<select>` → option list). `mine_grammar()` extends a base `CGI_GRAMMAR`/`QUERY_GRAMMAR` (rules per HTML input type: `<text>`, `<number>`, `<email>`, `<checkbox>`, …) into a grammar that produces valid submission URLs, pruning `unreachable_nonterminals()`. This is [[GrammarMining|grammar mining]] from a *user interface* rather than from program traces.
- **`WebFormFuzzer`** — a [[GrammarFuzzer|`GrammarFuzzer`]] subclass that, given only a URL, fetches the HTML (`get_html()`), mines the grammar (`get_grammar()`), and fuzzes the form. Limitations: one form per page, `GET` only (no `POST`), HTML only (no JavaScript).
- **A crawler (`crawl()` / `LinkHTMLParser`)** ([[WebCrawler]]) — a generator that BFS-walks `<a href>` links from a start page, respecting `robots.txt` (`urllib.robotparser`), staying on the same host by default, capped by `max_pages`. Combined with `WebFormFuzzer`, it fuzzes every form discovered on a site.
- **Web attacks** — [[HTMLInjection|HTML injection]] (a malicious link embedded in the `name` field is reflected *and persisted* in the database), [[CrossSiteScripting|XSS]] (an injected `<script>` runs in the page's origin and can steal session cookies), and [[SQLInjection|SQL injection]] (a `name` value like `Jane', 'x','x','x'); DELETE FROM orders; --` turns the `INSERT` into an arbitrary command — the canonical XKCD #327 "Little Bobby Tables" bug). The server also *leaks* its schema via tracebacks in error pages.
- **`SQLInjectionGrammarMiner` / `SQLInjectionFuzzer`** — extend `HTMLGrammarMiner` with an `ATTACKS` list of common SQL-injection schemes and a caller-supplied `sql_payload`, mining a grammar that tries injection in *every* field. `SQLInjectionFuzzer(url, "DELETE FROM orders")` empties the orders table in under a second, fully automatically.
- **Defenses (exercises)** — `BetterHTTPRequestHandler`: suppress tracebacks/error status codes, `html.escape()` all displayed values (stops HTML/XSS), use **parameterized SQL** (`execute("INSERT ... VALUES (?,?,?,?,?)", (...))` instead of `executescript()`), and validate required fields. The remedy across all three attacks is **input sanitization** — quoting/escaping so no input is interpretable as HTML, JavaScript, or SQL.

## Key Claims
- Web user interfaces can be fuzzed by *mining a grammar directly from the served HTML form* — no manual input model is needed; `WebFormFuzzer` needs only a URL.
- The entire pipeline — crawl a site for forms, parse each form's fields and value sets, then inject HTML/JS/SQL into every field — can run fully automatically; `SQLInjectionFuzzer` empties a database in well under a second from just the URL.
- All three classic Web attacks share one root cause: untrusted input crossing into a trusted interpreter (the browser's HTML/JS engine, or the database's SQL parser) as code rather than data (a [[CodeInjection|code-injection]] vulnerability).
- HTML/XSS injection becomes a *persistent* attack once the malicious payload is stored, multiplying its impact whenever the data is later displayed (e.g. to an operator reviewing orders).
- Verbose error pages leak schema/internal details (the `information_schema` data dictionary on real DBs), so even "insider knowledge" needed for SQL injection is often handed to the attacker.
- The correct defenses are concrete and cheap: `html.escape()` for output, *parameterized queries* for SQL, suppressing internal error detail, and validating inputs — but rolling your own Web server invites exactly these mistakes.
- As of the chapter's cited 2012 figures, XSS and SQL injection together accounted for more than 50% of Web-application vulnerabilities.

## Key Quotes
> "Do not attempt to write a Web server yourself, as you are likely to repeat all the mistakes of others." — Lessons Learned

> "We can crawl the Web pages of a host for possible forms, automatically identify form fields and possible values, inject SQL (or HTML, or JavaScript) into any of these fields — and all of this fully automatically, not needing anything but the URL of the site." — Fully Automatic Web Attacks

> "The best way to avoid information leakage through failures is of course not to fail in the first place. But if you fail, make it hard for the attacker to establish a link between the attack and the failure." — Leaking Internal Information

## Connections
- [[WebApplicationFuzzing]] — the chapter's overarching technique: testing Web apps over HTTP with generated requests.
- [[WebFormFuzzer]] — the headline class: mines a grammar from a served HTML form and fuzzes it.
- [[HTTPFuzzing]] — encoding form submissions as CGI-encoded `GET` URLs; the `WebRunner` HTTP oracle.
- [[SQLInjection]] / [[CrossSiteScripting]] / [[HTMLInjection]] — the three attacks demonstrated, and the automatic `SQLInjectionFuzzer`.
- [[CodeInjection]] — the unifying root cause; the chapter is referenced from Ch 19's information-flow treatment of the same `eval`/SQL danger.
- [[GrammarMining]] — `HTMLGrammarMiner` mines a grammar from a UI (a fourth sense alongside Ch 13/18/23 mining).
- [[GrammarFuzzer]] — `WebFormFuzzer` subclasses it; the order grammar is fuzzed with it.
- [[Grammar]] — the `ORDER_GRAMMAR` / `CGI_GRAMMAR` / mined `QUERY_GRAMMAR` data structure ([[fuzzingbook-09-grammars|Ch 9]]).
- [[MutationBasedFuzzing]] — the `MutationFuzzer` that finds the internal-error page from a grammar seed.
- [[WebCrawler]] / [[WebCrawling]] / [[WebScraping]] — `crawl()` discovers forms across a site (here for testing, not indexing/ETL).
- [[Parser]] — the chapter parses HTML with the stdlib `HTMLParser` rather than the book's own parser ([[fuzzingbook-12-parser|Ch 12]]).
- [[InputSanitization]] — the cross-cutting defense (escaping, parameterized SQL).
- [[InformationFlow]] / [[DynamicTaintAnalysis]] — Ch 19's principled defense for the same injection danger.
- [[AndreasZeller]] / [[CISPA]] — author and publisher.
- [[OWASP]] — the chapter's Background points to OWASP's ZAP security scanner and Web-application-security material.
- [[fuzzingbook-18-grammar-miner|Ch 18]] — mining grammars from program traces; Ch 27 mines them from HTML forms instead.
- [[fuzzingbook-28-gui-fuzzer|Ch 28]] — the next step: generic GUI fuzzing (JavaScript/mobile) beyond HTML forms.
- [[fuzzingbook-19-information-flow|Ch 19]] — the chapter cited as the principled way to detect/prevent the injection leaks shown here.

## Contradictions
- None identified.
