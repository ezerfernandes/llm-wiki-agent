---
title: "Exception Handling and Recovery (Agentic Pattern)"
type: concept
tags: [agents, agentic-design-patterns, exception-handling, recovery, reliability, fault-tolerance, retries, fallbacks, graceful-degradation, escalation, self-correction, control-flow]
sources: [agentic-design-patterns-ch12-exception-handling, agentic-design-patterns-ch18-guardrails]
last_updated: 2026-06-07
---

# Exception Handling and Recovery (Agentic Pattern)

**Exception Handling and Recovery** is the agentic design pattern that makes an agent **durable and resilient**: it detects operational failures (failed tool calls, unavailable services, malformed or incoherent outputs, timeouts), responds to them with a deliberate strategy, and restores the agent to a stable, operational state instead of crashing. It is the 12th of the 21 patterns in [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] (see [[agentic-design-patterns-ch12-exception-handling|Ch 12]]). Where the prior [[GoalSettingAndMonitoring|Goal Setting and Monitoring]] pattern *detects* deviation from the goal, this pattern supplies the *recovery* arm — turning *"fragile and unreliable systems into robust, dependable components."*

> "For AI agents to operate reliably in diverse real-world environments, they must be able to manage unforeseen situations, errors, and malfunctions… intelligent agents need robust systems to detect problems, initiate recovery procedures, or at least ensure controlled failure." — Ch 12

## Why it matters in agentic systems
Agents act in unpredictable environments through fallible tools and external services. A single failed [[ToolUse|tool call]] — bad input, a network blip, a 404/500, a service that's down — can derail a multi-step task, and unhandled failures **compound** across long autonomous chains (see [[CompoundErrorAccumulation]]). This pattern is what lets an agent be deployed in *critical or complex applications where consistent performance is essential*; without it, agents are fragile and prone to complete failure.

## The three stages
The pattern is an outer loop of **Error Detection → Error Handling → Recovery** (Ch 12, Fig. 1).

### 1. Error Detection
Identifying operational issues as they arise:
- **Invalid / malformed tool outputs** or **incoherent responses** that deviate from the expected format.
- **Specific API errors** — e.g. 404 (Not Found), 500 (Internal Server Error), 503 (Service Unavailable).
- **Timeouts** — unusually long response times from services or APIs.
- **Proactive monitoring** by other agents or specialized monitoring systems, to *"catch potential issues before they escalate."* (This is the [[GoalSettingAndMonitoring|monitoring]] half of the previous pattern, repurposed for fault detection.)

