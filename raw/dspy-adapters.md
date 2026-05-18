# DSPy Adapters

*Source: https://dspy.ai/learn/programming/adapters/ — page 6 of 13 of the DSPy Learn section.*

## What Adapters Do

Adapters function as **the bridge between `dspy.Predict` and the actual Language Model (LM)** — translators between DSPy's structured `Predict` module and language models. They handle three critical tasks:

1. Converting [[DSPySignatures|signatures]] into system messages that define the task.
2. Formatting input data per request structures.
3. Parsing LM responses into structured outputs like `dspy.Prediction` instances.

Adapters also handle:

- Managing conversation history and function calls.
- Converting DSPy types (`Tool`, `Image`, etc.) into prompt messages.

## Configuration Methods

You can set adapters globally via `dspy.configure(adapter=...)` or locally through `with dspy.context(adapter=...)`. When no adapter is specified, DSPy defaults to `ChatAdapter`.

```python
import dspy

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))

predict = dspy.Predict("question -> answer")
result = predict(question="What is the capital of France?")
```

The above is equivalent to:

```python
import dspy

dspy.configure(
    lm=dspy.LM("openai/gpt-4o-mini"),
    adapter=dspy.ChatAdapter(),  # This is the default value
)

predict = dspy.Predict("question -> answer")
result = predict(question="What is the capital of France?")
```

## System Architecture: Processing Flow

The processing flow follows these steps:

1. User invokes a DSPy module with inputs.
2. Inner `dspy.Predict` calls `Adapter.format()`.
3. Adapter converts signature, inputs, and demonstrations into multi-turn messages.
4. Language model generates response.
5. `Adapter.parse()` transforms the response into structured outputs.
6. Caller receives parsed results.

You can inspect formatted messages via `adapter.format(signature, demos, inputs)` or view only the system message with `adapter.format_system_message(signature)`.

```python
# Simplified flow example
signature = dspy.Signature("question -> answer")
inputs = {"question": "What is 2+2?"}
demos = [{"question": "What is 1+1?", "answer": "2"}]

adapter = dspy.ChatAdapter()
print(adapter.format(signature, demos, inputs))
```

```python
import dspy

signature = dspy.Signature("question -> answer")
system_message = dspy.ChatAdapter().format_system_message(signature)
print(system_message)
```

## ChatAdapter (Default)

**Structure:** Uses field delimiters like `[[ ## field_name ## ]]` to delineate sections. Complex types include their JSON schemas in instructions.

**Strengths:**

- **Universal compatibility:** Works with all language models.
- Includes automatic fallback to `JSONAdapter` on failure.
- More verbose but reliable for smaller models.

**Drawbacks:** Higher token count may increase latency compared to alternatives — "more boilerplate output tokens compared to other adapters."

### ChatAdapter with Complex Types

```python
import dspy
import pydantic

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"), adapter=dspy.ChatAdapter())


class ScienceNews(pydantic.BaseModel):
    text: str
    scientists_involved: list[str]


class NewsQA(dspy.Signature):
    """Get news about the given science field"""

    science_field: str = dspy.InputField()
    year: int = dspy.InputField()
    num_of_outputs: int = dspy.InputField()
    news: list[ScienceNews] = dspy.OutputField(desc="science news")

predict = dspy.Predict(NewsQA)
predict(science_field="Computer Theory", year=2022, num_of_outputs=1)
dspy.inspect_history()
```

For non-primitive output types, `ChatAdapter` includes the JSON schema of the pydantic model in the system instructions, then asks the LM to emit field values inside the `[[ ## field_name ## ]]` delimiters.

## JSONAdapter

**Structure:** Formats inputs like `ChatAdapter` but requests JSON-formatted responses containing all output fields. Prompts LMs to return JSON with all output fields.

**Strengths:**

- "Effective for models that support structured output via the `response_format` parameter."
- Leverages native structured output features when available.
- Minimizes boilerplate, reducing latency — "Minimal boilerplate in the LM response results in faster responses."
- Produces clean, parseable JSON responses.

**Limitations:** Requires models supporting the `response_format` parameter; incompatible with smaller open-source models lacking this capability.

### JSONAdapter with Complex Types

```python
import dspy
import pydantic

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"), adapter=dspy.JSONAdapter())


class ScienceNews(pydantic.BaseModel):
    text: str
    scientists_involved: list[str]


class NewsQA(dspy.Signature):
    """Get news about the given science field"""

    science_field: str = dspy.InputField()
    year: int = dspy.InputField()
    num_of_outputs: int = dspy.InputField()
    news: list[ScienceNews] = dspy.OutputField(desc="science news")

predict = dspy.Predict(NewsQA)
predict(science_field="Computer Theory", year=2022, num_of_outputs=1)
dspy.inspect_history()
```

## Additional Adapters

The documentation references `XMLAdapter` and `TwoStepAdapter` in the API reference section. These are alternative adapters available in the DSPy framework for specialized use cases (XML-formatted I/O and two-step extract-then-format workflows respectively), but the main page does not provide detailed implementations or usage guidance.

Custom adapter development remains possible for specialized requirements — users can subclass the base `Adapter` and override `format()` / `parse()`.

## Practical Considerations

- Select `ChatAdapter` for general compatibility, when working with diverse model types, or with smaller open-source models that don't support `response_format`.
- Choose `JSONAdapter` when latency matters and your model supports structured output via the `response_format` parameter.
- For specialized scenarios, consider `XMLAdapter`, `TwoStepAdapter`, or implement a custom adapter.

## Position in the DSPy Programming Model

Adapters are the **third** of the four orthogonal artifacts the DSPy Programming Model factors out of a conventional prompt:

| Concern | DSPy artifact |
|---|---|
| Typed I/O contract | Signatures |
| Strategy / prompting technique | Modules |
| **Formatting & parsing** | **Adapters** |
| Search over instructions / demos / weights | Optimizers |

The Adapter is the layer that closes the *typed-program ↔ string-API* gap: a [[DSPySignatures|Signature]] is a typed Python object; an LM accepts strings or messages. The Adapter is what makes the round trip possible — formatting the typed Signature + demos + inputs into messages on the way in, and parsing the LM's textual response back into a typed `dspy.Prediction` on the way out.
