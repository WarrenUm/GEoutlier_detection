# Maximum A Posteriori Estimation (MAP) and Multinomial Bayes

> Part of **Topic 17: Bayesian Statistics** · source item type: WikiPage

---
## Introduction

Maximum A Posteriori provides a means for estimating a parameter given some prior knowledge about a variable. In it, one assumes a given distribution for the variable and then estimates the parameter itself given additional information. In this lesson, you'll see how Bayes' theorem can be applied in this manner and then extended to multivariate cases.

## Objectives

You will be able to

- Identify how Maximum A Posteriori Estimation is related to MLE

## Maximum A Posteriori Estimation

Maximum A Posteriori Estimation (MAP) is similar to Maximum Likelihood Estimation but extends this concept by allowing one to also account for prior beliefs regarding the distribution of the variable in question. Recall Bayes' theorem:

$$ \large P(A|B) = \dfrac{P(B|A)(A)}{P(B)}$$

The Bayesian interpretation of this formula is

$$ \large \text{Posterior} = \dfrac{\text{Likelihood} \cdot \text{Prior}}{\text{Evidence}}$$

With MAP, you then attempt to optimize a parameter $\theta$ for the assumed distribution in order to maximize the posterior probability.

## Multinomial Bayes

Multinomial Bayes also extends the notions within Bayes' theorem, allowing one to chain inferences. The primary assumption for this is assuming that your variables are independent of one another. Recall that if you assume two events A and B are independent of one another, then $P(A \cap B) = P(A)\cdot P(B)$. Similarly, if independence is assumed when extending Bayes theorem to a multivariate case, one can multiply the successive probability estimates. Mathematically, this can be summarized as:

$$ \large P(Y|X*1, X*2,...,X*n) = \dfrac{P(X*1|Y)\cdot P(X*2|Y) \cdot ... \cdot P(X*n|Y)}{P(X*1, X*2,...,X_n)}P(Y)$$

## Summary

This lesson briefly introduced the concept of Maximum A Posteriori Estimation and extending Bayes' theorem to multivariate cases. In later sections, you'll investigate these ideas in practice, working with practical examples and coding your own implementations to gain a full understanding.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
