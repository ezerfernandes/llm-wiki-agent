---
title: "SQL Injection"
type: concept
tags: [security, vulnerability, injection, sql, web, fuzzing, database]
sources: [fuzzingbook-27-web-fuzzer]
last_updated: 2026-06-06
---

# SQL Injection

**SQL injection** is a vulnerability in which untrusted input is concatenated into a SQL command and thereby interpreted as *SQL code* rather than data — letting an attacker read, alter, or delete database contents, bypass authentication, or change the purpose of the original query. It is the database-targeting instance of [[CodeInjection|code injection]]; the canonical illustration is XKCD #327's "Little Bobby Tables." The defense is to never build SQL by string formatting: use **parameterized queries** (parameter substitution) and otherwise sanitize/escape input.

## From The Fuzzing Book — Testing Web Applications
[[fuzzingbook-27-web-fuzzer|Ch 27]]'s vulnerable shop server stores orders by formatting field values straight into `INSERT INTO orders VALUES ('{item}', '{name}', ...)` and running it with `db.executescript()`. Supplying the `name` field `Jane', 'x', 'x', 'x'); DELETE FROM orders; -- ` closes the `INSERT`, appends a `DELETE FROM orders`, and comments out the rest with `--`, wiping the table. The chapter then automates the attack:

- **`SQLInjectionGrammarMiner`** (subclass of `HTMLGrammarMiner`) holds an `ATTACKS` list of common injection schemes plus a caller-supplied `sql_payload`, and mines a grammar that tries injection in *every* form field.
- **`SQLInjectionFuzzer`** (subclass of [[WebFormFuzzer|`WebFormFuzzer`]]) wires this together: `SQLInjectionFuzzer(url, "DELETE FROM orders")` empties the orders table in **under a second**, needing nothing but the URL.

The chapter shows the server *leaks* the schema (table name, columns) through tracebacks in its error pages, supplying the "insider knowledge" an attacker would otherwise need (real databases expose this via the `information_schema` data dictionary). The fix (Exercise 1, Part 3) is **parameterized SQL** — `db.execute("INSERT INTO orders VALUES (?, ?, ?, ?, ?)", (...))` with `execute()` rather than `executescript()`, so values can never be parsed as commands.

## Connections
- [[CodeInjection]] — SQL injection is its database-targeting instance (untrusted input reaching a trusted interpreter).
- [[WebFormFuzzer]] — `SQLInjectionFuzzer` subclasses it, overriding `get_grammar()` with attack payloads.
- [[WebApplicationFuzzing]] — the broader context (testing/attacking Web apps over HTTP).
- [[CrossSiteScripting]] / [[HTMLInjection]] — the other two attacks Ch 27 demonstrates against the same server.
- [[InputSanitization]] — parameterized queries / escaping, the defense.
- [[InformationFlow]] / [[DynamicTaintAnalysis]] — [[fuzzingbook-19-information-flow|Ch 19]]'s principled source→sink defense against the same danger.
- [[Grammar]] / [[GrammarFuzzer]] — the engine that generates the injection payloads.
- [[fuzzingbook-27-web-fuzzer]] — the chapter that demonstrates and automates the attack.

## Sources
- [[fuzzingbook-27-web-fuzzer]] — *The Fuzzing Book* Ch 27, "Testing Web Applications."
