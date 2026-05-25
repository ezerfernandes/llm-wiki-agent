---
title: "Write Action"
type: concept
tags: [agents, tools, safety, security]
sources: [ai-engineering-ch06-rag-agents, ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Write Action

**Write action** is the third of [[ChipHuyen|Huyen]]'s three tool categories in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]: tools that **mutate the environment** — make changes to data sources, send messages, initiate transactions. Sister categories: [[KnowledgeAugmentation]] (read-only data access) and [[CapabilityExtension]] (model-deficiency fixes).

## The read vs write distinction

> *"Actions that allow an agent to perceive the environment are read-only actions, whereas actions that allow an agent to act upon the environment are write actions."*

The same tool surface (SQL executor, email API, banking API) often exposes both — `SELECT` is read; `INSERT`/`UPDATE`/`DELETE` is write. Email reading is read; email sending is write.

## What write actions enable

> *"Write actions enable a system to do more. They can enable you to automate the whole customer outreach workflow: researching potential customers, finding their contacts, drafting emails, sending first emails, reading responses, following up, extracting orders, updating your databases with new orders, etc."*

The autonomy unlock is what makes agents categorically different from RAG: a RAG system *informs* the user; a write-enabled agent *acts on behalf of* the user.

## The safety thesis

> *"Just as you shouldn't give an intern the authority to delete your production database, you shouldn't allow an unreliable AI to initiate bank transfers."*

Huyen names three policy mechanisms:

1. **Trust calibration** — for high-stakes actions, require explicit human approval before execution (or let humans execute).
2. **Tool-output sanitization** — defend against [[IndirectPromptInjection|indirect prompt injection]] (Ch 5) — tool outputs can carry malicious instructions.
3. **Per-action automation-level declaration** — the system must clearly define what level of automation is allowed for each action.

## Beyond the physical/digital distinction

The intuition pump that *"self-driving cars are scary because they're physical"* is a misdirection. Per Ch 6: *"An AI system can cause harm without a presence in the physical world. It can manipulate the stock market, steal copyrights, violate privacy, reinforce biases, spread misinformation and propaganda."*

Write actions are the **mechanism** by which an AI system causes real-world consequences, regardless of whether those consequences are physical or digital.

## Connections

- [[Agent]] / [[ToolInventory]] — what write actions are a category within.
- [[KnowledgeAugmentation]] / [[CapabilityExtension]] — sibling read-side tool categories.
- [[IndirectPromptInjection]] — the most-relevant attack surface (Ch 5).
- [[FunctionCalling]] — the API by which write actions are invoked.
- [[Hallucination]] — the failure mode that makes write actions dangerous.
- [[ai-engineering-ch06-rag-agents]] — primary source.

## From [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]]

Ch 10 places write actions in the **architectural** narrative as the source of the most-capable but most-dangerous step in the reference architecture (Step 5, after [[Agent|agent]] patterns):

> *"A model's outputs also can be used to invoke write actions, such as composing an email, placing an order, or initializing a bank transfer. Write actions allow a system to make changes to its environment directly. As discussed in Chapter 6, write actions can make a system vastly more capable but also expose it to significantly more risks. Giving a model access to write actions should be done with the utmost care."* — Ch 10

The Ch 10 framing makes the architectural cost explicit: write actions extend the failure surface that [[observability]], [[Guardrail|guardrails]], and [[HumanInTheLoopApproval|human approval]] all have to cover. The chapter's broader thesis — *"each additional component can potentially make your system more capable, safer, or faster but will also increase the system's complexity"* — applies most acutely to write actions, which is why Huyen positions them last in the additive architecture walkthrough.
