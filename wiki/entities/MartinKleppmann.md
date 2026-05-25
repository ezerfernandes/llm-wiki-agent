---
name: MartinKleppmann
title: "Martin Kleppmann"
type: entity
tags: [person, researcher, author, data-systems]
sources: [dmls-ch01-overview, dmls-ch03-data-engineering]
last_updated: 2026-05-23
---

# Martin Kleppmann

Software engineer and researcher at the University of Cambridge. Author of *Designing Data-Intensive Applications* (O'Reilly, 2017), the textbook [[ChipHuyen|Huyen]] explicitly recommends in [[dmls-ch03-data-engineering|DMLS Ch 3]] as the foundational reference for data systems.

## Cited contributions in DMLS
- **Latency vs. response time distinction** (DMLS Ch 1) — Huyen explicitly notes she's overloading Kleppmann's stricter usage ("response time" = client-perceived end-to-end; "latency" = a specific narrow piece).
- **OLTP vs. OLAP terminology and the convergence story** (DMLS Ch 3) — the framing of [[CockroachDB]] / [[ApacheIceberg]] / [[DuckDB]] / [[Snowflake]] as the OLTP-OLAP convergence cohort traces back to Kleppmann's framing.
- **Slowest-percentile observation** (DMLS Ch 1) — Kleppmann's note that the slowest-percentile requests typically come from the highest-value customers (more data → more processing); cited by Huyen in support of monitoring p95/p99 not p50.
- **RPC vs. REST framing** (DMLS Ch 3) — Kleppmann's argument that RPC is fine for intra-org calls; REST is for cross-network surfaces.

## Other work
- *Designing Data-Intensive Applications* (2017) — the canonical modern data-systems textbook.
- CRDT and distributed-systems research.
- *Local-first software* (2019) — vision paper.

## Connections
- [[ChipHuyen]] — DMLS author who cites Kleppmann throughout.
- [[OLTP]] / [[OLAP]] / [[ETL]] / [[ELT]] — concepts Kleppmann's framing anchors.
- [[Latency]] — terminology Huyen explicitly references Kleppmann on.
- [[DesigningDataIntensiveApplications]] — the book.
- [[CambridgeUniversityPress]] — adjacent academic publisher.
