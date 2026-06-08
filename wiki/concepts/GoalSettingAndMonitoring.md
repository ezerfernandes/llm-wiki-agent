---
title: "Goal Setting and Monitoring (Agentic Pattern)"
type: concept
tags: [agents, agentic-design-patterns, goal-setting, monitoring, feedback-loop, smart-goals, self-evaluation, course-correction, control-flow]
sources: [agentic-design-patterns-ch11-goal-setting, agentic-design-patterns-ch19-evaluation]
last_updated: 2026-06-07
---

# Goal Setting and Monitoring (Agentic Pattern)

**Goal Setting and Monitoring** is the agentic design pattern that gives an agent (1) **specific, measurable objectives** to work toward and (2) a **mechanism to track its own progress** and determine whether those objectives have been met. It is the 11th of the 21 patterns in [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] (see [[agentic-design-patterns-ch11-goal-setting|Ch 11]]). Where [[GoalOriented|goal-orientation]] is the *characteristic* of working toward objectives, this pattern is the concrete *machinery* — defining the goals, the success criteria, and the monitoring loop that closes around them.

> This is the **agentic self-management** sense of "monitoring." For the MLOps/production sense (tracking deployed-system health, drift, latency, cost) see [[Monitoring]] and [[observability]] — same word, different referent. Gulli makes this split explicit in [[EvaluationAndMonitoring|Ch 19 (Evaluation and Monitoring)]], which is the *external* measurement counterpart to this *internal* loop: Ch 11 asks "am I making progress toward my goal?"; Ch 19 ([[agentic-design-patterns-ch19-evaluation|source]]) asks "is this deployed agent good, fast, cheap, safe, and not degrading?"

## Why it matters
Without defined objectives, an agent cannot independently tackle complex, multi-step problems, and *"there is no inherent mechanism for them to determine if their actions are leading to a successful outcome."* This caps autonomy at mere reactive task execution. The pattern *"embeds a sense of purpose and self-assessment into agentic systems,"* transforming a reactive agent into a **proactive, goal-driven, self-managing** one capable of reliable autonomous operation in dynamic, real-world scenarios.

## The two halves

### 1. Goal setting
- **Goal definition** — an explicit, high-level objective (e.g. "resolve the customer's billing inquiry," "safely transport passengers from A to B").
- **Goal decomposition** — breaking that objective into intermediate steps / **sub-goals**, the bridge to the [[Planning]] pattern and [[TaskDecomposition|task decomposition]] (initial state → goal state).
- **Success criteria / metrics** — *"clearly defining metrics and success criteria is essential for effective monitoring."* Goals are made operational as a measurable checklist (e.g. "simple," "functionally correct," "handles edge cases"; or accuracy + completion-time metrics; or false-positive/negative rates). Goals should be **[[SMARTGoals|SMART]]** — Specific, Measurable, Achievable, Relevant, Time-bound.

### 2. Monitoring
- **What is observed** — *"monitoring involves observing agent actions, environmental states, and tool outputs."*
- **Progress tracking / observability** — the monitor continuously compares current state against the goal/criteria.
- **Feedback loop** — the monitoring signal feeds a [[FeedbackLoop|feedback loop]] that lets the agent *"assess its performance, correct its course, and adapt its plan if it deviates from the path to success."* The three downstream actions: **adapt**, **revise the plan (replan)**, or **escalate** the issue (e.g. hand off to a human).

## How it works — the self-evaluation loop
The hands-on example (an autonomous coding agent) runs an iterative cycle of **creation → self-evaluation → improvement**:

1. **Generate** a candidate solution from the prompt (use case + the goals list).
2. **Self-review** the output against every item on the goal checklist (the agent as its own QA inspector) — a [[Reflection|reflection]] step.
3. **Verdict** — an [[LLMAsAJudge|LLM judge]] renders a binary `True` (all criteria met) / `False` (falls short) decision on whether the goals are met.
4. **If `False`** — use the self-critique to pinpoint weaknesses and rewrite; **loop back to step 1**.
5. **Stop** when the verdict is `True` *or* a predefined attempt cap is reached (the demo uses `max_iterations = 5`) — the cap prevents the loop from *"running forever."*

```
Prompt ─▶ Generate ─▶ Self-Review + Quality Checklist ─▶ [If Good?]
                            ▲                              │ True ─▶ Output
                            └──────── False (revise) ◀─────┘
```

## Caveats (course-correction is not free)
- **Goal misinterpretation** — *"an LLM may not fully grasp the intended meaning of a goal and might incorrectly assess its performance as successful."*
- **Self-judge conflict-of-interest** — *"when the same LLM is responsible for both writing the code and judging its quality, it may have a harder time discovering it is going the wrong direction."* The more robust fix is to **separate roles across a crew of agents** (a distinct Code Reviewer / judge, a Test Writer, etc. — see [[MultiAgentCollaboration]]), which *"significantly improves objective evaluation."*
- **Hallucination + verification** — LLMs *"do not produce flawless code by magic; you still need to run and test the produced code"*; the LLM-only self-monitor is illustrative, not production-grade.
- **Non-termination** — a naive monitoring loop risks running forever without an iteration/budget cap.

## In Google's ADK
*"In Google's ADK, goals are often conveyed through agent instructions, with monitoring accomplished through state management and tool interactions"* — i.e. goals live in the agent's instruction prompt, and progress is tracked via the shared session state and the outputs of the tools the agent calls ([[GoogleADK|Google ADK]]).

## Practical applications
Customer support (resolve inquiry, escalate if unresolved) · personalized learning (track accuracy + completion-time, adapt) · project management (monitor task statuses, flag delays, suggest corrective actions) · automated trading (maximize gains within risk tolerance, adjust on threshold breach) · robotics & autonomous vehicles (monitor environment + own state + route) · content moderation (track false-pos/neg, escalate ambiguous cases).

## Connections
- [[GoalOriented]] — the characteristic this pattern operationalizes.
- [[Planning]] / [[TaskDecomposition]] — goal-setting supplies the objective the planner decomposes into sub-goals.
- [[Prioritization]] — Ch 20; once goals/sub-goals exist, prioritization ranks them by urgency/importance/dependencies, and monitoring's replan/escalate arm triggers dynamic re-prioritization when progress stalls.
- [[Reflection]] — the self-review-and-revise inner loop is a reflection cycle, scored against explicit success criteria.
- [[FeedbackLoop]] — the control-theoretic loop monitoring closes (monitor → assess → correct).
- [[SMARTGoals]] — the prescribed goal-quality criteria.
- [[LLMAsAJudge]] / [[SelfEvaluation]] / [[SelfCritique]] — the success-verdict mechanism.
- [[GoalFailure]] — the failure mode this pattern guards against (and that self-judging can mask).
- [[ExceptionHandlingAndRecovery]] — the next pattern (Ch 12); monitoring's escalate/replan arm hands off to detection → handling → recovery when an operational failure (not just a quality miss) occurs.
- [[MultiAgentCollaboration]] — role separation (writer vs reviewer) as the robust monitoring design.
- [[Monitoring]] / [[observability]] — the MLOps sense; cross-referenced as distinct.
- [[EvaluationAndMonitoring]] — Ch 19; the *external* evaluation/measurement counterpart to this *internal* self-management loop.
- [[GoogleADK]] / [[LangChain]] / [[openai|OpenAI]] / [[gemini|Gemini]] / [[CrewAI]] — frameworks/models in the chapter's examples.
- [[AgenticDesignPatterns]] — the book hub; [[agentic-design-patterns-ch11-goal-setting|Ch 11]] is the source.
