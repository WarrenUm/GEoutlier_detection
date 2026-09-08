# Extension to Linear Models - Introduction

> Part of **Topic 20: Extensions to Linear Models** · source item type: WikiPage

---
## Introduction

In this section, you'll learn about some ways to make linear models more complex to account for complicated relationships in a dataset. Before diving in too deep, here is a roadmap for what you will be covering in this section.

## Extensions to linear models

Unfortunately, not every continuous variable can be predicted effectively using a straight line (a linear model). Imagine the relationship between your 5k time as a runner and how many hours a week you train. At the very least the improvements in your time are going to trail off with additional training (going from 0 -> 10 hrs training a week is going to have way more impact than going from 60 -> 70 hrs). And the chances are that at some point in time, you'll overtrain and additional training will actually degrade your performance. You could certainly model the relationship between weekly training hours and 5k time with a straight line, but for some values of weekly training time, the accuracy of the prediction would probably be extremely low.

In this section, you'll be introduced to a number of concepts to help you to make predictions when there is no linear relationship between the predictor and target variables.

### Interactions

We'll start by introducing the concept of interactions - where two or more variables interact in a non-additive manner thus affecting a third variable. Then you'll look at why they are important and how to account for them.

### Polynomial regression

You'll then implement higher-order equations for solving regressions. A linear expression can be described by an equation in the form of $y = mx + b$. A polynomial expression brings in higher powers of x (squared, cubed, etc). By allowing for equations containing higher-order terms you may be able to better fit a curve to your dataset, thus predicting future values more accurately.

### Bias-variance tradeoff

While polynomial regression can improve the accuracy of your models, they also exacerbate the risk of overfitting the data, making your model extremely accurate for the training set but completely inaccurate for any future data points the model wasn't trained on. You'll also look at the concept of bias-variance tradeoff and how it relates to underfitting and overfitting datasets.

## Summary

It's time to start learning about extensions to linear models, modeling non-linear relationships between the predictor and target variables!

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
- `ames.csv` — supporting data/helper file for the exercise.
