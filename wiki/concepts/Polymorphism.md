---
title: "Polymorphism"
type: concept
tags: [software-engineering, oop, patterns]
sources: [leh-ch03-data-engineering]
last_updated: 2026-05-22
---

## Definition
**Polymorphism** is the object-oriented property that lets a single interface — a method name with a fixed signature — dispatch to different implementations depending on the runtime type of its receiver. In Python it manifests as duck typing plus inheritance: any class implementing the expected methods can be substituted at a call site.

## In LLM Engineer's Handbook
[[leh-ch03-data-engineering]] relies on polymorphism for its crawler dispatcher: `BaseCrawler` is an `ABC` with an abstract `extract(link, **kwargs)` method and a `model: type[NoSQLBaseDocument]` class attribute. Each concrete crawler (`GithubCrawler`, `MediumCrawler`, `LinkedInCrawler`, `CustomArticleCrawler`) implements `extract()` differently — `git clone` for GitHub, Selenium scroll for Medium, LangChain for arbitrary articles — but the dispatcher calls `crawler.extract(link, user=user)` uniformly without knowing the concrete class. The same pattern is used in [[leh-ch04-rag-feature-pipeline]]'s `CleaningDispatcher` / `ChunkingDispatcher` / `EmbeddingDispatcher`: each calls a `HandlerFactory.create_handler(data_category)` that returns a concrete handler implementing `clean()` / `chunk()` / `embed_batch()`.

## Key details
- Polymorphism is what makes the dispatcher / factory / strategy patterns useful — they all assume that substitutable types share a method signature.
- Python supports polymorphism via abstract base classes (`ABC`), `Protocol` classes (PEP 544), and plain duck typing.
- The chapter's crawler hierarchy uses ABC-style polymorphism with `@abstractmethod` enforcement; the dispatcher catches `NotImplementedError` if a subclass forgets to override.
- Adding a new platform (X / Twitter) requires only a new subclass; the dispatcher does not change.

## Connections
- [[BuilderPattern]] — uses polymorphism to register substitutable crawler classes.
- [[ORM]] / [[ODM]] — rely on polymorphic class methods (`save`, `find`, `get_or_create`).
- [[WebCrawling]] — the chapter's concrete polymorphic application.
- [[Pydantic]] — used to define polymorphic typed-domain hierarchies.
