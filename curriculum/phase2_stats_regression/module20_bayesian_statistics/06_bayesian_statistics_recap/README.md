# Bayesian Statistics - Recap

> Part of **Topic 17: Bayesian Statistics** · source item type: WikiPage

---
## Introduction

Well done! You covered a lot of ground in this section. From Bayes' theorem to Maximum Likelihood Estimation (MLE), you now have the foundation to dive into the world of Bayesians!

## Bayes' Theorem

To start, you investigated Bayes' theorem and some hypothetical examples.

$$ \large P(A|B) = \dfrac{P(B|A)P(A)}{P(B)}$$

## Bayesian Statistics

From there, you then went on to read more about some of the philosophical differences between Bayesians and Frequentists. Bayesians interpret probability as the level of confidence or belief in an event. In contrast, Frequentists view probability as the limit as the number of trials goes to infinity of successes versus trials.

## MLE and MAP

In outlining the discussion of Bayesian techniques, you got an introduction to Maximum Likelihood Estimation and Maximum A Posteriori Estimation. In both, you saw methods for optimizing one's beliefs given certain information. This was used to estimate parameters for assumed distributions.

## Summary

Again, quite a bit was covered in this section. There are certainly plenty of additional resources available if you wish to further dive into MLE, MAP, or other Bayesian techniques. Bayesian inference can provide a powerful framework for quantifying and reasoning with uncertainty that has continued to gain popularity with additional computing resources.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
