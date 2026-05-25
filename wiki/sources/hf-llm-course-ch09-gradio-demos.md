---
title: "HuggingFace LLM Course — Ch 9: Building and sharing demos with Gradio"
type: source
tags: [hf-llm-course, course, gradio, demos, spaces, ui]
date: 2026-05-23
source_file: raw/hf-llm-course/ch09-gradio-demos.md
---

## Summary

Chapter 9 of the HuggingFace LLM Course teaches how to build interactive web demos for ML models using [[Gradio]], a Python library for wrapping any function in a browser GUI. The chapter progresses from the high-level `gr.Interface` API (fn + inputs + outputs) through component customization, temporary shareable links, permanent hosting on [[HuggingFaceSpaces]], one-line loading of Hub models via `Interface.load()`, advanced features (session state for chatbots, interpretation via default/SHAP), and finally the low-level [[GradioBlocks]] API for custom layouts (rows/columns/tabs), multi-step pipelines, and event-driven UIs. The throughline: democratize model demonstration so researchers, QA testers, and end users can probe model behavior, surface biases, and reproduce results without leaving Python.

## Key Claims

- Demos serve four audiences: ML developers presenting work, researchers reproducing models, QA/end users debugging failure points, and diverse users discovering algorithmic biases.
- `gr.Interface(fn, inputs, outputs)` wraps any Python function into a browser UI in just a few lines; both inputs and outputs accept string shortcuts (e.g. `"text"`, `"audio"`, `"image"`, `"label"`, `"sketchpad"`) or instantiated component classes (e.g. `gr.Textbox(label=..., placeholder=..., lines=...)`).
- Components like `gr.Audio` accept a `source` (e.g. `"microphone"`) and `type` (e.g. `"numpy"` returning a `(sample_rate, data)` tuple) — the same component works as input or output.
- Passing lists to `inputs`/`outputs` maps positionally to function parameters and return values, enabling multi-input/multi-output demos (e.g. `[gr.Dropdown, gr.Slider, gr.Number]` → audio tone).
- `Interface` polish parameters include `title`, `description`, `article` (Markdown/HTML), `theme` (`default`, `huggingface`, `grass`, `peach`, with optional `dark-` prefix), `examples` (nested list), and `live=True` (rerun on every input change, no submit button).
- `launch(share=True)` creates a public `*.gradio.app` proxy link valid for 72 hours; processing still happens on the local device and Gradio claims not to store data. Colab notebooks always auto-create share links.
- Hugging Face Spaces provides free permanent hosting where Gradio code lives in an `app.py` file in a public/private repo.
- `gr.Interface.load("huggingface/<model>")` or `"model/<model>"` builds a demo backed by the [[HuggingFaceInferenceAPI]] rather than loading the model in memory — ideal for huge models like GPT-J or T0pp.
- `gr.Interface.load("spaces/<user>/<space>")` recreates an entire Space locally and lets you override any parameter (e.g. swap `inputs="webcam"`, change `title`).
- Session state persists across submits within a single page load (not across users): add an extra function parameter, return the updated state, and add `"state"` to inputs and outputs — the canonical chatbot pattern uses `["text", "state"]` → `["chatbot", "state"]`.
- `interpretation="default"` adds an "Interpret" button highlighting which input regions drove predictions; `interpretation="shap"` with `num_shap` enables Shapley-based attribution; custom interpretation functions are also supported.
- [[GradioBlocks]] (`gr.Blocks`) is a low-level API for custom data flow and layout: instantiate components inside a `with gr.Blocks() as demo:` context manager and explicitly wire events.
- Layout primitives: `gr.Row()` (horizontal, flexbox-style), `gr.Column()` (vertical, default), `gr.Tabs()` with nested `gr.TabItem(name)` contexts for tabbed UIs.
- Events are methods on component instances: `textbox.change(fn, inputs, outputs)`, `btn.click(...)`, `audio.play/clear/pause(...)`, `textbox.submit(...)`. Each event takes `fn`, `inputs`, `outputs` (any may be `None`).
- Input and output can be the same component (e.g. a GPT completion appended in-place to a single textbox), and Blocks supports multi-step pipelines by reusing one component as output of one event and input of another (e.g. ASR → sentiment classifier).
- A component's properties (visibility, line count, dropdown choices) can be updated dynamically by returning `gr.Textbox.update(lines=8, visible=True)` from an event handler instead of a plain value.
- Blocks auto-infers `interactive` from event wiring; override explicitly via `interactive=True/False` on the component.

## Key Quotes

> "Gradio allows you to build, customize, and share web-based demos for any machine learning model, entirely in Python." — Section 1

> "Demos allow ... Diverse users to discover algorithmic biases in models." — Section 1

> "Loading a model in this way uses Hugging Face's Inference API, instead of loading the model in memory. This is ideal for huge models like GPT-J or T0pp which require lots of RAM." — Section 5

> "Hugging Face Spaces provides the infrastructure to permanently host your Gradio model on the internet, for free!" — Section 4

> "Interface: a high-level API that allows you to create a full machine learning demo simply by providing a list of inputs and outputs. Blocks: a low-level API that allows you to have full control over the data flows and layout of your application." — Section 7

> "Blocks automatically figures out whether a component should be interactive (accept user input) or not, based on the event triggers you define." — Section 7

## Code & Patterns

