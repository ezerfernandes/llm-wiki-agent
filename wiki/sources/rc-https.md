---
title: "HTTPS (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, networking, web]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/HTTPS
---

## Summary
This task asks the programmer to send a GET request over HTTPS to retrieve the resource at "https://www.w3.org/" and print the response body to the console. The key wrinkle versus a plain HTTP request is that the client must perform a TLS handshake and is recommended to verify the host's certificate for validity. Authentication is explicitly out of scope (covered by separate tasks).

## Task Requirements
- Send a GET request to the URL "https://www.w3.org/".
- Print the retrieved resource to the console.
- Validating the host certificate is recommended.
- Do not authenticate (that belongs to other tasks).

## Language Coverage
76 languages implement this task, spanning low-level systems languages, scripting languages, and high-level functional and BASIC dialects. Representative implementations include C, C#, Go, Rust, Java, Python, Perl, Haskell, Ruby, and Swift.

## Connections
- [[TransportLayerSecurity]] — the cryptographic protocol securing the connection
- [[HypertextTransferProtocol]] — the underlying request/response protocol
- [[PublicKeyCertificate]] — what the client validates against the host
- [[CertificateValidation]] — the recommended trust-checking step

## Contradictions
- None — reference task page.
