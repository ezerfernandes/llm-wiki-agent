---
title: "Heartbleed"
type: entity
tags: [vulnerability, security, openssl, memory-safety, fuzzing, cve]
sources: [fuzzingbook-03-fuzzer]
last_updated: 2026-06-06
---

# Heartbleed

**Heartbleed** (CVE-2014-0160) is a notorious security vulnerability in the **OpenSSL** cryptographic library's TLS *heartbeat* extension. A malicious client could request that the server echo back *more* bytes than it had supplied, causing the server to return adjacent process memory — potentially including private keys, certificates, and credentials. Because the over-read stayed within the process's *valid* address space, it left no trace and went undetected for years.

## Role in The Fuzzing Book
[[fuzzingbook-03-fuzzer|Ch 3]] uses Heartbleed as the headline real-world case for combining [[Fuzzing|fuzzing]] with runtime memory checkers. The chapter recounts that researchers at the **Codenomicon** company and at **Google** compiled OpenSSL with a memory sanitizer and flooded the heartbeat service with fuzzed commands; the sanitizer flagged the out-of-bounds access "very quickly." The chapter also frames Heartbleed as an [[InformationLeak|information leak]] (it simulates the heartbeat over-read in Python) and notes that [[AddressSanitizer]] catches the *out-of-bounds* variant but not in-bounds leaks. The XKCD #1354 comic is cited as a plain-language explanation.

## Connections
- [[OpenSSL]] — the affected library.
- [[AddressSanitizer]] — the class of memory checker that, combined with fuzzing, surfaced the bug.
- [[BufferOverflow]] / [[InformationLeak]] — Heartbleed is a buffer over-read causing an information leak.
- [[Fuzzing]] — the discovery method (sanitizer + fuzzed heartbeat commands).
- [[fuzzingbook-03-fuzzer|Ch 3]] — recounts the discovery as the motivating example for runtime checkers.

## Sources
- [[fuzzingbook-03-fuzzer]] — *The Fuzzing Book* Ch 3, "Fuzzing: Breaking Things with Random Inputs."
