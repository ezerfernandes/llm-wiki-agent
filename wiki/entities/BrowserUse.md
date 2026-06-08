---
title: "Browser Use"
type: entity
tags: [product, open-source, library, browser-automation, computer-use, agents, agentic-design-patterns]
sources: [agentic-design-patterns-appendices-bg]
last_updated: 2026-06-07
---

# Browser Use

**Browser Use** is an open-source library that provides a **high-level API for programmatic browser automation**, enabling AI agents to interface with web pages. Per [[agentic-design-patterns-appendices-bg|*Agentic Design Patterns* Appendix B]] (Gulli), it grants agents access to and control over the **Document Object Model (DOM)**, abstracting the intricate low-level commands of browser-control protocols into a simplified, intuitive set of functions.

## What it does
- Lets an agent perform complex action sequences: **data extraction from nested elements, form submissions, and automated navigation across multiple pages**.
- Transforms unstructured web data into a **structured format** an AI agent can systematically process for analysis or decision-making.
- Reference: https://docs.browser-use.com/introduction

## Why it matters
Browser Use is the open-source, DOM-level complement to the screenshot-driven [[ComputerUse|computer-use]] / [[guiagents|GUI-agent]] approach: instead of perceiving pixels, the agent manipulates the page's structured DOM directly — a more reliable channel for web automation.

## Connections
- [[agentic-design-patterns-appendices-bg]] — source (Appendix B).
- [[ComputerUse]] / [[guiagents]] — the broader GUI/computer-use theme.
- [[ToolUse]] — browser control as a tool/actuation channel.
