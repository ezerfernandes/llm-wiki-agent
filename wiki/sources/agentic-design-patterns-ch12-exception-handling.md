---
title: "Chapter 12 — Exception Handling and Recovery (Agentic Design Patterns)"
type: source
tags: [agentic-design-patterns, agents, exception-handling, recovery, reliability, fault-tolerance, retries, fallbacks, graceful-degradation, escalation]
date: 2025-06-01
source_file: raw/books/agentic-design-patterns.pdf
sources: [agentic-design-patterns]
---

## Summary
Chapter 12 of [[AgenticDesignPatterns|*Agentic Design Patterns*]] (Gulli) introduces **Exception Handling and Recovery** — the pattern that lets an AI agent detect operational failures (tool errors, service unavailability, malformed outputs), respond to them, and restore itself to a stable state rather than crashing (Agentic Design Patterns, PDF pp 196–203). It decomposes the pattern into three stages — **Error Detection → Error Handling → Recovery** — and catalogs the handling/recovery techniques: error logging, retries (for transient errors), fallbacks, graceful degradation, notifications/escalation to humans, state rollback, diagnosis, and self-correction/replanning. The hands-on example is a [[GoogleADK|Google ADK]] `SequentialAgent` wiring a `primary_handler`, a state-checking `fallback_handler`, and a `response_agent` into a layered, fault-tolerant location-lookup pipeline; the chapter notes the pattern is sometimes combined with [[Reflection|reflection]] (analyze a failed attempt, retry with a refined prompt).

