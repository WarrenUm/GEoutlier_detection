# Extensions To Linear Models - Recap

> Part of **Topic 20: Extensions to Linear Models** · source item type: WikiPage

---
## Introduction

Congratulations, you've just modeled some complex non-linear relationships with interaction terms and polynomials! Here is a recap of what you learned in this section.

## Key Takeaways

This section gave you the chance to learn about techniques whereby you can model non-linear relationships between the predictor and target variables. It's very rare that real-world problems can be modeled with a simple linear regression, so it's important to get yourself well acquainted with creating new features and selecting the most important ones.

- An interaction is a particular property of two or more variables where they interact in a non-additive manner when affecting a third variable
- Polynomial regression allows for bringing in higher orders of predictor variables (such as squared, cubed, etc)
- The risk of polynomial regression is that they can easily overfit to data, so it's important to consider the Bias-variance tradeoff when building models with greater complexity

## Summary

Excellent work! You learned a substantial amount about different ways to model non-linear relationships. You will continue to use and build upon the concepts learned in this section for the rest of your machine learning career.

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
- `ames.csv` — supporting data/helper file for the exercise.
