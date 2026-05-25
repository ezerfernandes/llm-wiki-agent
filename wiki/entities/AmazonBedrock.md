---
title: "Amazon Bedrock"
type: entity
tags: [product, aws, llm-api, serverless, cloud]
sources: [leh-ch02-tooling-and-installation, leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## What it is
Amazon Bedrock is AWS's serverless LLM API service that exposes a curated set of foundation models (Anthropic Claude, Meta Llama, Mistral, Cohere, Amazon Titan/Nova, AI21, Stability AI) behind a unified pay-per-token API.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) explicitly rejects Bedrock in favor of [[AmazonSageMaker]]: "Bedrock would have been an excellent solution for quickly prototyping something, but this is a book on LLM engineering, and our goal is to dig into all the engineering aspects that Bedrock tries to mask away." The authors note Bedrock's limited model catalog at writing (Mistral, Flan, Llama 2, Llama 3) and its hidden infrastructure layer. Ch. 10 ([[leh-ch10-inference-pipeline-deployment]]) re-lists Bedrock among alternative deployment platforms one could pick instead of running a SageMaker inference endpoint.

## Connections
- [[AmazonSageMaker]] — the platform the book uses instead.
- [[Amazon]] — parent company.
- [[Llama2_7BChat]] — one of Bedrock's hosted models at writing.
- [[Serverless]] — Bedrock's deployment model.
- [[AzureOpenAI]] / [[GoogleCloudVertexAI]] — peer hyperscaler LLM APIs.
