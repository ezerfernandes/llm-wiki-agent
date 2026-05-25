---
title: "CRUD (Create, Read, Update, Delete)"
type: concept
tags: [software-engineering, databases, patterns]
sources: [leh-ch03-data-engineering, leh-ch04-rag-feature-pipeline]
last_updated: 2026-05-22
---

## Definition
**CRUD** is the canonical four-operation API for persistent storage: **Create** (insert a new record), **Read** (retrieve one or many records), **Update** (modify an existing record), **Delete** (remove a record). CRUD is the lowest-common-denominator interface that ORMs, ODMs, and database APIs all expose.

## In LLM Engineer's Handbook
[[leh-ch03-data-engineering]] uses CRUD as the contract for the custom [[ODM]]: `NoSQLBaseDocument` exposes CRUD primitives via `save()` (create), `find()` / `bulk_find()` / `get_or_create()` (read), implicit upsert (update), and standard pymongo delete operations. [[leh-ch04-rag-feature-pipeline]] uses CRUD as a key differentiator between [[VectorDatabase|vector DBs]] and standalone vector indices like FAISS: "Vector DBs support CRUD operations, metadata filtering, scalability, real-time updates, backups, ecosystem integration, and robust data security, making them more suited for production environments than standalone indices."

## Key details
- The four-operation taxonomy traces back to early relational-database literature.
- All major persistence layers (SQL, NoSQL, vector DBs, key-value stores) expose CRUD plus extensions.
- CRUD is the minimum interface a feature store, model registry, or artifact store must implement.
- The chapter's custom ODM and OVM both reify CRUD as their public API.

## Connections
- [[ORM]] / [[ODM]] — patterns that wrap database CRUD as object methods.
- [[VectorDatabase]] — distinguished from vector indices by supporting CRUD.
- [[MongoDB]] / [[Qdrant]] — concrete data stores the book interacts with via CRUD.
- [[FeatureStore]] / [[ModelRegistry]] — MLOps stores that expose CRUD over their domain artifacts.
