# Transfer Learning - Recap

> Part of **Phase 4 Appendix: Transfer Learning** · source item type: WikiPage

---
## Introduction

In this section, you learned how you can adapt pretrained models to improve the performance of neural networks when limited training data is available. While you specifically investigated CNNs and the VGG-19 model, these concepts are also applicable to other domains as well. For example, GloVe (Global Vectors for Word Representation) is a pretrained model that can be useful in a variety of natural language processing tasks.

Remember that the general process for transfer learning begins by taking a pretrained model like VGG-19 and freezing the weights so that they remain constant. From there, you can then append a standard densely connected classifier to perform the task at hand. In essence, the pretrained model acts as a form of feature engineering applied to the underlying dataset.

After the classifier is trained with the frozen pretrained model, a few of the top layers from the pretrained model can be unfrozen for fine tuning. Remember that you should only do this after training the classifier on top of the fully frozen model. Unfreezing parts of the pretrained model earlier is prone to overwriting any useful feature weights encoded in the pretrained model as there will be large gradients in forward and backward propagation passes until the densely connected layers converge to a stable solution. Also, remember that little is to be gained by unfreezing more than a few of the top layers from a pretrained model. Base layers of models such as VGG-19 will pick up very granular features such as colors or edges in image recognition. As such, these base layers are typically well formulated features across many domains. Unfreezing top layers has far more impact on tuning as these final layers often pick up domain specific features, so when adopting a model to a new problem domain such as predicting flower species instead of predicting animal kingdoms, these top layers can often be more impactful if retrained to the specific application.

## Summary

In this section, you got an overview of transfer learning and how to adapt pretrained models. From here, you'll continue to learn about other neural network architectures and build upon your growing deep learning knowledge.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
