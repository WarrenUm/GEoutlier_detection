# Apache Spark - Recap

> Part of **Topic 35: Big Data in PySpark** · source item type: WikiPage

---
## Key Takeaways

The key takeaways from this section include:

- Big Data usually refers to datasets that grow so large that they become awkward to work with using traditional database management systems and analytical approaches
- Big data refers to data that is terabytes (TB) to petabytes (PB) in size
- MapReduce can be used to split big datasets up in smaller sets to be distributed over several machines to deal with Big Data Analytics
- Before starting to work, you need to install Docker and Kinematic on your environment
- Make sure to test your installation so you're sure everything is working
- When you start working with PySpark, you have to create a `SparkContext()`
- The creation or RDDs is essential when working with PySpark
- Examples of actions and transformations include `collect()`, `count()`, `filter()`, `first()`, `take()`, and `reduce()`
- Machine Learning on the scale of big data can be done with Spark using the `ml` library

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
