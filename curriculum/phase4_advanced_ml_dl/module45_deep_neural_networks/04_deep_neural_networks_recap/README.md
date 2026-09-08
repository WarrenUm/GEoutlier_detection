# Deep Neural Networks - Recap

> Part of **Topic 41: Deep Neural Networks** · source item type: WikiPage

---
## Key Takeaways

The key takeaways from this section include:

- Deep neural network representations can lighten the burden and automate certain tasks of heavy data preprocessing
- Deep representations need exponentially fewer hidden units than shallow networks, to obtain the same performance
- Parameter initialization, forward propagation, cost function evaluation, and backward propagation are again the cornerstones of deep networks
- Tensors are the building blocks of neural networks and a good understanding of them and how to use them in Python is crucial
- Scalars can be seen as 0-D tensors. Vectors can be seen as 1-D tensors, and matrices as 2-D tensors
- The usage of tensors reaches beyond matrices: tensors can have N dimensions
- Tensors can be created and manipulated using Numpy
- Keras makes building neural networks in Python easy, and you learned how to do that in this section
- You can use Keras to do some NLP as well, e.g. for tokenization

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
