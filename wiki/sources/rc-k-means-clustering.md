---
title: "K-means++ clustering (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, machine-learning, clustering, probability]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/K-means%2B%2B_clustering
---

## Summary
The task asks the programmer to implement the K-means++ clustering algorithm, which partitions a dataset of points into K groups so that points in the same cluster are similar. It is identical to the standard K-means algorithm except for how the initial centroids are chosen: instead of picking them uniformly at random, K-means++ seeds them with a probability proportional to each point's squared distance from the nearest already-chosen centroid, which leads to better and more consistent clustering.

## Task Requirements
- Implement a function taking two arguments: the number of clusters K (a positive integer) and the dataset (a list of points in the Cartesian plane).
- Return a list of clusters (related sets of points).
- Extra credit (awarded only if demonstrated): generate a list of random points to exercise the code; visualize results including centroids; generalize to polar coordinates (radians); generalize to points in arbitrary N-dimensional space (ℝ^N), discussing what changes versus the ℝ² case.
- For credit on the first two extras, visualize 6 clusters of 30,000 points in ℝ².

## Language Coverage
29 languages implement this task, spanning systems languages, functional languages, and math/array environments. Representative implementations include C, D, Go, Rust, Haskell, Java, JavaScript, Python, Julia, J, Mathematica/Wolfram Language, and Racket.

## Connections
- [[KMeansClustering]] — base algorithm that K-means++ improves via smarter initialization
- [[ClusterAnalysis]] — broader family of unsupervised partitioning methods
- [[EuclideanDistance]] — distance metric used to assign points and weight seeding
- [[ProbabilisticSampling]] — squared-distance-weighted selection of initial centroids
- [[Centroid]] — cluster centers iteratively recomputed as the mean of assigned points

## Contradictions
- None — reference task page.
