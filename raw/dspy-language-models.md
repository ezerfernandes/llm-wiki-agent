# DSPy — Language Models

Source: https://dspy.ai/learn/programming/language_models/
Section: DSPy Learn / Programming (page 3 of 13)

The first step in any DSPy code is to set up your language model. For example, you can configure OpenAI's GPT-4o-mini as your default LM as follows:

```python
# Authenticate via `OPENAI_API_KEY` env: import os; os.environ['OPENAI_API_KEY'] = 'here'
lm = dspy.LM('openai/gpt-4o-mini', api_key='YOUR_OPENAI_API_KEY')
dspy.configure(lm=lm)
```

A few pointers and details on different LM providers.

## Authenticating by setting the provider API key

You can also indirectly configure DSPy by setting the appropriate environment variable for your provider and then directly initializing `dspy.LM('model_name')`. For example, for OpenAI, you can set the `OPENAI_API_KEY` environment variable as follows:

```bash
export OPENAI_API_KEY='your_openai_api_key'
```

And then run:

```python
import dspy
lm = dspy.LM('openai/gpt-4o-mini')
dspy.configure(lm=lm)
```

### OpenAI

```python
import dspy
lm = dspy.LM('openai/gpt-4o-mini', api_key='YOUR_OPENAI_API_KEY')
dspy.configure(lm=lm)
```

### Anthropic

```python
import dspy
lm = dspy.LM('anthropic/claude-sonnet-4-5-20250929', api_key='YOUR_ANTHROPIC_API_KEY')
dspy.configure(lm=lm)
```

### Google Gemini

```python
import dspy
lm = dspy.LM('gemini/gemini-2.5-pro-preview-03-25', api_key='GEMINI_API_KEY')
dspy.configure(lm=lm)
```

### Vertex AI (GCP)

For Vertex AI, you need to set up service-account credentials. First install the required dependencies:

```bash
pip install "litellm[vertex_ai]"
```

Then configure DSPy with the service-account credentials:

```python
import dspy
import json

# Load credentials from your service account JSON
with open("path/to/your/service_account.json") as f:
    credentials = json.dumps(json.load(f))

lm = dspy.LM(
    model="vertex_ai/gemini-2.0-flash",
    vertex_credentials=credentials,
    vertex_project="your-gcp-project-id",
    vertex_location="us-central1",
)
dspy.configure(lm=lm)
```

Alternatively, you can use environment variables for authentication:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service_account.json"
export VERTEXAI_PROJECT="your-gcp-project-id"
export VERTEXAI_LOCATION="us-central1"
```

### Databricks

```python
import dspy
lm = dspy.LM('databricks/databricks-meta-llama-3-1-70b-instruct')
dspy.configure(lm=lm)
```

On Databricks, the SDK will pick up authentication automatically via their SDK.

### Local LMs on a GPU server

To host accurate open models on your own GPU(s), we recommend [SGLang](https://docs.sglang.ai/start/install.html). First, install and launch the SGLang server from a separate terminal:

```bash
> pip install "sglang[all]"
> pip install flashinfer -i https://flashinfer.ai/whl/cu121/torch2.4/

> CUDA_VISIBLE_DEVICES=0 python -m sglang.launch_server --port 7501 --model-path meta-llama/Meta-Llama-3-8B-Instruct
```

Then connect to it from your DSPy code as an OpenAI-compatible endpoint:

```python
lm = dspy.LM("openai/meta-llama/Meta-Llama-3-8B-Instruct",
             api_base="http://localhost:7501/v1",  # ensure this points to your port
             api_key="",
             model_type='chat')
dspy.configure(lm=lm)
```

### Local LMs on your laptop

First install [Ollama](https://ollama.ai/) and launch its server with your LM.

```bash
> curl -fsSL https://ollama.ai/install.sh | sh
> ollama run llama3.2:1b
```

Then connect to it from your DSPy code:

```python
import dspy
lm = dspy.LM('ollama_chat/llama3.2', api_base='http://localhost:11434', api_key='')
dspy.configure(lm=lm)
```

### Other providers

DSPy supports dozens of LLM providers via [LiteLLM](https://github.com/BerriAI/litellm). Just follow their instructions for whichever provider you want.

```python
lm = dspy.LM('anyscale/mistralai/Mistral-7B-Instruct-v0.1', api_key='ANYSCALE_API_KEY')

