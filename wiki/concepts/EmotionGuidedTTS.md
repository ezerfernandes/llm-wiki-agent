---
title: "Emotion-Guided TTS (prompt-optimized TTS pattern)"
type: concept
tags: [dspy, pattern, tts, audio, emotion, prompt-optimization, miprov2]
sources: [dspy-audio-tutorial]
last_updated: 2026-05-24
---

# Emotion-Guided TTS

**[[DSPy]] pattern** for treating a text-to-speech endpoint's `instructions=` parameter as **a prompt to be optimized by a prompt-optimizer**, even though the endpoint is not a chat-completion LM. Minted in [[dspy-audio-tutorial]] §3. The pattern is **provider-agnostic** in principle but the wiki's first receipt instantiates it on [[openai|OpenAI]]'s [[GPT4oMiniTTS|`gpt-4o-mini-tts`]] endpoint.

## Pattern shape

```python
class EmotionStylePromptSignature(dspy.Signature):
    """Generate an OpenAI TTS instruction that makes the TTS model
    speak the given line with the target emotion or style."""
    raw_line: str = dspy.InputField()
    target_style: str = dspy.InputField()
    openai_instruction: str = dspy.OutputField()

class EmotionStylePrompter(dspy.Module):
    def __init__(self):
        self.prompter = dspy.ChainOfThought(EmotionStylePromptSignature)
    def forward(self, raw_line, target_style):
        out = self.prompter(raw_line=raw_line, target_style=target_style)
        audio = generate_dspy_audio(raw_line, out.openai_instruction)  # TTS HTTP call
        return dspy.Prediction(audio=audio)
```

Three load-bearing structural choices:

1. **The TTS call is *outside* the DSPy LM abstraction** — wrapped in a plain helper `generate_dspy_audio(...)` invoked from `forward()`. DSPy's [[DSPyLM|`dspy.LM`]] client does not multiplex non-chat audio-output endpoints.
2. **The optimized object is the *instruction string***, not a chat-completion prompt — the LM call that produces it (`dspy.ChainOfThought(EmotionStylePromptSignature)`) *is* a chat completion, but the optimized artifact is consumed by a TTS HTTP endpoint.
3. **The module returns audio inside a [[DSPyPrediction|`dspy.Prediction`]]** with an `audio=` field of type [[DSPyAudio|`dspy.Audio`]] — preserves DSPy's standard return contract so any DSPy evaluation/optimization machinery can consume the result.

## Metric

[[Wav2Vec2]] mean-pooled embedding + [[CosineSimilarity|cosine similarity]] vs a reference recording. The `trace is not None` branch binarizes at `score > 0.8` (the DSPy optimizer-bootstrap convention).

## Headline result

[[MIPROv2|`MIPROv2(auto="light", prompt_model=gpt-4o-mini)`]] over `EmotionStylePrompter()` on [[CREMAD]] lifts cosine similarity **~0.57 → ~0.67** (~+17.5% relative). The optimizer drives the TTS instruction surface from short emotion-label injection ("speak this with anger") toward dense paralinguistic descriptors specifying tone, pitch, and speaker characteristics.

## Generalization

The pattern generalizes beyond emotion to **any TTS instruction axis** (formality, character voice, accent, pacing) and beyond TTS to **any non-chat generative endpoint whose call is parameterized by a natural-language string**: image-gen prompts to Imagen/DALL-E, code-action instructions to specialized agents, etc. The DSPy contribution is showing that a prompt-optimizer can optimize the *instruction-string* axis without owning the downstream API call.

## Connections

- [[DSPy]] / [[DSPyModules]] / [[DSPySignatures]] / [[DSPyPrediction]] — composed primitives.
- [[DSPyAudio]] — the output type.
- [[GPT4oMiniTTS]] — the TTS endpoint the first receipt targets.
- [[MIPROv2]] — the optimizer applied to the pattern.
- [[Wav2Vec2]] — the metric encoder.
- [[CosineSimilarity]] — the metric reduction.
- [[CREMAD]] — the dataset.
- [[chainofthought]] — the wrapper Module on the instruction-generation Signature.
- [[dspy-audio-tutorial]] — first wiki receipt.
