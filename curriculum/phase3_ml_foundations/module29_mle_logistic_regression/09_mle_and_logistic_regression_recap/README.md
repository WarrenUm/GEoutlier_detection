# MLE and Logistic Regression - Recap

> Part of **Topic 26: MLE and Logistic Regression** · source item type: WikiPage

---
## Introduction

Well done! In this section, you reviewed maximum likelihood estimation and logistic regression. This included writing some challenging code, including gradient descent which pushed you to think critically regarding algorithm implementation.

## Log-likelihoods in Maximum Likelihood Estimation

One of the nuances you saw in maximum likelihood estimation was that of log-likelihoods. Recall that the purpose of taking log-likelihoods as opposed to likelihoods themselves is that it allows us to decompose the product of probabilities as sums of log probabilities. Analytically, this is essential to calculating subsequent gradients in order to find the next steps for our optimization algorithm.

## Local minima in Gradient Descent

One of the most important notes from this section is that **gradient descent does not guarantee an optimal solution**. Gradient descent is meant to find optimal solutions, but it only guarantees a local minimum. For this reason, gradient descent is frequently run multiple times, and the parameters with the lowest loss function then being selected for the final model.

## Logistic Regression

After coding logistic regression on your own, you then further investigated tuning such models using regularization. Recall that while precision, recall, and accuracy are useful metrics for evaluating classifiers, determining an appropriate balance between false positives and false negatives will depend on the particular problem application and the relative costs of each. For example, in the context of medical screening, a false negative could be devastating, eliminating the possibility for early intervention of the given disease. On the other hand, in another context, such as finding spam email, the cost of false positives might be much higher than false negatives -- after all, having a spam email sneak its way into your inbox is probably preferable then missing an important time-sensitive email because it was marked as spam. Due to these contextual considerations, you as the practitioner are responsible for selecting appropriate tradeoffs.

## Summary

This section was designed to give you additional practice coding algorithms in Python, and a deeper understanding of how iterative algorithms such as logistic regression converge to produce underlying model parameters.

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
- `salaries_final.csv` — supporting data/helper file for the exercise.
