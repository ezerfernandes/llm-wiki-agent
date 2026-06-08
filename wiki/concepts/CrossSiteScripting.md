---
title: "Cross-Site Scripting"
type: concept
tags: [security, vulnerability, injection, xss, javascript, web, fuzzing]
sources: [fuzzingbook-27-web-fuzzer]
last_updated: 2026-06-06
---

# Cross-Site Scripting

**Cross-site scripting (XSS)** is a Web vulnerability in which an attacker injects JavaScript into a page that another user's browser then executes. Because injected script runs in the *origin* of the containing page, it executes with the trust of the vulnerable application — it can read page content, exfiltrate **session cookies**, run a keylogger, or act on the user's behalf. XSS is a special case of [[HTMLInjection|HTML injection]] (you inject `<script>` as part of injected HTML), and both are instances of [[CodeInjection|code injection]] against the browser's HTML/JS interpreter. As of the chapter's cited 2012 figures, XSS and [[SQLInjection|SQL injection]] together made up more than half of Web-application vulnerabilities.

## From The Fuzzing Book — Testing Web Applications
[[fuzzingbook-27-web-fuzzer|Ch 27]]'s server reflects (and stores) the `name` field unescaped, so an order with `name = Jane Doe<script>document.title = document.cookie.substring(0, 10);</script>` causes the browser to execute the script whenever the confirmation page is shown — in the demo, leaking the first ten characters of the Jupyter session cookie into the page title. The chapter stresses the **persistent** danger: because the payload is stored, it runs every time the order is later displayed (e.g. to an operator reviewing orders), and a real script could silently ship the cookie to a remote server to hijack the session. HTML injection is the milder variant — embedding a malicious link that looks trusted because it originates from the legitimate site. The fix (Exercise 1, Part 2) is to pass all displayed values through Python's `html.escape()`, encoding `<`, `&`, `>` so the input can no longer be parsed as HTML or script ([[InputSanitization|input sanitization]]).

## Connections
- [[HTMLInjection]] — XSS is its script-carrying special case; both reflect/persist unescaped input.
- [[CodeInjection]] — the unifying root cause (untrusted input run as code by a trusted interpreter).
- [[SQLInjection]] — the database-targeting sibling attack in the same chapter.
- [[WebApplicationFuzzing]] / [[WebFormFuzzer]] — the fuzzing context that injects the payload via form fields.
- [[InputSanitization]] — `html.escape()` on output, the defense.
- [[InformationFlow]] / [[DynamicTaintAnalysis]] — [[fuzzingbook-19-information-flow|Ch 19]]'s principled defense against such injections.
- [[fuzzingbook-27-web-fuzzer]] — the chapter demonstrating the attack.

## Sources
- [[fuzzingbook-27-web-fuzzer]] — *The Fuzzing Book* Ch 27, "Testing Web Applications."
