---
title: "DSPy Tutorial — Email Information Extraction"
type: source
tags: [dspy, tutorial, email, information-extraction, classification, chain-of-thought, pydantic, enum]
date: 2026-05-24
source_file: raw/dspy-email-extraction-tutorial.md
---

## Summary

The [[DSPy]] **Email Information Extraction** tutorial ([dspy.ai/tutorials/email_extraction](https://dspy.ai/tutorials/email_extraction/)) is the canonical receipt for **composing four [[DSPySignatures|Signatures]] into a single sequential [[DSPyModules|`dspy.Module`]] pipeline** that classifies, extracts, summarizes, and action-plans over arbitrary email content. The program is `EmailProcessor(dspy.Module)` with four [[chainofthought|`dspy.ChainOfThought`]] sub-modules — `classifier` ([[DSPySignatures|`ClassifyEmail`]]), `entity_extractor` (`ExtractEntities`), `summarizer` (`SummarizeEmail`), `action_generator` (`GenerateActionItems`) — wired in `forward(...)` so that **each stage's typed output becomes the next stage's typed input**: `classifier.email_type: EmailType` → `entity_extractor` input; `entity_extractor.key_entities: list[ExtractedEntity]` → `summarizer` + `action_generator` inputs; `summarizer.summary: str` → `action_generator.email_summary` input. The final return is a fan-in [[DSPyPrediction|`dspy.Prediction`]] aggregating 12 fields from the four sub-calls.

This is the **eleventh wiki-corpus DSPy tutorial** and slots beside [[dspy-ai-text-game-tutorial|the text-based AI game tutorial]] (three Signatures inside one Module, no Optimizer) and [[dspy-sample-code-generation-tutorial|the code-generation tutorial]] (two Signatures inside one Module, no Optimizer) on the **multi-Signature single-Module Programming-stage rung** — pipelines where the structural payoff is *how typed outputs of one Signature become typed inputs of the next* rather than optimization quality lifts. It is the **first wiki-corpus DSPy tutorial that uses an `Enum` type as both an OutputField (on `ClassifyEmail`) and an InputField (on `ExtractEntities` and `GenerateActionItems`)** — confirming the [[dspy-signatures|Signatures page's]] five-tier type system composes symmetrically across Signature boundaries when the same Enum class is referenced.

The tutorial is also the **first wiki-corpus DSPy tutorial whose central application is *email triage*** — a structurally distinct application from chatbot / agent / NER / RAG / math / code-generation / interactive-fiction, and the closest the corpus gets to the *"office productivity automation"* use case enterprise customers most commonly request. The three demo emails (order confirmation / server-outage support / Q4 meeting invite) cover the **three highest-volume business-email categories** and exercise the urgency-classification surface across all four `UrgencyLevel` values.

Three load-bearing structural claims distinguish this tutorial from prior multi-Signature DSPy tutorials:

1. **The pipeline is strictly sequential with typed handoffs**, not parallel — `forward(...)` is five linear steps (classify → extract → summarize → action → aggregate), each step's output explicitly named-and-passed into the next. No tool selection, no [[react|ReAct]] loop, no `dspy.History` thread.
2. **Custom [[Pydantic]] models compose as `list[T]` typed OutputFields *and* as `list[T]` typed InputFields** — `ExtractedEntity` is the OutputField type on `ExtractEntities` (`key_entities: list[ExtractedEntity]`) and the InputField type on `GenerateActionItems` (`extracted_entities: list[ExtractedEntity]`). Confirms the [[DSPyAdapters|Adapter]] correctly serializes-and-parses round-trips of arbitrary Pydantic models across Signature boundaries.
3. **`Optional[T]` is a valid OutputField type** — `financial_amount: Optional[float]` and `deadline: Optional[str]` declare nullable outputs the LM is expected to set to `None` when not applicable (e.g., a newsletter has no financial amount). This is the **first wiki-corpus DSPy tutorial that ships `Optional[...]` in an OutputField**.

## Key Claims

- **Four [[DSPySignatures|Signatures]] compose inside one [[DSPyModules|`dspy.Module`]] with typed inter-Signature handoffs.** The `EmailProcessor.forward(...)` method runs (1) `classifier(email_subject, email_body, sender) -> email_type, urgency, reasoning`; (2) `entity_extractor(email_content, email_type=classification.email_type) -> key_entities, financial_amount, important_dates, contact_info`; (3) `summarizer(email_subject, email_body, key_entities=entities.key_entities) -> summary`; (4) `action_generator(email_type=classification.email_type, urgency=classification.urgency, email_summary=summary.summary, extracted_entities=entities.key_entities) -> action_required, action_items, deadline, priority_score`. The data-flow graph is a **diamond** — `classifier` outputs flow to both `entity_extractor` and `action_generator`; `entity_extractor.key_entities` flows to both `summarizer` and `action_generator`. **Three of the four sub-Signatures consume at least one previously-extracted field**; only `classifier` is a leaf input node.

- **`Enum` types cross Signature boundaries as first-class.** `EmailType` (8 values: `ORDER_CONFIRMATION`, `SUPPORT_REQUEST`, `MEETING_INVITATION`, `NEWSLETTER`, `PROMOTIONAL`, `INVOICE`, `SHIPPING_NOTIFICATION`, `OTHER`) is `OutputField` on `ClassifyEmail` and `InputField` on both `ExtractEntities` and `GenerateActionItems`. `UrgencyLevel` (4 values: `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`) is `OutputField` on `ClassifyEmail` and `InputField` on `GenerateActionItems`. Both Enums inherit from `(str, Enum)` — the **string-Enum** pattern that allows the LM to emit the enum's `.value` string verbatim and have the [[DSPyAdapters|Adapter]] parse it back into the enum member. This is the [[dspy-signatures|five-tier type system's]] **Literal-set-via-Enum** alternative to `typing.Literal["..."]`; the [[DSPyOptimizers|Banking77 classification receipt]] in [[dspy-optimizers|page 13]] used `Literal[tuple(CLASSES)]` instead, demonstrating both patterns are valid.

- **Custom [[Pydantic]] models with confidence scores compose at the list level.** `class ExtractedEntity(BaseModel): entity_type: str; value: str; confidence: float` — a three-field Pydantic model — is the element type of `key_entities: list[ExtractedEntity]` (OutputField on `ExtractEntities`) and `extracted_entities: list[ExtractedEntity]` (InputField on `GenerateActionItems`) and `key_entities: list[ExtractedEntity]` (InputField on `SummarizeEmail`). The **confidence scoring is delegated to the LM** — every entity carries an LM-emitted `confidence: float ∈ [0, 1]` value alongside its `entity_type` and `value`. This is the **first wiki-corpus DSPy tutorial that embeds LM-emitted confidence scores inside structured outputs** — a [[ModelCalibration|calibration]]-adjacent surface the rest of the DSPy corpus has not exercised.

- **`Optional[T]` OutputFields signal "may not apply".** `financial_amount: Optional[float] = dspy.OutputField(desc="Any monetary amounts found (e.g., '$99.99')")` declares that the LM should return `None` when the email contains no financial information — and the framework will not error if it does. Same for `deadline: Optional[str]` on `GenerateActionItems`. The [[dspy-signatures|page 4]] five-tier type system's tier-two `typing` composites include `Optional[...]`; the email-extraction tutorial is the **first wiki-corpus receipt to use it on an OutputField** rather than an InputField. **Soft tension**: the `desc` example *"e.g., `'$99.99'`"* is a **string**, but the type is `float` — the LM is expected to parse the dollar sign off before emitting; the desc-vs-type mismatch is a minor tutorial-side inconsistency that the [[DSPyAdapters|Adapter]] absorbs at parse time.

- **Every sub-Signature is wrapped in [[chainofthought|`dspy.ChainOfThought`]], never bare [[DSPyPredict|`dspy.Predict`]].** All four sub-modules — `self.classifier`, `self.entity_extractor`, `self.action_generator`, `self.summarizer` — are `dspy.ChainOfThought(SignatureClass)`. This means every sub-call **adds a `reasoning` field under the hood** ([[chainofthought|the `dspy.ChainOfThought` mechanism]]); the user-visible `classifier.reasoning` is the one declared on `ClassifyEmail`, but the other three sub-calls **also** have a hidden `reasoning` field that is generated and discarded. This is the [[dspy-ai-text-game-tutorial|same *"start with CoT and don't justify"* default]] the AI-game tutorial follows — never argued for, just adopted. The performance penalty (extra output tokens per sub-call × four sub-calls) is the structural cost.

- **[[DSPyPrediction|`dspy.Prediction(...)`]] is the explicit fan-in aggregator.** The `forward(...)` method's final statement is `return dspy.Prediction(email_type=..., urgency=..., summary=..., key_entities=..., financial_amount=..., important_dates=..., action_required=..., action_items=..., deadline=..., priority_score=..., reasoning=classification.reasoning, contact_info=...)` — **12 named kwargs**, fanning in fields from all four sub-Signature outputs. This is the **first wiki-corpus DSPy tutorial that calls `dspy.Prediction(...)` constructor-style with > 10 kwargs**; prior tutorials either return a sub-module's `Prediction` directly (e.g., [[dspy-customer-service-agent|customer-service]] returns the `dspy.ReAct` Prediction) or aggregate fewer fields.

- **The LM is `openai/gpt-4o-mini` — single-LM throughout.** `dspy.LM(model='openai/gpt-4o-mini')` + `dspy.configure(lm=lm)`. No teacher/student split (unlike [[dspy-tutorial-rag-as-agent|the HoVer agent tutorial]]), no per-sub-module LM context (unlike a hypothetical "use GPT-4o for classification, GPT-4o-mini for extraction" pattern). All four sub-modules share the global LM, consistent with the [[dspy-ai-text-game-tutorial|text-game tutorial]] and [[dspy-sample-code-generation-tutorial|code-generation tutorial]] precedents.

- **No [[DSPyMetrics|metric]], no [[DSPyEvaluate|`dspy.Evaluate`]], no [[DSPyOptimizers|Optimizer]] — Programming-stage exit.** Like [[dspy-ai-text-game-tutorial|the text-game tutorial]] and [[dspy-sample-code-generation-tutorial|the code-generation tutorial]], the email-extraction tutorial **exits at the Programming rung** of [[DSPyProgrammingModel|the three-stage workflow]]. No training set is collected, no metric defined, no [[MIPROv2|MIPROv2]] sweep. The tutorial's *Next Steps* section names *"Different LLM experimentation and optimization strategies"* as a future direction but does not implement it. This is consistent with the **structural-receipt-only** scope of the multi-Signature single-Module tutorial cluster.

- **[[MLflow|MLflow]] integration is opt-in and limited to tracing.** The tutorial recommends optional MLflow setup for *"visualization of prompts and optimization progress, tracing DSPy behavior, experiment tracking and explainability"* but does not provide the four-step setup recipe ([[dspy-entity-extraction-tutorial|the entity-extraction tutorial]] documents in full). Since there is no optimization, the **"optimization progress"** framing is forward-looking — MLflow here is purely for **per-sub-call tracing** (visualize the four LM calls inside `forward()`).

- **The `os.environ["OPENAI_API_KEY"]` assignment happens *after* `dspy.configure(lm=lm)` in the demo function.** The code shown is `lm = dspy.LM(model='openai/gpt-4o-mini'); dspy.configure(lm=lm); os.environ["OPENAI_API_KEY"] = "<YOUR OPENAI KEY>"`. **This ordering is wrong** — the [[LiteLLM]] backend reads `OPENAI_API_KEY` at LM-invocation time, not at construction time, so the demo *does* work as written (the env var is set before the first LM call inside `processor(...)`), but the ordering is misleading. The correct pattern (set env var *first*) is documented in [[dspy-language-models|the Language Models page]]. **Minor tutorial-side documentation bug**, not a structural framework issue.

## Key Quotes

> *"This tutorial demonstrates building an intelligent email processing system using DSPy that automatically extracts, classifies, and structures information from various email types."* — opening scope statement; positions email processing as a multi-stage information-extraction task.

> *"Classification of email types (orders, support requests, meetings, newsletters, etc.); Entity extraction (dates, amounts, product names, contact details); Urgency level determination and action identification; Data structuring into consistent formats; Robust handling of multiple email formats."* — the five core capabilities the system addresses.

> *"A comprehensive email processing system using DSPy."* — the `EmailProcessor(dspy.Module)` class docstring. **Three words — "comprehensive", "email processing", "system"** — frame the application as a *system* (multi-Module) not a *function* (single-Signature).

> *"Step 1: Classify the email ... Step 2: Extract entities ... Step 3: Generate summary ... Step 4: Determine actions ... Step 5: Structure the results."* — the in-code comments inside `forward()` that document the five-step pipeline. **The fifth step is `dspy.Prediction(...)` aggregation** — packaging is treated as its own structural step, not an afterthought.

> *"The classified type of email ... The urgency level of the email ... Brief explanation of the classification."* — the three `OutputField(desc=...)` strings on `ClassifyEmail`. The `reasoning: str` OutputField is **user-declared** alongside [[chainofthought|`dspy.ChainOfThought`]]'s implicit `reasoning` field — overlapping naming, no documented conflict resolution; the user's `reasoning` field wins because it was declared on the Signature.

> *"List of extracted entities with type, value, and confidence."* — the `key_entities` OutputField desc. **Confirms the LM is expected to emit `ExtractedEntity` instances with all three fields populated**, including the `confidence: float` self-report.

> *"Whether any action is required ... List of specific actions needed ... Deadline for action if applicable ... Priority score from 1-10."* — the four OutputFields of `GenerateActionItems`. The `priority_score: int` from 1–10 is the **second classification-like surface** in the program (alongside `UrgencyLevel`); the two are correlated but the framework leaves the correlation to the LM rather than enforcing it.

> *"Different LLM experimentation and optimization strategies"* — *Next Steps* item naming the unexplored Optimization stage. The tutorial **explicitly defers** optimization to future work.

## Code Receipts

### Receipt 1 — Data structures

```python
from enum import Enum
from typing import Optional
from pydantic import BaseModel
import dspy

class EmailType(str, Enum):
    ORDER_CONFIRMATION = "order_confirmation"
    SUPPORT_REQUEST = "support_request"
    MEETING_INVITATION = "meeting_invitation"
    NEWSLETTER = "newsletter"
    PROMOTIONAL = "promotional"
    INVOICE = "invoice"
    SHIPPING_NOTIFICATION = "shipping_notification"
    OTHER = "other"

class UrgencyLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class ExtractedEntity(BaseModel):
    entity_type: str
    value: str
    confidence: float
```

### Receipt 2 — Four Signatures

```python
class ClassifyEmail(dspy.Signature):
    """Classify the type and urgency of an email based on its content."""
    email_subject: str = dspy.InputField(desc="The subject line of the email")
    email_body: str = dspy.InputField(desc="The main content of the email")
    sender: str = dspy.InputField(desc="Email sender information")
    email_type: EmailType = dspy.OutputField(desc="The classified type of email")
    urgency: UrgencyLevel = dspy.OutputField(desc="The urgency level of the email")
    reasoning: str = dspy.OutputField(desc="Brief explanation of the classification")

class ExtractEntities(dspy.Signature):
    """Extract key entities and information from email content."""
    email_content: str = dspy.InputField(desc="The full email content including subject and body")
    email_type: EmailType = dspy.InputField(desc="The classified type of email")
    key_entities: list[ExtractedEntity] = dspy.OutputField(desc="List of extracted entities with type, value, and confidence")
    financial_amount: Optional[float] = dspy.OutputField(desc="Any monetary amounts found (e.g., '$99.99')")
    important_dates: list[str] = dspy.OutputField(desc="List of important dates found in the email")
    contact_info: list[str] = dspy.OutputField(desc="Relevant contact information extracted")

class GenerateActionItems(dspy.Signature):
    """Determine what actions are needed based on the email content and extracted information."""
    email_type: EmailType = dspy.InputField()
    urgency: UrgencyLevel = dspy.InputField()
    email_summary: str = dspy.InputField(desc="Brief summary of the email content")
    extracted_entities: list[ExtractedEntity] = dspy.InputField(desc="Key entities found in the email")
    action_required: bool = dspy.OutputField(desc="Whether any action is required")
    action_items: list[str] = dspy.OutputField(desc="List of specific actions needed")
    deadline: Optional[str] = dspy.OutputField(desc="Deadline for action if applicable")
    priority_score: int = dspy.OutputField(desc="Priority score from 1-10")

class SummarizeEmail(dspy.Signature):
    """Create a concise summary of the email content."""
    email_subject: str = dspy.InputField()
    email_body: str = dspy.InputField()
    key_entities: list[ExtractedEntity] = dspy.InputField()
    summary: str = dspy.OutputField(desc="A 2-3 sentence summary of the email's main points")
```

### Receipt 3 — `EmailProcessor` Module

```python
class EmailProcessor(dspy.Module):
    """A comprehensive email processing system using DSPy."""
    def __init__(self):
        super().__init__()
        self.classifier = dspy.ChainOfThought(ClassifyEmail)
        self.entity_extractor = dspy.ChainOfThought(ExtractEntities)
        self.action_generator = dspy.ChainOfThought(GenerateActionItems)
        self.summarizer = dspy.ChainOfThought(SummarizeEmail)

    def forward(self, email_subject: str, email_body: str, sender: str = ""):
        classification = self.classifier(
            email_subject=email_subject, email_body=email_body, sender=sender
        )
        full_content = f"Subject: {email_subject}\n\nFrom: {sender}\n\n{email_body}"
        entities = self.entity_extractor(
            email_content=full_content, email_type=classification.email_type
        )
        summary = self.summarizer(
            email_subject=email_subject, email_body=email_body,
            key_entities=entities.key_entities
        )
        actions = self.action_generator(
            email_type=classification.email_type, urgency=classification.urgency,
            email_summary=summary.summary, extracted_entities=entities.key_entities
        )
        return dspy.Prediction(
            email_type=classification.email_type, urgency=classification.urgency,
            summary=summary.summary, key_entities=entities.key_entities,
            financial_amount=entities.financial_amount,
            important_dates=entities.important_dates,
            action_required=actions.action_required,
            action_items=actions.action_items, deadline=actions.deadline,
            priority_score=actions.priority_score,
            reasoning=classification.reasoning, contact_info=entities.contact_info,
        )
```

### Receipt 4 — Configuration + invocation

```python
import os
lm = dspy.LM(model='openai/gpt-4o-mini')
dspy.configure(lm=lm)
os.environ["OPENAI_API_KEY"] = "<YOUR OPENAI KEY>"
processor = EmailProcessor()
result = processor(
    email_subject="Order Confirmation - MacBook Pro #12345",
    email_body="...",
    sender="orders@apple.com",
)
# result.email_type == EmailType.ORDER_CONFIRMATION
# result.urgency == UrgencyLevel.LOW
# result.financial_amount == 2399.0
# result.priority_score == 3
```

## Demo Results

The tutorial reports successful execution on three sample emails:

| Email | `email_type` | `urgency` | `financial_amount` | Key extracted fields |
|---|---|---|---|---|
| MacBook Pro purchase | `ORDER_CONFIRMATION` | `LOW` | `$2,399.00` | tracking number, delivery date |
| Server outage alert | `SUPPORT_REQUEST` | `CRITICAL` | `None` | incident timestamp, affected service |
| Q4 planning meeting | `MEETING_INVITATION` | `MEDIUM` | `None` | meeting date, agenda items |

**No quantitative accuracy reported** — the tutorial demonstrates the *shape* of the pipeline output, not a benchmarked accuracy number. Unlike [[dspy-entity-extraction-tutorial|the entity-extraction tutorial]]'s 86.0% → 93.0% lift on CoNLL-2003, the email-extraction tutorial offers **zero quantitative claim** — consistent with its Programming-stage-only scope.

## Connections

- **[[DSPy]]** — entity. Extends [[DSPy]]'s wiki footprint with an *email-triage* application slice — the eleventh wiki-corpus DSPy tutorial.
- **[[DSPyModules|`dspy.Module`]]** — concept. `EmailProcessor(dspy.Module)` is a **four-sub-module** Module subclass — fits the [[DSPyModules|composition discipline]] from [[dspy-modules|page 5]] (sub-modules as `self.*` attributes for `named_predictors()` walks; PyTorch-shaped `__init__` + `forward()`).
- **[[DSPySignatures]]** — concept. Four Signatures composed across one `forward()` — the highest **Signature-count per Module** in the wiki's DSPy tutorial corpus (alongside [[dspy-ai-text-game-tutorial|the text-game tutorial's]] three).
- **[[chainofthought|`dspy.ChainOfThought`]]** — concept. All four sub-modules use CoT. Confirms the *"start with CoT and don't justify"* default across the multi-Signature tutorial cluster.
- **[[DSPyPredict|`dspy.Predict`]]** — concept. The minimal primitive that [[chainofthought|`dspy.ChainOfThought`]] is built on; the four CoT sub-modules each contain a [[DSPyPredict|`Predict`]] under the hood.
- **[[DSPyPrediction|`dspy.Prediction`]]** — concept. The 12-kwarg fan-in aggregator at the end of `forward()` — the largest kwarg-count Prediction construction in the wiki's DSPy tutorial corpus.
- **[[DSPyLM|`dspy.LM`]]** — concept. `dspy.LM(model='openai/gpt-4o-mini')` + `dspy.configure(lm=lm)` is the canonical [[DSPyLM]] global-bind pattern.
- **[[DSPyAdapters]]** — concept. The Adapter serializes [[Pydantic]] `ExtractedEntity` instances + Enum types both *outbound* (Signature → LM) and *inbound* (LM → typed Python). The email-extraction tutorial exercises Adapter round-trips of arbitrary Pydantic models more heavily than any prior wiki DSPy tutorial.
- **[[Pydantic]]** — entity. `ExtractedEntity(BaseModel)` is the third-tier type from [[dspy-signatures|page 4]]'s five-tier type system. Same compositional discipline [[dspy-customer-service-agent|the customer-service-agent tutorial]] used for its `Date` / `UserProfile` / `Flight` / `Itinerary` / `Ticket` domain.
- **Python `Enum`** — `EmailType` and `UrgencyLevel` are `(str, Enum)` subclasses. The **string-Enum** pattern is the [[dspy-signatures|five-tier type system's]] alternative to `typing.Literal[...]` for closed-set classification — both patterns now have wiki-corpus DSPy receipts.
- **[[EntityExtraction]]** — concept. The `ExtractEntities` Signature's `key_entities: list[ExtractedEntity]` is a **typed-record** variant of the [[EntityExtraction]] surface; unlike the [[dspy-entity-extraction-tutorial|CoNLL-2003 tutorial's]] token-list output, this tutorial emits structured `(entity_type, value, confidence)` triples (the **list-of-typed-records** schema pattern named on the [[EntityExtraction]] page).
- **[[Classification]]** — concept. `ClassifyEmail` is a **two-output classification Signature** (`email_type` + `urgency`) — the first wiki-corpus DSPy tutorial with **two simultaneous classification outputs**.
- **[[ZeroShotClassification]]** — concept. No few-shot demos are supplied; the LM zero-shot-classifies based on the Enum value names + docstring.
- **[[IntentClassifier]]** — concept. `EmailType` classification is structurally an intent-classification surface — "what *kind* of email is this".
- **[[openai|OpenAI]]** — entity. `gpt-4o-mini` is the demo LM (single-LM throughout).
- **[[MLflow]]** — entity. Optional tracing integration named in *Next Steps* but not implemented.
- **[[dspy-ai-text-game-tutorial]]** — sibling tutorial. Same **multi-Signature single-Module** structural pattern: three Signatures inside one Module, all wrapped in [[chainofthought|CoT]], no Optimizer, single LM. The email-extraction tutorial is the **four-Signature counterpart** with stricter inter-Signature typed handoffs (sequential pipeline rather than three parallel methods).
- **[[dspy-sample-code-generation-tutorial]]** — sibling tutorial. Same **multi-Signature single-Module** pattern: two Signatures (LibraryAnalyzer + CodeGenerator) inside one Module. The email tutorial is the more elaborate **diamond-shaped** generalization of the same idiom.
- **[[dspy-customer-service-agent]]** — sibling tutorial. Same Pydantic-typed-domain discipline; the customer-service tutorial wires the typed domain through [[react|`dspy.ReAct`]] *tools*, the email-extraction tutorial wires it through **inter-Signature InputFields / OutputFields**.
- **[[dspy-entity-extraction-tutorial]]** — sibling tutorial. Same *extraction* application family, but: (a) email-extraction is **structured multi-field**, entity-extraction is **subset-selection of tokens**; (b) email-extraction has **four Signatures**, entity-extraction has **one**; (c) email-extraction is **Programming-stage-only**, entity-extraction is **end-to-end optimized** (86 → 93 with MIPROv2).
- **[[dspy-conversation-history]]** — sibling tutorial. Both Programming-stage-only DSPy tutorial receipts; the email-extraction tutorial is **single-turn multi-Signature** vs the conversation-history tutorial's **multi-turn single-Signature**.
- **[[DSPyProgrammingModel]]** — concept. Programming-stage exit — no Evaluation, no Optimization.
- **[[BootstrapFewShot]]**, **[[MIPROv2]]** — concepts. **Not used** but named as the structural next step the user is encouraged to take.
- **[[ModelCalibration]]** — concept. The `ExtractedEntity.confidence: float` field is the wiki's first DSPy receipt embedding **LM-self-reported confidence scores** in a structured output — a calibration-adjacent surface that DSPy's metric / evaluation machinery does not yet provide tooling for.

