---
title: "HTTPS/Client-authenticated (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, networking, security, tls]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/HTTPS/Client-authenticated
---

## Summary
This task asks the programmer to connect to a web server over HTTPS in a scenario where the server requires the client to present its own certificate to prove its identity. Unlike ordinary HTTPS authentication, the client must be verified through mutual TLS rather than a username/password or session cookie. The key insight is that both parties exchange and validate X.509 certificates during the TLS handshake, giving the server strong cryptographic assurance of who the client is.

## Task Requirements
- Connect to a web server using HTTPS (TLS).
- Present a client certificate so the server can verify the client's identity.
- Do not authenticate via username/password or a set cookie — only the certificate is acceptable.
- Demonstrates a use case common to webservice clients (e.g., Amazon Web Services) needing high-assurance counterparty verification.

## Language Coverage
23 languages implement this task, spanning systems, scripting, JVM, and functional ecosystems. Representative implementations include C#, Go, Java, Kotlin, Python, Perl, Ruby, Rust, Scala, Tcl, and Raku.

## Connections
- [[TransportLayerSecurity]] — the protocol providing the encrypted, authenticated channel
- [[MutualTLS]] — the bidirectional certificate exchange this task specifically requires
- [[PublicKeyInfrastructure]] — X.509 certificates and certificate authorities underpin client identity
- [[HTTPS]] — HTTP layered over TLS
- [[ClientCertificate]] — the credential the client presents during the handshake

## Contradictions
- None — reference task page.
