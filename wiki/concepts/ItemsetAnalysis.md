---
title: "Itemset Analysis"
type: concept
tags: [data-mining, statistics]
sources: [parproc-ch14-statistics-data-mining]
last_updated: 2026-05-17
---

# Itemset Analysis

A data-mining task that finds frequent co-occurrences of items across a set of transactions, and derives association rules from those co-occurrences. The canonical example is the [[MarketBasketProblem]].

## Definitions

Given a transaction database represented as a binary matrix S (rows = transactions, columns = items, S_{ij} = 1 if transaction i contains item j):

- An **itemset** is a subset of the item universe T₀, ..., T_{b-1}.
- A **frequent** itemset appears in at least r transactions (r = support threshold).
- An **association rule** I → J is an ordered pair of disjoint itemsets I and J.
- The **support** of I → J is the proportion of records containing both I and J — i.e., P(I and J).
- The **confidence** of I → J is the proportion of records containing J among those that contain I — i.e., P(J|I).

A data miner sets thresholds for both support and confidence, then finds all association rules exceeding both.

## Scale and Motivation

In the old days of statistics, a dataset of 300 observations on 3–4 variables was considered large. Modern data easily reaches tens of thousands to tens of millions of observations with thousands of variables. This scale makes combinatorial enumeration expensive and parallel methods necessary. The high variable count also dramatically increases the risk of spurious associations (overfitting).

## Algorithms

The [[AprioriAlgorithm]] is the most famous algorithm for finding frequent itemsets. It uses breadth-first search with monotone pruning: infrequent itemsets cannot yield frequent supersets.

## Connections

- [[AprioriAlgorithm]] — the standard algorithm for solving this problem.
- [[MarketBasketProblem]] — primary motivating application.
- [[parproc-ch14-statistics-data-mining]] — primary source (§14.1).