## Contradictions

None with existing wiki content. Two **internal tutorial-side inconsistencies** worth flagging (not framework-level contradictions):

- **`financial_amount: Optional[float]` with `desc="(e.g., '$99.99')"`** — the example value is a string, but the type is `float`. The [[DSPyAdapters|Adapter]] absorbs the parsing (strips `$`, parses to float), but the desc string is misleading.
- **`os.environ["OPENAI_API_KEY"] = "..."` is set *after* `dspy.configure(lm=lm)`** — the demo works because [[LiteLLM]] reads the env var at LM-invocation time, not LM-construction time, but the ordering is reversed from the canonical pattern [[dspy-language-models|page 3]] documents.

Soft tension (not contradiction): the `reasoning: str = dspy.OutputField(...)` field on `ClassifyEmail` **overlaps** the implicit `reasoning` field that [[chainofthought|`dspy.ChainOfThought`]] adds. The user-declared field takes precedence (DSPy doesn't error or warn), but this is the **first wiki-corpus DSPy receipt where the user-declared field name collides with a Module-injected field name** — a soft surface for future framework-level disambiguation.

## Scope Limits

The tutorial is deliberately narrow. **Out of scope** (the tutorial does not address):

- **Optimization** — no [[DSPyMetrics|metric]], no training set, no [[MIPROv2|MIPROv2]] / [[BootstrapFewShot]] / [[GEPA]] sweep. The tutorial names "Different LLM experimentation and optimization strategies" as a *Next Steps* item.
- **Evaluation** — no benchmarked accuracy numbers. Only three sample emails are shown; no held-out test set.
- **Email-provider integration** — Gmail API / Outlook / IMAP integration is named in *Next Steps* but not implemented. The tutorial operates on hardcoded string subject/body/sender triples.
- **Multilingual support** — named in *Next Steps* but not implemented. The Enum value strings and docstrings are English-only.
- **Adversarial / prompt-injection emails** — the tutorial does not address spam-with-injected-instructions, phishing-with-typed-payloads, or other adversarial email content. A production email-triage system would need [[DSPyAssertions|`dspy.Assert`]] guards or input sanitization that the tutorial does not show.
- **Confidence-score calibration** — the `ExtractedEntity.confidence: float` field is emitted by the LM with no calibration check. Whether the LM's self-reported confidences are well-calibrated against ground-truth correctness is not measured. See [[ModelCalibration]] for the broader concern.
- **Long emails / context-window overflow** — the `email_content` InputField on `ExtractEntities` is `str` with no token-budget discussion. A 50KB newsletter would consume substantial context.
- **Streaming / batched processing** — the tutorial processes one email at a time synchronously. [[BatchInference]] / [[OnlineInference]] patterns are not exercised.
- **Cost tracking** — unlike [[dspy-entity-extraction-tutorial|the entity-extraction tutorial's]] `sum(x['cost'] for x in lm.history if x['cost'])` pattern, this tutorial does not measure per-email cost (four LM calls per email × `gpt-4o-mini` ≈ low cents per email at typical email lengths, but unmeasured).
- **MIPROv2 ablation on a four-Signature pipeline** — an open question the tutorial seeds but does not answer: does [[MIPROv2|MIPROv2]] optimize each sub-Signature independently, or jointly across the pipeline? The [[dspy-modules|Modules page]] notes that DSPy's compile-time tracing walks `named_predictors()` — so MIPROv2 would optimize all four sub-Signatures, but the cross-Signature behavior (does it propagate optimized outputs from `classifier` into `entity_extractor` bootstrapping?) is not exercised here.

## Position in the DSPy Tutorial Series

This is the **eleventh wiki-corpus DSPy tutorial**. The application-layer rungs as the corpus stands:

| Application slice | DSPy primitives | Wiki anchor |
|---|---|---|
| Single LM call | [[DSPyPredict|`dspy.Predict`]] | [[dspy-modules]] |
| Single LM-program call | [[DSPyModules|`dspy.Module`]] subclass | [[dspy-modules]] |
| Multi-turn conversation | [[DSPyHistory|`dspy.History`]] in a Signature | [[dspy-conversation-history]] |
| Classical-NLP token classification | [[ChainOfThought|`dspy.ChainOfThought`]] + [[MIPROv2|`dspy.MIPROv2`]] + simple-metric | [[dspy-entity-extraction-tutorial]] |
| Multi-Signature single-Module pipeline (creative-systems) | Three-Signature [[DSPyModules|`dspy.Module`]] with CoT wrappers | [[dspy-ai-text-game-tutorial]] |
| Multi-Signature single-Module pipeline (code-generation) | Two-Signature [[DSPyModules|`dspy.Module`]] + external HTTP layer | [[dspy-sample-code-generation-tutorial]] |
| **Multi-Signature single-Module pipeline (email-triage)** | **Four-Signature diamond-shaped [[DSPyModules|`dspy.Module`]] with typed inter-Signature handoffs** | **this tutorial** |
| Math reasoning | [[ChainOfThought|CoT]] + [[MIPROv2]] on [[MATH-benchmark|MATH]] | [[dspy-tutorial-math]] |
| Single-agent multi-tool task (typed domain) | [[react|`dspy.ReAct`]] + [[Pydantic]] domain | [[dspy-customer-service-agent]] |
| Single-agent multi-tool task (LangChain integration) | [[react|`dspy.ReAct`]] + [[LangChain]] tool | [[dspy-yahoo-finance-react-tutorial]] |
| Multi-hop retrieval agent | [[react|`dspy.ReAct`]] + [[MIPROv2]] on [[HoVer]] | [[dspy-tutorial-rag-as-agent]] |
| RAG | [[DSPyModules|`dspy.Module`]] + retrieval | [[dspy-rag-tutorial]] / [[dspy-custom-module]] |

The email-extraction rung is the **largest multi-Signature single-Module pipeline in the corpus** — four Signatures, diamond data-flow, twelve aggregated output fields — and serves as the canonical *"how do I chain four typed LM calls inside one `forward()`?"* shape for DSPy.
