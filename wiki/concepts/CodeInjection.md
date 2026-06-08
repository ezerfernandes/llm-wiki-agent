---
title: "Code Injection"
type: concept
tags: [security, vulnerability, injection, information-flow, taint-analysis, fuzzing, sql-injection]
sources: [fuzzingbook-19-information-flow, fuzzingbook-27-web-fuzzer]
last_updated: 2026-06-06
---

# Code Injection

**Code injection** is a vulnerability in which untrusted input crosses into a *trusted* execution context and is interpreted as code rather than data — letting an attacker run commands of their choosing. SQL injection, OS-command injection, and the abuse of language `eval()`/`exec()` are all instances. The defense is to keep untrusted input from reaching the dangerous *sink* unsanitized — exactly the property [[InformationFlow|information-flow]] / [[DynamicTaintAnalysis|taint]] tracking is designed to enforce: untrusted *sources* taint input, the sink checks the taint, and only a *sanitizer* may clear it.

## From The Fuzzing Book — Tracking Information Flow
[[fuzzingbook-19-information-flow|Ch 19]] motivates taint analysis with a stark code-injection example. Its in-memory SQL database evaluates `where`/`select` expressions with Python's `eval()` for convenience, which means a query like `select __import__("os").popen("pwd").read() from inventory` executes arbitrary Python — "the full power of Python expressions turns back on us." Ordinary fuzzing does not surface this because no *crash* occurs. The chapter's fix is information flow: `TrustedDB.sql()` accepts only strings tainted `TRUSTED`, `sanitize()` whitelists a safe character set via regex and re-taints sanitized input as `TRUSTED`, and `TaintedDB.my_eval()` raises a `Tainted` exception if a non-`TRUSTED` string ever reaches the `eval` sink. This is presented as the same defense used against the SQL/code injections discussed in the Web Fuzzing chapter, and as the target that [[TaintDirectedFuzzing|taint-directed fuzzing]] is steered toward.

## From The Fuzzing Book — Testing Web Applications
[[fuzzingbook-27-web-fuzzer|Ch 27]] is where the book *attacks* a real interpreter chain with code injection. Its vulnerable shop server builds SQL by string-formatting form values into `INSERT INTO orders VALUES ('{name}', ...)` and reflects them unescaped into HTML, so it is simultaneously vulnerable to [[SQLInjection|SQL injection]] (a `name` like `Jane', 'x','x','x'); DELETE FROM orders; --` runs an arbitrary command), [[HTMLInjection|HTML injection]], and [[CrossSiteScripting|XSS]] — three faces of one root cause: untrusted input crossing into a trusted interpreter (the SQL parser, the browser's HTML/JS engine) as code. A `SQLInjectionFuzzer` automates the attack from just a URL. The chapter's defense is [[InputSanitization|input sanitization]] (escaping output, parameterized SQL), which is the practical counterpart to Ch 19's information-flow discipline.

## Connections
- [[SQLInjection]] / [[CrossSiteScripting]] / [[HTMLInjection]] — the three Web-injection instances demonstrated in Ch 27.
- [[InputSanitization]] — the escaping/parameterization defense (Ch 27).
- [[InformationFlow]] / [[DynamicTaintAnalysis]] — the source→sink discipline that prevents injection.
- [[TaintedString]] — `tstr` taints (`TRUSTED`/`UNTRUSTED`) gate the `eval` sink in Ch 19.
- [[TaintDirectedFuzzing]] — fuzzing directed at reaching the injectable `eval` sink.
- [[Fuzzing]] — injection bugs are crash-free, so they need a stronger oracle than fuzzing's default.
- [[fuzzingbook-19-information-flow]] — the chapter using the `eval()`-vulnerable database as its running example.

## Sources
- [[fuzzingbook-19-information-flow]] — *The Fuzzing Book* Ch 19, "Tracking Information Flow."
- [[fuzzingbook-27-web-fuzzer]] — *The Fuzzing Book* Ch 27, "Testing Web Applications" (SQL/HTML/XSS injection against a vulnerable Web server).
