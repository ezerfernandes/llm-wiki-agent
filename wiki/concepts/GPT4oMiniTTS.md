---
title: "gpt-4o-mini-tts (Text-to-Speech Model)"
type: concept
tags: [model, openai, tts, audio, gpt4o, multimodal]
sources: [dspy-audio-tutorial]
last_updated: 2026-05-24
---

# gpt-4o-mini-tts

[[openai|OpenAI]]'s **instruction-controllable text-to-speech model** — the audio-output sibling of [[GPT4oMiniAudio|`gpt-4o-mini-audio-preview-*`]]. Distinguishing feature vs prior OpenAI TTS endpoints: an explicit `instructions=` parameter that lets the caller specify **how** the line should be spoken (tone, pitch, emotion, speaker characteristics) in natural language — the lever the [[EmotionGuidedTTS|emotion-guided TTS]] pattern in [[dspy-audio-tutorial]] optimizes.

## API surface

```python
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
response = client.audio.speech.create(
    model="gpt-4o-mini-tts",
    voice="coral",                  # one of 11 named voices
    input=raw_line,                  # the text to speak
    instructions=prompt,             # natural-language style/emotion directive
    response_format="wav",
)
```

- **Endpoint**: `client.audio.speech.create(...)` — **not** the chat-completion endpoint. Lives outside DSPy's [[DSPyLM|`dspy.LM`]] abstraction; the [[dspy-audio-tutorial|tutorial]] wraps it inside a manual `dspy.Module.forward()`.
- **Voice catalog**: **11 named voices** per [[dspy-audio-tutorial]] (specific voices include `"coral"` — tutorial fixes this voice as a constant and treats voice selection as out-of-scope for prompt optimization).
- **Response formats**: `wav`, plus other audio container formats common to OpenAI's TTS line.

## DSPy integration pattern

Because the endpoint is non-chat, integration requires a hand-rolled wrapper:

```python
def generate_dspy_audio(raw_line: str, prompt: str) -> dspy.Audio:
    response = client.audio.speech.create(
        model="gpt-4o-mini-tts", voice="coral",
        input=raw_line, instructions=prompt, response_format="wav",
    )
    # encode response bytes → base64 → dspy.Audio
    ...
```

`prompt` is the field the [[EmotionGuidedTTS|EmotionStylePrompter]] Module optimizes via [[MIPROv2]] — i.e. DSPy treats the TTS instruction as a **prompt to be tuned by a prompt optimizer**, even though no DSPy LM call sends it.

## Wiki receipts

- **[[dspy-audio-tutorial]]** — first wiki receipt. Optimized [[MIPROv2|MIPROv2]] over the `instructions=` string lifts [[Wav2Vec2|Wav2Vec 2.0]] cosine similarity from **~0.57 → ~0.67** on [[CREMAD|CREMA-D]] line-emotion pairs.

## Connections

- [[openai|OpenAI]] — provider.
- [[GPT4oMiniAudio]] — audio-input sibling.
- [[GPT4]] / [[GPT35Turbo]] — lineage.
- [[DSPyAudio]] — the primitive the wrapper emits.
- [[EmotionGuidedTTS]] — the prompt-optimization pattern minted around this endpoint.
- [[CREMAD]] — the benchmark used.
- [[MIPROv2]] — the optimizer.
- [[dspy-audio-tutorial]] — first wiki receipt.
