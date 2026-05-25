---
title: "Business Metric"
type: concept
tags: [evaluation, business, methodology, ai-engineering]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Business Metric

The **dollar-or-engagement metric** that an AI application's quality should ultimately drive. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "Within a business, an application must serve a business goal. The application's metrics must be considered in the context of the business problem it's built to solve."

## Mapping AI metrics to business metrics

Ch 4's customer-support chatbot example:

| Factual consistency | What it lets the business do |
|---|---|
| 80% | Automate 30% of customer support requests |
| 90% | Automate 50% |
| 98% | Automate 90% |

This **gradient** is what makes investment decisions tractable — *"if you know how much gain you can get from improving a certain metric, you might have more confidence to invest resources into improving that metric."*

## The usefulness threshold

> "It's also helpful to determine the [[UsefulnessThreshold|usefulness threshold]]: what scores must an application achieve for it to be useful? For example, you might determine that your chatbot's factual consistency score must be at least 50% for it to be useful."

Below the threshold, the application is unusable. Above it, marginal AI improvements translate to marginal business gains.

## Common business metrics

- **[[StickinessMetric|Stickiness]]** — [[DAUWAUMAU|DAU/WAU/MAU]] (daily/weekly/monthly active users).
- **[[EngagementMetric|Engagement]]** — conversations/month, session duration.
- **Revenue** — direct or attributed.
- **Cost savings** — automated tickets, fraud prevented.
- **Customer satisfaction** — NPS, CSAT.

## The dark-pattern warning

> "While an emphasis on stickiness and engagement metrics can lead to higher revenues, it may also cause a product to prioritize addictive features or extreme content, which can be detrimental to users."

Choose business metrics that align with user value, not just engagement.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[UsefulnessThreshold]] — the threshold framing.
- [[EvaluationPipeline]] — parent process.
- [[DAUWAUMAU]] / [[StickinessMetric]] / [[EngagementMetric]] — common business metrics.
- [[EvaluationDrivenDevelopment]] — the principle this connects to.
