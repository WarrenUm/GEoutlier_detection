# Clustering - Recap

> Part of **Topic 34: Clustering** · source item type: WikiPage

---
## Key Takeaways

The key takeaways from this section include: * There are two main types of clustering algorithms: non-hierarchical clustering (k-means) and hierarchical agglomerative clustering * You can quantify the performance of a clustering algorithm using metrics such as variance ratios * When working with the k-means clustering algorithm, it is useful to create elbow plots to find an optimal value for $k$ * When using hierarchical agglomerative clustering, different linkage criteria can be used to determine which clusters should be merged and at what point * Dendrograms and clustergrams are very useful visual tools in hierarchical agglomerative clustering * Advantages of k-means clustering include easy implementation and speed, whereas the main disadvantage is that it isn't always straightforward how to pick the "right" value for $k$ * Advantages of hierarchical agglomerative clustering include easy visualization and intuitiveness, whereas the main disadvantage is that the result is very distance-metric-dependent * You can use supervised and unsupervised learning together in a few different ways. Applications of this are look-alike models in market segmentation and semi-supervised learning

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
