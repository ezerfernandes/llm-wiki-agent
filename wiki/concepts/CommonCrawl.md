---
title: "Common Crawl"
type: concept
tags: [dataset, pretraining, corpus, web-crawl]
sources: [ai-engineering-ch02-foundation-models, hands-on-llm-ch01-introduction-to-llms]
last_updated: 2026-05-23
---

# Common Crawl

A nonprofit organization that **sporadically crawls websites on the internet**, releasing the raw text dumps publicly. As of 2022–2023, Common Crawl produced roughly **2–3 billion web pages per month**. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]], variations of Common Crawl are used in most foundation models that disclose their training data — including [[openai|OpenAI]]'s [[GPT3|GPT-3]] and [[google|Google]]'s [[gemini|Gemini]] — and presumably in most that don't disclose.

## Quality issues

Huyen's blunt summary: *"The data quality of Common Crawl, and [[c4|C4]] to a certain extent, is questionable — think clickbait, misinformation, propaganda, conspiracy theories, racism, misogyny, and every sketchy website you've ever seen or avoided on the internet."* A Washington Post study found the top 1,000 sites in the dataset include several outlets rated low on NewsGuard's trustworthiness scale.

## English bias

According to Lai et al. (2023):
- **English: 45.88%** of Common Crawl
- Russian: 5.97% (next-largest)
- 12 languages with ≥1% representation in total

Under-represented languages have world-population-to-Common-Crawl ratios of 36×–231× — Bengali at 36×, Punjabi at 231× being the chapter's most striking examples.

## Filtering recipes

Different model developers filter Common Crawl differently:
- **C4** ([[c4|Colossal Clean Crawled Corpus]], [[google|Google]]) — heavily heuristic-filtered subset; see [[c4]] for the construction recipe.
- **GPT-2 filtering** ([[openai|OpenAI]]) — used Reddit links with ≥3 upvotes as a proxy for "links people care about."

## Access restrictions tightening

Longpre et al. (2024), cited in Ch 2: between 2023 and 2024, **45% of [[c4|C4]] became fully restricted** by changes in source Terms of Service and crawling restrictions — 28% of the most critical sources became fully restricted. This is one of the chapter's two named [[ScalingBottlenecks|scaling bottlenecks]] (data).

## Connections
- [[c4]] — the canonical filtered subset.
- [[ai-engineering-ch02-foundation-models]] — primary source.
- [[LowResourceLanguage]] — the consequence of the English bias.
- [[MultilingualModel]] — models trained specifically to compensate.
- [[ScalingBottlenecks]] — Common Crawl growth vs new-data generation as the data-side bottleneck.
- [[pretraining]] — the workflow stage that consumes Common Crawl.

## In *Hands-On LLMs* Ch 1

[[hands-on-llm-ch01-introduction-to-llms|Ch 1]] cites Common Crawl as **the primary web-page training corpus for [[GPT|GPT-1]]**:

> "GPT-1 was trained on a corpus of 7,000 books and Common Crawl, a large dataset of web pages." — Ch 1

This is the chapter's earliest concrete training-data anchor for the decoder-only [[GenerativeModel|generative model]] lineage.
