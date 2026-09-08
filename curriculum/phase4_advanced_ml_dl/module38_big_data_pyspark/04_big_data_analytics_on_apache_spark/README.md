# Big Data Analytics on Apache Spark

> Part of **Topic 35: Big Data in PySpark** · source item type: WikiPage

---
## Introduction

Big data analytics is an emerging area of interest both for business and academia. There are a lot of details around the characteristics of big data and how Apache Spark eases up the job of analyzing huge amounts of data using a simple programming paradigm. In this section, we will look at understanding and implementing a simple problem using MapReduce in PySpark. Real world problems, however, are much more complicated than this and you should be able to scale up the takeaways from the simple word count example we will complete to much bigger problems. This lesson aims to provide you with a wider understanding of MapReduce and big data computation in the Apache Spark environment.

## Objectives

You will be able to:

- Describe the role of Apache Spark in Big data analytics

- List some of the Spark functionalities
- Describe the role of RDDs in spark

For this lesson, you are required to read the following review article:

[https://link.springer.com/article/10.1007/s41060-016-0027-9](https://link.springer.com/article/10.1007/s41060-016-0027-9)

International Journal of Data Science and Analytics, November 2016, Volume 1, Issue 3–4, pp 145–164. Authors: Salman Salloum, Ruslan Dautov, Xiaojun Chen, Patrick Xiaogang Peng, Joshua Zhexue Huang

*"In this paper, we present a technical review on big data analytics using Apache Spark. This review focuses on the key components, abstractions and features of Apache Spark. More specifically, it shows what Apache Spark has for designing and implementing big data algorithms and pipelines for machine learning, graph analysis and stream processing. In addition, we highlight some research and development directions on Apache Spark for big data analytics."* - from the abstract. Here is an image from the paper giving a general overview of how the spark ecosystem functions:

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-big-data-analytics-apache-spark/master/images/spark.gif)

You are expected to spend around 90 - 120 minutes reading this article. It is an excellent article and all the key aspects of spark computational environment are summarized and presented in an excellent manner.

## Summary

In this lesson, you read the scientific article "Big Data Analytics on Apache Spark", which covers the key aspects of Spark's computational environment. You'll now move on to working with Spark through Python.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
