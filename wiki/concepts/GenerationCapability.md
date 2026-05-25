---
title: "Generation Capability"
type: concept
tags: [evaluation, criteria, ai-engineering, nlg]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Generation Capability

The **second bucket** of evaluation criteria in [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]'s taxonomy — *"how coherent or faithful the summary is."* Generation capability covers the qualities of open-ended outputs.

## Historical NLG roots

NLG (natural language generation) metrics — fluency, coherence, faithfulness, relevance — predate generative AI. Some have been repurposed for foundation models, but as FM outputs became human-indistinguishable, fluency and coherence became less important. They remain useful for *"weaker models or for applications involving creative writing and low-resource languages,"* evaluable via [[LLMAsAJudge|AI judges]] or [[Perplexity|perplexity]].

## What dominates today: factual consistency and safety

Per Ch 4, two metrics matter most for modern generation evaluation:

- **[[FactualConsistency|Factual consistency]]** — *"hallucinations are desirable for creative tasks, not for tasks that depend on factuality."* Splits into [[LocalFactualConsistency|local]] (against given context) and [[GlobalFactualConsistency|global]] (against open knowledge).
- **[[Safety|Safety]]** — *"an umbrella term for all types of toxicity and biases."* Six categories: inappropriate language, harmful tutorials, hate speech, violence, stereotypes, political/religious bias.

## Other generation-quality dimensions

Application-specific qualities Huyen names from her own work:
- **Controversiality** — content that's not harmful but causes heated debates.
- **Friendliness**, **positivity**, **creativity**, **conciseness**.

Each can typically be evaluated via [[LLMAsAJudge|AI judges]] with a custom rubric.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[DomainSpecificCapability]] / [[InstructionFollowingCapability]] / [[CostAndLatency]] — sibling buckets.
- [[FactualConsistency]] / [[Safety]] — the two metrics that dominate.
- [[Hallucination]] — what factual-consistency metrics detect.
- [[LLMAsAJudge]] / [[Perplexity]] — the dominant evaluation methods.
