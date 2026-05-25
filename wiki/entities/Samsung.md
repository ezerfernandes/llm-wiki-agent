---
title: "Samsung"
type: entity
tags: [company, conglomerate, data-privacy, case-study]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Samsung

South Korean conglomerate. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]], **the canonical [[ModelBuildVsBuy|build-vs-buy data-privacy cautionary tale]]**:

> "One of the most notable early incidents was when Samsung employees put Samsung's proprietary information into ChatGPT, accidentally leaking the company's secrets."

The leak was reported by *TechRadar* (April 2023). Samsung **banned ChatGPT in May 2023** in response — *"It's unclear how Samsung discovered this leak and how the leaked information was used against Samsung. However, the incident was serious enough for Samsung to ban ChatGPT in May 2023."*

## Significance

The Samsung incident is the most cited single data point in the data-privacy axis of build-vs-buy. It illustrates two distinct risks:

1. **Inadvertent leakage** — employees treating an external API as if it were internal.
2. **Training-data risk** — *"there's a risk that the API provider will use your data to train its models."*

Together with [[Zoom]]'s August 2023 ToS-update backlash, it's why companies with strict data privacy policies often categorically rule out external model APIs.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[Zoom]] — sibling data-privacy case study.
- [[ModelBuildVsBuy]] — the decision framework this informs.
- [[CommercialModel]] — the model class whose data-handling is in question.
- [[openai|OpenAI]] — provider of the model in question.
