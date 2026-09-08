# Transfer Learning - Introduction

> Part of **Phase 4 Appendix: Transfer Learning** · source item type: WikiPage

---
## Introduction

In this section you'll learn all about transfer learning and how it could be specifically applied to convolutional neural networks. There are also other applications of transfer learning like NLP.

## Convolutional Neural Networks (Continued)

In an earlier section, you learned about the fundamentals of convolutional neural networks and how to use them. In this section, you'll deepen your CNN knowledge and learn about concepts that will allow you to reuse pretrained models from other image recognition tasks. This will help you solve problems where only limited data is available.

### Using Pretrained Networks

You will learn about the concept of "convolutional bases" and why they are useful. The use of a convolutional base, or a "pretrained network" has the advantage that hierarchical features that already have been "pre-learned" by this network can act as a generic model. Because of that reason, these networks can be used for a wide variety of computer vision tasks, even if your new problem involves completely different classes of images. You'll learn about the pretrained networks that are available in Keras, the use of pretrained networks through feature extraction (meaning that you run your new data through the pretrained network and training a new classifier on top of the pretrained network), and the use of pretrained networks through finetuning.

### Image Classification

At the end of this section, you'll work through a lab that combines the knowledge you gained in this section and the previous one. You'll work on a dog breed classification problem, a dataset used in a Kaggle competition, and build both a convolutional neural network from scratch, and a CNN using a pretrained network.

## Summary

In this section, you'll extend your deep learning knowledge by learning about transfer learning.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
