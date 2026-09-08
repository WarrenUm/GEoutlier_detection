# Support Vector Machines - Introduction

> Part of **Topic 31: Support Vector Machines** · source item type: WikiPage

---
## Introduction

A Support Vector Machine (SVM) is a type of classifier which modifies the loss function for optimization to not only take into account overall accuracy metrics of the resulting predictions, but also to maximize the decision boundary between the data points. In essence, this further helps tune the classifier as a good balance between underfitting and overfitting.

## Support Vector Machines

In addition to optimizing for accuracy, support vector machines add a slack component, trading in accuracy to increase the distance between data points and the decision boundary. This provides an interesting perspective that can help formalize the intuitive visual choices a human would make in balancing precision and generalization to strike a balance between overfitting and underfitting.

## Kernel Functions

Initially, you'll explore linear support vector machines that divide data points into their respective groups by drawing hyperplanes using the dimensions from the feature space. In practice, these have limitations and the dataset may not be cleanly separable. As a result, kernel functions are an additional tool that can be used. Essentially, kernels reproject data onto a new parameter space using combinations of existing features. From there, the same process of applying SVMs to this transformed space can then be employed.

## Summary

Support Vector Machines are a powerful algorithm and may have the top performance among the out of the box classifiers from scikit-learn. Moreover, learning to properly tune SVMs is critical. In the upcoming labs and lessons, you'll investigate and apply these concepts.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
