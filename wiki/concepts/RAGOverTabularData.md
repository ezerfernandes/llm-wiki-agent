---
title: "RAG over Tabular Data"
type: concept
tags: [rag, sql, tabular, retrieval]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# RAG over Tabular Data

**RAG over tabular data** is the RAG variant in which the external knowledge source is a **structured database** (SQL, NoSQL, spreadsheet) instead of a corpus of unstructured documents. Per [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]], *"the workflow for augmenting a context using tabular data is significantly different from the classic RAG workflow"* — the substitution of embedding-based retrieval with **structured query execution** is the central change.

## The three-step workflow

1. **[[TextToSQL|Text-to-SQL]]** — based on the user query and available table schemas, the LM generates a SQL query (semantic parsing).
2. **SQL execution** — run the SQL against the database.
3. **Generation** — generate the natural-language response from the SQL result + original query.

## The Kitty Vogue example

For the question *"How many units of Fruity Fedora were sold in the last 7 days?"* over a `Sales` table:

```sql
SELECT SUM(units) AS total_units_sold
FROM Sales
WHERE product_name = 'Fruity Fedora'
  AND timestamp >= DATE_SUB(CURDATE(), INTERVAL 7 DAY);
```

## Why this is harder than text RAG

- **Schema selection**: if the database has many tables whose schemas can't all fit in the model context, an intermediate **table-selection** step is needed.
- **SQL correctness is binary**: a malformed SQL query returns nothing useful. There's no fuzzy-match tolerance — either the query is correct or it isn't.
- **Specialized models**: text-to-SQL can be done by the same LM that generates the final response, or by a dedicated text-to-SQL model (e.g. for hard schemas).

## Position in the chapter

RAG over tabular data is the bridge to the **agent** discussion — the agent's environment includes the SQL executor as a tool. Per Huyen: *"In this section, we've discussed how tools such as retrievers and SQL executors can enable models to handle more queries and generate higher-quality responses. ... Tool use is a core characteristic of the agentic pattern."*

## Connections

- [[rag]] — parent application.
- [[TextToSQL]] — the critical semantic-parsing step.
- [[Agent]] — what RAG-over-tabular-data is on the path to.
- [[BIRDSQL]] / [[WikiSQL]] — text-to-SQL benchmarks.
- [[ai-engineering-ch06-rag-agents]] — primary source.
