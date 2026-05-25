# HuggingFace LLM Course — Chapter 9: Building and sharing demos with Gradio
Source: https://huggingface.co/learn/llm-course/chapter9/
Sections: 1,2,3,4,5,6,7,8
---

## Section 1: Introduction to Gradio

In this chapter we will be learning about how to build **interactive demos** for your machine learning models.

Why build a demo or a GUI for your machine learning model in the first place? Demos allow:

- **Machine learning developers** to easily present their work to a wide audience including non-technical teams or customers
- **Researchers** to more easily reproduce machine learning models and behavior
- **Quality testers** or **end users** to more easily identify and debug failure points of models
- **Diverse users** to discover algorithmic biases in models

We'll be using the Gradio library to build demos for our models. Gradio allows you to build, customize, and share web-based demos for any machine learning model, entirely in Python.

Here are some examples of machine learning demos built with Gradio:

* A **sketch recognition** model that takes in a sketch and outputs labels of what it thinks is being drawn.
* An extractive **question answering** model that takes in a context paragraph and a quest and outputs a response and a probability score (we discussed this kind of model in Chapter 7).
* A **background removal** model that takes in an image and outputs the image with the background removed.

This chapter is broken down into sections which include both _concepts_ and _applications_. After you learn the concept in each section, you'll apply it to build a particular kind of demo, ranging from image classification to speech recognition. By the time you finish this chapter, you'll be able to build these demos (and many more!) in just a few lines of Python code.

> [!TIP]
> Check out Hugging Face Spaces to see many recent examples of machine learning demos built by the machine learning community!

---

## Section 2: Building your first demo

Let's start by installing Gradio! Since it is a Python package, simply run:

`$ pip install gradio `

You can run Gradio anywhere, be it from your favourite Python IDE, to Jupyter notebooks or even in Google Colab!
So install Gradio wherever you run Python!

Let's get started with a simple "Hello World" example to get familiar with the Gradio syntax:

```py
import gradio as gr

def greet(name):
    return "Hello " + name

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch()
```

Let's walk through the code above:

- First, we define a function called `greet()`. In this case, it is a simple function that adds "Hello" before your name, but it can be *any* Python function in general. For example, in machine learning applications, this function would *call a model to make a prediction* on an input and return the output.
- Then, we create a Gradio `Interface` with three arguments, `fn`, `inputs`, and `outputs`. These arguments define the prediction function, as well as the _type_ of input and output components we would like. In our case, both components are simple text boxes.
- We then call the `launch()` method on the `Interface` that we created.

