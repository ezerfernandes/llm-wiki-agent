---
title: "Iterative Image Prompt Refinement"
type: concept
tags: [pattern, image-generation, prompt-iteration, llm-as-judge, multimodal, feedback-loop]
sources: [dspy-image-generation-prompting-tutorial]
last_updated: 2026-05-24
---

# Iterative Image Prompt Refinement

A **critic-then-revise loop** for text-to-image generation: a vision-capable LM scores a generated image against the user's *desired* prompt, returns natural-language feedback plus a revised prompt, and a host Python loop re-generates with the revision until the critic returns a match (or a max-iteration budget is hit). **First wiki receipt: [[dspy-image-generation-prompting-tutorial]]** (the dspy.ai *Image Generation Prompt Iteration* tutorial), which mechanizes the pattern as a single [[DSPyPredict|`dspy.Predict`]] call:

```python
dspy.Predict(
    "desired_prompt: str, current_image: dspy.Image, current_prompt: str "
    "-> feedback: str, image_strictly_matches_desired_prompt: bool, revised_prompt: str"
)
```

driven by an outer `for i in range(max_iter)` that early-breaks on `result.image_strictly_matches_desired_prompt`.

## Why the pattern matters

Text-to-image models are notoriously prompt-sensitive: a faithful realization of *"a scene that's both peaceful and tense"* may require dozens of paralinguistic descriptors (fog, shadows, specific objects) the user does not initially supply. The pattern **outsources prompt engineering to a vision LM that can see the gap** between intent and output, then **closes the loop** by revising the prompt rather than (e.g.) post-editing the image. The DSPy framing lets a single Signature express both the critique and the revision atomically.

## Structural shape

| Slot | Role |
|---|---|
| Image generator | A text-to-image model (e.g. [[FluxPro|Flux Pro]] via [[FAL]]) treated as an external black-box service. |
| Vision LM | A vision-capable LM (e.g. [[GPT4oMini|`gpt-4o-mini`]]) consuming the generated image as a [[DSPyImage|`dspy.Image`]] `InputField`. |
| Critic Signature | `desired_prompt × current_image × current_prompt → feedback × match: bool × revised_prompt` — three-input, three-output Signature. |
| Outer loop | Plain Python `for` with early break on the boolean match field; rebinds `current_prompt = result.revised_prompt` on non-match. |

The shape is intentionally **not** a [[DSPyModules|`dspy.Module`]] subclass in the first wiki receipt — the loop lives outside the Module abstraction, which means the program **cannot be passed to a [[DSPyOptimizers|DSPy Optimizer]]** as-is.

## Limits (per [[dspy-image-generation-prompting-tutorial]])

- **No ground-truth image-similarity metric** — the loop trusts the critic LM's boolean self-judgement. No [[CLIP|CLIP]] / [[CosineSimilarity|cosine]] / human-eval anchor.
- **No labeled dataset, no Optimizer** — the tutorial's closing aside (*"a future upgrade would be to create a dataset of initial, final prompts to optimize the prompt generation"*) names exactly this gap. The natural lift is to wrap the loop in a `dspy.Module`, collect `(initial_prompt, final_prompt)` pairs, define a metric on revision quality, and run [[MIPROv2]] / [[GEPA]] / [[BootstrapFewShotWithRandomSearch]] over it.
- **No cost / wall-time disclosure** — each iteration runs a [[FluxPro|Flux Pro]] generation (5–30 s typical) and a vision-LM call.
- **Critic ↔ generator drift** — the critic and the generator are different models with different aesthetic priors; the critic's idea of "matches the prompt" need not align with downstream human judgement.

## Lift to a framework-native shape

The pattern is structurally close to what [[GEPA|`dspy.GEPA`]] does internally: a reflective-prompt-mutation Optimizer that reads natural-language feedback per example and proposes a revised instruction. The hand-rolled loop is *what GEPA automates* — making this pattern the **single most natural candidate** in the DSPy tutorial corpus for a GEPA receipt on a multimodal task. None of the current GEPA tutorials in the wiki ([[dspy-tutorial-gepa-aime]], [[dspy-tutorial-gepa-facilitysupportanalyzer]], [[dspy-tutorial-gepa-papillon]], [[dspy-tutorial-gepa-trusted-monitor]]) exercise the image modality.

## Connections

- [[DSPy]] / [[DSPyPredict]] / [[DSPySignatures]] — the framework substrate.
- [[DSPyImage]] — the typed `InputField` carrying the current image.
- [[GPT4oMini]] — the critic LM in the first receipt.
- [[FluxPro]] / [[FAL]] — the image-generation service in the first receipt.
- [[PromptEngineering]] — broader concept; this pattern mechanizes prompt iteration with an LM-as-judge.
- [[FeedbackLoop]] / [[NaturalLanguageFeedback]] — adjacent concepts; the critic returns natural-language feedback driving the next iteration's revision.
- [[GEPA]] — the framework-native Optimizer that automates this pattern; the natural lift target.
- [[MultimodalLLM]] — broader concept; this pattern is a single-call vision-input instance.
- [[dspy-image-generation-prompting-tutorial]] — first wiki receipt.
