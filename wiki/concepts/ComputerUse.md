---
title: "Computer Use"
type: concept
tags: [agents, computer-use, gui-agents, automation, multimodal, agentic-design-patterns]
sources: [agentic-design-patterns-appendices-bg]
last_updated: 2026-06-07
---

# Computer Use

**Computer use** (a.k.a. GUI agents / Agent–Computer Interfaces) is the capability that lets an AI agent perceive and operate a computer's **Graphical User Interface** — icons, buttons, text fields — the way a human does, rather than through developer-dependent API and system calls. As framed in [[agentic-design-patterns-appendices-bg|*Agentic Design Patterns* Appendix B]] (Gulli), this lets agents automate digital tasks through the visual "front door" of software, making automation far more flexible than rigid, brittle scripting.

## How it works (the GUI-interaction loop)
The book describes a four-stage loop:
1. **Visual Perception** — the agent captures a screenshot of the screen.
2. **GUI Element Recognition** — it parses the image into a structured layout of interactive components (distinguishing a clickable "Submit" button from a static banner or an editable field).
3. **Contextual Interpretation** — an **ACI (Agent–Computer Interface) module** bridges the visual data to the agent's core LLM reasoning, mapping UI affordances to meaning (a magnifying-glass icon ⇒ "search"; radio buttons ⇒ a choice) so the agent can plan from visual evidence.
4. **Dynamic Action and Response** — the agent programmatically drives the mouse and keyboard (click, type, scroll, drag) while continuously monitoring the screen for feedback, reacting to pop-ups, loading screens, and errors across multi-step workflows.

## Named systems (Appendix B)
- **[[anthropic|Anthropic]] Computer Use** — Claude as a direct desktop user via screenshots + programmatic mouse/keyboard, orchestrating workflows across multiple unconnected apps.
- **[[openai|OpenAI]] ChatGPT Operator** — desktop task automation (e.g. spreadsheet → CRM, travel booking) without per-service API access.
- **[[google|Google]] Project Mariner** — a research-prototype agent operating inside the Chrome browser.
- **[[BrowserUse]]** — an open-source library exposing a high-level API over the **DOM** for programmatic browser automation.

## Real-world / physical environment (related)
The same appendix extends "interaction" beyond the screen to the physical world via multimodal agents: Google **Project Astra**, **[[gemini|Gemini]] Live**, OpenAI **[[GPT|GPT-4o]]** (Realtime API, speech-to-speech), OpenAI **ChatGPT Agent**, and Microsoft **Seeing AI** (accessibility narration).

## Why it matters in agentic systems
Computer use is a powerful form of [[ToolUse|tool use]] / actuation: it gives agents a *universal* interface to any software with a GUI, eliminating the need for bespoke API integrations. It is also a key vector for the safety concerns the book raises (OpenAI's ChatGPT Agent ships with a "System Card" and explicit-authorization safeguards), since an agent that can act on a real desktop has real-world consequences. See [[guiagents]], [[AgenticAI]].

## Connections
- [[agentic-design-patterns-appendices-bg]] — source.
- [[guiagents]] — sub-concept / synonym (GUI agents).
- [[BrowserUse]] — DOM-automation library.
- [[ToolUse]] / [[FunctionCalling]] — computer use as actuation.
- [[anthropic]] / [[openai]] / [[google]] — vendors of named computer-use systems.
