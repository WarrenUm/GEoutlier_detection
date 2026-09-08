# Deep NLP with Word Embeddings - Recap

> Part of **Phase 4 Appendix: Deep NLP** · source item type: WikiPage

---
## Introduction

Congratulations! You know have a myriad of powerful NLP tools that you can begin to tap into and further explore. With that, take a minute to review some of the key concepts you were exposed to in this section.

## RNNs and Word Embeddings

Remember that word embeddings are a type of vectorization strategy that computes word vectors from a text corpus. They use similarity metrics, which can reveal how certain words relate to each other, or "semantic relationships".

Unlike TF-IDF vectorization, the size of word embeddings is a tunable parameter, which can help overcoming the curse of dimensionality. Word embeddings can be created using Word2Vec models -- given enough training data.

Since deep learning is used to create Word2Vec models, training word embeddings can be really time consuming, and when building a predictive model you'd want to avoid spending a lot of time here. Pretrained word vectors are very useful here, and GLoVe is the most commonly used model. When using GLoVe, and moving towards a vector representation for any arbitrarily-sized block of text, mean word embeddings can be used.

## GRUs and LSTMs

Building on this, you then took a look at some new architectures for neural nets. Aside from having a temporal aspect as with RNNs, GRUs (Gated Recurrent Units) and LSTMs (Long Short Term Memory Cells) have capabilities for both summarizing important information seen prior and forgetting needless details to free up memory. This acts as an analogy to human memory and allows for improved performance in many tasks.

## Summary

In this section you learned about advanced deep network architectures including RNNs, GRUs, and LSTMs. You also saw how to create word embeddings, an alternative methodology for encoding textual data into numerical spaces. With that, you also saw how to use transfer learning to apply Word2Vec models and improve NLP classification algorithms.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
