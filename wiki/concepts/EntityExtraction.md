---
title: "Entity Extraction"
type: concept
tags: [nlp, information-extraction, ner, entity-extraction, dspy, llm-task]
sources: [dspy-entity-extraction-tutorial, hands-on-llm-ch11-fine-tuning-representation-models, dspy-email-extraction-tutorial]
last_updated: 2026-05-24
---

# Entity Extraction

**Entity extraction** is the [[InformationExtraction|information-extraction]] task of **returning the subset of an input text that refers to entities of interest** — usually persons, organizations, locations, dates, or domain-specific types (chemicals, products, gene names). It is the practical, application-shaped counterpart to [[NamedEntityRecognition|Named-Entity Recognition (NER)]]: where **NER** assigns a **label to every token** (using [[BIOTagging|BIO]] or similar tag schemes — `B-PER`, `I-PER`, `O`, etc.), **entity extraction** returns only the **mentions that match** — a list of tokens or spans, often without per-token labels at all.

The distinction is operational, not formal: every NER system can be reduced to an extractor by filtering for non-`O` tokens; every extractor can be lifted to NER by inserting `O` tags for non-matches. But the **API surface** differs:

| Task framing | Input | Output | Canonical eval |
|---|---|---|---|
| **NER** | sequence of tokens | sequence of BIO tags, same length | span-level [[seqeval]] F1 |
| **Entity extraction** | text or token list | subset (list of tokens / spans / typed records) | exact-match / list-F1 / per-record F1 |

## Why the distinction matters in 2026

The rise of **decoder LLMs as the default NLP substrate** has made entity extraction the more natural framing for many production pipelines. An encoder-NER model emits a **dense BIO tag sequence** — every token gets a label — which a downstream consumer must then collapse into entity records. A decoder LLM, prompted with a [[DSPySignatures|typed Signature]] or a JSON schema, emits **the records directly** — there is no intermediate BIO surface. This is the framing the [[dspy-entity-extraction-tutorial|DSPy Entity Extraction tutorial]] makes canonical:

```python
class PeopleExtraction(dspy.Signature):
    """Extract contiguous tokens referring to specific people..."""
    tokens: list[str] = dspy.InputField()
    extracted_people: list[str] = dspy.OutputField()
```

The output is **`list[str]` of the matching tokens** — no per-token labels, no BIO tags. The [[LanguageModel|LM]] is responsible for the subset-selection decision; the framework is responsible for typed I/O and prompt synthesis.

## Two operational templates

### 1. Encoder fine-tuning (classical)

The classical template — documented in the wiki via [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]: a [[BERT|BERT]]-class encoder (`bert-base-cased`, etc.) fine-tuned with a **per-token classification head** on a [[BIOTagging|BIO]]-tagged dataset like [[CoNLL2003|CoNLL-2003]]. Eval is span-level [[seqeval]] F1. Inference returns BIO tags; a post-processing step collapses contiguous `B-XXX I-XXX` runs into entity records.

### 2. Decoder LLM with structured output (modern)

The modern template — documented via [[dspy-entity-extraction-tutorial|the DSPy Entity Extraction tutorial]]: a decoder LLM (e.g., `gpt-4o-mini`) wrapped in a [[DSPyModules|Module]] like [[ChainOfThought|`dspy.ChainOfThought`]] over a typed [[DSPySignatures|Signature]] that declares the output schema as `list[str]` or `list[EntityRecord]`. Optimization is via [[PromptOptimization|prompt optimization]] (e.g., [[MIPROv2|`dspy.MIPROv2`]]) against a metric. The tutorial's worked receipt: **86.0% exact-list-match zero-shot → 93.0% after MIPROv2** on [[CoNLL2003|CoNLL-2003]] person extraction (200-example test slice, `gpt-4o-mini`, $0.26 USD total).

## When to use which

| Decision factor | Favors encoder fine-tuning | Favors decoder LLM extraction |
|---|---|---|
| Large labeled dataset (10k+ examples) | ✓ | |
| Small labeled dataset (< 200 examples) | | ✓ |
| Strict latency / throughput requirements | ✓ (small model) | |
| Schema flexibility (new entity types frequently) | | ✓ |
| Need for per-token confidence scores | ✓ | |
| Need to extract typed records (not just spans) | | ✓ (output `list[Pydantic]`) |
| Local / on-prem deployment | ✓ (10-100M params) | depends (small LMs work; GPT-4 doesn't) |
| Multilingual / few-shot transfer | depends | ✓ |

The two templates are not mutually exclusive — a hybrid pipeline can use encoder NER as a candidate generator and a decoder LLM as a filter / typer.

## Output schema patterns

The decoder-LLM template supports richer output schemas than encoder-NER:

- **List of tokens** — `extracted_people: list[str]` (the [[dspy-entity-extraction-tutorial|tutorial pattern]]).
- **List of spans** — `extracted_people: list[tuple[int, int]]` (start/end token indices).
- **List of typed records** — `extracted_people: list[PersonRecord]` where `PersonRecord` is a [[Pydantic]] model with fields like `name: str`, `role: Optional[str]`, `confidence: float`.
- **Structured graph** — `entities: list[Entity], relations: list[Relation]` for joint entity + relation extraction.

## Connections

- [[NamedEntityRecognition]] — the classical formulation that entity extraction generalizes / reframes.
- [[BIOTagging]] — the per-token label scheme entity extraction commonly **bypasses** at the output layer.
- [[CoNLL2003]] — the canonical benchmark dataset, used by both templates.
- [[dspy-entity-extraction-tutorial]] — the wiki's canonical decoder-LLM extraction receipt.
- [[hands-on-llm-ch11-fine-tuning-representation-models]] — the wiki's canonical encoder-fine-tuning NER receipt.
- [[DSPy]] — the framework the modern template uses.
- [[ChainOfThought]] — the [[DSPyModules|Module]] the [[dspy-entity-extraction-tutorial|tutorial]] wraps the Signature in.
- [[MIPROv2]] — the optimizer the [[dspy-entity-extraction-tutorial|tutorial]] uses to lift baseline 86 → 93%.
- [[InformationExtraction]] — the broader task family entity extraction sits in.
- [[seqeval]] — the canonical span-level F1 tool, more commonly applied to the encoder-NER framing.
- [[FineTuningBert]] — the encoder-fine-tuning template's broader pattern.
- [[PromptOptimization]] — the optimization framework the modern template uses.