lm = dspy.LM('together_ai/togethercomputer/llama-2-70b-chat', api_key='TOGETHERAI_API_KEY')

lm = dspy.LM('azure/<your_deployment_name>', api_key='AZURE_API_KEY', api_base='AZURE_API_BASE', api_version='AZURE_API_VERSION')
```

If your provider offers an OpenAI-compatible endpoint, just add an `openai/` prefix to your full model name.

```python
import dspy
lm = dspy.LM('openai/your-model-name', api_key='PROVIDER_API_KEY', api_base='YOUR_PROVIDER_URL')
dspy.configure(lm=lm)
```

## Calling the LM directly

It's easy to call the `lm` you configured above directly. This gives you a unified API and lets you benefit from utilities like automatic caching.

```python
lm("Say this is a test!", temperature=0.7)  # => ['This is a test!']
lm(messages=[{"role": "user", "content": "Say this is a test!"}])  # => ['This is a test!']
```

## Using the LM with DSPy modules

Idiomatic DSPy involves using *modules*, which we discuss in the next guide.

```python
# Define a module (ChainOfThought) and assign it a signature (return an answer, given a question).
qa = dspy.ChainOfThought('question -> answer')

# Run with the default LM configured with `dspy.configure` above.
response = qa(question="How many floors are in the castle David Gregory inherited?")
print(response.answer)
```

Possible output:

```
The castle David Gregory inherited has 7 floors.
```

## Using multiple LMs

You can change the default LM globally with `dspy.configure` or change it inside a block of code with `dspy.context`. Using `dspy.configure` and `dspy.context` is thread-safe.

```python
dspy.configure(lm=dspy.LM('openai/gpt-4o-mini'))
response = qa(question="How many floors are in the castle David Gregory inherited?")
print('GPT-4o-mini:', response.answer)

with dspy.context(lm=dspy.LM('openai/gpt-3.5-turbo')):
    response = qa(question="How many floors are in the castle David Gregory inherited?")
    print('GPT-3.5-turbo:', response.answer)
```

Possible output:

```
GPT-4o-mini: The number of floors in the castle David Gregory inherited cannot be determined with the information provided.
GPT-3.5-turbo: The castle David Gregory inherited has 7 floors.
```

## Configuring LM generation

For any LM, you can configure any of the following attributes at initialization or in each subsequent call.

```python
gpt_4o_mini = dspy.LM('openai/gpt-4o-mini', temperature=0.9, max_tokens=3000, stop=None, cache=False)
```

By default, LMs in DSPy are cached. If you repeat the same call, you will get the same outputs. But you can turn off caching by setting `cache=False`.

Some inference providers (like OpenAI and Databricks) allow you to use a `rollout_id` parameter to bust the cache for a particular call to obtain different outputs. The `rollout_id` is treated as a part of the cache key, so different `rollout_id`s with `temperature > 0` yield different outputs.

```python
lm("Say this is a test!", rollout_id=1, temperature=1.0)  # => ['This is a test!']
lm("Say this is a test!", rollout_id=1, temperature=1.0)  # => ['This is a test!'] (cached)
lm("Say this is a test!", rollout_id=2, temperature=1.0)  # => ['Sure! This is a test!'] (different output)

predict = dspy.Predict("question -> answer", rollout_id=1, temperature=1.0)

predict = dspy.Predict("question -> answer")
predict(question="What is 1 + 52?", config={"rollout_id": 5, "temperature": 1.0})
```

## Inspecting output and usage metadata

Every LM object maintains the history of its interactions, including inputs, outputs, token usage (and $$$ cost), and metadata.

```python
len(lm.history)  # e.g., 3 calls to the LM

lm.history[-1].keys()  # access the last call to the LM, with all metadata
```

Output:

```
dict_keys(['prompt', 'messages', 'kwargs', 'response', 'outputs', 'usage', 'cost', 'timestamp', 'uuid', 'model', 'response_model', 'model_type'])
```

## Advanced: Using the Responses API

DSPy supports OpenAI's Responses API through the same `dspy.LM` interface. To use it, set `model_type="responses"` when initializing your LM.

```python
import dspy

dspy.configure(
    lm=dspy.LM(
        "openai/gpt-5-mini",
        model_type="responses",
        temperature=1.0,
        max_tokens=16000,
    ),
)
```

This is particularly useful for models that support OpenAI's newer Responses API surface (reasoning models, longer outputs, structured output features).
