---
title: "Wikipedia"
type: entity
tags: [knowledge-base, web, tool]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Wikipedia

**Wikipedia** is the free, collaborative online encyclopedia — and one of the most-common **knowledge-augmentation tool targets** for LLM agents. Cited in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] alongside [[Reddit]] and X as one of the social/knowledge APIs that [[AutoGPT]] focuses on.

## Position in the wiki

Wikipedia is also the corpus underlying the wiki's existing RAG receipts — [[ColBERTv2]] over the Wikipedia 2017 abstracts dump is the canonical [[DSPy]] retrieval target ([[dspy-custom-module]] / [[hotpotqa|HotpotQA]] tasks). This dual role — both a tool target for production agents and a benchmark substrate for RAG research — is the structural reason Wikipedia keeps appearing in the wiki.

## Connections

- [[KnowledgeAugmentation]] — the tool family Wikipedia serves.
- [[AutoGPT]] — agent framework that uses Wikipedia as a tool.
- [[hotpotqa]] — benchmark built over Wikipedia.
- [[ColBERTv2]] — the retriever most commonly paired with Wikipedia in the wiki.
- [[ai-engineering-ch06-rag-agents]] — primary source.
