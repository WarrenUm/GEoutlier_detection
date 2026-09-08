# K-Nearest Neighbors - Introduction

> Part of **Topic 27: K Nearest Neighbors** · source item type: WikiPage

---
## Introduction

In this section you'll look at an intuitive algorithm known as K-Nearest Neighbors (KNN). KNN is an effective classification and regression algorithm that uses nearby points in order to generate a prediction.

## KNN

The K-Nearest Neighbors algorithm works as follows:

1. Choose a point
2. Find the K-nearest points
  1. K is a predefined user constant such as 1, 3, 5, or 11

3. Predict a label for the current point:
  1. Classification - Take the most common class of the k neighbors
  2. Regression - Take the average target metric of the k neighbors
  3. Both classification or regression can also be modified to use weighted averages based on the distance of the neighbors

## Distance metrics

An incredibly important decision when using the KNN algorithm is determining an appropriate distance metric. This makes a monumental impact to the output of the algorithm. While there are additional distance metrics, such as cosine distance which we will not cover, you'll get a solid introduction to distance metrics by looking at the standard Euclidean distance and its more generic counterpart, Minkowski distance.

## K-means

While outside the scope of this section, it is worth mentioning the related K-means algorithm which uses similar principles as KNN but serves as an unsupervised learning clustering algorithm. In the K-means algorithm, K represents the number of clusters rather then the number of neighbors. Unlike KNN, K-means is an iterative algorithm which repeats until convergence. Nonetheless, its underlying principle is the same, in that it groups data points together using a distance metric in order to create homogeneous groupings.

## Summary

In this brief lesson, you were introduced to the KNN algorithm. From here, you'll jump straight to the details of KNN, practice coding your own implementation and then get an introduction to use pre-built tools within scikit-learn for KNN.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.

## Folded-in exercise material

This lesson includes the original hands-on material, converted for local use:

- [`lab.ipynb`](lab.ipynb) — the original exercise notebook. Work through
  it, or copy the parts you want into `work.ipynb`. `pytest` runs it too.
