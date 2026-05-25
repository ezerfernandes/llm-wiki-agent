---
title: "Nelson F. Liu"
type: entity
tags: [person, researcher, author, nlp, stanford, rag-evaluation]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Nelson F. Liu

**First author of *"Evaluating verifiability in generative search engines"*** (Liu, Zhang & [[PercyLiang|Liang]], 2023, arXiv:2304.09848) — the paper that defines the **four-axis [[RAGEvaluation|RAG-evaluation]] taxonomy** Ch 8 of *Hands-On LLMs* names as the canonical evaluation framework for generative search systems. Stanford PhD student at the time of publication, working with [[PercyLiang|Percy Liang]].

Note: distinct from the *Nelson Liu* who is first author of *"Lost in the Middle: How Language Models Use Long Contexts"* (different paper, **same author** — Nelson F. Liu, Stanford NLP). The [[lostinthemiddle]] paper is cited in [[hands-on-llm-ch06-prompt-engineering|Ch 6]] of the same book.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 cites the verifiability paper as the source of its **four-axis RAG-evaluation taxonomy**:

- **[[Fluency]]** — *"whether the generated text is fluent and cohesive."*
- **[[PerceivedUtility|Perceived utility]]** — *"whether the generated answer is helpful and informative."*
- **[[CitationRecall|Citation recall]]** — *"the proportion of generated statements about the external world that are fully supported by their citations."*
- **[[CitationPrecision|Citation precision]]** — *"the proportion of generated citations that support their associated statements."*

The footnote reads: *"Nelson F. Liu, Tianyi Zhang, and Percy Liang. 'Evaluating verifiability in generative search engines.' arXiv preprint arXiv:2304.09848 (2023)."*

## Why the paper matters

Before Liu / Zhang / Liang 2023, RAG evaluation was fragmented: retrieval-side metrics ([[MAP]] / [[NDCG]] / [[MRR]]) measured the retriever; generation-side metrics ([[bleu|BLEU]] / [[ROUGE]] / [[BERTScore]]) measured the LLM. Neither captured the **verifiability** property — *do the citations actually support the claims?* — that distinguishes RAG from generic Q&A.

The four-axis taxonomy makes this gap explicit by adding [[CitationRecall|citation recall]] + [[CitationPrecision|citation precision]] alongside [[Fluency|fluency]] + [[PerceivedUtility|perceived utility]]. The paper runs human evaluations on four commercial generative search engines (Bing Chat / NeevaAI / perplexity.ai / YouChat) and finds **only 51.5% of generated sentences are fully supported by citations on average** — *"existing generative search engines often fail to meet the lower bound of citation precision and recall."*

## Connections

- [[RAGEvaluation]] — the multi-axis evaluation surface this paper anchors.
- [[CitationRecall]] / [[CitationPrecision]] / [[Fluency]] / [[PerceivedUtility]] — the four axes.
- [[PercyLiang]] — last author, Stanford NLP professor.
- [[stanforduniversity]] — institutional affiliation.
- [[RAGAS]] — the LLM-as-a-judge automation library Ch 8 names as the canonical operationalization.
- [[llmasjudge]] — the technique used to automate the axes.
- [[lostinthemiddle]] — the same author's other widely-cited NLP paper.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
