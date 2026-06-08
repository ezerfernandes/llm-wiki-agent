---
title: "Chapter 6 — Planning (Agentic Design Patterns)"
type: source
tags: [agentic-design-patterns, agents, planning, task-decomposition, deep-research, plan-and-execute, dynamic-replanning]
date: 2025-06-01
source_file: raw/books/agentic-design-patterns.pdf
sources: [agentic-design-patterns]
---

## Summary
Chapter 6 of [[AgenticDesignPatterns|*Agentic Design Patterns*]] (Gulli) introduces **Planning** — the agent's ability to formulate a sequence of actions that moves from an initial state to a goal state, where the plan is *created in response to the request* rather than known in advance (Agentic Design Patterns, PDF pp 100–112). It frames planning as delegating the *what* (objective + constraints) while the agent autonomously discovers the *how*, stresses **adaptability** (an initial plan is a starting point, not a rigid script) and the **flexibility-vs-predictability trade-off**, then grounds the pattern in a CrewAI plan-then-write example and two real agentic systems: **Google Gemini DeepResearch** and the **OpenAI Deep Research API**.

## Key Claims
- **Planning = synthesizing a sequence of actions from an initial state to a goal state.** It is the ability "to formulate a sequence of actions to move from an initial state towards a goal state." The plan "is not known in advance; it is created in response to the request."
- **Delegate the *what*, let the agent discover the *how*.** Think of a planning agent as a specialist to whom you delegate a complex goal ("organize a team offsite"): you define the objective and its constraints (the *what*), not the steps (the *how*). The agent must first understand the initial state (e.g., budget, participants, dates) and goal state (a booked offsite), then chart the optimal action sequence.
- **Adaptability is a hallmark.** "An initial plan is merely a starting point, not a rigid script." A capable agent that hits an obstacle (venue unavailable, caterer booked) doesn't fail — it registers the new constraint, **re-evaluates its options, and formulates a new plan** (dynamic re-planning).
- **Flexibility-vs-predictability trade-off.** Dynamic planning is "a specific tool, not a universal solution." When the solution is already well-understood and repeatable, constraining the agent to a **predetermined, fixed workflow** is more effective — it limits autonomy to reduce uncertainty and guarantee consistent outcomes. The decision hinges on one question: *"does the 'how' need to be discovered, or is it already known?"*
- **Use cases**: procedural task automation (decompose employee onboarding into a directed sequence of sub-tasks), robotics / autonomous navigation (state-space traversal optimizing time/energy under constraints), structured information synthesis (research-report generation with distinct phases: gathering, summarization, structuring, iterative refinement), and multi-step customer support (diagnosis → solution → escalation).
- **CrewAI plan-then-execute example**: a single `planner_writer_agent` (role "Article Planner and Writer") is given a `Task` that explicitly asks it to *(1) create a bullet-point plan*, then *(2) write the summary based on that plan*; the `Crew` runs `Process.sequential` and `crew.kickoff()`. Planning behavior is **explicitly prompted** by the task description and `expected_output` format (a `### Plan` section followed by a `### Summary` section).
- **Google Gemini DeepResearch** is an agent-based system for autonomous information retrieval and synthesis via a multi-step agentic pipeline that **iteratively queries Google Search**. It deconstructs the prompt into a **multi-point research plan presented to the user for review/modification before execution** (collaborative shaping of the research trajectory), then runs an iterative search-and-analysis loop, dynamically formulating/refining queries, identifying knowledge gaps, corroborating data, and resolving discrepancies. It manages the long-running process **asynchronously** (resilient to single-point failures; the user can disengage and be notified on completion). Output is a structured multi-page report with citations.
- **OpenAI Deep Research API** automates complex research with an advanced agentic model that independently **reasons, plans, and synthesizes** from real-world sources. It breaks a high-level query into sub-questions, performs web searches via built-in tools, and returns a structured, citation-rich report. Models named: `o3-deep-research-2025-06-26` (high-quality) and `o4-mini-deep-research-2025-06-26` (faster, latency-sensitive). Called via `client.responses.create` with a `web_search_preview` tool; optional `code_interpreter` and custom **MCP** tools. Key benefits: structured cited output, **transparency** (exposes reasoning, search queries, and code run — unlike abstracted ChatGPT), and **extensibility** via the [[ModelContextProtocol|Model Context Protocol (MCP)]].
- **At a Glance**: *What* — complex problems need foresight and decomposition into smaller executable tasks; without structure an agent fails to strategize. *Why* — the Planning pattern has the agent first create a coherent plan, decomposing a high-level objective into a sequence of smaller, actionable steps / **sub-goals**; LLMs are well-suited to generate plausible plans from their training data, turning a reactive agent into a strategic executor that can adapt its plan. *Rule of thumb* — use it when a request is too complex for a single action/tool and requires a sequence of interdependent operations.