If you run this code, the interface below will appear automatically within a Jupyter/Colab notebook, or pop in a browser on **[http://localhost:7860](http://localhost:7860/)** if running from a script.

You'll notice that in this GUI, Gradio automatically inferred the name of the input parameter (`name`) and applied it as a label on top of the textbox. What if you'd like to change that? Or if you'd like to customize the textbox in some other way? In that case, you can instantiate a class object representing the input component.

Take a look at the example below:

```py
import gradio as gr

def greet(name):
    return "Hello " + name

# We instantiate the Textbox class
textbox = gr.Textbox(label="Type your name here:", placeholder="John Doe", lines=2)

gr.Interface(fn=greet, inputs=textbox, outputs="text").launch()
```

Here, we've created an input textbox with a label, a placeholder, and a set number of lines. You could do the same for the output textbox, but we'll leave that for now.

### Including model predictions

Let's now build a simple interface that allows you to demo a **text-generation** model like GPT-2.

We'll load our model using the `pipeline()` function from Transformers.

First, we define a prediction function that takes in a text prompt and returns the text completion:

```py
from transformers import pipeline

model = pipeline("text-generation")

def predict(prompt):
    completion = model(prompt)[0]["generated_text"]
    return completion
```

Example:

```
predict("My favorite programming language is")
```

```
>> My favorite programming language is Haskell. I really enjoyed the Haskell language, but it doesn't have all the features that can be applied to any other language. For example, all it does is compile to a byte array.
```

Now that we have a function for generating predictions, we can create and launch an `Interface` in the same way we did earlier:

```py
import gradio as gr

gr.Interface(fn=predict, inputs="text", outputs="text").launch()
```

---

## Section 3: Understanding the Interface class

In this section, we will take a closer look at the `Interface` class, and understand the main parameters used to create one.

### How to create an Interface

You'll notice that the `Interface` class has 3 required parameters:

`Interface(fn, inputs, outputs, ...)`

These parameters are:

- `fn`: the prediction function that is wrapped by the Gradio interface. This function can take one or more parameters and return one or more values
- `inputs`: the input component type(s). Gradio provides many pre-built components such as `"image"` or `"mic"`.
- `outputs`: the output component type(s). Again, Gradio provides many pre-built components e.g. `"image"` or `"label"`.

For a complete list of components, see the Gradio docs. Each pre-built component can be customized by instantiating the class corresponding to the component.

For example, instead of passing in `"textbox"` to the `inputs` parameter, you can pass in a `Textbox(lines=7, label="Prompt")` component to create a textbox with 7 lines and a label.

### A simple example with audio

Gradio provides many different inputs and outputs. So let's build an `Interface` that works with audio.

In this example, we'll build an audio-to-audio function that takes an audio file and simply reverses it.

We will use for the input the `Audio` component. When using the `Audio` component, you can specify whether you want the `source` of the audio to be a file that the user uploads or a microphone that the user records their voice with. In this case, let's set it to a `"microphone"`. Just for fun, we'll add a label to our `Audio` that says "Speak here...".

In addition, we'd like to receive the audio as a numpy array so that we can easily "reverse" it. So we'll set the `"type"` to be `"numpy"`, which passes the input data as a tuple of (`sample_rate`, `data`) into our function.

We will also use the `Audio` output component which can automatically render a tuple with a sample rate and numpy array of data as a playable audio file. In this case, we do not need to do any customization, so we will use the string shortcut `"audio"`.

```py
import numpy as np
import gradio as gr

def reverse_audio(audio):
    sr, data = audio
    reversed_audio = (sr, np.flipud(data))
    return reversed_audio

mic = gr.Audio(source="microphone", type="numpy", label="Speak here...")
gr.Interface(reverse_audio, mic, "audio").launch()
```

### Handling multiple inputs and outputs

Let's say we had a more complicated function, with multiple inputs and outputs. In the example below, we have a function that takes a dropdown index, a slider value, and number, and returns an audio sample of a musical tone.

The key here is that when you pass:
* a list of input components, each component corresponds to a parameter in order.
* a list of output components, each component corresponds to a returned value.

```py
import numpy as np
import gradio as gr

notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def generate_tone(note, octave, duration):
    sr = 48000
    a4_freq, tones_from_a4 = 440, 12 * (octave - 4) + (note - 9)
    frequency = a4_freq * 2 ** (tones_from_a4 / 12)
    duration = int(duration)
    audio = np.linspace(0, duration, duration * sr)
    audio = (20000 * np.sin(audio * (2 * np.pi * frequency))).astype(np.int16)
    return (sr, audio)

gr.Interface(
    generate_tone,
    [
        gr.Dropdown(notes, type="index"),
        gr.Slider(minimum=4, maximum=6, step=1),
        gr.Number(value=1, label="Duration in seconds"),
    ],
    "audio",
).launch()
```

### The `launch()` method

By default, the `launch()` method will launch the demo in a web server that is running locally. If you are running your code in a Jupyter or Colab notebook, then Gradio will embed the demo GUI in the notebook so you can easily use it.

You can customize the behavior of `launch()` through different parameters:

- `inline` - whether to display the interface inline on Python notebooks.
- `inbrowser` - whether to automatically launch the interface in a new tab on the default browser.
- `share` - whether to create a publicly shareable link from your computer for the interface. Kind of like a Google Drive link!

### Let's apply it: speech-recognition demo

Let's build an interface that allows you to demo a **speech-recognition** model. To make it interesting, we will accept *either* a mic input or an uploaded file.

```py
from transformers import pipeline
import gradio as gr

model = pipeline("automatic-speech-recognition")

def transcribe_audio(audio):
    transcription = model(audio)["text"]
    return transcription

gr.Interface(
    fn=transcribe_audio,
    inputs=gr.Audio(type="filepath"),
    outputs="text",
).launch()
```

Notice that by passing in the `optional` parameter as `True`, we allow the user to either provide a microphone or an audio file (or neither, but that will return an error message).

---

## Section 4: Sharing demos with others

Now that you've built a demo, you'll probably want to share it with others. Gradio demos can be shared in two ways: using a ***temporary share link*** or ***permanent hosting on Spaces***.

### Polishing your Gradio demo

To add additional content to your demo, the `Interface` class supports some optional parameters:

- `title`: you can give a title to your demo, which appears _above_ the input and output components.
- `description`: you can give a description (in text, Markdown, or HTML) for the interface, which appears above the input and output components and below the title.
- `article`: you can also write an expanded article (in text, Markdown, or HTML) explaining the interface. If provided, it appears _below_ the input and output components.
- `theme`: don't like the default colors? Set the theme to use one of `default`, `huggingface`, `grass`, `peach`. You can also add the `dark-` prefix, e.g. `dark-peach` for dark theme (or just `dark` for the default dark theme).
- `examples`: to make your demo *way easier to use*, you can provide some example inputs for the function. These appear below the UI components and can be used to populate the interface. These should be provided as a nested list, in which the outer list consists of samples and each inner list consists of an input corresponding to each input component.
- `live`: if you want to make your demo "live", meaning that your model reruns every time the input changes, you can set `live=True`. This makes sense to use with quick models.

```py
title = "Ask Rick a Question"
description = """
The bot was trained to answer questions based on Rick and Morty dialogues. Ask Rick anything!

"""

article = "Check out [the original Rick and Morty Bot](https://huggingface.co/spaces/kingabzpro/Rick_and_Morty_Bot) that this demo is based off of."

gr.Interface(
    fn=predict,
    inputs="textbox",
    outputs="text",
    title=title,
    description=description,
    article=article,
    examples=[["What are you doing?"], ["Where should we time travel to?"]],
).launch()
```

### Sharing your demo with temporary links

Interfaces can be easily shared publicly by setting `share=True` in the `launch()` method:

```python
gr.Interface(classify_image, "image", "label").launch(share=True)
```

This generates a public, shareable link that you can send to anybody! When you send this link, the user on the other side can try out the model in their browser for up to 72 hours. Because the processing happens on your device (as long as your device stays on!), you don't have to worry about packaging any dependencies. If you're working out of a Google Colab notebook, a share link is always automatically created. It usually looks something like this: **XXXXX.gradio.app**. Although the link is served through a Gradio link, we are only a proxy for your local server, and do not store any data sent through the interfaces.

Keep in mind, however, that these links are publicly accessible, meaning that anyone can use your model for prediction! Therefore, make sure not to expose any sensitive information through the functions you write, or allow any critical changes to occur on your device. If you set `share=False` (the default), only a local link is created.

### Hosting your demo on Hugging Face Spaces

Hugging Face Spaces provides the infrastructure to permanently host your Gradio model on the internet, **for free**! Spaces allows you to create and push to a (public or private) repo, where your Gradio interface code will exist in an `app.py` file.

### Let's apply it: Sketch Recognition demo

```py
from pathlib import Path
import torch
import gradio as gr
from torch import nn

LABELS = Path("class_names.txt").read_text().splitlines()

model = nn.Sequential(
    nn.Conv2d(1, 32, 3, padding="same"),
    nn.ReLU(),
    nn.MaxPool2d(2),
    nn.Conv2d(32, 64, 3, padding="same"),
    nn.ReLU(),
    nn.MaxPool2d(2),
    nn.Conv2d(64, 128, 3, padding="same"),
    nn.ReLU(),
    nn.MaxPool2d(2),
    nn.Flatten(),
    nn.Linear(1152, 256),
    nn.ReLU(),
    nn.Linear(256, len(LABELS)),
)
state_dict = torch.load("pytorch_model.bin", map_location="cpu")
model.load_state_dict(state_dict, strict=False)
model.eval()

def predict(im):
    x = torch.tensor(im, dtype=torch.float32).unsqueeze(0).unsqueeze(0) / 255.0
    with torch.no_grad():
        out = model(x)
    probabilities = torch.nn.functional.softmax(out[0], dim=0)
    values, indices = torch.topk(probabilities, 5)
    return {LABELS[i]: v.item() for i, v in zip(indices, values)}
```

```py
interface = gr.Interface(
    predict,
    inputs="sketchpad",
    outputs="label",
    theme="huggingface",
    title="Sketch Recognition",
    description="Who wants to play Pictionary? Draw a common object like a shovel or a laptop, and the algorithm will guess in real time!",
    article="Sketch Recognition | Demo Model",
    live=True,
)
interface.launch(share=True)
```

Notice the `live=True` parameter in `Interface`, which means that the sketch demo makes a prediction every time someone draws on the sketchpad (no submit button!). Furthermore, we also set the `share=True` argument in the `launch()` method.

---

## Section 5: Integrations with the Hugging Face Hub

Gradio integrates directly with Hugging Face Hub and Hugging Face Spaces. You can load demos from the Hub and Spaces with only *one line of code*.

### Loading models from the Hugging Face Hub

To start with, choose one of the thousands of models Hugging Face offers through the Hub.

Using the special `Interface.load()` method, you pass `"model/"` (or, equivalently, `"huggingface/"`) followed by the model name. For example, here is the code to build a demo for GPT-J, a large language model, add a couple of example inputs:

```py
import gradio as gr

title = "GPT-J-6B"
description = "Gradio Demo for GPT-J 6B, a transformer model trained using Ben Wang's Mesh Transformer JAX. 'GPT-J' refers to the class of model, while '6B' represents the number of trainable parameters. To use it, simply add your text, or click one of the examples to load them. Read more at the links below."
article = "GPT-J-6B: A 6 Billion Parameter Autoregressive Language Model"

gr.Interface.load(
    "huggingface/EleutherAI/gpt-j-6B",
    inputs=gr.Textbox(lines=5, label="Input Text"),
    title=title,
    description=description,
    article=article,
).launch()
```

Loading a model in this way uses Hugging Face's Inference API, instead of loading the model in memory. This is ideal for huge models like GPT-J or T0pp which require lots of RAM.

### Loading from Hugging Face Spaces

To load any Space from the Hugging Face Hub and recreate it locally, you can pass `spaces/` to the `Interface`, followed by the name of the Space.

```py
gr.Interface.load("spaces/abidlabs/remove-bg").launch()
```

One of the cool things about loading demos from the Hub or Spaces is that you customize them by overriding any of the parameters. Here, we add a title and get it to work with a webcam instead:

```py
gr.Interface.load(
    "spaces/abidlabs/remove-bg", inputs="webcam", title="Remove your webcam background!"
).launch()
```

---

## Section 6: Advanced Interface features

### Using state to persist data

Gradio supports *session state*, where data persists across multiple submits within a page load. Session state is useful for building demos of, for example, chatbots where you want to persist data as the user interacts with the model. Note that session state does not share data between different users of your model.

To store data in a session state, you need to do three things:

1. Pass in an *extra parameter* into your function, which represents the state of the interface.
2. At the end of the function, return the updated value of the state as an *extra return value*.
3. Add the 'state' input and 'state' output components when creating your `Interface`.

See the chatbot example below:

```py
import random

import gradio as gr

def chat(message, history):
    history = history or []
    if message.startswith("How many"):
        response = random.randint(1, 10)
    elif message.startswith("How"):
        response = random.choice(["Great", "Good", "Okay", "Bad"])
    elif message.startswith("Where"):
        response = random.choice(["Here", "There", "Somewhere"])
    else:
        response = "I don't know"
    history.append((message, response))
    return history, history

iface = gr.Interface(
    chat,
    ["text", "state"],
    ["chatbot", "state"],
    allow_screenshot=False,
    allow_flagging="never",
)
iface.launch()
```

Note: you can pass in a default value to the state parameter, which is used as the initial value of the state.

### Using interpretation to understand predictions

Most machine learning models are black boxes and the internal logic of the function is hidden from the end user. To encourage transparency, we've made it very easy to add interpretation to your model by simply setting the interpretation keyword in the Interface class to default. This allows your users to understand what parts of the input are responsible for the output.

```py
import requests
import tensorflow as tf

import gradio as gr

inception_net = tf.keras.applications.MobileNetV2()  # load the model

# Download human-readable labels for ImageNet.
response = requests.get("https://git.io/JJkYN")
labels = response.text.split("\n")

def classify_image(inp):
    inp = inp.reshape((-1, 224, 224, 3))
    inp = tf.keras.applications.mobilenet_v2.preprocess_input(inp)
    prediction = inception_net.predict(inp).flatten()
    return {labels[i]: float(prediction[i]) for i in range(1000)}

image = gr.Image(shape=(224, 224))
label = gr.Label(num_top_classes=3)

title = "Gradio Image Classifiction + Interpretation Example"
gr.Interface(
    fn=classify_image, inputs=image, outputs=label, interpretation="default", title=title
).launch()
```

Besides the default interpretation method Gradio provides, you can also specify `shap` for the `interpretation` parameter and set the `num_shap` parameter. This uses Shapley-based interpretation. Lastly, you can also pass in your own interpretation function into the `interpretation` parameter.

---

## Section 7: Introduction to Blocks

In the previous sections we have explored and created demos using the `Interface` class. In this section we will introduce our **newly developed** low-level API called `gradio.Blocks`.

Now, what's the difference between `Interface` and `Blocks`?

- `Interface`: a high-level API that allows you to create a full machine learning demo simply by providing a list of inputs and outputs.
- `Blocks`: a low-level API that allows you to have full control over the data flows and layout of your application. You can build very complex, multi-step applications using `Blocks` (as in "building blocks").

### Why Blocks?

The `Interface` API is extremely easy to use but lacks the flexibility that the `Blocks` API provides. For example, you might want to:

- Group together related demos as multiple tabs in one web application
- Change the layout of your demo, e.g. to specify where the inputs and outputs are located
- Have multi-step interfaces, in which the output of one model becomes the input to the next model, or have more flexible data flows in general
- Change a component's properties (for example, the choices in a dropdown) or its visibility based on user input

### Creating a simple demo using Blocks

```py
import gradio as gr

def flip_text(x):
    return x[::-1]

demo = gr.Blocks()

with demo:
    gr.Markdown(
        """
    # Flip Text!
    Start typing below to see the output.
    """
    )
    input = gr.Textbox(placeholder="Flip this text")
    output = gr.Textbox()

    input.change(fn=flip_text, inputs=input, outputs=output)

demo.launch()
```

This simple example above introduces 4 concepts that underlie Blocks:

1. Blocks allow you to build web applications that combine markdown, HTML, buttons, and interactive components simply by instantiating objects in Python inside of a `with gradio.Blocks` context. The order in which you instantiate components matters as each element gets rendered into the web app in the order it was created.

2. You can define regular Python functions anywhere in your code and run them with user input using `Blocks`.

3. You can assign events to any `Blocks` component. This will run your function when the component is clicked, changed, etc. When you assign an event, you pass in three parameters: `fn`: the function that should be called, `inputs`: the (list) of input component(s), and `outputs`: the (list) of output components that should be called.

4. Blocks automatically figures out whether a component should be interactive (accept user input) or not, based on the event triggers you define. You can override this by passing a boolean to the `interactive` parameter of the component.

### Customizing the layout of your demo

How can we use `Blocks` to customize the layout of our demo? By default, `Blocks` renders the components that you create vertically in one column. You can change that by creating additional columns `with gradio.Column():` or rows `with gradio.Row():` and creating components within those contexts.

Any components created under a `Column` (this is also the default) will be laid out vertically. Any component created under a `Row` will be laid out horizontally, similar to the flexbox model in web development.

Finally, you can also create tabs for your demo by using the `with gradio.Tabs()` context manager. Within this context, you can create multiple tabs by specifying `with gradio.TabItem(name_of_tab):` children.

```py
import numpy as np
import gradio as gr

demo = gr.Blocks()

def flip_text(x):
    return x[::-1]

def flip_image(x):
    return np.fliplr(x)

with demo:
    gr.Markdown("Flip text or image files using this demo.")
    with gr.Tabs():
        with gr.TabItem("Flip Text"):
            with gr.Row():
                text_input = gr.Textbox()
                text_output = gr.Textbox()
            text_button = gr.Button("Flip")
        with gr.TabItem("Flip Image"):
            with gr.Row():
                image_input = gr.Image()
                image_output = gr.Image()
            image_button = gr.Button("Flip")

    text_button.click(flip_text, inputs=text_input, outputs=text_output)
    image_button.click(flip_image, inputs=image_input, outputs=image_output)

demo.launch()
```

### Exploring events and state

Just as you can control the layout, `Blocks` gives you fine-grained control over what events trigger function calls. Each component and many layouts have specific events that they support.

For example, the `Textbox` component has 2 events: `change()` (when the value inside of the textbox changes), and `submit()` (when a user presses the enter key while focused on the textbox). More complex components can have even more events: for example, the `Audio` component also has separate events for when the audio file is played, cleared, paused, etc.

You can attach event trigger to none, one, or more of these events. You create an event trigger by calling the name of the event on the component instance as a function -- e.g. `textbox.change(...)` or `btn.click(...)`. The function takes in three parameters:

- `fn`: the function to run
- `inputs`: a (list of) component(s) whose values should supplied as the input parameters to the function. Each component's value gets mapped to the corresponding function parameter, in order. This parameter can be None if the function does not take any parameters.
- `outputs`: a (list of) component(s) whose values should be updated based on the values returned by the function. Each return value sets the corresponding component's value, in order. This parameter can be None if the function does not return anything.

You can even make the input and output component be the same component:

```py
import gradio as gr

api = gr.Interface.load("huggingface/EleutherAI/gpt-j-6B")

def complete_with_gpt(text):
    # Use the last 50 characters of the text as context
    return text[:-50] + api(text[-50:])

with gr.Blocks() as demo:
    textbox = gr.Textbox(placeholder="Type here and press enter...", lines=4)
    btn = gr.Button("Generate")

    btn.click(complete_with_gpt, textbox, textbox)

demo.launch()
```

### Creating multi-step demos

In some cases, you might want a _multi-step demo_, in which you reuse the output of one function as the input to the next. This is really easy to do with `Blocks`, as you can use a component for the input of one event trigger but the output of another.

```py
from transformers import pipeline

import gradio as gr

asr = pipeline("automatic-speech-recognition", "facebook/wav2vec2-base-960h")
classifier = pipeline("text-classification")

def speech_to_text(speech):
    text = asr(speech)["text"]
    return text

def text_to_sentiment(text):
    return classifier(text)[0]["label"]

demo = gr.Blocks()

with demo:
    audio_file = gr.Audio(type="filepath")
    text = gr.Textbox()
    label = gr.Label()

    b1 = gr.Button("Recognize Speech")
    b2 = gr.Button("Classify Sentiment")

    b1.click(speech_to_text, inputs=audio_file, outputs=text)
    b2.click(text_to_sentiment, inputs=text, outputs=label)

demo.launch()
```

### Updating Component Properties

You can change other properties of a component, like the visibility of a textbox or the choices in a radio button group, by returning a component class's `update()` method instead of a regular return value from your function.

```py
import gradio as gr

def change_textbox(choice):
    if choice == "short":
        return gr.Textbox.update(lines=2, visible=True)
    elif choice == "long":
        return gr.Textbox.update(lines=8, visible=True)
    else:
        return gr.Textbox.update(visible=False)

with gr.Blocks() as block:
    radio = gr.Radio(
        ["short", "long", "none"], label="What kind of essay would you like to write?"
    )
    text = gr.Textbox(lines=2, interactive=True)

    radio.change(fn=change_textbox, inputs=radio, outputs=text)
    block.launch()
```

Just like with `Interfaces`, you can create cool demos that can be shared by using `share=True` in the `launch()` method or deployed on Hugging Face Spaces.

---

## Section 8: Gradio, check!

This wraps up the chapter on building cool ML demos with Gradio. To recap, in this chapter we learned:

- How to create Gradio demos with the high-level `Interface` API, and how to configure different input and output modalities.
- Different ways to share Gradio demos, through temporary links and hosting on Hugging Face Spaces.
- How to integrate Gradio demos with models and Spaces on the Hugging Face Hub.
- Advanced features like storing state in a demo or providing authentication.
- How to have full control of the data flow and layout of your demo with Gradio Blocks.

### Where to next?

If you want to learn more about Gradio you can:

- Take a look at Demos in the gradio-app/gradio repo, there are quite a lot of examples there.
- See the Guides page at gradio.app/guides, where you can find guides about cool and advanced features.
- Check the Docs page at gradio.app/docs to learn the details.
