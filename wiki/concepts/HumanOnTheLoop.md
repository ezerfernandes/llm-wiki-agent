---
title: "Human-on-the-Loop"
type: concept
tags: [agentic-design-patterns, agents, hitl, oversight, supervision, policy, escalation]
sources: [agentic-design-patterns-ch13-human-in-the-loop]
last_updated: 2026-06-07
---

# Human-on-the-Loop

**Human-on-the-loop (HOTL)** is the **supervisory** variation of [[HumanInTheLoop|Human-in-the-Loop]] in which *"human experts define the overarching policy, and the AI then handles immediate actions to ensure compliance"* ([[AntonioGulli|Gulli]], [[AgenticDesignPatterns|*Agentic Design Patterns*]], [[agentic-design-patterns-ch13-human-in-the-loop|Ch 13]]). The human operates at the **policy and oversight level** — setting the rules and monitoring outcomes — rather than being in the critical path of each individual decision. The AI executes high-speed actions autonomously, bounded by the slower, strategic guidance of the human.

## On-the-loop vs in-the-loop

| | **In-the-loop** | **On-the-loop** |
|---|---|---|
| Human role | Validator / approver / collaborator on individual actions | Policy-setter and supervisor of an autonomous system |
| Position | In the critical path of each decision | Above the loop — watching, intervening by exception |
| AI autonomy | Pauses for human input per action | Acts continuously within human-set rules |
| Latency profile | Bounded by human response time | High-speed automated execution; human is asynchronous |
| Scales to high volume? | No (operator bottleneck) | Yes (the policy is applied automatically) |

On-the-loop is Gulli's answer to HITL's primary caveat — **lack of scalability**: a human cannot approve millions of transactions, but a human *can* author the policy that governs millions of automated executions, retaining oversight without being the throughput bottleneck.

## Worked examples (Gulli)
- **Automated financial trading** — a human expert sets the strategy/rules ("maintain 70% tech / 30% bonds, no more than 5% in any single company, auto-sell anything that falls 10% below purchase price"); the AI monitors the market in real time and executes trades instantly when the predefined conditions are met.
- **Modern call center** — a human manager sets high-level routing policy ("any call mentioning 'service outage' → technical support specialist"; "if a customer's tone indicates high frustration, offer to connect to a human agent"); the AI handles initial interactions and **autonomously routes/escalates** per the manager's policy without per-call human intervention.

## Why it matters in agentic systems
HOTL is how teams keep **human oversight** over high-throughput autonomous agents without sacrificing scale. It pairs naturally with [[Guardrails|guardrails]] (the automated enforcement of the human-set policy) and with **escalation policies** (the exception path back to [[HumanInTheLoop|in-the-loop]] handling when the agent's confidence or authority is exceeded — a confidence-threshold-triggered [[AgentHandoff|handoff]]). The two postures are complementary, not exclusive: a system is typically on-the-loop for routine volume and falls back to in-the-loop for the long tail of ambiguous or high-stakes cases.

## Connections
- [[HumanInTheLoop]] — the parent pattern; HOTL is its supervisory variation.
- [[AgenticDesignPatterns]] / [[AgenticDesignPattern]] — the book and meta-concept; [[agentic-design-patterns-ch13-human-in-the-loop|Ch 13]] is the source.
- [[AntonioGulli]] — author.
- [[Guardrails]] — the automated enforcement layer that applies the human-set policy at machine speed.
- [[AgentHandoff]] — the escalation/handoff that drops from on-the-loop back to in-the-loop on low confidence or high stakes.
- [[GoalSettingAndMonitoring]] — monitoring is the oversight half of the on-the-loop posture.
- [[HumanInTheLoopApproval]] — the in-the-loop approval-gate counterpart for impactful actions.
