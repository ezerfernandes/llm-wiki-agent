---
title: "Market Basket Problem"
type: concept
tags: [data-mining, statistics, retail]
sources: [parproc-ch14-statistics-data-mining]
last_updated: 2026-05-17
---

# Market Basket Problem

The canonical application of [[ItemsetAnalysis]]: given a database of retail sales transactions, find sets of products that frequently appear together in the same purchase, and derive association rules for targeted recommendations.

## Problem Setup

A store's sales are represented as a binary matrix S of size t × b, where t is the number of transactions and b is the number of distinct items (e.g., book titles). S_{ij} = 1 if the i-th transaction included item j.

The goal is to find association rules I → J (disjoint itemsets) such that:
- **Support** (proportion of records containing both I and J) exceeds a threshold.
- **Confidence** (proportion of records containing J among those containing I, i.e., P(J|I)) exceeds a threshold.

## Practical Use

High confidence and high support rules motivate targeted advertising: "We see you bought books X and Y. We think you may be interested in Z." Low support rules, even with high confidence, may not be worth acting on — the combination occurs too rarely.

## Generalization

The retail framing is the typical introduction, but the terminology generalizes: "items" are any binary attributes, "database records" are any binary observations. The problem appears in web clickstream analysis, medical diagnosis, and genomics.

## Algorithms

The [[AprioriAlgorithm]] is the best-known algorithm for finding frequent itemsets. It uses breadth-first search with monotone pruning on support.

## Connections

- [[ItemsetAnalysis]] — the general framework; market basket is the canonical instance.
- [[AprioriAlgorithm]] — primary algorithm for solving this problem.
- [[parproc-ch14-statistics-data-mining]] — primary source (§14.1.2).
