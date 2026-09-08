# Performing Principal Component Analysis

> Part of **Topic 33: Principal Component Analysis** · source item type: Assignment

---
## Introduction

In this lesson, we'll write the PCA algorithm from the ground up using NumPy. This should provide you with a deeper understanding of the algorithm and help you practice your linear algebra skills.

## Objectives

You will be able to:

- List the steps required to perform PCA on a given dataset

- Decompose and reconstruct a matrix using eigendecomposition
- Perform a covariance matrix calculation with NumPy

## Step 1: Get some data

To start, generate some data for PCA!

```python
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
np.random.seed(42)

x1 = np.random.uniform(low=0, high=10, size=100)
x2 = [(xi*3)+np.random.normal(scale=2) for xi in x1]
plt.scatter(x1, x2);
```

![png](https://raw.githubusercontent.com/learn-co-curriculum/dsc-performing-principle-component-analysis/master/index_files/index_2_0.png)

## Step 2: Subtract the mean

Next, you have to subtract the mean from each dimension of the data.

```python
import pandas as pd

data = pd.DataFrame([x1,x2]).transpose()
data.columns = ['x1', 'x2']
data.head()
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      x1 x2     0 3.745401 11.410298   1 9.507143 27.923414   2 7.319939 22.143340   3 5.986585 13.984617   4 1.560186 4.241215

```python
data.mean()
```

```python
x1     4.701807
x2    14.103262
dtype: float64
```

```python
mean_centered = data - data.mean()
mean_centered.head()
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      x1 x2     0 -0.956406 -2.692964   1 4.805336 13.820153   2 2.618132 8.040078   3 1.284777 -0.118645   4 -3.141621 -9.862046

## Step 3: Calculate the covariance matrix

Now that you have normalized your data, you can calculate the covariance matrix.

```python
cov = np.cov([mean_centered['x1'], mean_centered['x2']])
cov
```

```python
array([[ 8.84999497, 25.73618675],
       [25.73618675, 78.10092586]])
```

## Step 4: Calculate the eigenvectors and eigenvalues of the covariance matrix

It's time to compute the associated eigenvectors. These will form the new axes when it's time to reproject the dataset on the new basis.

```python
eigen_value, eigen_vector = np.linalg.eig(cov)
eigen_vector
```

```python
array([[-0.94936397, -0.31417837],
       [ 0.31417837, -0.94936397]])
```

```python
eigen_value
```

```python
array([ 0.33297363, 86.61794719])
```

## Step 5: Choosing components and forming a feature vector

If you look at the eigenvectors and eigenvalues above, you can see that the eigenvalues have very different values. In fact, it turns out that **the eigenvector with the highest eigenvalue is the principal component of the dataset.**

In general, once eigenvectors are found from the covariance matrix, the next step is to order them by eigenvalue in descending order. This gives us the components in order of significance. Typically, PCA will be used to reduce the dimensionality of the dataset and as such, some of these eigenvectors will be subsequently discarded. In general, the smaller the eigenvalue relative to others, the less information encoded within said feature.

Finally, you need to form a **feature vector**, which is just a fancy name for a matrix of vectors. This is constructed by taking the eigenvectors that you want to keep from the list of eigenvectors, and forming a matrix with these eigenvectors in the columns as shown below:

```python
# Get the index values of the sorted eigenvalues
e_indices = np.argsort(eigen_value)[::-1]

# Sort
eigenvectors_sorted = eigen_vector[:, e_indices]
eigenvectors_sorted
```

```python
array([[-0.31417837, -0.94936397],
       [-0.94936397,  0.31417837]])
```

## Step 5: Deriving the new dataset

This the final step in PCA, and is also the easiest. Once you have chosen the components (eigenvectors) that you wish to keep in our data and formed a feature vector, you simply take the transpose of the vector and multiply it on the left of the original dataset, transposed.

```python
transformed = eigenvectors_sorted.dot(mean_centered.T).T
transformed[:5]
```

```python
array([[  2.85708504,   0.06190663],
       [-14.63008778,  -0.2200194 ],
       [ -8.45552104,   0.04045849],
       [ -0.29101209,  -1.25699704],
       [ 10.34970068,  -0.11589976]])
```

## Summary

That's it! We just implemented PCA on our own using NumPy! In the next lab, you'll continue to practice this on your own!

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
