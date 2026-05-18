---
title: "Made With ML — Machine Learning Product Design"
type: source
tags: [mlops, made-with-ml, product-design, ml-canvas]
date: 2026-05-15
source_file: raw/madewithml/mlops-product-design.md
---

## Summary
This lesson covers the *What* and *Why* of building an ML product before any modeling begins. It introduces the [[MLCanvas]] template and walks through five product-design sections: Background (users, goals, pains), Value Proposition, Objectives, Solution (core features, integrations, alternatives, constraints, out-of-scope), and Feasibility. The running example builds a content-classification service that auto-tags ML articles into `natural-language-processing`, `computer-vision`, `mlops`, or `other`, with a latency constraint of <100ms.

## Key Claims
- Product design must precede systems design — answering *what* and *why* before *how* is "extremely crucial for creating great products."
- The user-centric Background frame uses three lenses: users (persona), goals, and pains.
- A complete Solution definition includes core features, integrations, alternatives, constraints (latency/security/UX), and explicit out-of-scope items.
- The example task constrains predictions to a fixed approved tag list (`natural-language-processing`, `computer-vision`, `mlops`, `other`) — anything else is out of scope to avoid noisy free-form labels.
- A low-latency constraint (>100ms classification) is treated as a first-class product requirement, not an afterthought.
- Feasibility must be assessed against available data, money, and team — and whether the existing dataset has the signal to meet objectives.
- The product's value proposition is to save users time by aggregating and categorizing ML content scattered across Reddit, Twitter, and similar noisy sources.

## Key Quotes
> "Before we start developing any machine learning models, we need to first motivate and design our application. While this is a technical course, this initial product design process is extremely crucial for creating great products."

> "Product design (What & Why) → Systems design (How)."

## Connections
- [[MadeWithML]] — parent course.
- [[GokuMohandas]] — author.
- [[Anyscale]] — course publisher.
- [[MLCanvas]] — the design template introduced here.
- [[ProductDesign]] — the methodology this lesson teaches.
- [[MLOps]] — overall course context.
- [[TextClassification]] — the task type for the running example.
- [[LatencyConstraints]] — the <100ms requirement is a core constraint.
- [[UserPersona]] — Background section frame.
- [[ValueProposition]] — product-centric framing concept.
- [[Feasibility]] — final check tying data/cost/team to deliverability.
- [[ColdStartProblem]] — referenced as a downside of the manual-tagging alternative.
- [[ContentClassification]] — application domain for the example.

## Contradictions
- None identified.
