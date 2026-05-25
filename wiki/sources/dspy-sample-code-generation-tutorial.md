---
title: "DSPy Tutorial — Sample Code Generation from Documentation"
type: source
tags: [dspy, tutorial, chain-of-thought, code-generation, signatures, web-scraping]
date: 2026-05-24
source_file: raw/dspy-sample-code-generation-tutorial.md
---

## Summary

Official [[DSPy]] tutorial demonstrating a **documentation-powered code generation system** — a [[DSPyModules|`dspy.Module`]] subclass (`DocumentationLearningAgent`) that composes **two custom [[DSPySignatures|Signatures]] under [[chainofthought|`dspy.ChainOfThought`]]** (`LibraryAnalyzer` for documentation analysis, `CodeGenerator` for code synthesis) and fronts them with an external HTTP-fetching layer (`requests` + `BeautifulSoup` + `html2text`) to learn libraries from their own documentation URLs and produce working code examples. **Demonstrates the *rapid technology adoption* use case** the tutorial names explicitly — using DSPy to ingest a previously-unknown library's docs and emit runnable examples. **Fills the *meta-programming / code-generation* application rung** in the DSPy tutorial corpus; sits alongside [[dspy-ai-text-game-tutorial]] as a Programming-stage-only receipt (no [[DSPyOptimizers|Optimizer]], no [[DSPyMetrics|metric]], no eval set). The worked examples are [[FastAPI]] and Streamlit; the canonical output is a JWT-authentication FastAPI snippet with explanation + best-practices list.

## Key Claims

- **Two-stage Signature composition under `dspy.Module`** is the structural core: `LibraryAnalyzer` consumes raw documentation markdown and emits structured analysis (core concepts, patterns, methods, installation info, examples); `CodeGenerator` consumes the structured analysis + a use-case string and emits code + imports + explanation + best practices. The same [[chainofthought|`dspy.ChainOfThought`]] Module wraps both — `dspy.ChainOfThought(LibraryAnalyzer)` and `dspy.ChainOfThought(CodeGenerator)`.
- **DSPy is *not* the fetching layer.** External Python libraries (`requests`, `beautifulsoup4`, `html2text`) own HTTP-fetching, HTML parsing, and markdown conversion *before* any LM call. The `DocumentationFetcher` class is plain Python — retry logic (3 attempts with delays), User-Agent header, scripts/styles/navigation/footer stripped via BeautifulSoup, HTML → markdown via `html2text`. DSPy receives clean markdown text as a string input field.
- **`pip install dspy requests beautifulsoup4 html2text`** — four-package dependency footprint. Smallest non-trivial DSPy tutorial dependency set after [[dspy-ai-text-game-tutorial|the text-game tutorial]] (3 packages).
- **No [[DSPyOptimizers|Optimizer]], no [[DSPyMetrics|metric]], no eval set, no benchmark dataset.** Pure Programming-stage receipt — exits at rung 1 of [[DSPyProgrammingModel|the three-stage workflow]]. The tutorial does not claim a numeric quality bar; output is qualitative ("generates working code examples").
- **Multi-stage analysis is named as a design principle**: *"Separates documentation understanding from code generation for better results."* The two-Signature decomposition is the structural payoff — `LibraryAnalyzer` does not see use-case strings; `CodeGenerator` does not see raw HTML. Each Signature has narrower I/O than a monolithic doc-to-code Signature would.
- **Three default use cases** (`Basic Setup and Hello World`, `Common Operations`, `Advanced Usage`) drive the `generate_examples_for_library()` loop; users can override with custom use cases through the `interactive_learning_session()` CLI.
- **Save/load via plain JSON** — generated examples can be persisted; consistent with the broader DSPy save/load discipline ([[dspy-optimizers]] uses the same plain-text JSON for optimized programs).

## Key Quotes

> "Separates documentation understanding from code generation for better results."

> "DSPy enables rapid technology adoption and exploration by automating documentation analysis and practical code generation."

## Code Receipt — structural

