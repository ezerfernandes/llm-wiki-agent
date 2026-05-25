---
title: "SQLAlchemy"
type: entity
tags: [tool, library, python, orm, database, open-source]
sources: [leh-ch03-data-engineering]
last_updated: 2026-05-22
---

## What it is
SQLAlchemy is the dominant Python SQL toolkit and Object-Relational Mapper. It provides both a low-level expression language and a high-level ORM that maps Python classes to SQL tables.

## In LLM Engineer's Handbook
Ch. 3 ([[leh-ch03-data-engineering]]) cites SQLAlchemy as the canonical example of the ORM pattern when motivating the chapter's hand-rolled **ODM** (Object-Document Mapper) on top of `pymongo`: "The ODM pattern is extremely similar to ORM, but instead of working with SQL databases and tables, it works with NoSQL databases (such as MongoDB) and unstructured collections." [[SQLModel]] is namechecked as the FastAPI-flavored wrapper over SQLAlchemy.

## Connections
- [[SQLModel]] — FastAPI's SQLAlchemy wrapper.
- [[ORM]] / [[ODM]] — patterns the chapter contrasts.
- [[Mongoengine]] — production ODM in the same spirit for MongoDB.
- [[Pydantic]] — typed-model framework (SQLModel combines Pydantic + SQLAlchemy).
- [[Python]] — language.
