---
title: "AI Interface"
type: concept
tags: [interface, ux, ai-engineering, frontend]
sources: [ai-engineering-ch01-intro]
last_updated: 2024-12-04
---

# AI Interface

**The user-facing surface through which end users interact with an AI application.** A core application-development responsibility in the [[AIEngineeringStack|AI engineering stack]]. Per [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]], the rising importance of interface design is one of the main reasons AI engineering converges toward full-stack engineering rather than classical ML engineering.

## Why interface matters more now

Before foundation models, AI was usually **embedded** in existing products (fraud detection in Stripe / Venmo / PayPal; recommender systems in Netflix / TikTok / Spotify). Foundation models flipped this: **anyone can build standalone AI applications**, so the interface itself becomes a first-class product decision.

## Common AI interface patterns (Ch 1)

| Pattern | Examples |
|---|---|
| **Standalone web / desktop / mobile apps** | [[ChatGPT]], [[Perplexity]] |
| **IDE / Office plug-ins** | [[GitHubCopilot]] (VSCode), Microsoft 365 |
| **Browser extensions** | [[Grammarly]] |
| **Chat-app integrations** | [[Midjourney]] (Discord); bots in Slack, WeChat, WhatsApp |
| **Plug-in / add-on APIs** | VSCode, Shopify, Microsoft 365 — also consumed by AI agents |
| **Voice** | Siri, Alexa, [[google\|Google]] Assistant |
| **Embodied / 3D** | [[Convai]], [[Inworld]] NPCs; AR/VR |

## Tools for building AI interfaces

Ch 1 footnote: *"Streamlit, Gradio, and Plotly Dash are common tools for building AI web apps."* The JavaScript ecosystem is growing too — LangChain.js, Transformers.js, OpenAI's Node library, Vercel's AI SDK.

## Interfaces shape feedback collection

> *"These new AI interfaces also mean new ways to collect and extract user feedback. The conversation interface makes it so much easier for users to give feedback in natural language, but this feedback is harder to extract."*

Chapter 10 of the book is the deep dive on user feedback design.

## The stack-comparison verdict

| Category | Traditional ML | Foundation models |
|---|---|---|
| AI interface | **Less important** | **Important** |

## Connections

- [[AIEngineering]] / [[AIEngineeringStack]] — discipline-level home.
- [[GitHubCopilot]] / [[ChatGPT]] / [[Grammarly]] / [[Midjourney]] / [[Perplexity]] — interface-pattern exemplars.
- [[Convai]] / [[Inworld]] — embodied / 3D interface exemplars.
- [[Agent]] / [[llmagents]] — agents consume plug-in APIs to interact with the world.
- [[ai-engineering-ch01-intro]] — primary source (Ch 1, references Ch 10 user feedback deep dive).