### Minimal Interface (greet)
```py
import gradio as gr
def greet(name):
    return "Hello " + name
gr.Interface(fn=greet, inputs="text", outputs="text").launch()
```

### Customized component
```py
textbox = gr.Textbox(label="Type your name here:", placeholder="John Doe", lines=2)
gr.Interface(fn=greet, inputs=textbox, outputs="text").launch()
```

### Pipeline-backed model demo (GPT-2 text generation, ASR)
```py
from transformers import pipeline
import gradio as gr
model = pipeline("text-generation")
def predict(prompt): return model(prompt)[0]["generated_text"]
gr.Interface(fn=predict, inputs="text", outputs="text").launch()
```

### Multi-input audio tone generator
```py
gr.Interface(
    generate_tone,
    [gr.Dropdown(notes, type="index"),
     gr.Slider(minimum=4, maximum=6, step=1),
     gr.Number(value=1, label="Duration in seconds")],
    "audio",
).launch()
```

### Polished + shareable demo
```py
gr.Interface(
    fn=predict, inputs="textbox", outputs="text",
    title=title, description=description, article=article,
    examples=[["What are you doing?"], ["Where should we time travel to?"]],
).launch(share=True)
```

### Live sketchpad with theme
```py
gr.Interface(predict, inputs="sketchpad", outputs="label",
             theme="huggingface", title="Sketch Recognition",
             live=True).launch(share=True)
```

### Loading from the Hub / Spaces
```py
gr.Interface.load("huggingface/EleutherAI/gpt-j-6B", inputs=gr.Textbox(lines=5)).launch()
gr.Interface.load("spaces/abidlabs/remove-bg", inputs="webcam", title="...").launch()
```

### Chatbot with session state
```py
gr.Interface(chat, ["text", "state"], ["chatbot", "state"],
             allow_screenshot=False, allow_flagging="never").launch()
```

### Interpretation (default / SHAP)
```py
gr.Interface(fn=classify_image, inputs=image, outputs=label,
             interpretation="default").launch()
```

### Blocks — basic with event wiring
```py
with gr.Blocks() as demo:
    inp = gr.Textbox(placeholder="Flip this text")
    out = gr.Textbox()
    inp.change(fn=flip_text, inputs=inp, outputs=out)
demo.launch()
```

### Blocks — Tabs + Rows + Buttons
```py
with gr.Tabs():
    with gr.TabItem("Flip Text"):
        with gr.Row():
            text_input = gr.Textbox(); text_output = gr.Textbox()
        text_button = gr.Button("Flip")
text_button.click(flip_text, inputs=text_input, outputs=text_output)
```

### Blocks — multi-step pipeline (ASR → sentiment)
```py
b1.click(speech_to_text, inputs=audio_file, outputs=text)
b2.click(text_to_sentiment, inputs=text, outputs=label)
```

### Blocks — dynamic component update
```py
def change_textbox(choice):
    if choice == "short": return gr.Textbox.update(lines=2, visible=True)
    elif choice == "long": return gr.Textbox.update(lines=8, visible=True)
    else: return gr.Textbox.update(visible=False)
radio.change(fn=change_textbox, inputs=radio, outputs=text)
```

## Connections

- [[Gradio]] — the library that this entire chapter teaches.
- [[GradioInterface]] — high-level `gr.Interface(fn, inputs, outputs)` API covered in sections 2–6.
- [[GradioBlocks]] — low-level layout/event API covered in section 7.
- [[GradioComponents]] — Textbox, Audio, Image, Label, Dropdown, Slider, Number, Sketchpad, Radio, Button, Markdown, Chatbot, etc.
- [[HuggingFaceSpaces]] — free permanent hosting for Gradio demos via `app.py`.
- [[HuggingFaceHub]] — `Interface.load("huggingface/...")` builds demos from any Hub model.
- [[HuggingFaceInferenceAPI]] — backs `Interface.load` so RAM-heavy models (GPT-J, T0pp) work without local loading.
- [[Pipeline]] — `transformers.pipeline()` is the typical prediction function wrapped by an Interface.
- [[GPT2]], [[GPTJ]] — example text-generation models demoed.
- [[Wav2Vec2]] — `facebook/wav2vec2-base-960h` used in the speech-to-text Blocks example.
- [[MobileNetV2]] — used in the image classification + interpretation example.
- [[SHAP]] — Shapley-based interpretation option (`interpretation="shap"`, `num_shap=...`).
- [[InterpretableML]] / model explainability — connects to the interpretation feature.
- [[Chatbot]] — session-state pattern is the canonical chatbot demo.
- [[Colab]] / [[JupyterNotebook]] — supported runtimes; Colab auto-creates share links.
- [[AbubakarAbid]] — Gradio creator (`abidlabs` namespace appears in `spaces/abidlabs/remove-bg`).
- [[BackgroundRemoval]], [[SketchRecognition]], [[QuestionAnswering]] — example demos referenced.
- [[InferenceAPI]] — same as HF Inference API endpoint pattern.
- HF Course chapter 1 (text generation), chapter 4 (Hub), chapter 7 (QA) are cross-referenced.

## Contradictions

- None internal to this chapter. Note: Gradio's API has since evolved (modern versions deprecate `source=` on Audio and the `Interface.load` signature; `gr.Textbox.update` is replaced by returning `gr.update(...)` or the component directly). The chapter reflects an earlier Gradio 2.x/3.x API. No active contradictions with other wiki pages yet.
