---
title: "Hash-Chained Audit"
type: concept
tags: [concept]
sources: [2605.00424-skills-as-verifiable-artifacts]
last_updated: 2026-05-10
---

# Hash-Chained Audit

Append-only log where every gate event (request, decision, executed, denied, integrity failure) carries a prevHash field. Concurrent appends serialize through an in-process queue. Source of truth for biconditional post-hoc verification.
