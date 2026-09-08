# Tuning Neural Networks - Recap

> Part of **Topic 42: Tuning Neural Networks** · source item type: WikiPage

---
## Key Takeaways

The key takeaways from this section include:

- Validation and test sets are used when iteratively building deep neural networks
- Like traditional machine learning models, we need to watch out for the bias variance trade-off when building deep learning models
- Several regularization techniques can help us limit overfitting: L1 Regularization, L2 Regularization, Dropout Regularization, etc ...
- Training of deep neural networks can be sped up by using normalized inputs
- Normalized inputs can also help mitigate a common issue of vanishing or exploding gradients
- Examples of alternatives for gradient descent are: RMSprop, Adam, Gradient Descent with Momentum, etc.
- Hyperparameter tuning is of crucial importance when working with deep learning models, as setting the parameters right can lead to great improvements in model performance

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
- `Bank_complaints.csv` — supporting data/helper file for the exercise.
