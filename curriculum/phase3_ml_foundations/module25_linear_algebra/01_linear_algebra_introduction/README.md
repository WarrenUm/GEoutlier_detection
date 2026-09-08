# Linear Algebra - Introduction

> Part of **Topic 22: Linear Algebra** · source item type: WikiPage

---
## Introduction

In this section, we're going to take a step back to learn some of the basics of linear algebra - the math that powers most machine learning models. You may not need to know linear algebra just to call a method in scikit-learn to do some modeling, but this introduction to linear algebra should give you a much better understanding of how your models are working "under the hood".

## The importance of linear algebra

We're going to kick this section off by looking at some of the many places that linear algebra is used in machine learning - from deep learning through Natural Language Processing and dimensionality reduction techniques such as Principle Component Analysis.

## Systems of linear equations

We then start to dig into the math! We look at the idea of linear simultaneous equations - a set of two or more equations each of which is linear (can be plotted on a graph as a straight line). We then see how such equations can be represented as vectors or matrices to represent such systems efficiently.

## Scalars, vectors, matrices, and tensors

In a code along, we'll introduce the concepts and concrete representations (in NumPy) of scalars, vectors, matrices, and tensors - why they are important and how to create them.

## Vector/matrix operations

We then start to build up the basic skills required to perform matrix operations such as addition and multiplication. You will also cover key techniques used by many machine learning models to perform their calculations covering both the Hadamard product and the (more common) dot product.

## Solving systems of linear equations using NumPy

We then bring the previous work together to look at how to use NumPy to solve systems of linear equations, introducing the identity and inverse matrices along the way.

## Regression analysis using linear algebra and NumPy

Having built up a basic mathematical and computational foundation for linear algebra, you will solve a real data problem - looking at how to use NumPy to solve a linear regression using the ordinary least squares (OLS) method.

## Computational complexity

Finally, we look at the idea of computational complexity and Big O notation, showing why OLS is computationally inefficient, and that a gradient descent algorithm can instead be used to solve a linear regression much more efficiently.

## Summary

Linear Algebra is so foundational to machine learning that you're going to see it referenced many times as the course progresses. In this section, the goal is to give you both a theoretical introduction and some computational practice, solving a real-life problem by writing the code required to solve a linear regression using OLS.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
