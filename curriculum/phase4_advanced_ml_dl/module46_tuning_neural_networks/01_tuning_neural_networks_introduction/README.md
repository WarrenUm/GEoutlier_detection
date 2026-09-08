# Tuning Neural Networks - Introduction

> Part of **Topic 42: Tuning Neural Networks** · source item type: WikiPage

---
## Introduction

Now that you have a general sense of the architecture of neural networks and some of their underlying concepts, its time to further investigate how to properly tune a model for optimal performance. Specifically, you'll take a look at two main techniques: regularization and normalization.

## Regularization

You've seen regularization before in many other models including linear regression. For example, recall the L1 and L2 penalties which modify ordinary linear regression. These updated loss functions can help tune models so they do not overfit to the training data. For neural networks, you'll use a surprisingly similar process in order to achieve well trained models that are neither overfit nor underfit.

## Normalization and Tuning Neural Networks

Another modeling problem occurs when one gets trapped into a local minimum when searching for an optimal solution using an iterative approach such as gradient descent. One technique for counteracting this scenario is normalizing features. Normalization in deep learning models can drastically decrease computation time, mitigate common issues such as vanishing or exploding gradients, and increase model performance.

### Optimization

Finally, you'll look at alternative optimization algorithms. These are of primary interest when one encounters local minimum. Knowing when one has hit such a pitfall can be challenging and typically requires experimenting with different optimization approaches and learning rates.

## Summary

In this section, you'll extend your deep learning knowledge by learning about regularization and optimizing your neural network models.

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
- `Bank_complaints.csv` — supporting data/helper file for the exercise.
