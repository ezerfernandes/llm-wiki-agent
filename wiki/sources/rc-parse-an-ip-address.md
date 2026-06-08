---
title: "Parse an IP Address (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, networking, string-processing, parsing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Parse_an_IP_Address
---

## Summary
The task asks the programmer to parse text-format IP addresses in both IPv4 and IPv6 forms and emit each as a hexadecimal integer representing the address, identify which address space it belongs to, and capture an optional port number. The key insight is handling the variant nature of the result (address number, space, port, and a flag indicating whether a port was specified) and recognizing equivalences such as the IPv4-mapped IPv6 form (`::ffff:127.0.0.1`).

## Task Requirements
- Parse the six given inputs: `127.0.0.1`, `127.0.0.1:80`, `::1`, `[::1]:80`, `2605:2700:0:3::4713:93e3`, and `[2605:2700:0:3::4713:93e3]:80`.
- Emit each address as a hexadecimal integer (e.g. `127.0.0.1` becomes `7F000001`).
- Report the address space (IPv4 vs IPv6).
- Report the port number when one is specified, and indicate whether a port was present.
- Handle bracketed IPv6 notation `[...]:port` and IPv6 abbreviation/compression (`::`).

## Language Coverage
43 languages implement this task, spanning systems, functional, and scripting families. Representative entries include C, C++, C#, Rust, Go, Java, Python, Haskell, OCaml, Perl, Raku, Ruby, and Tcl.

## Connections
- [[IPAddressParsing]] — core subject of the task
- [[IPv6]] — address compression and bracketed-port notation
- [[StringParsing]] — tokenizing and validating address text
- [[HexadecimalRepresentation]] — emitting the address as an integer in hex
- [[NetworkProgramming]] — domain context for address spaces and ports

## Contradictions
- None — reference task page.
