# Introduction

> Part of **Topic 23: Calculus, Cost Function and Gradient Descent** · source item type: WikiPage

---
## Introduction

In this section, you'll learn about the mechanism behind many machine learning optimization algorithms: gradient descent!

## Calculus and Solving a Linear Regression Using Gradient Descent

In this section, we're going to see how you can apply a "gradient descent" to solve a linear regression. Along the way, we'll also look at cost functions and will provide a foundation in calculus that will be valuable to you throughout your career as a data scientist.

### An Introduction to Derivatives

We're going to start off by introducing derivatives - the "instantaneous rate of change of a function" or (more graphically) the "slope of a curve". We'll start off by looking at how to calculate the slope of a curve for a straight line, and then we'll explore how to calculate the rate of change for more complex (non-linear) functions.

### Gradient Descent

Now that we know how to calculate the slope of a curve - and, by extension, to find a local minima (low point) or maxima (high point) where the curve is flat (the slope of the curve is zero), we'll look at the idea of a gradient descent to step from some random point on a cost curve to find the local optima to solve for a given linear equation. We'll also look at how best to select the step sizes for descending the cost function, and how to use partial derivatives to optimize both slope and offset to more effectively solve a linear regression using gradient descent.

## Summary

Just as we used solving a linear regression using OLS as an excuse to introduce you to linear algebra - one of the foundational elements of mathematics underpinning machine learning, we're now using the idea of gradient descent to introduce enough calculus to both understand and have good intuitions about many of the machine learning models that you're going to learn throughout the rest of the course.

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
