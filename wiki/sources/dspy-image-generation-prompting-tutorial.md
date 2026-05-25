---
title: "DSPy Tutorial — Image Generation Prompt Iteration (dspy.Image + Flux Pro via FAL)"
type: source
tags: [dspy, tutorial, multimodal, image, image-generation, prompt-iteration, flux, fal, gpt-4o-mini, vision]
date: 2026-05-24
source_file: raw/dspy-tutorials/image-generation-prompting.md
sources: []
---

# DSPy Tutorial — Image Generation Prompt Iteration (`dspy.Image` + Flux Pro via FAL)

Official [[DSPy]] tutorial at `https://dspy.ai/tutorials/image_generation_prompting/` — **first wiki receipt of an image modality in DSPy** and the first source to exercise the `dspy.Image` primitive on a [[DSPySignatures|Signature]] `InputField`. Builds a **single-step [[DSPyPredict|`dspy.Predict`]] critic-then-revise loop** that, given a `desired_prompt`, a `current_image`, and a `current_prompt`, returns `feedback`, a `revised_prompt`, and a boolean `image_strictly_matches_desired_prompt` — used as a hand-rolled **iterative image-prompt refinement** loop against the [[FluxPro|Flux Pro v1.1 Ultra]] text-to-image model hosted by [[FAL]]. **Twentieth wiki-corpus DSPy tutorial** and the **shortest** to date (single Signature, no [[DSPyModules|`dspy.Module`]] subclass, no [[DSPyOptimization|Optimization stage]], no [[DSPyMetrics|metric]], no eval set — programming-stage-only with an externally-driven loop). Author credit in the tutorial: *"based off of a tweet from [@ThorondorLLC](https://x.com/ThorondorLLC)"* ([tweet](https://x.com/ThorondorLLC/status/1880048546382221313)).

## Summary

§1 — **install** pins `dspy`, `fal-client`, `pillow`, `dotenv` — **smallest DSPy tutorial dependency footprint after [[dspy-ai-text-game-tutorial|the text-game tutorial's]] 3 packages** and the only one with **zero `requests`-from-the-LM dependencies** beyond the image-fetch (`requests` is imported only for the helper that downloads the [[FAL]]-hosted JPEG for IPython `display`). No [[HuggingFace|HuggingFace]] datasets, no `torch`/`torchaudio`, no [[MLflow]], no [[OpenAI]] SDK directly (DSPy routes [[GPT4oMini|`gpt-4o-mini`]] through [[LiteLLM]]). First DSPy tutorial in the wiki whose external model surface is **two providers** ([[OpenAI]] for the LM, [[FAL]] for the image generator) **without** an [[HuggingFace|HF]] dataset host.

§2 — **environment** configures `dspy.LM(model="gpt-4o-mini", temperature=0.5)` and `dspy.configure(lm=lm)`. **`temperature=0.5` is the highest fixed temperature in any DSPy tutorial in the corpus** for a single-Signature critic — sits between the conservative `0.0` of evaluation-shaped tutorials and the `0.7` of [[dspy-tool-use-tutorial]]'s trajectory ChainOfThought. The two API keys (`FAL_API_KEY`, `OPENAI_API_KEY`) are loaded via `python-dotenv`'s `load_dotenv()` — **first wiki DSPy tutorial to use `.env`-file credential loading** rather than `os.environ[...] = ...` or `os.getenv(...)`.

§3 — **`generate_image(prompt)` helper** calls `fal_client.submit("fal-ai/flux-pro/v1.1-ultra", arguments={"prompt": prompt}).request_id` then `fal_client.result("fal-ai/flux-pro/v1.1-ultra", request_id)`, extracts `result["images"][0]["url"]`, and wraps the URL via **`dspy.Image.from_url(url)`** — **first wiki receipt of `dspy.Image.from_url(...)`** as a construction path. The DSPy framework's `Image` primitive carries the URL through the [[DSPyAdapters|Adapter]] into the chat-completion request **without re-downloading the bytes locally**; the adapter serializes the field as `<image_url: https://fal.media/files/.../*.jpg>` (visible in the `dspy.inspect_history(5)` excerpt), i.e. **URL passthrough** rather than base64 inlining. The fact that the same URL surfaces verbatim in the rendered prompt-trace text is the load-bearing evidence for the URL-passthrough adapter behavior — distinct from [[DSPyAudio|`dspy.Audio`]]'s base64-in-`data` storage path.

§4 — **`display_image(image)` helper** then `requests.get(image.url)` + `PIL.Image.open(BytesIO(...))` + `image.resize((w//4, h//4))` for in-notebook rendering. The helper exists **only for visual inspection during iteration**, not for the LM call (which sees the URL string). The DSPy `Image` primitive exposes `.url` as a public attribute usable for client-side downloads — first wiki receipt of the `.url` accessor.

§5 — **the critic Signature** is declared inline as a **string-spec [[DSPyPredict|`dspy.Predict`]]**:

```python
check_and_revise_prompt = dspy.Predict(
    "desired_prompt: str, current_image: dspy.Image, current_prompt:str "
    "-> feedback:str, image_strictly_matches_desired_prompt: bool, revised_prompt: str"
)
```

**First wiki receipt of `dspy.Image` named inline in a string Signature** — prior receipts ([[dspy-signatures]], [[dspy-modules]]) showed only `str`/`bool`/`int`/`list[str]` in string-spec form. This proves the **string-Signature parser resolves `dspy.Image` (and by symmetry `dspy.Audio`) as a typed field reference**, not just primitive Python types. Three output fields (`feedback`, `image_strictly_matches_desired_prompt`, `revised_prompt`) — note the **field order is not enforced**: §3 of the [[dspy-inspect-history|inspect_history excerpt]] shows the first run with output order `feedback / revised_prompt / image_strictly_matches_desired_prompt` and subsequent runs with `feedback / image_strictly_matches_desired_prompt / revised_prompt`. The string-Signature parser is **field-set-canonical, not field-order-canonical** — a structural disclosure no prior DSPy tutorial in the corpus had surfaced.

§6 — **the iteration loop** is a plain Python `for i in range(max_iter)` with `max_iter = 5`, an early `break` on `result.image_strictly_matches_desired_prompt`, and `current_prompt = result.revised_prompt` rebind on each non-match iteration. **The loop is not a [[DSPyModules|`dspy.Module`]]** — there is no `class IterativePromptRefiner(dspy.Module)` subclass with a `forward()` method. This is a deliberate framework-philosophy choice: the tutorial frames the program as a *programming-overview* exercise ("a good example of how to use multimodal DSPy") rather than as an optimizable Module. Consequence: the loop **cannot be optimized by any DSPy Optimizer** (no Signature for the loop's stop condition; no metric for the per-iteration revision). The tutorial's closing aside — *"a future upgrade would be to create a dataset of initial, final prompts to optimize the prompt generation"* — names exactly this gap. **First wiki DSPy tutorial that explicitly disclaims its own optimizability while shipping the working program**.

§7 — **the sample run** starts from `"A scene that's both peaceful and tense"` and the printed log shows the critic returning `False` for iterations 1–3 (autumn-scene variants lacking explicit tension), then `True` at iteration 4 with `Final prompt: A serene autumn scene with fog and shadows, capturing both peace and tension.` The `dspy.inspect_history(5)` excerpt shows that **the first call (with `current_prompt == desired_prompt == "A scene that's both peaceful and tense"` and a café-scene image) returned `True`** — a *cached-history-from-prior-run* artifact whose café-scene feedback contradicts the autumn-scene feedback of the printed run. The two transcripts are from different runs of the same notebook; the rendered notebook is **not internally consistent across the run-log and the `inspect_history(5)` capture**. First wiki DSPy tutorial whose `inspect_history(...)` output disagrees with the printed cell output above it.

## Key Claims

- **`dspy.Image` is DSPy's first-class image primitive** — supports at minimum two construction paths (`dspy.Image.from_url(url)` for hosted images and `dspy.Image.from_file(...)` / base64 paths inherited from the broader DSPy primitive family). The `.url` attribute is public and usable for client-side downloads after construction.
- **Image-`InputField`s serialize as URL passthrough through the [[DSPyAdapters|Adapter]]** — the chat-completion request carries the URL string (`<image_url: https://...>`), not base64-inlined image bytes. The LM's vision modality reads the URL on its side. Distinct from [[DSPyAudio|`dspy.Audio`]]'s base64-in-`data` storage path; the two non-text primitives use **opposite transport disciplines**.
- **`dspy.Image` works inline in string-spec Signatures** — `"... current_image: dspy.Image ..."` parses correctly. The string-Signature parser recognizes `dspy.Image` as a typed field reference alongside the primitive Python types.
- **String-Signature outputs are field-set-canonical, not field-order-canonical** — the `inspect_history(5)` excerpt shows runs of the same Signature with different output-field orders (`feedback / revised_prompt / image_strictly_matches_desired_prompt` in run 1 vs `feedback / image_strictly_matches_desired_prompt / revised_prompt` in runs 2–5). DSPy's Adapter does not pin field order across runs for string-spec Signatures.
- **The image-prompt-iteration pattern is a [[DSPyPredict|`dspy.Predict`]]-only critic loop** wrapped in a plain Python `for` loop — no [[DSPyModules|`dspy.Module`]] subclass, no [[DSPyOptimization|Optimizer]], no [[DSPyMetrics|metric]], no eval set. **The tutorial explicitly disclaims its own optimizability** and points to the natural next step (collect an initial/final prompt dataset to enable [[DSPyOptimizers|Optimizer]]-driven training).
- **[[FluxPro|Flux Pro v1.1 Ultra]] via [[FAL]] is the chosen image generator** — `fal_client.submit("fal-ai/flux-pro/v1.1-ultra", arguments={"prompt": prompt})` + polling via `fal_client.result(...)`. The DSPy framework treats the image generator as an **external black-box service**, not as a `dspy.LM` (output-side image generation is out of the LM abstraction's scope — symmetric to [[DSPyAudio|`dspy.Audio`]] output handling in [[dspy-audio-tutorial]] which wraps the [[GPT4oMiniTTS|OpenAI TTS]] endpoint outside the LM client).
- **[[GPT4oMini|`gpt-4o-mini`]] is the vision-capable critic LM** — fixed at `temperature=0.5`. First DSPy tutorial in the wiki to fix the highest non-zero temperature for a single-Signature critic.
- **Two-provider, no-HF-dataset shape** — first DSPy tutorial whose external surface is `OpenAI + FAL` with no [[HuggingFace]] dataset; only `python-dotenv` mediates credentials, smallest tutorial dependency footprint after [[dspy-ai-text-game-tutorial]].

## Key Quotes

> "This is not DSPy prompt optimization as it is normally used, but it is a good example of how to use multimodal DSPy." — §0 (framework-philosophy framing; first wiki DSPy tutorial to explicitly decouple "DSPy ergonomics" from "DSPy optimization" as separable value props).

> "A future upgrade would be to create a dataset of initial, final prompts to optimize the prompt generation." — §0 closing aside (the only acknowledgement that the program is not exercising the DSPy Optimizer surface; the explicit upgrade path is *labeled* data → BootstrapFewShot/MIPROv2-style refinement).

> "For this example, we'll use Flux Pro from FAL." — §1 (the model+provider declaration; first wiki receipt of [[FluxPro|Flux Pro]] / [[FAL]] in the DSPy corpus).

## Connections

- [[DSPy]] — the framework.
- [[DSPyImage]] — minted concept page for the `dspy.Image` primitive (first image-modality concept in the wiki's DSPy taxonomy; structural sibling to [[DSPyAudio]]).
- [[DSPyPredict]] — the single Module used; `dspy.Predict(string_spec)` invocation.
- [[DSPySignatures]] — string-spec Signature with `dspy.Image` typed `InputField`.
- [[DSPyAdapters]] — the URL-passthrough serialization disclosure originates at the adapter layer (`<image_url: ...>` wire shape in `inspect_history`).
- [[DSPyLM]] — [[GPT4oMini|`gpt-4o-mini`]] as a vision-capable LM consumed via [[LiteLLM]].
- [[FluxPro]] — minted concept page for the Flux Pro v1.1 Ultra text-to-image model (the tutorial's image generator).
- [[FAL]] — minted entity page for the model-serving company hosting Flux Pro (`fal-ai/flux-pro/v1.1-ultra` endpoint).
- [[BlackForestLabs]] — minted entity page for the company that builds the Flux family of models.
- [[GPT4oMini]] — vision-capable critic LM at `temperature=0.5`; minted concept page for the model.
- [[OpenAI]] — model provider for the critic LM (routed via [[LiteLLM]]).
- [[LiteLLM]] — DSPy's unified provider client.
- [[DSPyAudio]] — sibling non-text primitive; opposite serialization discipline (base64 in `data` vs URL passthrough in `dspy.Image`).
- [[dspy-audio-tutorial]] — the wiki's prior multimodal-DSPy receipt (audio); this tutorial is the image-modality counterpart.
- [[MultimodalLLM]] — broader concept of LM with non-text modality; this tutorial is a single-call vision-input instance.
- [[IterativeImagePromptRefinement]] — minted concept page for the critic-then-revise loop pattern.
- [[PromptEngineering]] — broader concept; this tutorial mechanizes prompt iteration with an LM-as-judge in the loop.
- [[FeedbackLoop]] / [[NaturalLanguageFeedback]] — adjacent concepts; the critic returns natural-language feedback that drives the next iteration's revised prompt.
- [[GEPA]] — kin concept (reflective-prompt-evolution Optimizer); the tutorial's closing aside about *"create a dataset of initial, final prompts to optimize"* describes the natural lift from this hand-rolled loop to a [[GEPA]]-style framework-optimized program with a feedback-bearing metric.

## Contradictions

- **Run log ↔ `inspect_history` mismatch** — the printed iteration log shows autumn-scene images and `False` matches for iterations 1–3 before a `True` at iteration 4, but `dspy.inspect_history(5)` shows a café-scene image returning `True` at the first call. The two captures are from different notebook runs of the same code; the rendered tutorial does not flag the disagreement. **First wiki DSPy tutorial whose printed `inspect_history` output disagrees with the printed cell output above it** — readers cannot trace a single run end-to-end.
- **Field-order drift between runs** — the Signature's output-field declaration order is `feedback / image_strictly_matches_desired_prompt / revised_prompt` in the Python source, but the `inspect_history(5)` system messages show run 1 with adapter-emitted order `feedback / revised_prompt / image_strictly_matches_desired_prompt` and runs 2–5 with `feedback / image_strictly_matches_desired_prompt / revised_prompt`. The [[DSPyAdapters|Adapter]] does not pin field order for string-spec Signatures across runs. Implication: anything downstream that string-parses the LM output by field position will break; consumers must field-name-parse.
- **`max_iter = 5` is unmotivated** — the budget is hard-coded; no ablation on `max_iter ∈ {3, 5, 10}`, no convergence-rate disclosure across desired prompts. The pattern's quality-vs-budget curve is undocumented.
- **No image-similarity metric** — the loop's only termination condition is the critic's own boolean self-judgement (`result.image_strictly_matches_desired_prompt`). There is no [[CLIP|CLIP]]-similarity / [[CosineSimilarity|cosine]]-similarity / human-eval grounding to validate the critic's judgement. Symmetric to [[dspy-audio-tutorial|the audio tutorial's]] honest [[Wav2Vec2]]-as-metric caveat — but this tutorial does not flag the same caveat about LM-as-judge image evaluation.
- **`temperature=0.5` for a deterministic critic** — the critic is asked for a boolean and a textual revision; a non-zero temperature on the boolean-emitting field is a low-grade source of nondeterminism the tutorial does not flag.
- **Cost / wall-time / token-count not disclosed** — continuing gap across the DSPy tutorial corpus; especially load-bearing here given each iteration runs a [[FluxPro|Flux Pro]] generation (5–30 s typical) and a vision-LM call.
- **`fal-ai/flux-pro/v1.1-ultra` endpoint pinned without a [[FluxSchnell|Flux Schnell]] / [[FluxDev|Flux Dev]] cost-quality comparison** — the higher-tier endpoint is chosen by default; no ablation across the Flux family.

## Scope-limit gaps

- **No [[DSPyModules|`dspy.Module`]] subclass** — the loop is not encapsulated as a Module, so the program **cannot be passed to any [[DSPyOptimizers|Optimizer]]** (`compile(...)` would have no Module to walk). The tutorial's closing aside about "create a dataset of initial, final prompts to optimize the prompt generation" describes exactly the work needed to lift the program into an optimizable shape: (1) collect labeled `(initial_prompt, final_prompt)` pairs, (2) wrap the loop in a `dspy.Module` subclass with a `forward()`, (3) define a metric over `revised_prompt` quality, (4) run [[MIPROv2]] / [[GEPA]] / [[BootstrapFewShotWithRandomSearch]] over the wrapper.
- **No [[GEPA]] receipt** — the natural Optimizer for this pattern (per-iteration natural-language feedback as a metric signal) is not exercised. [[GEPA]]'s [[ReflectivePromptMutation|reflective prompt mutation]] is structurally the framework-native version of the loop the tutorial hand-rolls.
- **No CLIP / aesthetic-score / human-preference baseline** — the critic's `image_strictly_matches_desired_prompt` boolean is the only signal; no external image-quality metric grounds the loop.
- **No save/load receipt** — the program is not round-tripped through `program.save / program.load`.
- **No streaming / async / observability composition** — no [[DSPyStreaming|`dspy.streamify`]] / [[DSPyAsync|`dspy.asyncify`]] / [[MLflow|MLflow autolog]] receipts.
- **No multi-image input** — the Signature carries one `current_image: dspy.Image` field; no `list[dspy.Image]` for batch comparison.
- **No [[DSPyAudio|Audio]] composition** — the tutorial does not multiplex image + audio in the same Signature, even though the framework supports both primitives.
- **No image-output `dspy.Image` receipt** — the tutorial generates images via the [[FAL]] HTTP API and wraps the returned URL into `dspy.Image.from_url(...)` for *input* on the next iteration; the framework's `dspy.Image` does not appear as a Signature `OutputField`. Symmetric to [[DSPyAudio|`dspy.Audio`]]'s "no first-class output" disclosure in [[dspy-audio-tutorial]]; the wiki's multimodal coverage is now consistently "input-side first-class, output-side wrapped HTTP".
- **No mention of [[DallE|DALL-E 3]] / [[StableDiffusion|Stable Diffusion]] / [[MidJourney]] alternatives** — the [[FluxPro|Flux Pro]] endpoint is presented as the choice without comparison to the broader text-to-image landscape.
- **No retry / error-handling** — the loop has no fallback if `fal_client.result(...)` fails, if the vision-LM call times out, or if the critic returns malformed output.
