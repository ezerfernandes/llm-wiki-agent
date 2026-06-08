---
title: "OWASP"
type: entity
tags: [organization, security, web, nonprofit, tool]
sources: [fuzzingbook-27-web-fuzzer]
last_updated: 2026-06-06
---

# OWASP

**OWASP** (the Open Web Application Security Project) is a nonprofit foundation focused on improving the security of software, best known for its Web-application-security guidance and open-source tooling. Its **Zed Attack Proxy (ZAP)** is a widely used open-source website security scanner.

## Role in The Fuzzing Book
[[fuzzingbook-27-web-fuzzer|Ch 27]]'s Background points readers to OWASP's **Zed Attack Proxy (ZAP)** as a production security scanner that implements — among many more — the kinds of automated checks the chapter builds by hand: crawling a site, discovering forms, and probing fields for [[SQLInjection|SQL injection]] and [[CrossSiteScripting|XSS]]. The chapter positions its own `WebFormFuzzer`/`SQLInjectionFuzzer` as proof-of-concept demonstrators of techniques that tools like ZAP productionize.

## Connections
- [[WebApplicationFuzzing]] — ZAP automates the crawl-and-attack pipeline the chapter prototypes.
- [[SQLInjection]] / [[CrossSiteScripting]] — vulnerability classes scanned by ZAP and demonstrated in Ch 27.
- [[fuzzingbook-27-web-fuzzer]] — the chapter that cites OWASP/ZAP in its Background.

## Sources
- [[fuzzingbook-27-web-fuzzer]] — *The Fuzzing Book* Ch 27, "Testing Web Applications."
