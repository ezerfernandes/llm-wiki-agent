---
title: "Table creation/Postal addresses (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, databases, sql, data-modeling]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Table_creation/Postal_addresses
---

## Summary
This task asks the programmer to design and create a database table for storing USA postal addresses. Beyond a unique identifier, the table must hold a street address, a city, a state code, and a zipcode, each with an appropriately chosen data type. The key exercise is schema modeling: picking sensible column types (e.g. fixed-length CHAR for the two-letter state code versus variable-length text for the street) and demonstrating how a non-database language opens a connection and issues a CREATE TABLE statement.

## Task Requirements
- Create a table to store addresses, assuming all are located in the USA.
- Include a field holding a unique identifier (primary key).
- Include a field for the street address.
- Include a field for the city.
- Include a field for the state code.
- Include a field for the zipcode.
- Choose appropriate types for each field.
- For non-database languages, show how to open a connection to a database of your choice and create the address table within it.

## Language Coverage
56 languages implement this task. Coverage spans dedicated database engines and SQL dialects (MariaDB, MySQL, PostgreSQL, SQLite, Oracle, Transact-SQL, Apache Derby, DuckDB, SQL PL) alongside general-purpose languages that connect to an embedded database, typically SQLite (Python, Perl, Tcl, PHP, PowerShell, Ruby), plus functional and scripting languages such as Haskell, Clojure, Racket, and AWK.

## Connections
- [[RelationalDatabase]] — the task is fundamentally about modeling data in a relational table.
- [[SQL]] — most implementations express the schema via a CREATE TABLE statement.
- [[DataModeling]] — choosing appropriate column types for each address field is the core design decision.
- [[PrimaryKey]] — the required unique identifier field is a primary key.
- [[SQLite]] — the most common embedded database used by non-database languages here.

## Contradictions
- None — reference task page.
