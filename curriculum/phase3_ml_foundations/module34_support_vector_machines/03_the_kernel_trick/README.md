# The Kernel Trick

> Part of **Topic 31: Support Vector Machines** · source item type: WikiPage

---
## Introduction

In this lesson, you'll learn how to create SVMs with non-linear decision boundaries data using kernels!

## Objectives

You will be able to:

- Define the kernel trick and explain why it is important in an SVM model
- Describe a radial basis function kernel

 - Describe a sigmoid kernel
 - Describe a polynomial kernel - Determine when it is best to use specific kernels within SVM

## Non-linear problems: The Kernel trick

In the previous lab, you looked at a plot where a linear boundary was clearly not sufficient to separate the two classes cleanly. Another example where a linear boundary would not work well is shown below. How would you draw a max margin classifier here? The intuitive solution is to draw an arc around the circles, separating them from the surrounding diamonds. To generate non-linear boundaries such as this, you use what is known as a kernel.

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-the-kernel-trick/master/images/new_SVM_nonlin.png)

The idea behind kernel methods is to create (nonlinear) combinations of the original features and project them onto a higher-dimensional space. For example, take a look at how this dataset could be transformed with an appropriate kernel from a two-dimensional dataset onto a new three-dimensional feature space.

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-the-kernel-trick/master/images/new_SVM_kernel.png)

## Types of kernels

There are several kernels, and an overview can be found in this lesson, as well as in the scikit-learn documentation [here](https://scikit-learn.org/stable/modules/svm.html#kernel-functions). The idea is that kernels are inner products in a transformed space.

### The Linear kernel

The linear kernel is, as you've seen, the default kernel and simply creates linear decision boundaries. The linear kernel is represented by the inner product of the $\langle x, x' \rangle$. It is important to note that some kernels have additional parameters that can be specified and knowing how these parameters work is critical to tuning SVMs.

### The RBF kernel

There are two parameters when training an SVM with the *R*adial *B*asis *F*unction: $C$ and $gamma$.

-

The parameter $C$ is common to all SVM kernels. Again, by tuning the $C$ parameter when using kernels, you can provide a trade-off between misclassification of the training set and simplicity of the decision function. A high $C$ will classify as many samples correctly as possible (and might potentially lead to overfitting)
-

$gamma$ defines how much influence a single training example has. The larger $gamma$ is, the closer other examples must be to be affected

The RBF kernel is specified as:

$$\exp{(-\gamma \lVert x - x' \rVert^2)} $$

Gamma has a strong effect on the results: a $gamma$ that is too large will lead to overfitting, while a $gamma$ which is too small will lead to underfitting (kind of like a simple linear boundary for a complex problem).

In scikit-learn, you can specify a value for $gamma$ using the parameter `gamma`. The default `gamma` value is "auto", if no other gamma is specified, gamma is set to $1/\text{number*of*features}$ . You can find more on parameters in the RBF kernel [here](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html).

### The Polynomial kernel

The Polynomial kernel is specified as

$$(\gamma \langle x - x' \rangle+r)^d $$

- $d$ can be specified by the parameter `degree`. The default degree is 3.
- $r$ can be specified by the parameter `coef0`. The default is 0.

### The Sigmoid kernel

The sigmoid kernel is specified as:

$$\tanh ( \gamma\langle x - x' \rangle+r) $$

This kernel is similar to the signoid function in logistic regression.

## Some more notes on SVC, NuSVC, and LinearSVC

### NuSVC

NuSVC is similar to SVC, but adds an additional parameter, $\nu$, which controls the number of support vectors and training errors. $\nu$ jointly creates an upper bound on training errors and a lower bound on support vectors.

Just like SVC, NuSVC implements the "one-against-one" approach when there are more than 2 classes. This means that when there are n classes, $\dfrac{n*(n-1)}{2}$ classifiers are created, and each one classifies samples in 2 classes.

### LinearSVC

LinearSVC is similar to SVC, but instead of the "one-versus-one" method, a "one-vs-rest" method is used. So in this case, when there are $n$ classes, just $n$ classifiers are created, and each one classifies samples in 2 classes, the one of interest, and all the other classes. This means that SVC generates more classifiers, so in cases with many classes, LinearSVC actually tends to scale better.

## Probabilities and predictions

You can make predictions using support vector machines. The SVC decision function gives a probability score per class. However, this is not done by default. You'll need to set the `probability` argument equal to `True`. Scikit-learn internally performs cross-validation to compute the probabilities, so you can expect that setting `probability` to `True` makes the calculations longer. For large datasets, computation can take considerable time to execute.

## Summary

Great! You now have a basic understanding of how to use kernel functions in Support Vector Machines. You'll do just that in the upcoming lab!

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