```python
import dspy
import requests
from bs4 import BeautifulSoup
import html2text

class LibraryAnalyzer(dspy.Signature):
    """Analyze library documentation to extract core concepts, patterns, methods, installation info, and examples."""
    documentation: str = dspy.InputField()
    core_concepts: list[str] = dspy.OutputField()
    patterns: list[str] = dspy.OutputField()
    methods: list[str] = dspy.OutputField()
    installation: str = dspy.OutputField()
    examples: list[str] = dspy.OutputField()

class CodeGenerator(dspy.Signature):
    """Generate working code examples for a specific use case given library analysis."""
    library_info: str = dspy.InputField()
    use_case: str = dspy.InputField()
    code: str = dspy.OutputField()
    imports: list[str] = dspy.OutputField()
    explanation: str = dspy.OutputField()
    best_practices: list[str] = dspy.OutputField()

class DocumentationLearningAgent(dspy.Module):
    def __init__(self):
        super().__init__()
        self.analyzer = dspy.ChainOfThought(LibraryAnalyzer)
        self.generator = dspy.ChainOfThought(CodeGenerator)

    def analyze_library(self, documentation: str):
        return self.analyzer(documentation=documentation)

    def generate_example(self, library_info: str, use_case: str):
        return self.generator(library_info=library_info, use_case=use_case)
```

