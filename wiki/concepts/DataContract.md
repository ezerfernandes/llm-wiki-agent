---
title: "Data Contract"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, reliability, governance]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Data Contract

An explicit, codified agreement between upstream data producers and downstream ML consumers about schema and distributional expectations (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]). Data contracts and [[SchemaValidation|schema validation]] at the ingestion interface are "the defense against entropy."

Without them, changes in one system cause catastrophic, silent failures in another — the canonical **pipeline jungle** example: an upstream team changed `zip_code` from `integer` to `string`, the pipeline silently cast "02139" to 2139, the leading zero was lost, and the model treated "2139" as a new high-risk category, rejecting an entire region's applicants. Contracts codified through tools like [[GreatExpectations|Great Expectations]] or Pandera **fail fast** when schemas drift, rather than letting brittle parsing workarounds accumulate ([[SchemaEvolution|schema debt]]).

## Connections

- [[SchemaValidation]] — the enforcement mechanism.
- [[SchemaEvolution]] — the failure mode contracts prevent.
- [[GreatExpectations]] — contract-codification tooling.
- [[DataDebt]] — schema debt accumulates without contracts.
- [[mlsysbook-ch04-data-engineering]] — source.
