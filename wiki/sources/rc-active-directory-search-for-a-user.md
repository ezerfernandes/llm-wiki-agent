---
title: "Active Directory/Search for a user (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, directory-services, ldap, system-administration]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Active_Directory/Search_for_a_user
---

## Summary
This task asks the programmer to query a Microsoft Active Directory directory service to locate a user account. It builds directly on the companion task of establishing an authenticated connection to the directory, then issues a search filter (typically LDAP-style) to retrieve a matching user entry. The key insight is that Active Directory is an LDAP-compatible store, so most solutions reduce to constructing and executing an LDAP search query.

## Task Requirements
- Assume a working connection to Active Directory has already been established (see the prerequisite "Connect to Active Directory" task).
- Perform a search against the directory to find a user, generally by supplying a search base and an LDAP filter such as `(&(objectClass=user)(sAMAccountName=name))`.
- Return or display the matching user record(s).

## Language Coverage
25 languages implement this task, spanning system-administration and general-purpose languages, often via native LDAP bindings or platform directory APIs. Representative implementations include C, Go, Haskell, Java, Perl, PHP, Python, PowerShell, Ruby, Tcl, and VBScript, with PowerShell and VBScript leaning on built-in Windows directory tooling.

## Connections
- [[ActiveDirectory]] — the directory service being queried
- [[LDAP]] — the protocol and filter syntax most solutions use
- [[DirectoryServices]] — the broader category this task belongs to
- [[Authentication]] — searching presupposes an authenticated bind to the directory

## Contradictions
- None — reference task page.
