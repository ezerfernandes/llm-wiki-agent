---
title: "Active Directory/Connect (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, networking, directory-services]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Active_Directory/Connect
---

## Summary
This task asks the programmer to establish a connection to an Active Directory or LDAP (Lightweight Directory Access Protocol) server. The core challenge is binding to the directory service — typically supplying a host, port, distinguished name, and credentials — usually by leaning on an existing LDAP client library rather than implementing the protocol by hand.

## Task Requirements
- Open a connection to an Active Directory or LDAP server.
- Authenticate / bind against that server (host, port, and credentials as needed).

## Language Coverage
30 languages implement this task, spanning systems languages and scripting languages alike, most of which delegate to a platform or third-party LDAP library. Representative implementations include C, C#, D, Go, Haskell, Java, Python, Perl, Ruby, Rust, Tcl, and VBScript.

## Connections
- [[LDAP]] — the directory access protocol the task targets
- [[ActiveDirectory]] — Microsoft's directory service implementation
- [[AuthenticationBinding]] — the bind/credential step required to connect
- [[ClientServerNetworking]] — the underlying networked client connection model

## Contradictions
- None — reference task page.
