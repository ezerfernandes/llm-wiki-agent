---
title: "Azure OpenAI Service"
type: entity
tags: [product, azure, llm-api, cloud]
sources: [leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## What it is
Azure OpenAI Service is Microsoft's commercial channel for OpenAI's GPT, embedding, and image models on Azure, with enterprise networking, governance, and SLAs layered on top.

## In LLM Engineer's Handbook
Ch. 10 ([[leh-ch10-inference-pipeline-deployment]]) lists Azure OpenAI as one of several alternative LLM-serving destinations (alongside [[AmazonBedrock]], [[GoogleCloudVertexAI]], [[AzureML]], [[Modal]], etc.) the reader could pick instead of running the fine-tuned TwinLlama on a SageMaker endpoint.

## Connections
- [[openai]] — model provider behind the service.
- [[microsoft]] — operator of Azure.
- [[AzureML]] — peer Azure ML platform.
- [[AmazonBedrock]] — peer hyperscaler LLM API on AWS.
