# Convolutional Neural Networks - Introduction

> Part of **Phase 4 Appendix: Convolutional Neural Networks** · source item type: WikiPage

---
## Introduction

Until now, you've learned about densely connected networks and how they can be super powerful for classification problems when you have unstructured data such as text or images. In one of the previous labs, you analyzed images and used densely connected neural networks to classify images according to whether they contained Santa or not. In this section you'll learn about another type of neural networks that work particularly well on image data: Convolutional Neural Networks.

### Convolutional Neural Networks

There are several issues when using densely connected neural networks on image data. Firstly, dense layers learn global patterns rather than local patterns, and densely connected networks can really grow very big if we have high resolution images. In this section, you'll see why Convolutional Neural Networks are often preferred over densely connected networks for image processing. Additionally, you'll learn what a convolution operation is, the different building blocks of convolutional neural networks (including filters, padding schemes, strided convolutions, etc.), and the types of network layers that are part of your convolutional neural networks.

### Building a CNN from Scratch

Once you understand how CNNs work, you'll practice building one from scratch. You'll learn how to preprocess your image data so your model can be trained using Keras. Just like with densely connected networks, Keras provides an extremely user-friendly tool to build CNNs.

### Visualizing Intermediate Activations

As with densely connected networks, CNNs are complicated networks that are considered a "black box" tool with little insight in what's happening in the network layers. However, when using CNNs, you're essentially changing your image through filters in every layer. You'll learn to get some insight in your black box models by visualizing the intermediate layers in your CNNs!

## Summary

In this section, you'll extend your deep learning knowledge by learning about convolutional neural networks.

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
