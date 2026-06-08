---
title: "DNS query (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, networking, dns]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/DNS_query
---

## Summary
This task asks the programmer to use the Domain Name System to resolve a hostname into its corresponding IP addresses. Specifically, the host `www.kame.net` must be resolved to both its IPv4 (A record) and IPv6 (AAAA record) addresses, with both printed. The key point is exercising a dual-stack name lookup, since the chosen host is a classic example with both address families.

## Task Requirements
- Use DNS to resolve the hostname `www.kame.net`.
- Obtain both the IPv4 and the IPv6 addresses for that host.
- Print both addresses.

## Language Coverage
68 languages implement this task, showing broad coverage across both high-level and systems languages. Representative implementations include C, C++, Rust, Go, Python, Java, C#, Perl, Ruby, and Haskell.

## Connections
- [[DomainNameSystem]] — the protocol being queried
- [[IPAddress]] — IPv4 and IPv6 address formats returned
- [[NameResolution]] — translating hostnames into network addresses
- [[NetworkSockets]] — the typical OS-level API (e.g. getaddrinfo) used for lookups

## Contradictions
- None — reference task page.