### 2. Error Handling — five strategies
Once an error is detected, a thought-out response plan engages:
1. **Logging** — record error details meticulously for later debugging and analysis. See [[Logging]] / [[StructuredLogging]].
2. **Retries** — retry the action/request, *"sometimes with slightly adjusted parameters, especially for transient errors."* The robust implementation is [[ExponentialBackoff|exponential backoff with jitter]] (and [[Idempotency|idempotent]] operations so a retry can't double-apply a side effect).
3. **Fallbacks** — switch to an alternative strategy/method so *some* functionality is maintained (the chapter's ADK example wires an explicit fallback handler).
4. **[[GracefulDegradation|Graceful degradation]]** — when full recovery isn't immediately possible, maintain **partial functionality to provide at least some value**.
5. **Notification** — alert human operators or other agents when human intervention or collaboration is required (the on-ramp to **escalation**).

### 3. Recovery — restoring a stable state
- **State rollback** — reverse recent changes or transactions to undo the effects of the error (see [[RollbackStrategy]]; pairs with [[Idempotency]]).
- **Diagnosis** — a thorough investigation into the *cause* to prevent recurrence.
- **Self-correction / replanning** — adjust the agent's plan, logic, or parameters so it doesn't make the same error again (a [[Planning|replanning]] step; closely related to [[Reflection|reflection]]).
- **Escalation** — in complex or severe cases, delegate the issue to a human operator or a higher-level system. This is the bridge to [[HumanInTheLoop|Human-in-the-Loop]] (Ch 13): notification/escalation is HITL invoked on failure.

## Coupling with Reflection
The chapter explicitly notes this pattern *"may sometimes be used with [[Reflection|reflection]]."* If an initial attempt fails and raises an exception, a reflective process can analyze the failure and **reattempt with a refined approach** (e.g. an improved prompt). Recovery's self-correction step is reflection scored against a failure signal rather than open-ended self-critique.

## Hands-on realization (Google ADK)
The chapter's worked example builds a fault-tolerant location lookup in [[GoogleADK|Google ADK]] as a layered `SequentialAgent` (`robust_location_agent`) with three sub-agents executed in guaranteed order (all `gemini-2.0-flash-exp`):

1. **`primary_handler`** — tries the precise tool `get_precise_location_info`.
2. **`fallback_handler`** — inspects shared `state["primary_location_failed"]`; if `True`, extracts the city from the user's query and calls the coarser `get_general_area_info`; if `False`, does nothing.
3. **`response_agent`** — reads `state["location_result"]` and presents it, **apologizing if it's empty**.

```
robust_location_agent = SequentialAgent(
    sub_agents=[primary_handler, fallback_handler, response_agent]
)
```

The `SequentialAgent` enforces the order so the fallback only fires after the primary records its failure in state — *"a layered approach to location information retrieval."* This is the fallback + graceful-degradation strategy expressed in ADK's [[GoogleADK|sub-agent + session-state]] substrate.

## Practical applications
Customer-service chatbots (catch a DB/API error → inform user / suggest retry later / escalate to a human, don't crash) · automated trading ("insufficient funds"/"market closed" → log, *avoid repeatedly retrying the invalid trade*, adjust strategy) · smart-home automation (network/device failure → detect, retry, then notify the user / suggest manual intervention) · data-processing agents (skip a corrupted file, log it, continue the batch, report skipped files at the end — a [[DeadLetterQueue|dead-letter]]-style park-and-continue) · web-scraping agents (CAPTCHA / changed structure / 404 / 503 → pause, use a proxy, report the failing URL) · robotics & manufacturing (failed pickup via sensor feedback → readjust, retry, escalate to a human if persistent).

## Relation to software-engineering reliability primitives
This pattern is the direct transposition of classic software resilience into agentic systems (the chapter cites McConnell's *Code Complete* and two multi-agent fault-tolerance papers). It composes with the wiki's existing reliability toolkit: [[ExponentialBackoff]] (retry timing), [[Idempotency]] (safe retries), [[CircuitBreaker]] (stop hammering a dead dependency), [[GracefulDegradation]] (partial service under failure/overload), [[RollbackStrategy]] (undo to a stable state), and [[DeadLetterQueue]] (park the un-processable). Note these primitives predate the agentic framing; Gulli names logging/retries/fallbacks/graceful-degradation/rollback/escalation explicitly, while circuit breaker and backoff are the standard implementations behind "retry transient errors" and "stop calling a failing service."

## As a guardrail layer (Ch 18)
[[agentic-design-patterns-ch18-guardrails|Chapter 18 (Guardrails/Safety Patterns)]] reuses this pattern as part of the layered guardrail defense: *"Error handling and resilience are also essential. Anticipating failures and designing the system to manage them gracefully includes using try-except blocks and implementing retry logic with [[ExponentialBackoff|exponential backoff]] for transient issues. Clear error messages are key for troubleshooting."* In Ch 18's [[crewai|CrewAI]] policy-enforcer example, the `validate_policy_evaluation` guardrail and `run_guardrail_crew` are wrapped in try-except blocks that log and return graceful failure verdicts rather than crashing — exception handling protecting the guardrail itself. See [[Guardrail]].

## Connections
- [[Guardrail]] / [[agentic-design-patterns-ch18-guardrails]] — Ch 18 reuses error-handling/resilience (try-except, retry with exponential backoff, graceful failure) as a guardrail layer.
- [[AgenticDesignPatterns]] — the book hub; [[agentic-design-patterns-ch12-exception-handling|Ch 12]] is the source. The meta-concept is [[AgenticDesignPattern]].
- [[GoalSettingAndMonitoring]] — the prior pattern; monitoring detects the deviation that this pattern recovers from (shared feedback loop ending in adapt/replan/**escalate**).
- [[HumanInTheLoop]] — escalation/notification on failure is HITL; the next pattern (Ch 13).
- [[ToolUse]] — failed tool calls are the central failure source this pattern guards.
- [[Reflection]] — analyze a failed attempt and retry with a refined prompt (explicit coupling).
- [[Planning]] — self-correction = replanning to avoid recurrence.
- [[Logging]] / [[StructuredLogging]] — the diagnostic record handling writes to.
- [[ExponentialBackoff]] / [[Idempotency]] — robust, safe retries for transient errors.
- [[GracefulDegradation]] — maintain partial functionality.
- [[RollbackStrategy]] — restore a stable state (state rollback).
- [[CircuitBreaker]] / [[DeadLetterQueue]] — adjacent reliability primitives the pattern composes with.
- [[FeedbackLoop]] — detection → handling → recovery is a control loop.
- [[CompoundErrorAccumulation]] — the failure-compounding risk this pattern counters in long agent chains.
- [[GoogleADK]] / [[gemini|Gemini]] — the hands-on `SequentialAgent` (primary → fallback → response) example.
- [[LangChain]] / [[LangGraph]] / [[CrewAI]] — the book's other framework families.
- [[AntonioGulli]] — author.