(Field signatures reconstructed from the tutorial's prose description; the source page does not publish a full inline transcript of the two `dspy.Signature` class bodies — see [scope-limit gaps](#scope-limit-gaps).)

## Position in the DSPy Tutorial Corpus

This is the **first wiki-corpus DSPy tutorial whose central task is *code generation from documentation*** — a meta-programming application distinct from RAG, agents, NER, math, conversation, and interactive fiction. Coverage map:

| Tutorial | Task shape | Optimizer? | Distinctive structural property |
|---|---|---|---|
| [[dspy-conversation-history]] | Multi-turn chatbot | — | `dspy.History` field type |
| [[dspy-customer-service-agent]] | 7-tool [[react\|ReAct]] agent | — | Pydantic domain model |
| [[dspy-custom-module]] | 3-stage [[rag\|RAG]] template | — | `dspy.Module` subclass with `forward()` |
| [[dspy-tutorial-rag-as-agent]] | Multi-hop ReAct agent | MIPROv2 | Teacher/student decoupling |
| [[dspy-rag-tutorial]] | Single-hop RAG | MIPROv2 | `SemanticF1` LLM-as-judge metric |
| [[dspy-entity-extraction-tutorial]] | Decoder-LM NER | MIPROv2 | CoNLL-2003 with `list[str]` outputs |
| [[dspy-tutorial-math]] | Single-step CoT | MIPROv2 | `dspy.datasets.MATH` + 4+4 demos |
| [[dspy-ai-text-game-tutorial]] | Interactive fiction | — | 3 Signatures, deterministic state |
| **dspy-sample-code-generation-tutorial** *(this page)* | **Doc-driven code gen** | **—** | **2 Signatures + external HTTP-fetching pre-layer** |

## Structural Firsts in the Wiki

1. **First DSPy tutorial composing custom `dspy.Signature` classes with an external HTTP-fetching layer** as the pre-LLM transformation stage. Where [[dspy-tutorial-rag-as-agent]] uses [[react|ReAct]] tools to surface external data *during* the LM call, this tutorial does all fetching *before* any LM call — closer to the [[rag|RAG]] *retrieval-then-generation* split but with arbitrary URLs instead of a corpus.
2. **First DSPy tutorial naming `requests` + `beautifulsoup4` + `html2text` as the canonical web-scraping triple** for documentation-flavored inputs. Establishes the *HTML → markdown → DSPy* pre-processing pattern.
3. **First DSPy tutorial whose explicit motivating use case is *learning a library from its own docs*** — the *rapid technology adoption* framing. Distinct from RAG (Q&A over a fixed corpus) and from agents (tool-use over a defined toolset).
4. **First DSPy tutorial worked against [[FastAPI]] and Streamlit as the example libraries.** Promotes the [[FastAPI]] entity page from a 1-line stub to its second corpus appearance.

## Two-Signature Decomposition

The tutorial's most generalizable design move is splitting documentation-to-code into **two narrower Signatures** rather than a single `documentation, use_case -> code` Signature:

| Signature | Inputs | Outputs | Why narrower works |
|---|---|---|---|
| `LibraryAnalyzer` | `documentation` (raw markdown) | `core_concepts`, `patterns`, `methods`, `installation`, `examples` | Use-case-independent; can be cached and reused across many use cases for the same library. |
| `CodeGenerator` | `library_info` (structured analysis), `use_case` | `code`, `imports`, `explanation`, `best_practices` | Use-case-specific; sees structured analysis rather than raw HTML, so prompt envelope is smaller and noise is filtered. |

This is the [[DSPyProgrammingModel|*separation-of-concerns* discipline]] applied at the **Signature** layer: each Signature has a single typed I/O contract that is easier to reason about than the combined contract. The pattern echoes [[dspy-custom-module|the custom-module tutorial's]] three-stage RAG template (`generate_query → retrieve → generate_answer`) — multi-stage Signature composition under one `dspy.Module` is the canonical DSPy idiom for non-trivial pipelines.

## Connections

- [[DSPy]] — the framework being demonstrated.
- [[chainofthought|`dspy.ChainOfThought`]] — wraps both Signatures; the *start simple* default from [[dspy-programming-overview]].
- [[DSPySignatures]] — both `LibraryAnalyzer` and `CodeGenerator` are class-form Signatures; **required** here because outputs include `list[str]` containers (per [[DSPySignatures|the type-system tiers]]).
- [[DSPyModules]] — `DocumentationLearningAgent` is the `dspy.Module` subclass that composes the two Signatures.
- [[DSPyProgrammingModel]] — Programming-stage-only receipt; the tutorial exits at rung 1 of the three-stage model.
- [[DSPyPredict]] — not used directly; [[chainofthought|`dspy.ChainOfThought`]] is the chosen Module.
- [[FastAPI]] — the worked-example library; first wiki receipt where [[FastAPI]] is the *subject* of an LM-driven analysis rather than the *implementation* of an ML serving layer.
- [[Streamlit]] — the second worked-example library; forward reference.
- [[BeautifulSoup]] — HTML parsing library; forward reference.
- [[html2text]] — HTML → markdown converter; forward reference.
- [[dspy-ai-text-game-tutorial]] — sibling Programming-stage-only DSPy tutorial; both exit before [[DSPyOptimizers|Optimization]].
- [[dspy-custom-module]] — the canonical multi-Signature `dspy.Module` template (3-stage RAG); this tutorial is its 2-stage analogue applied to documentation.
- [[dspy-tutorial-rag-as-agent]] — alternative pattern for external-content access (in-call [[react|ReAct]] tool calls vs pre-call HTTP fetching).
- [[rag|RAG]] — adjacent pattern; this tutorial uses *retrieval-then-generation* over arbitrary URLs without a fixed corpus or vector index.

## Contradictions

None with the existing wiki. The tutorial reinforces:

- The [[chainofthought|`dspy.ChainOfThought`]] *start simple* default — both Signatures are wrapped in `ChainOfThought` with no justification given; it's the unexamined choice.
- The [[DSPySignatures|class-form mandatory for container-typed outputs]] discipline ([[dspy-ai-text-game-tutorial|cross-confirmed]] by the text-game tutorial's `list[str]` / `dict[str, int]` outputs).
- The pattern that **Programming-stage-only DSPy tutorials skip both metric and Optimizer** ([[dspy-ai-text-game-tutorial|sibling receipt]]) — the absence is deliberate when output quality is qualitative.

## Scope-Limit Gaps

- **No full code transcript** — the tutorial source the fetched page renders is a high-level walk-through; the exact `dspy.Signature` class bodies and field annotations are inferred from the prose description, not transcribed verbatim. A second pass against the canonical DSPy GitHub source would resolve this.
- **No quality measurement** — generated FastAPI / Streamlit code is shown but never run, tested, or scored. No metric. No comparison to a hand-written baseline. No comparison across LM choices.
- **No [[DSPyOptimizers|Optimizer]]** — the tutorial does not optimize either Signature against any metric; the *"could be optimized with [[MIPROv2]] over an authored use-case test set"* extension is unexplored.
- **No LM specified** — the tutorial walk-through does not name which LM the `ChainOfThought` modules run against (likely `openai/gpt-4o-mini` by tutorial-corpus convention, but not stated).
- **No multi-library cross-validation** — the *interactive_learning_session* claims to "Learn multiple libraries in one session", but the example output only covers FastAPI; Streamlit is named as a target URL set but no Streamlit output is shown.
- **No prompt-injection / supply-chain hardening** — the system fetches arbitrary URLs supplied by the user and feeds raw HTML-to-markdown content into the LM context. No discussion of malicious documentation pages.
- **No caching layer for the analysis stage** — the `LibraryAnalyzer` output is reusable across many use cases for the same library; the tutorial does not propose persisting it.
