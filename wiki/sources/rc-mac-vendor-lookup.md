---
title: "MAC vendor lookup (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, networking, http-client]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/MAC_vendor_lookup
---

## Summary
Every networked device carries a unique Media Access Control (MAC) address, and a common network-administration task is identifying a device's manufacturer from that address alone. This task asks the programmer to call one or more public web APIs that map a supplied MAC address back to its vendor. The key practical insight is handling the two distinct failure modes correctly and respecting API rate limits.

## Task Requirements
- Interface with at least one internet API to retrieve the device manufacturer for a given MAC address.
- A MAC address that yields no valid result must return the string "N/A".
- A network-connectivity or API error must return a null result (distinct from "N/A").
- Be mindful of rate limiting: providers such as http://api.macvendors.com/ throttle after a few calls, so implementations should build in a delay between requests.

## Language Coverage
57 languages implement this task, reflecting broad coverage across general-purpose and scripting languages with HTTP support. Representative implementations include C, C++, C#, Go, Haskell, Java, JavaScript, Python, Perl, Raku, Ruby, Rust, and PowerShell.

## Connections
- [[MACAddress]] — the input identifier being resolved to a vendor
- [[HTTPClient]] — making the outbound API request
- [[RESTAPI]] — the web service interface consumed
- [[RateLimiting]] — throttling behavior that implementations must accommodate
- [[ErrorHandling]] — distinguishing "N/A" from a null network/API error

## Contradictions
- None — reference task page.
