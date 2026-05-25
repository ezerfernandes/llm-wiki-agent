---
title: "DSPy Tutorial — Audio (Spoken QA + Emotion-Guided TTS)"
type: source
tags: [dspy, tutorial, audio, multimodal, tts, speech-recognition, miprov2, bootstrapfewshotwithrandomsearch, wav2vec2, spoken-squad, crema-d]
date: 2026-05-24
source_file: raw/dspy-audio-tutorial.md
sources: []
---

# DSPy Tutorial — Audio (Spoken QA + Emotion-Guided TTS)

Official [[DSPy]] tutorial at `https://dspy.ai/tutorials/audio/` — **the wiki's first receipt of an audio modality in DSPy** and the first source to exercise the `dspy.Audio` primitive end-to-end across both **input-side** (audio → text) and **output-side** (text → audio) tasks. Builds two complete, independently-optimizable [[DSPyModules|`dspy.Module`]] programs: (1) a **spoken question-answering** classifier over [[SpokenSQuAD]] using an [[GPT4oMiniAudio|audio-input LLM]] (`gpt-4o-mini-audio-preview-2024-12-17`), and (2) an **emotion-guided text-to-speech generator** over [[CREMAD|CREMA-D]] that wraps the [[GPT4oMiniTTS|`gpt-4o-mini-tts`]] HTTP API inside a `dspy.Module` and optimizes its **instruction prompt** via [[MIPROv2]] against a [[Wav2Vec2|Wav2Vec 2.0]] embedding-similarity metric.

## Summary

§1 — installation pins `torch==2.0.1+cu118` / `torchaudio==2.0.2+cu118` alongside `dspy`, `datasets`, `soundfile` — first wiki DSPy tutorial with **explicit CUDA-build torch pins** (justified by the [[Wav2Vec2|Wav2Vec2]] embedding metric in §3, the only stage that needs local GPU torch).

§2 — **Spoken Question Answering** on [[SpokenSQuAD|Spoken-SQuAD]] (`AudioLLMs/spoken_squad_test` on [[HuggingFace]]). Loads via `dspy.datasets.DataLoader().from_huggingface(...)` with `fields=("context","instruction","answer")` and `input_keys=("context","instruction")`, then transforms `x.context["array"]` + `x.context["sampling_rate"]` through `dspy.Audio.from_array(array, sampling_rate)` into a [[DSPyAudio|`dspy.Audio`]] primitive — **first wiki receipt of `dspy.Audio.from_array(...)`**. Signature:

```python
class SpokenQASignature(dspy.Signature):
    """Answer the question based on the audio clip."""
    passage_audio: dspy.Audio = dspy.InputField()
    question: str = dspy.InputField()
    answer: str = dspy.OutputField(desc='factoid answer between 1 and 5 words')
```

Program is `dspy.ChainOfThought(SpokenQASignature)` against [[GPT4oMiniAudio|`gpt-4o-mini-audio-preview-2024-12-17`]] — **first wiki receipt of an OpenAI audio-input model in DSPy**; the `-audio-preview-2024-12-17` suffix is the snapshot tag the tutorial pins, distinct from the rolling `gpt-4o-audio-preview` alias. Evaluation uses `dspy.Evaluate(devset=testset, metric=dspy.evaluate.answer_exact_match, display_progress=True, num_threads=10, display_table=True)` — built-in [[DSPyMetrics|exact-match]] metric, no judge.

§2.1 — **optimization with [[BootstrapFewShotWithRandomSearch]]** uses `metric=dspy.evaluate.answer_exact_match, max_bootstrapped_demos=2, max_labeled_demos=2, num_candidate_programs=5`. Tutorial explicitly warns *"audio tokens can be costly"* — first DSPy tutorial to flag the **per-modality token-cost asymmetry** as an optimizer-budget constraint (audio tokens dominate cost vs text demos).

