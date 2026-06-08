---
title: "OpenSSL"
type: entity
tags: [library, security, cryptography, tls, open-source, c-language]
sources: [fuzzingbook-03-fuzzer]
last_updated: 2026-06-06
---

# OpenSSL

**OpenSSL** is a widely deployed open-source C library implementing the SSL/TLS cryptographic protocols that secure most network communication (including HTTPS). Because it is written in C and handles untrusted network input, it is a high-value, much-fuzzed target.

## Role in The Fuzzing Book
[[fuzzingbook-03-fuzzer|Ch 3]] cites OpenSSL as the home of the [[Heartbleed]] bug (CVE-2014-0160): a buffer over-read in its TLS *heartbeat* service that could leak private keys and other secrets. The chapter highlights that Heartbleed was discovered by compiling OpenSSL with a memory sanitizer (à la [[AddressSanitizer]]) and fuzzing the heartbeat service — a concrete demonstration of [[Fuzzing|fuzzing]] plus runtime checkers finding a critical [[InformationLeak|information leak]] in production-grade C code.

## Connections
- [[Heartbleed]] — the OpenSSL vulnerability the chapter centers on.
- [[AddressSanitizer]] — the sanitizer approach used to find the bug.
- [[BufferOverflow]] / [[InformationLeak]] — the memory-safety classes implicated.
- [[Fuzzing]] — the discovery technique.
- [[fuzzingbook-03-fuzzer|Ch 3]] — recounts the OpenSSL/Heartbleed case.

## Sources
- [[fuzzingbook-03-fuzzer]] — *The Fuzzing Book* Ch 3, "Fuzzing: Breaking Things with Random Inputs."
