---
title: "Parameterized SQL statement (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, database, security]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Parameterized_SQL_statement
---

## Summary
This task asks the programmer to build and execute a parameterized (prepared) SQL statement rather than concatenating values directly into the query string. The concrete example is an `UPDATE players` statement that sets `name`, `score`, and `active` filtered by `jerseyNum`. The key insight is that binding values as parameters lets the SQL driver sanitize input automatically, defeating SQL injection attacks while also improving performance through statement reuse.

## Task Requirements
- Construct a parameterized SQL statement equivalent to: `UPDATE players SET name = ?, score = ?, active = ? WHERE jerseyNum = ?`.
- Bind the parameters to the given values: name = "Smith, Steve", score = 42, active = true, jerseyNum = 99.
- Execute the prepared statement against a database.

## Language Coverage
37 languages implement this task, spanning general-purpose languages with database bindings as well as SQL dialects themselves. Representative implementations include Python, Java, C#, Go, Perl, Ruby, Haskell, PHP, Tcl, and dedicated database environments such as SQL, MariaDB, SQL PL, and DuckDB.

## Connections
- [[SQLInjection]] — the attack class that parameterized statements are designed to prevent
- [[PreparedStatement]] — the mechanism used to bind parameters separately from the query text
- [[SQL]] — the query language the task operates in
- [[InputSanitization]] — the driver-level escaping that parameter binding provides
- [[DatabaseAccess]] — the broader category of operations this task belongs to

## Contradictions
- None — reference task page.
