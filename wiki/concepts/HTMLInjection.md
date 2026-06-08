---
title: "HTML Injection"
type: concept
tags: [security, vulnerability, injection, html, web, fuzzing]
sources: [fuzzingbook-27-web-fuzzer]
last_updated: 2026-06-06
---

# HTML Injection

**HTML injection** is a Web vulnerability in which untrusted input is rendered back to users *as HTML* rather than as plain text. An attacker can embed markup — most simply a link to a malicious site — that appears to originate from the trusted application. If the injected HTML is also **stored** (e.g. in a database), it becomes a *persistent* attack: the attacker need not lure victims to a crafted page, because the payload re-renders whenever the data is later displayed. HTML injection is an instance of [[CodeInjection|code injection]] against the browser's HTML interpreter, and [[CrossSiteScripting|cross-site scripting (XSS)]] is its more dangerous form (injecting executable `<script>` rather than passive markup).

## From The Fuzzing Book — Testing Web Applications
[[fuzzingbook-27-web-fuzzer|Ch 27]] demonstrates HTML injection by setting the order form's `name` field to text containing a `<strong><a href="www.lots.of.malware">…</a></strong>` link. The server reflects it unescaped into the confirmation page *and* stores it in the `orders` database — so anyone later querying the orders (e.g. an operator) also sees the malicious link, multiplying its impact until the entry is deleted. The fix (Exercise 1, Part 2) is to pass all displayed values through Python's `html.escape()` before output ([[InputSanitization|input sanitization]]).

## Connections
- [[CrossSiteScripting]] — the executable-script variant of the same reflect-and-persist flaw.
- [[CodeInjection]] — the unifying root cause.
- [[SQLInjection]] — the database-targeting sibling attack in the same chapter.
- [[WebApplicationFuzzing]] / [[WebFormFuzzer]] — the fuzzing context that injects via form fields.
- [[InputSanitization]] — `html.escape()` on output, the defense.
- [[fuzzingbook-27-web-fuzzer]] — the chapter demonstrating the attack.

## Sources
- [[fuzzingbook-27-web-fuzzer]] — *The Fuzzing Book* Ch 27, "Testing Web Applications."
