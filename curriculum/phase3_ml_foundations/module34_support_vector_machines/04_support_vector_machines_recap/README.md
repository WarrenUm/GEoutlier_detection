# Support Vector Machines - Recap

> Part of **Topic 31: Support Vector Machines** · source item type: WikiPage

---
## Introduction

As you saw, support vector machines are another classification tool to add to your repertoire. While computationally expensive, they can be powerful tools providing substantial performance gains in many instances.

## Kernel Functions

Probably the most important information worth reviewing is some of the various kernel functions that you can apply:

1. Radial Basis Function (RBF)
  1. `c`
  2. $\gamma$, which can be specified using `gamma` in scikit-learn

2. Polynomial Kernel
  1. $\gamma$, which can be specified using `gamma` in scikit-learn
  2. $r$, which can be specified using `coef0` in scikit-learn
  3. $d$, which can be specified using `degree` in scikit-learn

3. Sigmoid Kernel
  1. $\gamma$, which can be specified using `gamma` in scikit-learn
  2. $r$, which can be specified using `coef0` in scikit-learn

Also recall that in general, `c` is the parameter for balancing standard accuracy metrics for tuning classifiers with the decision boundary distance.

## Summary

While it may appear that this section was a bit brief, Support Vector Machines are a powerful algorithm that deserve attention, so make sure you investigate them properly. Moreover, learning to properly tune SVMs using kernels and an appropriate `c` value is critical.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
