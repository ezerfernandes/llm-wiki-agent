---
title: "ORM (Object-Relational Mapping)"
type: concept
tags: [software-engineering, databases, patterns]
sources: [leh-ch03-data-engineering]
last_updated: 2026-05-22
---

## Definition
**Object-Relational Mapping (ORM)** is a software pattern that maps object-oriented classes to relational database tables — class names map to tables, instances to rows, fields to columns — so application code interacts with database records as native Python (or Java, Ruby, etc.) objects rather than raw SQL strings.

## In LLM Engineer's Handbook
[[leh-ch03-data-engineering]] uses ORM as the motivating analogy for the chapter's custom [[ODM]] layer: "ORM maps Python classes to SQL tables; ODM maps them to NoSQL JSON-like documents." The chapter names [[SQLAlchemy]] as the canonical Python ORM and [[SQLModel]] (FastAPI's SQLAlchemy wrapper) as a typed convenience layer. ORMs are explicitly out of scope for the LLM Twin because its warehouse is [[MongoDB]] (NoSQL), but understanding the ORM pattern is required to understand why the authors build an ODM.

## Key details
- ORMs provide a high-level CRUD API (`session.add`, `session.query(...)`, `obj.save()`) over SQL.
- Trade-offs: developer productivity vs. SQL fluency and query-plan control.
- Migrations: schema evolution becomes a versioned set of Python files (Alembic for SQLAlchemy, Django migrations).
- ORMs unify the impedance mismatch between OO code and relational storage.
- Common Python ORMs: SQLAlchemy, Django ORM, Tortoise ORM, SQLModel.

## Connections
- [[ODM]] — the NoSQL analogue ORM motivates.
- [[CRUD]] — the operations ORMs encapsulate.
- [[SQLAlchemy]] / [[SQLModel]] — canonical Python ORM implementations.
- [[FastAPI]] — SQLModel's parent framework.
- [[Polymorphism]] — the OOP property ORMs lean on for inheritance-based table mappings.
