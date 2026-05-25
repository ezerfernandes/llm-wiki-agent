---
title: "FastAPI"
type: entity
tags: [tool, web-framework, python]
sources: [madewithml-mlops-serving, dspy-sample-code-generation-tutorial, dspy-deployment-tutorial, leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-24
---

# FastAPI

Modern, async Python web framework.

## Wiki receipts

- **As ML serving layer** — used to wrap [[RayServe]] endpoints and expose the trained model as an HTTP API in [[madewithml-mlops-serving]].
- **As LM-driven analysis target** — the worked-example library in [[dspy-sample-code-generation-tutorial]] (alongside Streamlit). Documentation URLs ingested: `fastapi.tiangolo.com/`, `tutorial/first-steps/`, `tutorial/path-params/`, `tutorial/query-params/`. The tutorial's canonical generated output is a **JWT-authentication FastAPI snippet** (HTTPBearer security + login endpoint + protected route + HTTP-exception error handling) — the first wiki receipt where FastAPI is the *subject* of an LM-driven analysis rather than the *implementation* of an ML serving layer.
- **As DSPy-program serving layer** — [[dspy-deployment-tutorial|the DSPy Deployment tutorial]] canonicalizes FastAPI as the **lightweight production-serving path** for DSPy programs. Pattern: [[Pydantic]] `BaseModel` for the request schema, `@app.post("/predict")` handler, `dspy.asyncify(program)` wrap, `await dspy_program(...)` inside the handler, [[Uvicorn]] as the ASGI runner (`uvicorn fastapi_dspy:app --reload`). Streaming variant pairs `dspy.streamify(...)` with `fastapi.responses.StreamingResponse(..., media_type="text/event-stream")` for [[ServerSentEvents|SSE]] token delivery. First wiki receipt of FastAPI fronting a [[DSPy]] program (prior DSPy/FastAPI co-mentions were LM-driven *analysis* of FastAPI code, not FastAPI hosting DSPy code). See [[DSPyAsync]] for the `asyncify` pattern.
