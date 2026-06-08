---
title: "Send email (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, networking, email]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Send_email
---

## Summary
This task asks the programmer to write a function that sends an email, exposing parameters for the From, To, and Cc addresses, the subject, the message body, and optionally the mail server name and login credentials. The core insight is that email delivery is almost always handled through SMTP, so most solutions either lean on a language's built-in/library SMTP client or shell out to an external mail program when no native support exists.

## Task Requirements
- Implement a function with parameters for From, To, and Cc addresses, the Subject, and the message text.
- Optionally accept fields for the server name and login details.
- Where appropriate, explain what notifications of success or failure the solution provides.
- Prefer language libraries/built-in functions; if unavailable, external programs may be used with an explanation.
- Note the portability of multi-OS solutions across operating systems.
- Obfuscate any sensitive data (credentials, real addresses) shown in examples.

## Language Coverage
57 languages implement this task, spanning general-purpose, scripting, and BASIC-family languages, with most relying on SMTP libraries or system mail tools. Representative implementations include Python, Java, C#, Go, Perl, Ruby, Haskell, PHP, PowerShell, and Tcl.

## Connections
- [[SMTP]] — the underlying protocol nearly every solution uses to relay mail.
- [[NetworkProgramming]] — sending email requires a client/server socket exchange.
- [[Authentication]] — optional login details cover SMTP AUTH for authenticated relays.
- [[EmailProtocols]] — broader family of standards (MIME, addressing) involved in message composition.

## Contradictions
- None — reference task page.
