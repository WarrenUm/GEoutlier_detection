# Decision Trees - Recap

> Part of **Topic 29: Decision Trees** · source item type: WikiPage

---
## Key Takeaways

The key takeaways from this section include:

- Decision trees can be used for both categorization and regression tasks
- They are a powerful and interpretable technique for many machine learning problems (especially when combined with ensemble methods)
- Decision trees are a form of Directed Acyclic Graphs (DAGs) - you traverse them in a specified direction, and there are no "loops" in the graphs to go backward
- Algorithms for generating decision trees are designed to maximize the information gain from each split
- A popular algorithm for generating decision trees is ID3 - the Iterative Dichotomiser 3 algorithm
- There are several hyperparameters for decision trees to reduce overfitting - including maximum depth, minimum samples to split a node that is currently a leaf, minimum leaf sample size, maximum leaf nodes, and maximum features

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
- `data_banknote_authentication.csv` — supporting data/helper file for the exercise.
