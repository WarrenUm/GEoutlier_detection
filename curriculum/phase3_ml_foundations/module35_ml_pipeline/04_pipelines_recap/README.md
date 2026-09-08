# Pipelines - Recap

> Part of **Topic 32: Building a Machine Learning Pipeline** · source item type: WikiPage

---
## Key Takeaways

The key takeaways from this section include:

- Machine Learning Pipelines create a nice workflow to combine data manipulations, preprocessing, and modeling
- Machine Learning Pipelines can be used along with grid search to evaluate several parameter settings
- Grid search can considerably blow up computation time when computing for several parameters along with cross-validation
- Some models are very sensitive to hyperparameter changes, so they should be chosen with care, and even with big grids a good outcome isn't always guaranteed

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
- `winequality-red.csv` — supporting data/helper file for the exercise.
