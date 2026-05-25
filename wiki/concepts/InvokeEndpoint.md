---
title: "InvokeEndpoint (SageMaker)"
type: concept
tags: [aws, sagemaker, inference, api]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## Definition
**InvokeEndpoint** is the SageMaker Runtime API call (`boto3.client("sagemaker-runtime").invoke_endpoint(...)`) used to send a synchronous inference request to a hosted SageMaker model endpoint. It is the runtime surface through which LLM clients pass inputs and receive generations.

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] wraps `invoke_endpoint` in the chapter's `LLMInferenceSagemakerEndpoint` class. The wrapper sets the payload (input string + sampling parameters: `max_new_tokens`, `top_p`, `temperature`, `return_full_text`), serializes it as JSON, calls `client.invoke_endpoint(EndpointName=..., ContentType="application/json", Body=...)`, and decodes the JSON response. When the endpoint uses [[InferenceComponent|inference components]], the call adds `InferenceComponentName=<component>` to address the specific component. The wrapper pattern decouples the rest of the application from the SageMaker SDK so swapping in a local model (or another vendor) requires only a new `Inference` subclass.

## Key details
- Synchronous: the call blocks until the model returns a response (no streaming in the book's example, though TGI supports SSE).
- Payload schema: `{"inputs": "...", "parameters": {...}}` where parameters drive `max_new_tokens`, `temperature`, `top_p`, `repetition_penalty`.
- ContentType is `application/json` for the book; SageMaker also supports CSV, JSONLines, and custom protocols.
- The endpoint name is what the API targets; the inference component (if any) is a sub-target.
- Pairs with the SDK's `InvokeEndpointAsync` for asynchronous variants.

## Connections
- [[AWSSageMakerInferenceEndpoint]] — the resource InvokeEndpoint targets.
- [[InferenceComponent]] — the sub-resource addressed via `InferenceComponentName`.
- [[Boto3]] — the SDK providing this API.
- [[JSON]] — the wire format used.
- [[OnlineRealTimeInference]] — the archetype this API serves.
- [[ModelServing]] — the broader practice.
