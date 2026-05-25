---
title: "Information Aggregation"
type: concept
tags: [use-case, ai-engineering, summarization]
sources: [ai-engineering-ch01-intro]
last_updated: 2024-12-04
---

# Information Aggregation

**The use case of distilling and summarizing information** — one of the eight [[FoundationModelUseCases|foundation-model use case categories]] in [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]]. Among the largest in surveyed adoption: per Salesforce's 2023 *Generative AI Snapshot Research*, **74% of generative-AI users use it to distill complex ideas and summarize information.**

## Consumer patterns

- **Talk-to-your-docs** — load contracts, disclosures, papers; retrieve info conversationally.
- **Summarize websites, research, papers.**
- **Compare and synthesize** across sources.

## Enterprise patterns

- **Faster middle-management.** Efficient info aggregation reduces the burden on middle managers and lets organizations stay leaner.
- **Customer/competitor intelligence**: surface critical info on potential customers, run competitor analyses.

## Worked example: [[Instacart|Instacart's]] "Fast Breakdown"

Huyen's anchor example: Instacart's **internal prompt marketplace** — most popular template was **"Fast Breakdown"**, which:
1. Takes meeting notes, emails, Slack conversations as input.
2. Returns facts, open questions, and action items.
3. Action items are automatically inserted into a project-tracking tool and assigned to the right owner.

This pattern bridges **information aggregation** with **[[WorkflowAutomation|workflow automation]]** — the summary becomes input to an automated routing step.

## Where it appears in the consumer/enterprise table

| | Consumer | Enterprise |
|---|---|---|
| Information aggregation | Summarization, talk-to-your-docs | Summarization, market research |

## Connections

- [[FoundationModelUseCases]] — parent category.
- [[DataOrganization]] — goes hand-in-hand; *"the more information you gather, the more important it is to organize it."*
- [[WorkflowAutomation]] — natural downstream step (e.g., Instacart's auto-routing).
- [[rag|RAG]] — the canonical retrieval technique for talk-to-your-docs patterns.
- [[Instacart]] — worked example.
- [[ai-engineering-ch01-intro]] — primary source.
