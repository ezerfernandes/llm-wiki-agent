# DSPy Audio Tutorial

Source: https://dspy.ai/tutorials/audio/

## Overview

Tutorial demonstrates building audio-based applications using DSPy. Two use cases: spoken question answering and emotion-guided text-to-speech generation.

## Installation & Dependencies

```python
pip install -U dspy
pip install datasets soundfile torch==2.0.1+cu118 torchaudio==2.0.2+cu118
```

## Part 1: Spoken Question Answering

### Dataset: Spoken-SQuAD

Uses Spoken-SQuAD dataset, which "contains spoken audio passages used for question-answering." Loaded via HuggingFace:

```python
kwargs = dict(fields=("context", "instruction", "answer"),
              input_keys=("context", "instruction"))
spoken_squad = DataLoader().from_huggingface(
    dataset_name="AudioLLMs/spoken_squad_test",
    split="train",
    trust_remote_code=True,
    **kwargs)
```

### Audio Preprocessing

Audio data converted to byte arrays with sampling rates using DSPy's Audio primitive:

```python
def preprocess(x):
    audio = dspy.Audio.from_array(
        x.context["array"],
        x.context["sampling_rate"])
    return dspy.Example(
        passage_audio=audio,
        question=x.instruction,
        answer=x.answer
    ).with_inputs("passage_audio", "question")
```

### Signature Definition

```python
class SpokenQASignature(dspy.Signature):
    """Answer the question based on the audio clip."""
    passage_audio: dspy.Audio = dspy.InputField()
    question: str = dspy.InputField()
    answer: str = dspy.OutputField(
        desc='factoid answer between 1 and 5 words')
```

### Model Configuration

Program uses `gpt-4o-mini-audio-preview-2024-12-17`, which "can process input audio":

```python
dspy.configure(lm=dspy.LM(
    model='gpt-4o-mini-audio-preview-2024-12-17'))
spoken_qa = dspy.ChainOfThought(SpokenQASignature)
```

### Evaluation

Exact-match metric comparison against reference answers:

```python
evaluate_program = dspy.Evaluate(
    devset=testset,
    metric=dspy.evaluate.answer_exact_match,
    display_progress=True,
    num_threads=10,
    display_table=True)
```

### Optimization

Two optimizers demonstrated:

**BootstrapFewShotWithRandomSearch:**
```python
optimizer = dspy.BootstrapFewShotWithRandomSearch(
    metric=dspy.evaluate.answer_exact_match,
    max_bootstrapped_demos=2,
    max_labeled_demos=2,
    num_candidate_programs=5)
optimized_program = optimizer.compile(
    spoken_qa, trainset=trainset)
```

**MIPROv2:**
Tutorial notes "audio tokens can be costly," recommending conservative configuration with 0-2 few-shot examples. MIPROv2's dataset summarizer "cannot process the audio files," so the `data_aware_proposer` is disabled:

```python
prompt_lm = dspy.LM(model='gpt-4o-mini')
optimizer = dspy.MIPROv2(
    metric=dspy.evaluate.answer_exact_match,
    auto="light",
    prompt_model=prompt_lm)
optimized_program = optimizer.compile(
    spoken_qa,
    trainset=trainset,
    max_bootstrapped_demos=2,
    max_labeled_demos=2,
    data_aware_proposer=False)
```

Results showed approximately 10% improvement over baseline.

## Part 2: Emotion-Guided Text-to-Speech

### Dataset: CREMA-D

Dataset "includes audio clips of chosen participants speaking the same line with one of six target emotions: neutral, happy, sad, anger, fear, and disgust."

```python
label_map = ['neutral', 'happy', 'sad', 'anger', 'fear', 'disgust']
```

### TTS Implementation

Uses OpenAI's `gpt-4o-mini-tts` with instruction-based voice control:

```python
def generate_dspy_audio(raw_line: str, prompt: str) -> dspy.Audio:
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        input=raw_line,
        instructions=prompt,
        response_format="wav")
    # Returns encoded dspy.Audio object
```

Voice selection flexibility: "this can be configured to any of the 11 offered OpenAI TTS voices."

### TTS Instruction Signature

```python
class EmotionStylePromptSignature(dspy.Signature):
    """Generate an OpenAI TTS instruction that makes the TTS
    model speak the given line with the target emotion or style."""
    raw_line: str = dspy.InputField()
    target_style: str = dspy.InputField()
    openai_instruction: str = dspy.OutputField()
```

### Module Design

```python
class EmotionStylePrompter(dspy.Module):
    def __init__(self):
        self.prompter = dspy.ChainOfThought(
            EmotionStylePromptSignature)

    def forward(self, raw_line, target_style):
        out = self.prompter(
            raw_line=raw_line,
            target_style=target_style)
        audio = generate_dspy_audio(
            raw_line,
            out.openai_instruction)
        return dspy.Prediction(audio=audio)
```

### Audio Similarity Metric

Embedding-based comparison using Wav2Vec 2.0:

```python
bundle = torchaudio.pipelines.WAV2VEC2_BASE
model = bundle.get_model().eval()

def decode_dspy_audio(dspy_audio):
    audio_bytes = base64.b64decode(dspy_audio.data)
    array, _ = sf.read(
        io.BytesIO(audio_bytes),
        dtype="float32")
    return torch.tensor(array).unsqueeze(0)

def extract_embedding(audio_tensor):
    with torch.inference_mode():
        return model(audio_tensor)[0].mean(dim=1)

def audio_similarity_metric(example, pred, trace=None):
    ref_audio = decode_dspy_audio(example.reference_audio)
    gen_audio = decode_dspy_audio(pred.audio)

    ref_embed = extract_embedding(ref_audio)
    gen_embed = extract_embedding(gen_audio)

    score = cosine_similarity(ref_embed, gen_embed)

    if trace is not None:
        return score > 0.8
    return score
```

Tutorial acknowledges "audio reference comparisons is generally a non-trivial task due to subjective variations of evaluating speech, especially with emotional expression," noting "human feedback or perceptual metrics would be more suitable."

### TTS Optimization with MIPROv2

```python
prompt_lm = dspy.LM(model='gpt-4o-mini')
teleprompter = dspy.MIPROv2(
    metric=audio_similarity_metric,
    auto="light",
    prompt_model=prompt_lm)
optimized_program = teleprompter.compile(
    EmotionStylePrompter(),
    trainset=trainset)
```

Optimization produced refined prompts with detailed specifications for tone, pitch, and speaker characteristics, improving similarity scores from ~0.57 to ~0.67.

## Key Concepts

- **dspy.Audio**: Primitive for audio data handling supporting array conversion and base64 encoding
- **ChainOfThought**: Module enabling reasoning before generating outputs
- **Signatures**: Define input/output specifications with type annotations
- **Evaluation**: Metrics assess program performance on test sets
- **Optimization**: Teleprompters refine prompts and few-shot examples to improve downstream task performance
