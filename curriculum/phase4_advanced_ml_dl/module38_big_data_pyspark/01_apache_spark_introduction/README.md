# Apache Spark - Introduction

> Part of **Topic 35: Big Data in PySpark** · source item type: WikiPage

---
## Introduction

In this section, you will be introduced to the idea of big data and the tools data scientists use to manage it.

## Big Data in PySpark

Big data is undoubtedly one of the most hyped terms in data science these days. Big data analytics involves dealing with data that is large in volume and high in variety and velocity, making it challenging for data scientists to run their routine analysis activities. In this section, you'll learn the basics of dealing with big data through parallel and distributed computing. In particular, you will be introduced to Apache Spark, an open-source distributed cluster-computing framework. You'll learn how to use the popular Apache Spark Python API, **PySpark**.

### Parallel and Distributed Computing with MapReduce

Before diving into PySpark, we start this section by providing more context on the ideas of parallel and distributed computing and MapReduce. When talking about distributed and parallel computing, we refer to the fact that complex (and big) data science tasks can be executed over a cluster of interconnected computers instead of on just one machine. You'll learn that MapReduce allows us to convert these big datasets into sets of tuples as key:value pairs, as we'll cover in more detail in this section.

### Apache Spark

As mentioned before, Apache Spark makes it easier (and feasible) to use huge amounts of data! You'll read a scientific article on the advantages of Apache Spark to understand its use and benefits better.

### Installing and Configuring PySpark with Docker

A big part of PySpark is actually getting PySpark up and running on your machine. You'll get an overview of how to do this so you can get started exploring distributed computing!

### PySpark

You'll learn about distributed and parallel computing and the different PySpark modules needed to create this parallelization.

### RDDs (Resilient Distributed Datasets)

Resilient Distributed Datasets (RDDs) are the core concept in PySpark. RDDs are immutable distributed collections of data objects. Each dataset in RDD is divided into logical partitions, which may be computed on different computers (so-called "nodes") in the Spark cluster. In this section, you'll learn how RDDs in Spark work. Additionally, you'll learn that RDD operations can be split into actions and transformations.

### Word Count with MapReduce

You'll use MapReduce to solve a basic NLP task where you compare the attributes of different authors of various texts.

### Machine Learning with Spark

After you've solved a basic MapReduce problem, you will learn about employing the machine learning modules of PySpark. You will perform both a regression and classification problem and get the chance to build a full parallelizable data science pipeline that can scale to work with big data. In this section, you'll also get a chance to work with PySpark DataFrames.

## Summary

In this section, you'll learn the foundations of Big Data and how to manage it with Apache Spark!

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
