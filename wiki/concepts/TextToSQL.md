---
title: "Text-to-SQL"
type: concept
tags: [semantic-parsing, sql, llm, agents]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Text-to-SQL

**Text-to-SQL** is the semantic-parsing task of **translating a natural-language query into an executable SQL statement** against a known schema. Named in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] as the load-bearing step in [[RAGOverTabularData|RAG over tabular data]] and as the canonical agent-tool example for [[KnowledgeAugmentation|knowledge augmentation]] over structured databases.

## The three-step pipeline (per Ch 6)

1. **Text-to-SQL**: based on the user query and provided table schemas, generate the SQL.
2. **SQL execution**: run the SQL.
3. **Response generation**: generate the natural-language answer from the SQL result + original query.

## Schema selection — the upstream problem

When a database has many tables whose combined schemas exceed the model's context, an **intermediate table-selection step** is needed before the LM can write SQL. This is the production-scale failure mode that benchmark-grade text-to-SQL papers often skip.

## Position in the wiki

Adjacent to [[BIRDSQL]] and [[WikiSQL]] (text-to-SQL benchmarks in the wiki), and to [[RAGOverTabularData]] (the RAG application). The dedicated or general LM that performs the translation is a **tool** in agent terminology — the SQL executor is the *separate* tool that runs the output.

## Connections

- [[RAGOverTabularData]] — primary application surface.
- [[BIRDSQL]] / [[BIRDSQLEfficiency]] / [[WikiSQL]] — benchmarks for text-to-SQL.
- [[Agent]] — text-to-SQL is one of the canonical tools an agent uses.
- [[KnowledgeAugmentation]] — the tool family text-to-SQL belongs to.
- [[FunctionCalling]] — text-to-SQL can be exposed as a function call.
- [[ai-engineering-ch06-rag-agents]] — primary source.
