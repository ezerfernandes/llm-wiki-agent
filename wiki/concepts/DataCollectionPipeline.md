---
title: "Data Collection Pipeline"
type: concept
tags: [data-engineering, etl, architecture]
sources: [leh-ch01-understanding-llm-twin-concept, leh-ch03-data-engineering]
last_updated: 2026-05-22
---

## Definition
A **data collection pipeline** is an ETL pipeline that gathers raw data from one or more external sources (web crawls, APIs, databases) and lands it into a unified warehouse — preceding any feature engineering, model training, or inference. In the *LLM Engineer's Handbook* architecture it is the **fourth** pipeline that sits before the [[FTIArchitecture|FTI trio]].

## In LLM Engineer's Handbook
[[leh-ch01-understanding-llm-twin-concept]] adds the data collection pipeline as a separate pipeline before feature/training/inference because the LLM Twin reflects a startup reality: data engineering and ML engineering have different SLOs and team owners. The data collection pipeline is owned by data engineering, runs on its own schedule, and communicates with the FTI pipelines only through the [[DataWarehouse|warehouse]]. [[leh-ch03-data-engineering]] implements it concretely as a [[ZenML]] pipeline orchestrating two steps — `get_or_create_user` and `crawl_links` — that dispatch via a `CrawlerDispatcher` ([[BuilderPattern]]) to per-platform [[Selenium]] / [[BeautifulSoup]] / [[LangChain]] / `git clone` crawlers, normalizing all output into three platform-agnostic categories (`ArticleDocument`, `PostDocument`, `RepositoryDocument`) and persisting them in [[MongoDB]] via a custom [[ODM]].

## Key details
- Classic ETL: **extract** (crawl LinkedIn / Medium / Substack / GitHub), **transform** (clean and standardize HTML into normalized text), **load** (write to MongoDB).
- Designed to be extensible — adding X/Twitter requires only a new crawler that emits a `PostDocument`.
- Decoupled from the downstream feature pipeline; they share state only through the warehouse and can run on independent schedules.
- Production-grade alternatives the book recommends: [[Scrapy]] for general scraping, [[Crawl4AI]] for LLM-targeted crawling.

## Connections
- [[ETL]] — the pattern instantiated.
- [[FTIArchitecture]] — the data collection pipeline precedes the FTI trio in the LLM Twin design.
- [[DataEngineering]] — the discipline that owns the data collection pipeline.
- [[DataWarehouse]] — the sink; in the LLM Twin, MongoDB plays this role.
- [[BuilderPattern]] — used by the `CrawlerDispatcher` to register per-domain crawlers.
- [[WebCrawling]] / [[Selenium]] / [[BeautifulSoup]] / [[Scrapy]] / [[Crawl4AI]] — the technique and tool stack.
- [[ODM]] — the persistence pattern used to write into [[MongoDB]].
- [[ZenML]] — the orchestrator wiring the pipeline together.
