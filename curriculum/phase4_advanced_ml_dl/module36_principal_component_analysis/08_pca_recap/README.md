# PCA - Recap

> Part of **Topic 33: Principal Component Analysis** · source item type: WikiPage

---
## Key Takeaways

The key takeaways from this section include:

- PCA is an *unsupervised learning technique* which does not require labeled data
- It is also a dimensionality reduction technique which can be used to compress data and experiment with its effects on machine learning algorithms as a preprocessing step
- There are four steps to conducting PCA:
  - Center each feature by subtracting the feature mean
  - Calculate the covariance matrix for your normalized dataset
  - Calculate the eigenvectors/eigenvalues for the covariance matrix
    - Reorder your eigenvectors based on their accompanying eigenvalues (in descending order of the eigenvalues)

  - Take the dot product of the transpose of the eigenvectors with the transpose of the normalized data

- You can also easily implement PCA using scikit-learn

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