§2.2 — **optimization with [[MIPROv2]]** uses `auto="light"`, `prompt_model=gpt-4o-mini` (text-only prompt LM separate from the audio task LM), with `data_aware_proposer=False` — **first wiki receipt of the `data_aware_proposer=False` MIPROv2 kwarg** and a previously-undocumented optimizer constraint: MIPROv2's dataset-summarizer proposer *"cannot process the audio files"* so it must be disabled on any task whose `InputField`s contain non-textual modalities. **Headline lift: ~10% absolute improvement over baseline** for both optimizers (specific numbers not printed in the rendered tutorial — first DSPy tutorial in the corpus to give only a qualitative "~10%" headline rather than printed accuracy cells).

§3 — **Emotion-Guided Text-to-Speech** on [[CREMAD|CREMA-D]] (Crowd-sourced Emotional Multimodal Actors Dataset). Six target emotions: `['neutral','happy','sad','anger','fear','disgust']`. Tutorial's task is **prompt-only fine-tuning of the TTS instruction string** — generate an OpenAI TTS `instructions=` parameter that makes [[GPT4oMiniTTS|`gpt-4o-mini-tts`]] speak `raw_line` with the requested emotion.

§3.1 — **TTS wrapper** is a plain function calling `OpenAI().audio.speech.create(model="gpt-4o-mini-tts", voice="coral", input=raw_line, instructions=prompt, response_format="wav")` and re-encoding the result as a `dspy.Audio`. Voice fixed at `"coral"`; tutorial notes the broader surface — *"this can be configured to any of the 11 offered OpenAI TTS voices"* — **first wiki documentation of OpenAI TTS's 11-voice catalog as a hyperparameter**. The wrapper is **not** a `dspy.LM` — it sits outside DSPy's LM abstraction because the TTS API is a non-chat HTTP endpoint that DSPy's LM client does not multiplex.

§3.2 — **Signature**:

```python
class EmotionStylePromptSignature(dspy.Signature):
    """Generate an OpenAI TTS instruction that makes the TTS model
    speak the given line with the target emotion or style."""
    raw_line: str = dspy.InputField()
    target_style: str = dspy.InputField()
    openai_instruction: str = dspy.OutputField()
```

§3.3 — **Module** wraps the Signature in [[chainofthought|`dspy.ChainOfThought`]], runs the wrapper function on the produced instruction, and returns a `dspy.Prediction(audio=audio)`:

```python
class EmotionStylePrompter(dspy.Module):
    def __init__(self):
        self.prompter = dspy.ChainOfThought(EmotionStylePromptSignature)
    def forward(self, raw_line, target_style):
        out = self.prompter(raw_line=raw_line, target_style=target_style)
        audio = generate_dspy_audio(raw_line, out.openai_instruction)
        return dspy.Prediction(audio=audio)
```

