---
title: "Class Imbalance"
type: concept
tags: [data, evaluation]
sources: []
last_updated: 2026-05-15
---

# Class Imbalance

A classification setting where some labels are dramatically rarer than others, biasing models toward the majority class and inflating accuracy while hiding poor minority recall. Mitigated via resampling, class weights, focal loss, and evaluated via [[F1Score]] rather than accuracy; tightly linked to [[DataQuality]] and [[DataSplitting]] hygiene.
