---
title: "SQL-based authentication (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, database, security, cryptography]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/SQL-based_authentication
---

## Summary
This task asks the programmer to implement a simple username/password authentication system backed by a MySQL database. It has three parts: connect to the database, create user records, and authenticate login attempts. The key insight is that passwords are never stored directly — each user gets 16 random salt bytes, and the stored credential is the MD5 hash of that salt concatenated with the password, so verification re-hashes the salt with the supplied password and compares.

## Task Requirements
- Connect to a MySQL database (`connect_db`).
- Create user/password records (`create_user`) in a `users` table with columns `userid`, `username`, `pass_salt` (16 random bytes), and `pass_md5` (binary MD5 of salt + password).
- Authenticate login requests against that table (`authenticate_user`) by re-hashing the stored salt with the provided password.
- Honor the given table schema, noting that `tinyblob` is used because MySQL before 5.0.15 strips trailing spaces from `binary(16)` values.

## Language Coverage
21 languages implement this task, a moderate spread reflecting the need for both a MySQL driver and a hashing library. Representative implementations include C, C#, Go, Java, Python, Perl, PHP, Ruby, Raku, and Tcl.

## Connections
- [[MD5]] — the hash function used to derive the stored credential
- [[PasswordSalting]] — random per-user salt defends against precomputed/rainbow attacks
- [[SQL]] — the table is defined and queried via SQL against MySQL
- [[Authentication]] — verifying identity by comparing re-hashed credentials
- [[DatabaseConnectivity]] — connecting an application to a relational database

## Contradictions
- None — reference task page.