§3.4 — **[[Wav2Vec2|Wav2Vec 2.0]] audio-similarity metric** is the load-bearing novel contribution. Uses `torchaudio.pipelines.WAV2VEC2_BASE.get_model().eval()`, decodes `dspy.Audio` via `base64.b64decode(...)` + `soundfile.read(io.BytesIO(...), dtype="float32")`, extracts a mean-pooled frame embedding `model(audio_tensor)[0].mean(dim=1)`, and scores `cosine_similarity(ref_embed, gen_embed)`. The `trace is not None` branch returns the binary `score > 0.8` — **first wiki receipt of the threshold-binarization-when-trace pattern for a non-textual metric** (DSPy's optimizer convention: return scalar at evaluation time, return bool when called inside `trace`-context bootstrapping). Tutorial is **honest** about the metric's limits: *"audio reference comparisons is generally a non-trivial task due to subjective variations of evaluating speech, especially with emotional expression"*; *"human feedback or perceptual metrics would be more suitable."* — **first DSPy tutorial in the corpus to ship a metric with a documented epistemic caveat about the metric itself** (not just about budget or scope).

§3.5 — **optimization with MIPROv2** using `auto="light"` and `prompt_model=gpt-4o-mini`. **Headline lift: ~0.57 → ~0.67 cosine similarity** (~+0.10 absolute on the [0,1] scale, ~+17.5% relative). Optimized prompts include detailed specifications for tone, pitch, and speaker characteristics — i.e. the optimizer drives the TTS instruction surface from short emotion-label injection ("speak this with anger") toward dense paralinguistic descriptors. **First wiki receipt of MIPROv2 optimizing prompts whose downstream consumer is a non-chat audio API rather than a chat LLM** — the optimizer is agnostic to where the resulting prompt is used.

## Key Claims

- **`dspy.Audio` is DSPy's first-class audio primitive** with two construction paths: `dspy.Audio.from_array(array, sampling_rate)` for raw NumPy arrays paired with a sampling rate, and base64-encoded bytes for serialized round-trips. Stores audio as `data` (base64-encoded WAV bytes) decodable via the `base64.b64decode(...)` + `soundfile.read(io.BytesIO(...))` idiom shown in §3.4.
- **Audio modality on InputFields requires an audio-capable LM** — `gpt-4o-mini-audio-preview-2024-12-17` for inputs; standard `gpt-4o-mini` cannot consume `dspy.Audio` InputFields.
- **Audio modality on OutputFields is not first-class in DSPy** — the tutorial wraps the OpenAI TTS HTTP endpoint manually inside a `dspy.Module.forward()` and returns the audio as a `dspy.Prediction` field. DSPy's LM client does not (yet) multiplex audio-output endpoints.
- **MIPROv2's `data_aware_proposer` must be disabled for non-textual InputFields** — the dataset-summarizer proposer cannot read audio bytes. Pattern generalizes: any `dspy.Audio` / `dspy.Image` / `dspy.Video` InputField on a Signature being optimized by MIPROv2 should set `data_aware_proposer=False`.
- **Audio tokens are expensive** — tutorial recommends 0–2 few-shot examples (`max_bootstrapped_demos=2, max_labeled_demos=2`) and conservative `num_candidate_programs` settings for any optimizer with audio in the demo set.
- **Wav2Vec 2.0 mean-pooled embeddings + cosine similarity is the tutorial's chosen proxy metric for TTS evaluation**, with the explicit caveat that human or perceptual metrics would be better.
- **OpenAI TTS exposes 11 named voices** — the tutorial uses `"coral"` but notes the full catalog. Voice is a hyperparameter not optimized in this tutorial.
- **Headline gains**: Spoken-SQuAD ~10% absolute improvement from optimization (qualitative); CREMA-D TTS ~0.57 → ~0.67 cosine similarity.

## Key Quotes

> "Audio tokens can be costly, so we recommend keeping the optimizer configuration conservative — 0 to 2 few-shot examples." — §2.2 (BootstrapFewShotWithRandomSearch / MIPROv2 budget warning).

> "MIPROv2's dataset summarizer cannot process the audio files, so we disable the `data_aware_proposer`." — §2.2 (first wiki receipt of this optimizer constraint).

> "This can be configured to any of the 11 offered OpenAI TTS voices." — §3.1 (TTS voice catalog).

> "Audio reference comparisons is generally a non-trivial task due to subjective variations of evaluating speech, especially with emotional expression. … Human feedback or perceptual metrics would be more suitable." — §3.4 (Wav2Vec2 metric caveat).

## Connections

- [[DSPy]] — the framework.
- [[DSPyAudio]] — minted concept page for the `dspy.Audio` primitive (first audio-modality concept in the wiki's DSPy taxonomy).
- [[SpokenSQuAD]] — minted dataset concept (audio variant of [[SQuAD]]).
- [[CREMAD]] — minted dataset concept (six-emotion vocal-acting corpus).
- [[GPT4oMiniAudio]] — minted model concept (`gpt-4o-mini-audio-preview-2024-12-17`).
- [[GPT4oMiniTTS]] — minted model concept (`gpt-4o-mini-tts`).
- [[Wav2Vec2]] — minted model concept; the `torchaudio.pipelines.WAV2VEC2_BASE` audio encoder used for the similarity metric.
- [[EmotionGuidedTTS]] — minted concept page for the prompt-optimized TTS pattern this tutorial introduces.
- [[chainofthought]] / [[DSPySignatures]] / [[DSPyModules]] / [[DSPyPrediction]] / [[DSPyEvaluate]] / [[DSPyMetrics]] — composed primitives.
- [[MIPROv2]] — optimizer used twice; **first wiki receipt of the `data_aware_proposer=False` kwarg**.
- [[BootstrapFewShotWithRandomSearch]] — optimizer used on the Spoken-SQuAD task.
- [[openai|OpenAI]] — model + TTS provider.
- [[HuggingFace]] — dataset host (`AudioLLMs/spoken_squad_test`).
- [[SQuAD]] — text-only progenitor of [[SpokenSQuAD]].
- [[GPT4]] / [[GPT35Turbo]] — sibling OpenAI models in the wiki's GPT lineage.
- [[CosineSimilarity]] — the scoring function the Wav2Vec2 metric reduces to.
- [[chainofthought]] — wrapped both Signatures.

## Contradictions

- **No printed accuracy cells** — the Spoken-SQuAD §2 "approximately 10% improvement" is the only quantitative headline; unlike most DSPy tutorials in the corpus, the rendered page does not show before/after evaluation tables. The CREMA-D §3 "~0.57 → ~0.67" is similarly approximate.
- **`coral` voice fixed without ablation** — the 11-voice catalog is named but the voice axis is treated as out-of-scope for optimization. Voice selection could plausibly dominate the prompt-instruction optimization the tutorial measures, but no comparison is run.
- **Wav2Vec 2.0 mean-pooled embeddings are a weak proxy for emotion fidelity** — Wav2Vec2 is a speech-recognition encoder trained on phonetic content, not emotion. The tutorial flags this honestly but proceeds anyway; a paralinguistic-emotion encoder ([[Wav2Vec2|wav2vec2-large-xlsr-emotion]] / emotion2vec / HuBERT-emotion) would likely give stronger metric signal.
- **No cost disclosure** — continuing gap across the DSPy tutorial corpus; especially load-bearing here given the audio-token cost warning that motivates the conservative optimizer budgets.
- **Torch pin is CUDA-specific** — `torch==2.0.1+cu118` will not install on macOS / CPU-only hosts; tutorial does not flag the platform constraint.

## Scope-limit gaps

- **No `dspy.ReAct` / agent receipt on audio** — both programs are single-Signature.
- **No fine-tuning receipt** — `dspy.BootstrapFinetune` is not exercised; the audio-input model is not fine-tuned even though the data exists.
- **No GEPA receipt** — no [[GEPA|`dspy.GEPA`]] is tried on either task despite the per-example feedback signal being natural for audio-similarity scores.
- **No streaming / async / observability composition** — the audio outputs are returned synchronously; no `dspy.streamify` / `dspy.asyncify` / MLflow autolog receipt.
- **No comparison to a Whisper-based pipeline** — the spoken-QA task could equivalently be solved via `Whisper(audio) → text` + a text-LM ChainOfThought; the tutorial does not benchmark this baseline.
- **No multi-voice / multi-speaker generalization** — `"coral"` is the only voice tested.
- **No alternative similarity metric ablation** — e.g. emotion-classifier accuracy on `(generated_audio, emotion_label)` pairs as a downstream-task metric.
- **No save/load receipt** — neither optimized program is round-tripped through `program.save/load`.
- **No cost / wall-time / token-count disclosure** — especially for the audio-input Spoken-SQuAD task where audio tokens dominate.
