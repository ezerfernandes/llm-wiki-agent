---
title: "Rule-Based Filtering"
type: concept
tags: [llm-engineering]
sources: [leh-ch05-supervised-fine-tuning]
last_updated: 2026-05-22
---

## Definition
Data-quality filter using explicit predefined rules (length, keyword, format).

## In LLM Engineer's Handbook
Simplest data-quality control: drop samples failing explicit rules. Three families per [[leh-ch05-supervised-fine-tuning]]: length filtering (min/max thresholds), keyword exclusion (blacklisted terms), format checking (JSON validity, code syntax, schema). Fast, scalable, transparent, but brittle — can remove valid edge cases and inject bias.
