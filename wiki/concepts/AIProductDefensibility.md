---
title: "AI Product Defensibility"
type: concept
tags: [strategy, moat, business, ai-engineering]
sources: [ai-engineering-ch01-intro]
last_updated: 2024-12-04
---

# AI Product Defensibility

**The moat structure of an AI application — how it stays competitive when the underlying foundation model is also available to competitors.** Per [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]], defensibility is a core consideration in AI-application planning because **the low entry barrier of AI engineering is both a blessing and a curse**: if it's easy to build, it's also easy for competitors to build.

## The three sources of competitive advantage

Huyen identifies three durable moats:

1. **Technology** — historically the AI moat, but with foundation models *"the core technologies of most companies will be similar"* (everyone uses the same underlying models via API).
2. **Data** — *"if a startup can get to market first and gather sufficient usage data to continually improve their products, data will be their moat."* Even if the data can't be used to train models, usage information shapes the product.
3. **Distribution** — *"the distribution advantage likely belongs to big companies."*

With foundation models, **technology converges; data and distribution become durable**.

## The "OpenAI wrappers" risk

> *"A running joke in the early days of generative AI is that AI startups are OpenAI or Claude wrappers."*

The structural risk: *if the underlying model expands in capabilities, the layer you provide might be subsumed by the model, rendering your application obsolete.* Huyen's PDF-parsing example — if you built one assuming [[ChatGPT|ChatGPT]] can't parse PDFs well, you're in trouble the next time OpenAI ships a PDF-parsing upgrade. **Mitigations**:
- Use open-source models so you can offer self-hosted versions.
- Target verticals where the FM-provider has weak distribution.
- Build data-collection-and-feedback loops that lock in a per-customer moat.

## The "feature of Google Docs" risk

A general partner at a major VC firm (quoted in Ch 1): *"she's seen many startups whose entire products could be a feature for Google Docs or Microsoft Office. If their products take off, what would stop Google or Microsoft from allocating three engineers to replicate these products in two weeks?"*

Counterpoints Huyen cites: **Calendly** could've been a Google Calendar feature; **Mailchimp** could've been a Gmail feature; **[[Photoroom]]** could've been a Google Photos feature. *"Many startups eventually overtake bigger competitors, starting by building a feature that these bigger competitors overlooked."*

## The "data flywheel" phrase

> *"During the process of writing this book, I could hardly talk to any AI startup without hearing the phrase 'data flywheel.'"* — Ch 1 footnote.

This captures the prevailing AI-startup theory of defensibility: get to market first → gather usage data → improve product → attract more users → gather more data.

## Connections

- [[AIEngineering]] — discipline this strategy concern is embedded in.
- [[UseCaseEvaluation]] — defensibility is one of the planning sub-questions.
- [[ModelAsAService]] — MaaS commoditization is the root cause of the defensibility threat.
- [[DatasetEngineering]] — data-moat realization layer.
- [[Photoroom]] — the chapter's worked example of a successful "feature could've been Google Photos" startup.
- [[ai-engineering-ch01-intro]] — primary source.
