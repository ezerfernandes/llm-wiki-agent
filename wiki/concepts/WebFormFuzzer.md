---
title: "WebFormFuzzer"
type: concept
tags: [fuzzing, testing, security, web, html, grammar-mining, grammar, python, class-hierarchy]
sources: [fuzzingbook-27-web-fuzzer]
last_updated: 2026-06-06
---

# WebFormFuzzer

**`WebFormFuzzer`** is *The Fuzzing Book*'s fuzzer for Web forms: given only a **URL**, it fetches the page's HTML, mines a [[Grammar|grammar]] of valid form submissions from it, and generates fuzzed submissions — no manual input model required. It is a subclass of [[GrammarFuzzer|`GrammarFuzzer`]] and the headline class of [[fuzzingbook-27-web-fuzzer|Ch 27]], the practical realization of [[WebApplicationFuzzing|Web-application fuzzing]].

## How it works
1. `get_html(url)` retrieves the page (`requests.get(url).text`).
2. `get_grammar(html_text)` delegates to a grammar-miner class (default `HTMLGrammarMiner`) whose `mine_grammar()` returns a [[Grammar|`Grammar`]].
3. The `GrammarFuzzer` superclass is initialized with that grammar, so `fuzz()` produces submission paths like `/order?item=lockset&name=%43+&...&submit=` — accessing the path is equivalent to filling out and submitting the form.

```python
web_form_fuzzer = WebFormFuzzer(httpd_url)
web_form_fuzzer.fuzz()
web_runner = WebRunner(httpd_url)
web_form_fuzzer.runs(web_runner, 10)   # run 10 fuzzed submissions
```

`HTMLGrammarMiner` (with its `FormHTMLParser`, built on the stdlib `html.parser.HTMLParser`) extracts the form's `action` and a `fields` map (input name → HTML type, or `<select>` name → option list), then extends a base `CGI_GRAMMAR`/`QUERY_GRAMMAR` (rules for `<text>`, `<number>`, `<email>`, `<checkbox>`, …) into a grammar producing valid URLs, dropping `unreachable_nonterminals()`. This is [[GrammarMining|grammar mining]] from a *user interface* rather than from program traces ([[fuzzingbook-18-grammar-miner|Ch 18]]).

## Limitations
Stated explicitly in the chapter: handles only **one form per page**, supports only **`GET`** actions (values encoded into the URL — no `POST`), and works on **HTML only** (no JavaScript / dynamic pages). `get_html()`/`get_grammar()` are overridable hooks — `SQLInjectionFuzzer` overrides `get_grammar()` to inject attacks.

## Connections
- [[GUIFuzzing]] / [[GUIFuzzer]] — [[fuzzingbook-28-gui-fuzzer|Ch 28]] generalizes this HTML-only fuzzer into a browser-driven GUI fuzzer that handles the JavaScript and `POST` cases listed under Limitations.
- [[WebApplicationFuzzing]] — the technique `WebFormFuzzer` embodies.
- [[GrammarFuzzer]] — its superclass; supplies the tree-based generation engine.
- [[GrammarMining]] — `HTMLGrammarMiner` mines the submission grammar from served HTML.
- [[Grammar]] — the mined `QUERY_GRAMMAR` it consumes.
- [[HTTPFuzzing]] — the `WebRunner` it pairs with to send requests and read HTTP status.
- [[SQLInjection]] — `SQLInjectionFuzzer` subclasses it, overriding `get_grammar()` with attack payloads.
- [[Parser]] — uses the stdlib `HTMLParser` instead of the book's own parser ([[fuzzingbook-12-parser|Ch 12]]).
- [[Fuzzing]] — the parent discipline.
- [[fuzzingbook-27-web-fuzzer]] — the chapter that introduces it.

## Sources
- [[fuzzingbook-27-web-fuzzer]] — *The Fuzzing Book* Ch 27, "Testing Web Applications."
