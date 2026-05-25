---
title: "Maarten Grootendorst"
type: entity
tags: [person, author, nlp, llm, open-source]
sources: [hands-on-llm-ch01-introduction-to-llms, hands-on-llm-ch02-tokens-and-embeddings, hands-on-llm-ch03-looking-inside-llms, hands-on-llm-ch04-text-classification, hands-on-llm-ch05-text-clustering-topic-modeling, hands-on-llm-ch06-prompt-engineering, hands-on-llm-ch07-advanced-text-generation, hands-on-llm-ch08-semantic-search-and-rag, hands-on-llm-ch09-multimodal-llms, hands-on-llm-ch10-creating-text-embedding-models, hands-on-llm-ch11-fine-tuning-representation-models, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# Maarten Grootendorst

Co-author (with [[JayAlammar]]) of *[[HandsOnLLM|Hands-On Large Language Models]]* ([[OReilly|O'Reilly Media]], 2024, ISBN 978-1-098-15096-9). Open-source NLP author; creator of **BERTopic** (topic modeling on Transformer embeddings + UMAP + HDBSCAN + class-based TF-IDF) and **KeyBERT** (keyword extraction with BERT embeddings) — two of the most widely-adopted modern NLP topic / keyword libraries. Also publishes the *"A Visual Guide to"* explainer series (e.g., *A Visual Guide to Mamba and State Space Models*, referenced in Ch 1 footnote 12).

## In *Hands-On LLMs*

In Ch 1 ([[hands-on-llm-ch01-introduction-to-llms]]), Grootendorst's BERTopic / clustering background is visible in the chapter's framing of **clustering tasks** as an application surface (mentioned as a Ch 5 forward reference) — the book treats embedding-based unsupervised clustering as a first-class LLM application alongside classification, search, and chat. The chapter explicitly forward-references Ch 5 for using bag-of-words and dense embeddings together.

## Connections

- [[JayAlammar]] — co-author.
- [[HandsOnLLM]] — the book.
- [[OReilly]] — publisher.
- [[HuggingFace]] — the model hub his book centers its tooling on.
- [[Embedding]] / [[bert|BERT]] — the embedding foundations BERTopic / KeyBERT build on.
- [[hands-on-llm-ch01-introduction-to-llms]] — Ch 1 source page.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — Ch 2 source page. Grootendorst's text-embedding / BERTopic / KeyBERT background underwrites Ch 2's text-embeddings section ([[SentenceTransformers]] + `all-mpnet-base-v2`).
- [[hands-on-llm-ch03-looking-inside-llms]] — Ch 3 source page. Grootendorst's *"A Visual Guide to"* explainer series (mentioned in Ch 1) is the pedagogical sibling of Ch 3's diagrams-first treatment of Transformer internals.
- [[hands-on-llm-ch04-text-classification]] — Ch 4 source page. The chapter's zero-shot-with-label-embeddings recipe — embed both documents and label descriptions in a shared space, then cosine-similarity-assign — is directly in line with Grootendorst's BERTopic ethos: **embeddings are versatile, frozen, and the right substrate for unsupervised and zero-shot NLP**.
- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — Ch 5 source page. **Grootendorst's signature chapter**: the book walks his own [[BERTopic]] framework end-to-end on his own [[ArXivNLP|`maartengr/arxiv_nlp`]] dataset (44,949 cs.CL abstracts) — embed with `gte-small` → UMAP → HDBSCAN → [[ClassBasedTFIDF|c-TF-IDF]] → optional [[KeyBERTInspired]] / [[MaximalMarginalRelevance|MMR]] / [[GenerativeTopicLabeling|GPT-3.5-labeling]] representation models. The chapter is also the wiki's first substantive coverage of his [[KeyBERT]] package.
- [[hands-on-llm-ch06-prompt-engineering]] — Ch 6 source page. Opens Part III on generative-model prompting; introduces the seven-component modular prompt + chain-prompting + chain-of-thought / self-consistency / tree-of-thought + grammar-constrained decoding via llama-cpp-python and GGUF Phi-3. The generalization of Ch 5's `[DOCUMENTS]`/`[KEYWORDS]` topic-labeling prompt template to the seven-component framework is a direct continuation of Grootendorst's BERTopic-side prompt-engineering work.
- [[hands-on-llm-ch07-advanced-text-generation]] — Ch 7 source page. The wiki's first LangChain-centric chapter — walks Model I/O / Chains / Memory / Agents at runnable-code granularity. The chapter's modular [[LangChain]] framing (chains as composable Lego blocks; memory as plug-in components; agents as `prompt | llm | tools` composition) echoes Grootendorst's BERTopic-side modularity ethos — swappable representation models in BERTopic ↔ swappable chain links in LangChain.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — Ch 8 source page. The book's headline **[[rag|RAG]] chapter**. Grootendorst's [[BERTopic]] reranking-pattern from Ch 5 (*"reranking an initial set of results is a main staple in neural search, a subject that we cover in Chapter 8"*) is directly cashed in: the [[ReRanking]] section of Ch 8 generalizes the same *"generate cheap candidates broadly, refine expensively on a small set"* pattern that BERTopic's representation models apply at the topic level.
- [[hands-on-llm-ch09-multimodal-llms]] — Ch 9 source page. The book's **vision-language chapter** — multimodal embeddings ([[CLIP]] / [[OpenCLIP]]) and multimodal generative LLMs ([[BLIP2|BLIP-2]]). Grootendorst's [[BERTopic]] *embeddings-are-versatile* ethos extends naturally here: Ch 9's [[MultimodalEmbeddingSpace|shared text-image vector space]] is precisely the artifact BERTopic-style downstream pipelines (topic modeling / search / clustering) would consume; the chapter explicitly names *"clustering of both images and keywords"* via CLIP as one of CLIP's four applications. The chapter is also the wiki's first runnable end-to-end vision-language pipeline.

## Open-source NLP packages

- **[[BERTopic]]** (2022, [[2203.05794-bertopic|arXiv:2203.05794]]) — modular topic-modeling framework.
- **[[KeyBERT]]** (2020) — BERT-embedding-based keyword extraction.
- Maintains the *"A Visual Guide to"* explainer series.
- Curator of the **[[ArXivNLP|`maartengr/arxiv_nlp`]]** Hugging Face dataset used as Ch 5's worked example.

## From Hands-On LLMs Ch 12

[[hands-on-llm-ch12-fine-tuning-generation-models|Ch 12]] — co-authored by Grootendorst — **completes the 12-chapter Hands-On LLMs ingest** (third fully-ingested book in the wiki after [[ai-engineering-chip-huyen|*AI Engineering*]] and [[LLMEngineersHandbook|*LLM Engineer's Handbook*]]). The chapter walks the **two-stage fine-tuning pipeline for generative LLMs** end-to-end on [[TinyLlama|TinyLlama-1.1B]] via [[QLoRA]] + the Hugging Face stack ([[transformers]] + [[peft|PEFT]] + [[bitsandbytes]] + [[trl|TRL]]) on a free Google Colab Tesla T4: **Stage 1** [[SFTTrainer|SFTTrainer]] on [[UltraChat]]; **Stage 2** [[DPOTrainer|DPOTrainer]] on `argilla/distilabel-intel-orca-dpo-pairs`. Grootendorst's BERTopic-side *swappable modular components* ethos surfaces in the chapter's structural point that the regime ([[SupervisedFinetuning|SFT]] vs [[DPO]]) is *"just a swap of the trainer + dataset on top"* of the QLoRA substrate.

Grootendorst's native-language-eval discipline becomes a Ch 12 anecdote: Grootendorst tests new models with Dutch prompts, Alammar with Arabic — the chapter's framing that *"you are the best evaluator"* is grounded in this personal practice.
