# Deploying Your DSPy Program

Source: https://dspy.ai/tutorials/deployment/
Fetched: 2026-05-24

This guide covers two production deployment approaches for DSPy programs: **FastAPI** for lightweight REST API deployments, and **MLflow** for enterprise-grade deployments with versioning, model registry, and packaging.

---

## Deploying with FastAPI

FastAPI is a modern, async-capable Python web framework. It is the lightweight option — wrap a DSPy program in a `@app.post(...)` handler.

### Install

```bash
pip install fastapi uvicorn
export OPENAI_API_KEY="your-openai-api-key"
```

### Minimal FastAPI app

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import dspy

app = FastAPI(
    title="DSPy Program API",
    description="A simple API serving a DSPy Chain of Thought program",
    version="1.0.0"
)

class Question(BaseModel):
    text: str

lm = dspy.LM("openai/gpt-4o-mini")
dspy.configure(lm=lm, async_max_workers=4)
dspy_program = dspy.ChainOfThought("question -> answer")
dspy_program = dspy.asyncify(dspy_program)

@app.post("/predict")
async def predict(question: Question):
    try:
        result = await dspy_program(question=question.text)
        return {
            "status": "success",
            "data": result.toDict()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

`dspy.asyncify(program)` converts a sync DSPy program into an awaitable callable that runs on a thread pool. `async_max_workers` (default 8) caps the size of that pool. This pattern is for **sync DSPy code running inside an async service** — distinct from writing native `aforward()` / `acall()`.

### Launch

```bash
uvicorn fastapi_dspy:app --reload
```

### Streaming with `dspy.streamify` (DSPy 2.6.0+)

```python
from dspy.utils.streaming import streaming_response
from fastapi.responses import StreamingResponse

dspy_program = dspy.asyncify(dspy.ChainOfThought("question -> answer"))
streaming_dspy_program = dspy.streamify(dspy_program)

@app.post("/predict/stream")
async def stream(question: Question):
    stream = streaming_dspy_program(question=question.text)
    return StreamingResponse(
        stream_streaming_response(stream),
        media_type="text/event-stream"
    )
```

`dspy.utils.streaming.streaming_response` converts the DSPy async stream into properly formatted Server-Sent Events (`text/event-stream`). Wrapping in `fastapi.responses.StreamingResponse` is the FastAPI-side glue.

### Client test

```python
import requests

response = requests.post(
    "http://127.0.0.1:8000/predict",
    json={"text": "What is the capital of France?"}
)
print(response.json())
```

---

## Deploying with MLflow

MLflow gives versioning, experiment tracking, and packaging. Recommended for production. Requires `mlflow>=2.18.0`.

### Install and start tracking server

```bash
pip install mlflow>=2.18.0
mlflow ui   # http://127.0.0.1:5000/
```

### Log a DSPy program as an MLflow model

**Critical constraint (MLflow 2.22.0+)**: must wrap in a custom `dspy.Module` subclass with a `forward()` accepting positional arguments. Bare `dspy.Predict` / `dspy.ChainOfThought` will not log directly.

```python
import dspy
import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5000/")
mlflow.set_experiment("deploy_dspy_program")

lm = dspy.LM("openai/gpt-4o-mini")
dspy.configure(lm=lm)

class MyProgram(dspy.Module):
    def __init__(self):
        super().__init__()
        self.cot = dspy.ChainOfThought("question -> answer")

    def forward(self, messages):
        return self.cot(question=messages[0]["content"])

dspy_program = MyProgram()

with mlflow.start_run():
    mlflow.dspy.log_model(
        dspy_program,
        "dspy_program",
        input_example={"messages": [{"role": "user", "content": "What is LLM agent?"}]},
        task="llm/v1/chat",
    )
```

`task="llm/v1/chat"` exposes the served model behind an OpenAI-compatible chat interface — the deployed endpoint accepts `{"messages": [{"role": "...", "content": "..."}]}` and clients written against OpenAI's chat-completions schema work unchanged.

### Serve

```bash
mlflow models serve -m runs:/{run_id}/model -p 6000
```

### Test the served model

```bash
curl http://127.0.0.1:6000/invocations \
  -H "Content-Type:application/json" \
  --data '{"messages": [{"content": "what is 2 + 2?", "role": "user"}]}'
```

### Containerize

```bash
mlflow models build-docker -m "runs:/{run_id}/model" -n "dspy-program"
docker run -p 6000:8080 dspy-program
```

---

## Best practices

- Manage dependencies via `conda.yaml` or `requirements.txt` (MLflow logs them with the model).
- Use meaningful version tags and descriptions on logged models.
- Define explicit `input_example` schemas.
- Add production monitoring and logging around the serving endpoint.
- For enterprise deployments, containerize via `mlflow models build-docker` and run on container orchestration.
