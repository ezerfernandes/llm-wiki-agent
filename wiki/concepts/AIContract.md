---
title: "AI Contract (Contractor Model)"
type: concept
tags: [agents, agentic-design-patterns, reliability, governance, contract, multi-agent]
sources: [agentic-design-patterns-ch19-evaluation]
last_updated: 2026-06-07
---

# AI Contract (Contractor Model)

The **AI "Contract"** is a control instrument proposed in [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] ([[agentic-design-patterns-ch19-evaluation|Ch 19]], drawing on the **Agent Companion** whitepaper, Gulli et al.) for the evolution **from simple AI agents to advanced "contractors"** — moving from probabilistic, often unreliable systems to **deterministic, accountable** ones designed for complex, high-stakes environments.

## The problem it solves
Today's common AI agents operate on **brief, underspecified instructions** — fine for demos but **brittle in production**, where ambiguity leads to failure. The contractor model addresses this by establishing a rigorous, formalized relationship between the user and the AI, *"much like a legal service agreement in the human world."*

## The four pillars
1. **Formalized Contract** — a detailed specification that is the *single source of truth* for a task, far beyond a simple prompt. It explicitly defines required deliverables, precise specifications, acceptable data sources, scope of work, and even expected computational cost and completion time — *"making the outcome objectively verifiable."* (E.g. not "analyze last quarter's sales" but "a 20-page PDF report analyzing European market sales from Q1 2025, including five specific data visualizations, a comparative analysis against Q1 2024, and a risk assessment…")
2. **Dynamic Lifecycle of Negotiation and Feedback** — the contract starts a *dialogue*, not a static command. The contractor agent can analyze the terms and **negotiate** — flagging ambiguities, inaccessible data sources, or risks before execution begins, preventing costly failures and aligning the output with the user's actual intent.
3. **Quality-Focused Iterative Execution** — unlike low-latency agents, a contractor prioritizes correctness via **self-validation and correction**. For a code-generation contract it generates multiple approaches, compiles and runs them against contract-defined unit tests, scores each on performance/security/readability, and submits only the version passing all criteria. This internal generate→review→improve loop is a [[Reflection|reflection]] mechanism for building trust.
4. **Hierarchical Decomposition via Subcontracts** — a primary contractor acts as a *project manager*, breaking the goal into smaller sub-tasks by generating new formal **subcontracts** (each a complete, independent contract with its own deliverables), assignable to specialized agents. Maps onto [[Planning|planning]] / [[TaskDecomposition|task decomposition]] and [[MultiAgentCollaboration|multi-agent]] orchestration.

## Contract execution flow (Fig. 2)
`Contract Submitted → Contract Assessment (feasibility, cost, duration) →` either **Contract Revision** (suggest modifications: ambiguities, cost, etc. → accepted or rejected) or **Contract Execution** (generate plan, execute tasks, generate subcontracts) `→ Task Resolution (candidate generation → review → scoring → ranking → evolution) → Contract Deliverables`. Contract Execution can loop back to suggest revisions.

## Why it matters
This embeds **formal specification, negotiation, and verifiable execution** into the agent's core logic, elevating AI from a promising-but-unpredictable assistant into a dependable system that autonomously manages complex projects with **auditable precision** — paving the way for deployment in mission-critical domains where **trust and accountability** are paramount. It is the reliability-engineering complement to the [[EvaluationAndMonitoring|Evaluation and Monitoring]] pattern.

## Connections
- [[EvaluationAndMonitoring]] — the Ch 19 pattern this concept closes; verifiable deliverables make evaluation objective.
- [[AgenticDesignPatterns]] — book hub; [[agentic-design-patterns-ch19-evaluation|Ch 19]] is the source; references the **Agent Companion** whitepaper.
- [[Reflection]] — the quality-focused iterative self-validation loop.
- [[Planning]] / [[TaskDecomposition]] — hierarchical subcontract decomposition.
- [[MultiAgentCollaboration]] — subcontracts assigned to specialized agents.
- [[Guardrail]] — formal scope/verifiability as a reliability guardrail for high-stakes tasks.
- [[DataContract]] — the data-engineering analog (a schema agreement between producer and consumer); the AI Contract generalizes the idea to whole-task agreements.
- [[AntonioGulli]] — author of the book and the Agent Companion whitepaper.
