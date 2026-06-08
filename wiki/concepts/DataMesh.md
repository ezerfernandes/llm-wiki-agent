---
title: "Data Mesh"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, storage, architecture, governance]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Data Mesh

An architectural pattern that **decentralizes data ownership** to manage scale organizationally, treating data as a product owned by domain teams (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]; Dehghani 2022).

Where the [[Lakehouse|data lakehouse]] is a *technical* response to [[DataGravity|data gravity]] (move compute to data), data mesh is the *organizational* response: rather than a single central platform team, each domain team owns and serves its data as a product. The two are cited together as the architectural answers to the fact that the engineering cost of moving petabyte datasets exceeds the wire cost by an order of magnitude.

## Connections

- [[DataGravity]] — the scale constraint it addresses organizationally.
- [[Lakehouse]] — the technical counterpart response.
- [[DataGovernance]] — domain ownership is a governance pattern.
- [[StorageArchitecture]] — the broader decision space.
- [[mlsysbook-ch04-data-engineering]] — source.
