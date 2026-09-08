# Neural Networks - Recap

> Part of **Topic 40: Neural Networks** · source item type: WikiPage

---
## Key Takeaways

The key takeaways from this section include:

- Neural networks are powerful models that can be customized and tweaked using various amounts of nodes, layers, ...
- The most basic neural networks are single-layer densely connected neural networks, which have very similar properties as logistic regression models
- Compared to more traditional statistics and ML techniques, neural networks perform particularly well when using unstructured data
- Apart from densely connected networks, other types of neural networks include convolutional neural networks, recurrent neural networks, and generative adversarial neural networks
- When working with image data, it's important to understand how image data is stored when working with them in Python
- Logistic regression can be seen as a single-layer neural network with a sigmoid activation function
- Neural networks use loss and cost functions to minimize the "loss", which is a function that summarizes the difference between the actual outcome (eg. pictures contain santa or not) and the model prediction (whether the model correctly identifies pictures with santas)
- Backward and forward propagation are used to estimate the so-called "model weights"
- Adding more layers to neural networks can substantially increase model performance
- Several activations can be used in model nodes, you can explore with different types and evaluate how it affects performance

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
