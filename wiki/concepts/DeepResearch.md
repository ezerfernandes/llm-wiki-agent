---
title: "Deep Research (Agent)"
type: concept
tags: [agents, agentic-design-patterns, planning, deep-research, information-synthesis, tool-use, research-automation]
sources: [agentic-design-patterns-ch06-planning, agentic-design-patterns-ch17-reasoning]
last_updated: 2026-06-07
---

# Deep Research

**Deep Research** is the class of agentic systems that automate end-to-end information retrieval and synthesis by *planning a research trajectory*, iteratively searching real-world sources, evaluating what they find, and consolidating the result into a structured, citation-rich report. In [[AgenticDesignPatterns|*Agentic Design Patterns*]] (Gulli) — [[agentic-design-patterns-ch06-planning|Chapter 6, Planning]] — Deep Research is the headline real-world exemplar of the [[Planning]] pattern, showing dynamic, iterative planning at production scale.

## Why it exemplifies planning
A Deep Research agent is not a single query-response event; it is a **managed, long-running process** that:
1. **Deconstructs** a user prompt into a multi-point research plan (decomposition into sub-goals / sub-questions — see [[TaskDecomposition]]).
2. **Executes** an iterative search-and-analysis loop, dynamically formulating and refining queries based on what it gathers — actively identifying knowledge gaps, corroborating data points, and resolving discrepancies (**dynamic re-planning**).
3. **Synthesizes** the vetted information into a structured, multi-page report with citations to original sources.

The chapter's Key Takeaway captures the loop concisely: Google Deep Research *"reflects, plans, and executes"* — combining [[Reflection]], [[Planning]], and [[ToolUse]] (web search as a tool).

## Two implementations detailed in Ch 6

### Google Gemini DeepResearch
Built on [[gemini|Gemini]], it iteratively queries **Google Search** as a tool. It presents the generated multi-point plan to the user for **review and modification before execution** (collaborative shaping of the research trajectory — a [[HumanInTheLoop]]-style checkpoint), then runs the search loop **asynchronously** so the long investigation (which can analyze hundreds of sources) is resilient to single-point failures and lets the user disengage and be notified on completion. It can also blend user-provided documents with web research. The final interactive report includes an audio overview, charts, and links to cited sources, and explicitly returns the full list of sources searched as citations for transparency.

### OpenAI Deep Research API
An [[openai|OpenAI]] API exposing an advanced agentic model that independently **reasons, plans, and synthesizes**. It breaks a high-level query into sub-questions, performs web searches via built-in tools, and returns a structured, citation-rich report. Named models: `o3-deep-research-2025-06-26` (high-quality synthesis) and `o4-mini-deep-research-2025-06-26` (faster, latency-sensitive). It is called via `client.responses.create` with a `web_search_preview` tool (optionally `code_interpreter` or custom **MCP** tools). Distinctive properties:
- **Structured, cited output** — inline citations linked to source metadata so claims are verifiable.
- **Transparency** — unlike the abstracted ChatGPT experience, the API exposes all intermediate steps: the agent's reasoning, the exact web-search queries it executed, and any code it ran. Useful for debugging and analysis.
- **Extensibility** — supports the [[ModelContextProtocol|Model Context Protocol (MCP)]], letting developers connect the agent to private knowledge bases and internal data, blending public web research with proprietary information.

## Why it matters in agentic systems
Deep Research is the canonical demonstration that the [[Planning]] pattern scales from simple sequential task execution (e.g. the chapter's CrewAI plan-then-write example) to **complex, dynamic systems** that create iterative research plans which adapt and evolve based on continuous information gathering. It automates the iterative search-and-filter cycle that is the core bottleneck of manual research, reducing selection bias by processing a larger volume and variety of sources than a human could in comparable time.

## As a Reasoning Technique (Gulli, Ch 17)

[[agentic-design-patterns-ch17-reasoning|Chapter 17 (Reasoning Techniques)]] revisits Deep Research as the **culmination** of the chapter's reasoning techniques — the application that shows how they combine into agents executing complex, long-running tasks autonomously. It names the major platforms — **[[Perplexity|Perplexity AI]]**, **[[gemini|Google Gemini]]** research, and **[[openai|OpenAI]]'s** advanced ChatGPT functions — and frames the key UX shift: a standard search returns links (leaving synthesis to you), whereas Deep Research takes a **"time budget" (usually a few minutes)** and returns a detailed report. During that budget the AI works agentically through four steps:

1. **Initial Exploration** — multiple targeted searches from the initial prompt.
2. **Reasoning and Refinement** — read/analyze the first wave of results, synthesize, and critically identify gaps, contradictions, or areas needing more detail.
3. **Follow-up Inquiry** — conduct new, more nuanced searches to fill those gaps.
4. **Final Synthesis** — compile all validated information into a single cohesive, structured summary.

The chapter ties this to the [[ScalingInferenceLaw|Scaling Inference Law]] (the time budget *is* the thinking budget) and provides a **hands-on code example**: Google's open-sourced **DeepSearch** in the `gemini-fullstack-langgraph-quickstart` repository (React frontend + [[langgraph|LangGraph]] backend, [[gemini|Gemini 2.5]], Apache 2.0). The backend graph (`backend/src/agent/graph.py`) cycles `generate_query → web_research → reflection → finalize_answer`, with a conditional edge that loops back to `web_research` while *"more research needed"* and exits to `finalize_answer` when context is sufficient — a concrete realization of the reflect-then-search loop (Fig. 6 shows multiple [[Reflection|Reflection]] steps).

## Connections
- [[Planning]] — the pattern Deep Research exemplifies (dynamic, iterative, adaptive).
- [[ReasoningTechniques]] / [[agentic-design-patterns-ch17-reasoning]] — Ch 17 frames Deep Research as the culmination of the reasoning techniques.
- [[ScalingInferenceLaw]] — the "time budget" is the inference-thinking budget.
- [[langgraph|LangGraph]] — backend orchestration of the open-source DeepSearch quickstart.
- [[Perplexity]] — named alongside Gemini/OpenAI as a major Deep Research platform.
- [[agentic-design-patterns-ch06-planning]] — source.
- [[AgenticDesignPatterns]] — the book hub.
- [[Reflection]] — Deep Research "reflects, plans, and executes"; reflection drives knowledge-gap detection and re-planning.
- [[react|ReAct]] — the underlying think-act-observe loop the iterative search performs.
- [[ToolUse]] / [[FunctionCalling]] — Google Search / `web_search_preview` / `code_interpreter` invoked as tools inside the plan.
- [[TaskDecomposition]] — query → sub-questions / multi-point plan.
- [[ModelContextProtocol|MCP]] — extensibility for private data in the OpenAI Deep Research API.
- [[gemini|Gemini]] / [[google|Google]] — Gemini DeepResearch.
- [[openai|OpenAI]] — the Deep Research API and `o3`/`o4-mini` deep-research models.
- [[HumanInTheLoop]] — Gemini's "edit plan before research" review checkpoint.
- [[autoresearch]] — adjacent autonomous-research concept in the wiki.
