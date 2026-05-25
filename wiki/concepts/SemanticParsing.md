---
title: "Semantic Parsing"
type: concept
tags: [nlp, structured-outputs, llm]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Semantic Parsing

The task of **converting natural language into a structured, machine-readable format**. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]:

> "Semantic parsing involves converting natural language into a structured, machine-readable format. Text-to-SQL is an example of semantic parsing, where the outputs must be valid SQL queries."

## Canonical examples

- **Text-to-SQL** — "*What's the average monthly revenue over the last 6 months?*" → valid SQL.
- **Text-to-PostgreSQL** — text-to-SQL specialized for Postgres syntax.
- **Text-to-regex** — Ch 2's worked example: "*Email address ->*" → `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`.
- **Text-to-API-call** — natural language → structured tool/function-call argument JSON.

## Why semantic parsing depends on [[StructuredOutputs|structured outputs]]

The structure isn't optional. An "almost-valid" SQL query crashes. A truncated regex doesn't match what was intended. Hence semantic parsing is the prototypical task class where the **structured-outputs toolkit** (prompting → post-processing → constrained sampling → finetuning) is needed.

## In the broader stack

- **[[AIInterface|AI interface]]** — semantic parsing is what lets users interact with APIs / databases through natural language without learning the underlying syntax.
- **Agentic workflows** — tool-using agents need their LLM to produce *structurally correct* tool-call arguments, which is essentially semantic parsing at every step.

## Connections
- [[StructuredOutputs]] — the broader enforcement family.
- [[ConstrainedSampling]] — a key technique for guaranteeing semantic-parsing outputs.
- [[AIInterface]] — the UX surface semantic parsing enables.
- [[ai-engineering-ch02-foundation-models]] — primary source.
- [[FineTuning]] — the most reliable enforcement layer for a specific semantic-parsing target format.
