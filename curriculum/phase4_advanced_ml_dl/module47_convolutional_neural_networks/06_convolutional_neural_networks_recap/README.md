# Convolutional Neural Networks - Recap

> Part of **Phase 4 Appendix: Convolutional Neural Networks** · source item type: WikiPage

---
## Introduction

Well done! In this section you learned all about convolutional neural networks! You should now have enough of an introductory primer to be able to do some image recognition tasks on your own!

## Key Takeaways

Remember that the essence of a CNN is the convolutional operation. A window is slided across the image based on a stride size. Padding can be used to prevent shrinkage and to make sure pixels at the edge of an image deserve the necessary attention. Each convolution then works to adjust the weights of the kernel through backpropagation during training. Going back to the general architecture, max pooling is typically used between convolutional layers to reduce the dimensionality.

Overall, CNNs are a useful model for image recognition due to their ability to recognize visual patterns at varying scales. After developing the convolutional and pooling layers to form a base, the end of the network architecture still connects back to a densely connected network to perform classification.

## Summary

In this section you learned all about convolutional neural networks! From here, you'll learn more about tuning neural networks and other neural network architectures!

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
