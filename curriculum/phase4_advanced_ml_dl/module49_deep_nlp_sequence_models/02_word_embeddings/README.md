# Word Embeddings

> Part of **Phase 4 Appendix: Deep NLP** · source item type: WikiPage

---
## Introduction

In this lesson, you'll learn about the concept of ***Word Embeddings***, and how you can use them to model the semantic meanings of words in a high-dimensional embedding space!

## Objectives

You will be able to:

- Demonstrate how word vectors are structured

- Compare and contrast word vector embeddings with other text vectorization strategies

## What Are Word Embeddings?

***Word Embeddings*** are a type of vectorization strategy that computes word vectors from a text corpus by training a neural network, which results in a high-dimensional embedding space, where each word in the corpus is a unique vector in that space. In this embedding space, the position of the vector relative to the other vectors captures semantic meaning. This method of creating distributed representations of words in a high-dimensional embedding space was first introduced in a landmark paper from members of the Google Brain team in 2013 at the Neural Information Processing Systems (NeurIPS, for short). You can read the full paper from Mikolov et al by following [this link](https://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf).

### Capturing Semantic Relationships

So far, the vectorization strategies you've learned have focused only on how often a word appears in a given text, but they don't focus at all on capturing the semantic meaning. This is one area where using the Word2Vec model to create ***Word Vector Embeddings*** really shines, because it will capture those semantic relationships between words, for instance, a Word2Vec model that is given enough data and training will learn that there is a semantic relationship between the word 'person' and 'people'. Furthermore, vector one would need to travel to get from the singular 'person' to the plural 'people' will be the same vector that will get you from the singular version of a word to it's plural - meaning that our model will 'learn' how to model the relationship between singular and plural versions of the same word. Take a look at the examples below:

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-word-embeddings/master/images/embeddings.png)

As you can see in the diagram above, the embedding space shows that the model has positioned the words 'king' and 'queen' in the same relationship that the vector 'man' has to 'woman'. The vector that gets you from 'king' to 'queen' or from 'man' to 'woman' is the vector for gender! You can see other examples show that the model also learns representations for verb tense, or even for countries and their capitals. This is more impressive when you realize that the model learns these relationships from reading a large enough corpus of text, without being given an explicit direction or instruction - that is, the researchers did not expressly feed the model sentences like "Madrid is the capital of Spain".

Since the words are all embedded in the same high-dimensional space, you can use the same similarity metrics you've used before, such as things like *Cosine Similarity* or even *Euclidean Distance*. In a future lab, you'll experiment with using a trained Word2Vec model for tasks like finding the most similar word(s) to a given word. Trained Word2Vec models also excel at things like the analogies questions that were made famous by the SAT test.

Let's end this lesson by taking a look at how the word vectors are actually structured.

## A Small Example

So far, you've learned vectorization strategies such as *Count Vectorization* and *TF-IDF Vectorization*. Recall that the vectors created by these algorithms are ***Sparse Vectors***. The length of a vector created by TF-IDF or Count Vectorization is the length of the total vocabulary of the text corpus. In these vectors, the vast majority of elements in the vector are 0, which is a massive waste of space, and a ton of extra dimensionality that can hurt our model's performance (recall the ***Curse of Dimensionality***)! If you were to use TF-IDF vectorization to turn the word 'apple' into a vector representation with a text corpus containing 100,000 words, then our word vector would contain a value at the element that corresponds to the word 'apple', and then 99,999 *0*s!

Vectors created through word embeddings are different - the size of the vector is a tunable parameter you can set.

Let's look at a toy example. Consider the diagram below. First, pay attention to what each of the columns mean. Let's assume that you built a model to 'rate' each of the animals across each of these four categories, relative to one another.

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-word-embeddings/master/images/vectors.png)

In this embedding space, the vectorized representation of the word 'dog' would be `[-0.4, 0.37, 0.02, -0.34]`. As you'll see when you study the actual Word2Vec model, you can use some nifty tricks to train a neural network to act as a sort of 'lookup table', where you can get the vector out for any given word. In the next lesson, you'll spend a bit more time understanding exactly how the model learns the correct values for each word.

## Summary

In this lesson, you learned about the concept of ***Word Embeddings***, and explored how they work.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
