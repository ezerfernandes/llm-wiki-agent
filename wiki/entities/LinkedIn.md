---
title: "LinkedIn"
type: entity
tags: [product, platform, social-network, microsoft]
sources: [leh-ch01-understanding-llm-twin-concept, leh-ch03-data-engineering, ai-engineering-ch02-foundation-models, ai-engineering-ch04-evaluate-ai-systems, ai-engineering-ch05-prompt-engineering, ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

## What it is
LinkedIn is the professional-networking platform owned by [[microsoft|Microsoft]]. Users publish posts, articles, and updates to a feed targeted at colleagues and a professional audience.

## In LLM Engineer's Handbook
LinkedIn is one of the four crawled sources for the LLM Twin's data-collection pipeline. Ch. 1 ([[leh-ch01-understanding-llm-twin-concept]]) names LinkedIn as the **posts** category source (alongside Medium / Substack articles and GitHub code) and the downstream **publishing target** for generated LinkedIn posts. Ch. 3 ([[leh-ch03-data-engineering]]) implements a `LinkedInCrawler` (inheriting `BaseSeleniumCrawler`) that logs in, scrolls the feed, and yields `PostDocument` instances into MongoDB.

## Connections
- [[microsoft]] — owner.
- [[Medium]] / [[Substack]] / [[GitHub]] — peer crawled sources.
- [[Selenium]] / [[BeautifulSoup]] — tools used to crawl LinkedIn.
- [[WebCrawling]] — domain.
- [[LLMTwin]] — running project whose corpus includes LinkedIn data.

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

Ch 2 cites LinkedIn for a concrete **[[StructuredOutputs|structured-outputs]] engineering result**:

> "LinkedIn's defensive YAML parser increased the percentage of correct YAML outputs from 90% to 99.99%." — Bottaro and Ramgopal (2020), cited in Ch 2.

LinkedIn also illustrates a YAML-vs-JSON cost choice:

> "JSON and YAML are common text formats. LinkedIn found that their underlying model, [[GPT4|GPT-4]], worked with both, but they chose YAML as their output format because it is less verbose, and hence requires fewer output tokens than JSON."

Per Ch 1, LinkedIn is also the canonical [[LastMileChallenge|last-mile-challenge]] case study — they reached 80% of target experience in one month, then needed four more months for the final 15%.

## From [[ai-engineering-ch04-evaluate-ai-systems|AI Engineering Ch 4]]

LinkedIn is the **most-cited deployed-AI case study** in Ch 4 — multiple insights drawn from their one-year-of-generative-AI retrospective:

1. **Evaluation guideline is the first hurdle.** *"In retrospect of one year of deploying generative AI applications, LinkedIn shared that the first hurdle was in creating an evaluation guideline."*
2. **The Job Assessment counter-example.** A correct response can be a bad response. *"The response 'You are a terrible fit' might be correct but not helpful, thus making it a bad response."* A good response explains the gap and provides actionable next steps.
3. **Production human evaluation.** *"LinkedIn developed a process to manually evaluate up to 500 daily conversations with their AI systems."* This is one of the strongest practitioner data points for "human evaluation in production" in the book.

These case studies inform [[EvaluationGuideline]], [[ScoringRubric]], and [[EvaluationPipeline]] design.

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

Ch 5 contributes a **fourth LinkedIn data point** to the wiki:

> "LinkedIn found that CoT also reduces models' hallucinations."

[[chainofthought|Chain-of-thought]] prompting's hallucination-mitigation effect, attributed to LinkedIn's deployed-AI experience. This complements Ch 4's [[Hallucination|hallucination]] thread (which focused on *measurement*) by adding a **mitigation lever** from a deployed system.

The combined Ch 1 / Ch 2 / Ch 4 / Ch 5 picture: LinkedIn is the wiki's most-data-rich production-AI case study, contributing the [[LastMileChallenge|last-mile challenge]] anecdote (80% in 1mo, 95% in another 4mo), the [[StructuredOutputs|YAML-over-JSON]] choice, the YAML-defensive-parser improvement (90% → 99.99%), the *"You are a terrible fit"* [[EvaluationGuideline|evaluation-guideline]] counter-example, the 500-conversations-per-day human-evaluation practice, and now the CoT-reduces-hallucinations finding.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 adds two LinkedIn data points to the wiki's case study:

### TBT (Time Between Tokens) — the metric name

> *"Time between tokens (TBT) is used by LinkedIn and inter-token latency (ITL) is used by NVIDIA."*

LinkedIn's preferred name for the streaming-cadence latency metric. See [[TBT]].

### Throughput-vs-latency trade-off

> *"According to the LinkedIn AI team in their reflection after a year of deploying generative AI products (LinkedIn, 2024), it's not uncommon to double or triple the throughput if you're willing to sacrifice TTFT and TPOT."*

This is the **load-bearing data point for [[Goodput|goodput]]** — the explicit acknowledgment that throughput-alone optimization destroys user experience. Goodput (SLO-respecting throughput) is the better optimization target, and LinkedIn's experience is what motivates it.
