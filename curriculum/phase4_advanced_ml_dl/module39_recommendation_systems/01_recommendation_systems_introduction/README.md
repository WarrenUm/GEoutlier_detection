# Recommendation Systems - Introduction

> Part of **Topic 36: Recommendation Systems** · source item type: WikiPage

---
## Introduction

In this section, you'll learn about machine learning algorithms that we encounter every day in our lives: recommendation systems!

## Developing a Recommendation System in PySpark

In this section you'll learn about recommendation system modeling approaches and you'll even build your own recommendation system in PySpark!

### Recommendation Systems

A recommendation system allows predicting the future preference list for a certain customer or user, and recommends the top preference for this user. Examples include: which books would a customer prefer to buy on Amazon, which Netflix movie or series would a user watch next, etc. You'll learn about several different types of recommendation system algorithms and how they work.

### Collaborative Filtering with Singular Value Decomposition

Collaborative Filtering (CF) is currently the most widely used approach to build recommendation systems. It often uses matrix factorization under the hood, which you'll learn about in this section.

### Implementing Recommender Systems with `surprise`

`surprise` is a library that is optimized to efficiently create recommendations. You'll get a chance to use this library to code up different implementations of collaborative filtering recommendation systems.

### Matrix Factorization with Alternating Least Squares

We'll also look at another matrix factorization technique called Alternating Least Squares (ALS). This method can prove to be much more effective and robust than SVD. You'll also learn how ALS is implemented in Spark's machine learning library `ml`.

### Building a Recommendation System in PySpark

You'll end this section by building your own recommendation system in PySpark using the `MovieLens` rating dataset!

## Summary

In this section, you'll learn the basics of recommendation systems and how to implement them in `surprise` and Spark!

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
