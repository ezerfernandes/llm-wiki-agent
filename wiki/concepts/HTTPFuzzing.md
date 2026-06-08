---
title: "HTTP Fuzzing"
type: concept
tags: [fuzzing, testing, web, http, protocol, cgi-encoding, python]
sources: [fuzzingbook-27-web-fuzzer]
last_updated: 2026-06-06
---

# HTTP Fuzzing

**HTTP fuzzing** is the construction and sending of HTTP requests as fuzzing inputs against a running Web server, and the interpretation of HTTP responses as a [[TestOracle|test oracle]]. For form-based applications the requests are typically `GET` URLs of the shape `<action>?field_1=value_1&field_2=value_2`, where values are **CGI-encoded** (spaces → `+`, other non-alphanumerics → `%nn` hex). It is the transport layer underneath [[WebApplicationFuzzing|Web-application fuzzing]].

## From The Fuzzing Book — Testing Web Applications
[[fuzzingbook-27-web-fuzzer|Ch 27]] treats a form submission as a CGI-encoded `GET` URL and provides `cgi_encode()` (the counterpart to `cgi_decode()` from [[fuzzingbook-04-coverage|Ch 4]]) so a [[Grammar|grammar]] can embed arbitrary strings — and, later, HTML/JS/SQL attack payloads — into URLs; a `do_not_encode` parameter preserves grammar metacharacters like `<>`. Requests are sent with the `requests` library (and a `webbrowser()` helper that also surfaces server log messages from a `multiprocess` queue). The HTTP **status code** is the oracle: a `WebRunner` (a subclass of the book's `Runner`, [[fuzzingbook-03-fuzzer|Ch 3]]) maps `200 OK` → `PASS`, `500 Internal Server Error` → `FAIL`, and anything else → `UNRESOLVED`, which lets a fuzzer detect crashes and lets the [[fuzzingbook-16-reducer|`DeltaDebuggingReducer`]] minimize a failing path. The chapter notes the response can also leak internals (tracebacks, schema) — itself an attack surface.

## Connections
- [[WebApplicationFuzzing]] — HTTP fuzzing is its transport/oracle layer.
- [[WebFormFuzzer]] — pairs with a `WebRunner` to send mined-grammar submissions over HTTP.
- [[Grammar]] / [[GrammarFuzzer]] — generate the request URLs (CGI-encoded with `cgi_encode()`).
- [[TestOracle]] — the HTTP status code is the pass/fail signal.
- [[SQLInjection]] / [[CrossSiteScripting]] — payloads carried inside CGI-encoded request fields.
- [[Fuzzing]] — the parent discipline; `WebRunner` extends the book's `Runner`.
- [[fuzzingbook-27-web-fuzzer]] — the chapter that introduces it.

## Sources
- [[fuzzingbook-27-web-fuzzer]] — *The Fuzzing Book* Ch 27, "Testing Web Applications."
