# Linear Algebra - Recap

> Part of **Topic 22: Linear Algebra** · source item type: WikiPage

---
## Introduction

In this section, you learned the fundamentals of linear algebra. An understanding of linear algebra will help you better understand the underlying mathematics behind some machine learning algorithms.

## Key Takeaways

The goal of this section was to provide both a conceptual and computational introduction to linear algebra - one of the foundational concepts underlying most machine learning models. Some of the key takeaways include:

- One use case for vectors and matrices is for representing and solving systems of linear equations
- A scalar is a single, real number. A vector is a one-dimensional array of numbers. A matrix is a 2-dimensional array of numbers
- A tensor is a generalized term for an n-dimensional rectangular grid of numbers. A vector is a one-dimensional (first-order tensor), a matrix is a two-dimensional (second-order tensor), etc.
- Two matrices can be added together if they have the same shape
- Scalars can be added to matrices by adding the scalar (number) to each element
- To calculate the dot product for matrix multiplication, the first matrix must have the same number of columns as the number of rows in the second matrix
- Operating on NumPy data types is substantially more computationally efficient than performing the same operations on native Python data types
- It is possible to use linear algebra in NumPy to solve for a linear regression using the OLS method
- OLS is not computationally efficient, so in practice, we usually perform a gradient descent instead to solve a linear regression

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
