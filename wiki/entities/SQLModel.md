---
title: "SQLModel"
type: entity
tags: [tool, library, python, orm, database, fastapi]
sources: [leh-ch03-data-engineering]
last_updated: 2026-05-22
---

## What it is
SQLModel is a Python ORM library by the author of [[FastAPI]] that combines [[SQLAlchemy]] (for SQL access) with [[Pydantic]] (for validation and typed schemas). One class can serve as both an ORM row and an HTTP request/response model.

## In LLM Engineer's Handbook
Ch. 3 ([[leh-ch03-data-engineering]]) mentions SQLModel alongside [[SQLAlchemy]] when motivating the chapter's hand-rolled ODM pattern. The book uses neither directly (it stores raw documents in MongoDB), but the SQLModel/SQLAlchemy ORM pairing is the explicit analog the authors invoke for their own NoSQL `NoSQLBaseDocument` ODM.

## Connections
- [[SQLAlchemy]] — underlying SQL toolkit.
- [[FastAPI]] — sibling project from the same author.
- [[Pydantic]] — validation backbone.
- [[ORM]] / [[ODM]] — patterns discussed.
- [[Python]] — language.
