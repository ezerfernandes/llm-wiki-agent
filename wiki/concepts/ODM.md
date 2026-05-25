---
title: "ODM (Object-Document Mapping)"
type: concept
tags: [software-engineering, databases, patterns, nosql]
sources: [leh-ch03-data-engineering]
last_updated: 2026-05-22
---

## Definition
**Object-Document Mapping (ODM)** is a software pattern that maps object-oriented classes to NoSQL document collections — class names map to collections, instances to documents, fields to nested keys — analogous to [[ORM]] but for JSON-like document stores rather than relational tables.

## In LLM Engineer's Handbook
[[leh-ch03-data-engineering]] builds a custom ODM from scratch on top of `pymongo` and [[Pydantic]] for the LLM Twin's [[MongoDB]] warehouse. The base class `NoSQLBaseDocument(BaseModel, Generic[T], ABC)` provides `save()`, `find()`, `bulk_find()`, `bulk_insert()`, `get_or_create()`, plus MongoDB `_id` ↔ Python `UUID4` conversion via `from_mongo()` / `to_mongo()`. Each subclass declares its collection name in a nested `Settings` class; misconfiguration raises `ImproperlyConfigured`. The chapter notes [[Mongoengine]] as the production-grade ODM the authors compare against, and explains the chapter implements one from scratch for pedagogical reasons.

## Key details
- ODMs are to NoSQL what ORMs are to SQL — the same OOP-over-storage abstraction.
- The book's hand-rolled ODM uses Python generics (`T = TypeVar("T", bound="NoSQLBaseDocument")`) for type-safe class methods.
- Collection name comes from each subclass's inner `Settings.name` (here a `DataCategory` enum value).
- Production-grade Python ODM: Mongoengine; lightweight alternative: Beanie.
- The chapter's domain documents (`ArticleDocument`, `PostDocument`, `RepositoryDocument`, `UserDocument`) all inherit from this ODM, ensuring uniform persistence semantics.

## Connections
- [[ORM]] — the SQL analogue.
- [[CRUD]] — the operations ODMs encapsulate.
- [[Pydantic]] — the type-validation library underpinning the chapter's ODM.
- [[Mongoengine]] — production-grade Python ODM.
- [[MongoDB]] — the document database the chapter's ODM targets.
- [[Polymorphism]] — OOP property the ODM uses for uniform `extract()` / `save()` calls.
- [[BuilderPattern]] — used alongside the ODM in the `CrawlerDispatcher`.
