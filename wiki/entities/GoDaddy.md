---
title: "GoDaddy"
type: entity
tags: [company, customer-support, chatbot, case-study]
sources: [ai-engineering-ch04-evaluate-ai-systems, ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# GoDaddy

Domain registrar and web-hosting company. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "Migrating from GPT-3.5-turbo-0301 to GPT-3.5-turbo-1106 led to … an improvement in GoDaddy's customer support chatbot."

## Significance

The "improvement" half of Ch 4's canonical paired anecdote with [[Voiceflow]] (which lost 10% intent classification on the same migration). Together they argue *"the best model overall might not be the best model for your application"* — a model update is good for one app and bad for another.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[Voiceflow]] — paired counter-case study.
- [[CommercialModel]] — the model class involved.
- [[openai|OpenAI]] — model provider.
- [[Evaluation]] — the discipline that catches this.

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

Ch 5 features GoDaddy in a **second, distinct role**: the **canonical [[PromptDecomposition|prompt-decomposition]] case study**.

> "GoDaddy (2024) found that the prompt for their customer support chatbot bloated to over 1,500 tokens after one iteration. After decomposing the prompt into smaller prompts targeting different subtasks, they found that their model performed better while also reducing token costs." — Ch 5

This is one of Ch 5's strongest production-data points: prompt decomposition can improve **both** performance and cost — a rare double-win in prompt engineering. The GoDaddy data anchors the chapter's argument that monolithic prompts should be the exception, not the default.

So GoDaddy appears twice in the wiki's *AI Engineering* corpus:
- **Ch 4**: model-update beneficiary (GPT-3.5-turbo-0301 → 1106 helped their chatbot).
- **Ch 5**: prompt-decomposition success story (1,500-token prompt → decomposed → better + cheaper).

Both anecdotes are from the same customer-support chatbot. The combined picture: GoDaddy's customer-support engineering team is one of the wiki's recurring production-AI case-study sources.