## Key Claims
- **Definition.** The Exception Handling and Recovery pattern addresses *"the need for AI agents to manage operational failures"* — anticipating issues such as tool errors or service unavailability and developing strategies to mitigate them. It is the 12th of the 21 patterns in the book and turns *"fragile and unreliable systems into robust, dependable components."*
- **Three components (Fig. 1).** The pattern is structured as **Error Detection → Error Handling → Recovery**, an outer loop that feeds detected/handled failures back into recovery.
- **Error Detection.** Meticulously identifying operational issues as they arise: *"invalid or malformed tool outputs, specific API errors such as 404 (Not Found) or 500 (Internal Server Error) codes, unusually long response times from services or APIs, or incoherent and nonsensical responses that deviate from expected formats."* Monitoring by other agents or specialized monitoring systems enables proactive anomaly detection *"before they escalate."* (Detection can also involve **timeouts** — flagging unusually long response times — per the Key Takeaways.)
- **Error Handling — five strategies.** Once an error is detected: (1) **logging** — recording error details meticulously for later debugging and analysis; (2) **retries** — retrying the action/request, *"sometimes with slightly adjusted parameters, especially for transient errors"*; (3) **fallbacks** — using alternative strategies or methods so *"some functionality is maintained"*; (4) **graceful degradation** — where complete recovery isn't immediately possible, *"the agent can maintain partial functionality to provide at least some value"*; (5) **notification** — alerting human operators or other agents for situations requiring human intervention or collaboration.
- **Recovery — restoring a stable state.** Recovery *"is about restoring the agent or system to a stable and operational state after an error."* It can involve **state rollback** — *"reversing recent changes or transactions to undo the effects of the error"*; **diagnosis** — a thorough investigation into the cause to prevent recurrence; **self-correction / replanning** — *"adjusting the agent's plan, logic, or parameters through a self-correction mechanism or replanning process… to avoid the same error in the future"*; and **escalation** — *"in complex or severe cases, delegating the issue to a human operator or a higher-level system."*
- **Used with Reflection.** *"This pattern may sometimes be used with reflection. For example, if an initial attempt fails and raises an exception, a reflective process can analyze the failure and reattempt the task with a refined approach, such as an improved prompt, to resolve the error."*
- **Hands-On (Google ADK).** The code defines a robust location-retrieval system as an ADK `SequentialAgent` (`robust_location_agent`) with three sub-agents run in guaranteed order: `primary_handler` (tries `get_precise_location_info`), `fallback_handler` (a backup that inspects `state["primary_location_failed"]`; if `True`, extracts the city from the user's query and calls `get_general_area_info`; if `False`, does nothing), and `response_agent` (reads `state["location_result"]` and presents it, apologizing if absent). All three use `gemini-2.0-flash-exp`. *"This structure allows for a layered approach to location information retrieval."*
- **At a Glance.** *What* — agents in real-world environments inevitably hit unforeseen situations, errors, and malfunctions (tool failures, network issues, invalid data); without a structured way to manage them agents are fragile and prone to complete failure. *Why* — the pattern provides a standardized solution combining **proactive error detection** (monitoring tool outputs and API responses) with **reactive handling** (logging, retrying transient failures, fallbacks) and **recovery protocols** (revert to a stable state, self-correct by adjusting the plan, or escalate to a human). *Rule of thumb* — use it for any AI agent deployed in a dynamic, real-world environment where system failures, tool errors, network issues, or unpredictable inputs are possible and operational reliability is a key requirement.
- **Practical applications.** Customer-service chatbots (detect a DB/API error, inform the user, suggest retrying later, or escalate to a human agent — don't crash); automated financial trading (handle "insufficient funds"/"market closed" by logging, *not* repeatedly retrying the same invalid trade, and adjusting strategy); smart-home automation (network/device failure → detect, retry, then notify the user and suggest manual intervention); data-processing agents (skip a corrupted file, log it, continue the batch, report skipped files at the end rather than halting); web-scraping agents (handle CAPTCHA / changed structure / 404 / 503 by pausing, using a proxy, or reporting the failing URL); robotics & manufacturing (failed pickup detected via sensor feedback → readjust, retry, and if persistent alert a human or switch components).
- **References.** McConnell, *Code Complete* (2004); Shi et al., *Towards Fault Tolerance in Multi-Agent Reinforcement Learning* (arXiv:2412.00534, 2024); O'Neill, *Improving Fault Tolerance and Reliability of Heterogeneous Multi-Agent IoT Systems Using Intelligence Transfer* (Electronics 2022).

## Key Quotes
> "For AI agents to operate reliably in diverse real-world environments, they must be able to manage unforeseen situations, errors, and malfunctions. Just as humans adapt to unexpected obstacles, intelligent agents need robust systems to detect problems, initiate recovery procedures, or at least ensure controlled failure." — chapter opening

> "This pattern may sometimes be used with reflection. For example, if an initial attempt fails and raises an exception, a reflective process can analyze the failure and reattempt the task with a refined approach, such as an improved prompt, to resolve the error." — overview (the Reflection coupling)

> "Recovery: This stage is about restoring the agent or system to a stable and operational state after an error. It could involve reversing recent changes or transactions to undo the effects of the error (state rollback)… In complex or severe cases, delegating the issue to a human operator or a higher-level system (escalation) might be the best course of action." — Pattern Overview

> "Implementation of this robust exception handling and recovery pattern can transform AI agents from fragile and unreliable systems into robust, dependable components capable of operating effectively and resiliently in challenging and highly unpredictable environments." — Pattern Overview

> "The SequentialAgent ensures that these three agents execute in a predefined order. This structure allows for a layered approach to location information retrieval." — Hands-On Code Example (ADK)

## Connections
- [[ExceptionHandlingAndRecovery]] — the chapter's named pattern; this source is the primary source for that concept page (12th of the 21 patterns).
- [[AgenticDesignPatterns]] — the book hub; this is its Chapter 12.
- [[AntonioGulli]] — author.
- [[ToolUse]] / [[agentic-design-patterns-ch05-tool-use|Ch 5 Tool Use]] — failed tool calls (bad input, dependent external service down) are the chapter's central failure source; exception handling guards the tool-use boundary.
- [[GoalSettingAndMonitoring]] / [[agentic-design-patterns-ch11-goal-setting|Ch 11]] — monitoring detects deviations; this pattern is the *recovery* arm of the same monitor → assess → correct/escalate loop (the prior pattern's feedback loop terminates in adapt/replan/**escalate**).
- [[HumanInTheLoop]] — escalation to a human operator is the bridge to the next pattern (Ch 13); notification/escalation is HITL invoked on failure.
- [[Reflection]] / [[agentic-design-patterns-ch04-reflection|Ch 4]] — the chapter explicitly pairs exception handling with reflection: analyze the failed attempt, retry with a refined prompt.
- [[Planning]] / [[agentic-design-patterns-ch06-planning|Ch 6]] — recovery's self-correction is a *replanning* step (adjust the plan/logic to avoid recurrence).
- [[Logging]] / [[StructuredLogging]] — the diagnostic substrate the handling stage writes to.
- [[ExponentialBackoff]] — the standard implementation of the "retries for transient errors" handling strategy.
- [[GracefulDegradation]] — the explicitly-named "maintain partial functionality" handling strategy.
- [[RollbackStrategy]] — the software-engineering realization of the chapter's "state rollback" recovery step.
- [[CircuitBreaker]] / [[Idempotency]] / [[DeadLetterQueue]] — adjacent software-reliability primitives this pattern composes with (idempotency makes retries safe; a circuit breaker stops hammering a dead dependency; a dead-letter queue parks the un-processable, like the data-processing agent's skipped corrupted file).
- [[GoogleADK]] — the framework of the hands-on `SequentialAgent` (primary → fallback → response) example.
- [[gemini|Gemini]] — `gemini-2.0-flash-exp` powers all three handlers in the example.
- [[LangChain]] / [[LangGraph]] / [[CrewAI]] — the book's other framework families (named at the hub; this chapter's code is ADK-only).
- [[GracefulDegradation]] / [[RollbackStrategy]] / [[CircuitBreaker]] — the reliability/fault-tolerance toolkit the pattern delivers (the chapter's cited references are multi-agent fault-tolerance papers: Shi et al. 2024, O'Neill 2022).
- [[CompoundErrorAccumulation]] — exception handling is the counter-measure to the error-compounding risk of long autonomous agent chains.

## Contradictions
- vs [[GracefulDegradation]] (the *Hands-On LLMs* / mlsysbook serving-overload framing): **scope difference, not contradiction.** That page defines graceful degradation as a tail-latency/overload strategy (return approximate results under load); Gulli uses the term in the broader sense of *maintaining partial functionality when full recovery isn't possible*. Same principle, different triggering condition (overload vs. arbitrary failure); cross-referenced.
- vs [[Monitoring]] (MLOps production-monitoring): the chapter's "monitoring for proactive anomaly detection" is the agent-self-management sense, as flagged on [[GoalSettingAndMonitoring]]; terminology overlap, not contradiction.
- None other found.
