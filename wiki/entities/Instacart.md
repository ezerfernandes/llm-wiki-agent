---
title: "Instacart"
type: entity
tags: [company, grocery-delivery, ai-deployer]
sources: [ai-engineering-ch01-intro, ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Instacart

Public grocery-delivery company. Cited in [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]] for its **internal prompt marketplace** — a notable enterprise pattern for democratizing prompt engineering across an organization. Huyen reports that the most popular prompt template Instacart found was **"Fast Breakdown"**, which asks AI to summarize meeting notes, emails, and Slack conversations into facts, open questions, and action items, with action items inserted into a project-tracking tool and auto-assigned. This is the chapter's canonical worked example of [[InformationAggregation|information aggregation]] in an enterprise.

## Connections

- [[InformationAggregation]] — the use case Instacart's prompt marketplace surfaces.
- [[WorkflowAutomation]] — action-item routing.
- [[FoundationModelUseCases]] — enterprise info-aggregation pattern.
- [[ai-engineering-ch01-intro]] — Ch 1 source.

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

Ch 5 references Instacart's **Prompt Exchange** as the canonical example of an **internal prompt marketplace** at one organization — same artifact Ch 1 introduced ("Fast Breakdown" template), now positioned in Ch 5 as the practitioner instance of the [[PromptCatalog|prompt catalog]] pattern.

> "Some organizations have internal prompt marketplaces for employees to share and reuse their best prompts, such as Instacart's Prompt Exchange." — Ch 5

The Prompt Exchange is the internal-marketplace counterpart to public marketplaces like [[PromptHero]], [[PromptBase]], and [[CursorDirectory]]. Same model — share, upvote, reuse — scoped to one company's needs and proprietary prompts.