## Key Quotes
> "At its core, planning is the ability for an agent or a system of agents to formulate a sequence of actions to move from an initial state towards a goal state." — Planning Pattern Overview

> "When you ask it to 'organize a team offsite,' you are defining the what—the objective and its constraints—but not the how. The agent's core task is to autonomously chart a course to that goal. ... The plan is not known in advance; it is created in response to the request." — the delegate-the-what framing

> "An initial plan is merely a starting point, not a rigid script. The agent's real power is its ability to incorporate new information and steer the project around obstacles. ... It registers the new constraint, re-evaluates its options, and formulates a new plan." — adaptability / dynamic re-planning

> "Dynamic planning is a specific tool, not a universal solution. When a problem's solution is already well-understood and repeatable, constraining the agent to a predetermined, fixed workflow is more effective. ... does the 'how' need to be discovered, or is it already known?" — the flexibility-vs-predictability trade-off

> "Google Deep Research is an agent analyzing on our behalf sources obtained using Google Search as a tool. It reflects, plans, and executes." — Key Takeaways

## Connections
- [[Planning]] — the chapter's named pattern; this source augments that concept page with Gulli's practitioner framing (initial→goal state, delegate-the-what, adaptability, flexibility-vs-predictability, goal→plan→action).
- [[AgenticDesignPatterns]] — the book hub; this is its Chapter 6 (6th of 21 patterns).
- [[AgenticDesignPattern]] — the meta-concept of reusable agent design patterns.
- [[AntonioGulli]] — author.
- [[DeepResearch]] — the agentic application class exemplifying advanced, dynamic, iterative planning (Google Gemini DeepResearch + OpenAI Deep Research API), both detailed in this chapter.
- [[react|ReAct]] — the chapter's Key Takeaway describes DeepResearch as it "reflects, plans, and executes"; planning is the deliberative half of the think-act-observe loop, distinct from per-step ReAct reasoning.
- [[Reflection]] — DeepResearch "reflects, plans, and executes"; iterative re-planning evaluates gathered information (a reflection step) before re-planning.
- [[GoalOriented|Goal-Oriented Behavior]] — planning operationalizes goal-orientation: it bridges goal → plan → action (initial state → goal state).
- [[PromptChaining]] / [[Routing]] / [[Parallelization]] / [[Reflection]] / [[ToolUse]] — the five prior patterns; planning composes them (a plan orchestrates tools, branches, and reflection steps in logical order).
- [[MultiAgentCollaboration]] — the chapter notes "an agent or a system of agents" plan; the next pattern (Ch 7) handles multi-agent coordination.
- [[CrewAI]] — framework of the hands-on plan-then-write example (`Process.sequential`, `crew.kickoff()`).
- [[gemini|Gemini]] — Google Gemini DeepResearch is built on Gemini.
- [[google|Google]] — author affiliation; DeepResearch and Google Search tool integration.
- [[openai|OpenAI]] — the Deep Research API (`o3-deep-research-2025-06-26`, `o4-mini-deep-research-2025-06-26`).
- [[ModelContextProtocol|MCP]] — the Deep Research API's extensibility mechanism for connecting to private knowledge bases/internal data.
- [[ToolUse]] / [[FunctionCalling]] — DeepResearch uses Google Search and `web_search_preview` / `code_interpreter` as tools, executed inside the plan.
- [[TaskDecomposition]] — planning decomposes a high-level objective into smaller actionable steps / sub-goals (the chapter calls plan generation "task decomposition").

## Contradictions
- vs [[Planning]] (the existing academic-symbolic-planning page, per [[2402.01817-llm-modulo|LLM-Modulo]] and [[ChipHuyen|Huyen]] AI Engineering Ch 6): the LLM-Modulo line argues LLMs *alone cannot plan soundly* and need external sound critics, whereas Gulli's chapter takes the optimistic practitioner view that "LLMs are particularly well-suited for this, as they can generate plausible and effective plans based on their vast training data." This is a **framing tension, not a strict contradiction** — Gulli says "plausible" (not "sound") plans and emphasizes dynamic re-planning/adaptation as the recovery mechanism, which is complementary to the iterate-with-critics view. Recorded on the [[Planning]] page.
