---
title: "Citation Generation"
type: concept
tags: [rag, generation, citations, verifiability, hallucination-mitigation]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Citation Generation

**Citation generation** is the [[rag|RAG]] primitive that produces **explicit, mechanically-checkable links from spans of the generated answer to the source documents that grounded them**. Ch 8 of *Hands-On LLMs* demonstrates citation generation as a first-class managed-API feature via [[Cohere]] `co.chat(documents=...)`.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

The signature Ch 8 example — a [[GroundedGeneration|grounded generation]] response on the *Interstellar* corpus with `query = "income generated"`:

```python
response = co.chat(message=query, documents=docs_dict)
print(response.text)
# → "The film generated a worldwide gross of over $677 million, or $773 million with subsequent re-releases."

# The citations are returned alongside:
citations=[
    ChatCitation(start=21, end=36, text='worldwide gross',         document_ids=['doc_0']),
    ChatCitation(start=40, end=57, text='over $677 million',       document_ids=['doc_0']),
    ChatCitation(start=62, end=103, text='$773 million with subsequent re-releases.', document_ids=['doc_0']),
]
documents=[{'id': 'doc_0', 'text': 'The film had a worldwide gross over $677 million ...'}]
```

Each citation has three load-bearing properties:

- **`start` / `end` byte offsets** into the response text — pinpoint which span of the answer is being cited.
- **`text`** — the cited span verbatim (redundant given offsets, useful for display).
- **`document_ids`** — back-pointers to the document(s) supporting this span; the `documents` field returned alongside lets the consumer resolve them.

## Why it matters

Citation generation **operationalizes verifiability**. A RAG answer without citations is *"trust me, I synthesized this from the docs you sent."* A RAG answer with span-level citations is *"this span on these offsets is supported by document X."* The downstream consumer (human reviewer / programmatic checker / RAG-evaluation harness) can audit each claim against its source.

This is exactly what the [[NelsonFLiu|Liu / Zhang / Liang]] 2023 *"Evaluating verifiability in generative search engines"* paper measures via its [[CitationRecall|citation recall]] + [[CitationPrecision|citation precision]] axes — both of which require span-level citations to be computable.

## The two paths Ch 8 demonstrates

| Path | Citations available? |
|---|---|
| **Managed: [[Cohere]] `co.chat(documents=...)`** | ✓ Automatic span-level citations |
| **Local: [[Phi3Mini|Phi-3]] + [[LangChain]] `RetrievalQA(chain_type='stuff')`** | ✗ — *"we will lose the ability to do span citations"* |

The managed path's citation primitive is built into the model's output protocol; the local path's prompt-template approach (*"answer the following question using the relevant information provided above"*) doesn't emit structured citations because the LLM is generating free text.

## Connections

- [[rag]] — the parent technique family.
- [[GroundedGeneration]] — the generation step citation generation augments.
- [[CitationRecall]] — *"the proportion of generated statements about the external world that are fully supported by their citations."*
- [[CitationPrecision]] — *"the proportion of generated citations that support their associated statements."*
- [[RAGEvaluation]] — the multi-axis evaluation surface that uses these citations.
- [[CohereChat]] — the worked managed-API primitive.
- [[Hallucination]] — the failure mode citation-aware answers help detect.
- [[Faithfulness]] — the [[RAGAS|Ragas]] metric closely related to citation-supported correctness.
- [[NelsonFLiu]] / [[PercyLiang]] — authors of the verifiability paper.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
