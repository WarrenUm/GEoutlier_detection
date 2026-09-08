# Bayesian Classification - Introduction

> Part of **Topic 28: Bayes Classification** · source item type: WikiPage

---
## Introduction

In an earlier section, you learned about Bayesian statistics with plenty of theory and application of Bayes theorem. You'll now take a look at using Bayes theorem to perform some classification tasks. Here, you'll see that the Bayes theorem can be applied to multiple variables simultaneously.

## Bayes Classification

Naive Bayes algorithms extend Bayes' formula to multiple variables by assuming that these features are independent of one another, which may not be met, (hence its naivety) it can nonetheless provide strong results in scenarios with clean and well normalized datasets. This then allows you to estimate an overall probability by multiplying the conditional probabilities for each of the independent features.

Bayes' formula extended to multiple features is:

$$ \Large P(y|x*1, x*2, ..., x*n) = \frac{P(y)\prod*{i}^{n}P(x*i|y)}{P(x*1, x*2, ..., x*n)}$$

## Document Classification

An interesting application of Bayes' theorem is to use *bag of words* for document classification. A bag of words representation takes a text document and converts it into a word frequency representation. In this section, you'll use bag of words and Naive Bayes to classify YouTube videos into appropriate topics.

## Summary

Over the next few lessons you will learn about another fundamental classification algorithm which has many practical applications. It's time to jump into the wonderful Bayesian world again! This section will help you solidify your understanding of Bayesian stats.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
