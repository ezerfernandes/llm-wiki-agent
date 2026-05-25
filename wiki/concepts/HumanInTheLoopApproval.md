---
title: "Human-in-the-Loop Approval"
type: concept
tags: [llm-security, defense, system-design, hitl, agents]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Human-in-the-Loop Approval

**A system-level defense in which the LLM cannot execute *impactful* tool calls without explicit human review and approval.** Named in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as the structural mitigation for tool-use attacks where [[Isolation|isolation]] alone is insufficient (because the side effect — sending an email, deleting a row — happens *outside* the sandbox by design).

> "Another good practice is to not allow any potentially impactful commands to be executed without explicit human approvals. For example, if your AI system has access to an SQL database, you can set a rule that all queries attempting to change the database, such as those containing 'DELETE', 'DROP', or 'UPDATE', must be approved before executing." — Ch 5

## What counts as "impactful"

Ch 5's worked example is SQL: gate any `DELETE`, `DROP`, `UPDATE`. The pattern generalizes to:

| Tool class | Gated action |
|---|---|
| Database | `DELETE` / `DROP` / `UPDATE` / schema changes |
| Email / messaging | Sending to external recipients |
| Financial | Money movement |
| Files | Writing outside scratch space |
| Network | Outbound calls beyond an allowlist |
| Code deployment | Production deploys |

## Relation to Crawl-Walk-Run

The HITL-approval pattern is a structural application of Microsoft's [[CrawlWalkRun|Crawl-Walk-Run]] framework (Ch 1) to security — the model starts in **Crawl mode** for impactful actions (human approves every action), and graduates toward **Walk** / **Run** modes only as confidence accrues from per-action evaluation data.

## Why it complements isolation

[[Isolation|Isolation]] contains the blast radius of code execution. HITL approval prevents side effects that are *intended* to escape the sandbox — sending emails, mutating databases, calling external APIs. Both layers are needed.

## Failure mode: approval fatigue

If approval gates fire on too many actions, operators rubber-stamp them and the defense degrades to no defense. Designing approval gates to fire only on impactful actions (and to surface enough context for an informed click) is itself a design problem.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[Isolation]] — paired system-level defense.
- [[humanintheloop|Human in the loop (HITL)]] — broader pattern this specializes.
- [[CrawlWalkRun]] — Microsoft framework that places HITL approval on a deployment-ladder.
- [[DefensivePromptEngineering]] — parent discipline.
- [[Agent]] — agentic systems with side-effectful tools are the primary deployment pattern that needs this.
- [[PromptInjection]] / [[IndirectPromptInjection]] — the attacks this defense bounds.
