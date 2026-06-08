---
title: "SOAP (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, networking, web-services]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/SOAP
---

## Summary
This task asks the programmer to build a SOAP client that consumes a web service described by a WSDL document located at a given URL. The client must discover the available operations and invoke two remote procedures, `soapFunc()` and `anotherSoapFunc()`. The key insight is that most implementations lean on a SOAP/WSDL library that parses the service contract and generates callable stubs, rather than hand-crafting XML envelopes.

## Task Requirements
- Create a SOAP client that accesses functions defined at the WSDL endpoint `http://example.com/soap/wsdl`.
- Call the remote function `soapFunc()`.
- Call the remote function `anotherSoapFunc()`.

## Language Coverage
26 languages implement this task, spanning general-purpose, scripting, and enterprise-oriented languages, reflecting SOAP's historical reach in web-service integration. Representative examples include C, Go, Python, Perl, Ruby, PHP, F#, Kotlin, Tcl, and Wren.

## Connections
- [[SOAP]] — the XML-based messaging protocol the client speaks
- [[WSDL]] — the contract document describing the service's operations
- [[WebServices]] — the broader integration paradigm this task exemplifies
- [[XML]] — the underlying envelope format for SOAP messages
- [[RemoteProcedureCall]] — the conceptual model of invoking remote functions

## Contradictions
- None — reference task page.
