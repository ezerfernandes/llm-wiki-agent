---
title: "Input Sanitization"
type: concept
tags: [security, defense, injection, escaping, validation, web]
sources: [fuzzingbook-27-web-fuzzer]
last_updated: 2026-06-06
---

# Input Sanitization

**Input sanitization** is the practice of treating third-party input so that no part of it can be (mis)interpreted as code by a downstream interpreter — the standard defense against [[CodeInjection|injection]] attacks. It takes two complementary forms: **escaping/quoting** input before it crosses into an interpreter (HTML-escaping output, using parameterized SQL), and **validating** input against expectations (whitelisting allowed values, requiring fields) before processing. The principle is that input must reach a dangerous *sink* only as data, never as commands — the same source→sink discipline enforced by [[InformationFlow|information-flow]] / [[DynamicTaintAnalysis|taint]] tracking.

## From The Fuzzing Book — Testing Web Applications
[[fuzzingbook-27-web-fuzzer|Ch 27]] motivates sanitization by breaking a server that omits it, then fixes it in Exercise 1's `BetterHTTPRequestHandler`:

- **HTML/XSS** — pass every displayed value through Python's `html.escape()` (encoding `<`, `&`, `>`) so it cannot be parsed as HTML or `<script>`; defeats [[HTMLInjection]] and [[CrossSiteScripting|XSS]].
- **SQL** — use **parameterized queries** (`db.execute("INSERT ... VALUES (?, ?, ?, ?, ?)", (...))`) and `execute()` rather than `executescript()`, so values can never be parsed as SQL; defeats [[SQLInjection]].
- **Robustness/leakage** — validate that required fields are present (return to the form otherwise), and suppress tracebacks/error status codes so failures don't leak schema or internals.

The chapter's summary distills this to: *"Consequent sanitizing of inputs prevents common attacks such as code and SQL injection."* Exercise 2 explores the alternative of an external blacklist/whitelist filter (the whitelist built with a [[Parser|parser]] and a dedicated [[Grammar|grammar]]) when the server code cannot be changed.

## Connections
- [[CodeInjection]] — the attack class sanitization defends against.
- [[SQLInjection]] / [[CrossSiteScripting]] / [[HTMLInjection]] — the specific attacks neutralized by escaping/parameterization.
- [[WebApplicationFuzzing]] — the chapter's vulnerable-server context.
- [[InformationFlow]] / [[DynamicTaintAnalysis]] — the principled source→sink view of sanitizing ([[fuzzingbook-19-information-flow|Ch 19]]).
- [[Parser]] / [[Grammar]] — used to build a whitelisting filter (Ch 27 Exercise 2).
- [[fuzzingbook-27-web-fuzzer]] — the chapter that presents the defenses.

## Sources
- [[fuzzingbook-27-web-fuzzer]] — *The Fuzzing Book* Ch 27, "Testing Web Applications."
