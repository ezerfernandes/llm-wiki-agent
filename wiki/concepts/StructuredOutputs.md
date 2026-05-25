---
title: "Structured Outputs"
type: concept
tags: [sampling, inference, llm, json, agents]
sources: [ai-engineering-ch02-foundation-models, ai-engineering-ch04-evaluate-ai-systems, ai-engineering-ch07-finetuning, dspy-ai-text-game-tutorial]
last_updated: 2026-05-24
---

# Structured Outputs

Generating model outputs that **conform to a specific format** — JSON, YAML, SQL, regex, etc. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]], structured outputs are crucial in two scenarios:

1. **Tasks requiring structured outputs.** [[SemanticParsing|Semantic parsing]] like text-to-SQL, text-to-regex; classification tasks with valid-class output constraints.
2. **Tasks whose outputs feed downstream applications** that need to parse them — especially **agentic workflows** where LLM outputs are passed as inputs to tools (covered in Ch 6 of the book).

## The five-layer stack of techniques

Per Ch 2, you can enforce structured outputs at five layers of the AI stack:

| Layer | Approach | Strength |
|---|---|---|
| **Prompting** | Tell the model what format you want | First line of action; depends on the model's instruction-following |
| **Post-processing** | Fix common mistakes after generation | Cheap; works if mistakes are easy to fix |
| **[[TestTimeCompute|Test-time compute]]** | Keep generating until output matches format | Bandage; can be expensive |
| **[[ConstrainedSampling|Constrained sampling]]** | Filter logits to only valid tokens at each step | Intensive treatment; needs a grammar |
| **[[FineTuning|Finetuning]]** | Train the model on examples of the target format | Most effective; works with any format |

The first three are "bandages"; constrained sampling and finetuning are the "intensive treatments."

## Frameworks

Ch 2 names: **guidance**, **outlines**, **instructor**, **llama.cpp**.

Provider-side: **[[openai|OpenAI]] introduced JSON mode** first. Note: JSON mode typically guarantees only that outputs are *valid JSON* — not the *content* of the JSON. Outputs can also be truncated if generation stops too early (see [[StoppingCondition]]).

## Worked example: LinkedIn YAML

LinkedIn's defensive YAML parser increased valid-YAML output rate from **90% to 99.99%** (Bottaro and Ramgopal 2020). They chose YAML over JSON because YAML is less verbose → fewer output tokens → lower cost.

## Worked example: GPT-4o text-to-regex

Ch 2 shows GPT-4o generating regex from English descriptions:

| Input | Output |
|---|---|
| `Email address ->` | `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` |
| `Dates ->` | `(?:\d{1,2}[\/\-\.])(?:\d{1,2}[\/\-\.])?\d{2,4}` |

## AI-as-judge for validation

Some teams use a **separate AI call to validate and/or correct the original output** — the "[[LLMAsAJudge|AI as a judge]]" approach (discussed in Ch 3 of the book). This adds latency and cost but can significantly improve validity.

## Forward-looking prediction from Ch 2

> "We need techniques for structured outputs because of the assumption that the model, by itself, isn't capable of generating structured outputs. However, as models become more powerful, we can expect them to get better at following instructions. I suspect that in the future, it'll be easier to get models to output exactly what we need with minimal prompting, and these techniques will become less important."

## Connections
- [[ConstrainedSampling]] — the lowest-level enforcement.
- [[SemanticParsing]] — the primary task class needing structured outputs.
- [[TestTimeCompute]] — the multiple-output approach.
- [[FineTuning]] — the most reliable enforcement layer.
- [[StoppingCondition]] — the failure mode of premature termination.
- [[LLMAsAJudge]] — the validate-with-another-AI approach.
- [[AgentCoupling]] / [[agenticharness]] — the downstream consumer of structured outputs.
- [[ai-engineering-ch02-foundation-models]] — primary source.

## From [[ai-engineering-ch04-evaluate-ai-systems|AI Engineering Ch 4]]

Ch 4 names structured outputs in two contexts:

1. **As an [[InstructionFollowingCapability|instruction-following]] sub-capability.** *"Instruction-following capability is essential for applications that require structured outputs, such as in JSON format or matching a regular expression (regex)."* Breaking format = breaking downstream consumers.
2. **As a [[ModelBuildVsBuy|build-vs-buy]] functionality dimension.** APIs differ in whether/how well they support structured outputs out of the box; this is one factor weighing toward commercial APIs over raw self-hosting.

Ch 4 also broadens *what counts* as instruction-following: outputs constrained to JSON are one case, but outputs constrained to *"only use words of at most four characters"* ([[Ello]]'s use case) is non-format structural following — same evaluation problem.

## From [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]]

Ch 7 reinforces structured outputs as **a canonical [[FineTuning|finetuning]] use case** ([[BehaviorBasedFailure|behavior-based failure]], not [[InformationBasedFailure|information-based]]). [[ChipHuyen|Huyen]]'s framing:

> "Semantic parsing is a category of tasks whose success hinges on the model's ability to generate outputs in the expected format and, therefore, often requires finetuning. ... Strong off-the-shelf models are generally good for common, less complex syntaxes like JSON, YAML, and regex. However, they might not be as good for syntaxes with fewer available examples on the internet, such as a domain-specific language for a less popular tool or a complex syntax."

So the rule from Ch 7: **off-the-shelf models for common formats; finetune for uncommon/DSL formats**. This is one of the clearest examples of the chapter's "[[FineTuning|finetuning]] is for form" thesis.
