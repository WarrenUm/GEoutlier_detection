# Pivot Tables with Pandas

> Part of **Topic 5: Data Cleaning in Pandas** · source item type: Assignment

---
## Introduction

In this lesson, we'll learn about the various ways we can index and structure our data sets to make it easier to process or understand. We start by learning about the difference between the ***Wide*** format and the ***Long*** format, compare basic flattened index structures with multi-hierarchical index structures, and then create them ourselves using aggregation functions and pivot tables!

## Objectives

You will be able to:

- Describe what is meant by long and wide format data

- Use multi-hierarchical indexing to access aggregated data
- Use pivot to create a more organized aggregated DataFrame
- Use stack and unstack to move between different level of multi-indexing

## Long and Wide Formats

These two different formats refer to how we structure our data in a DataFrame. We'll start by comparing the two, and discussing the salient points of each.

### Wide Format

This is the common setup you're probably used to seeing. In the wide format, each column of data represents a variable, and each row represents 1 observation. If this were a medical dataset, each row would be the data corresponding to a different patient.

In wide format, the index usually an integer, with 0 being the topmost row.

### Long Format

In Long format, each index is a point in time for each observation. See the following diagram for comparison of the two:

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-pivot-tables-pandas/master/images/Image_200_wide_v_long.png)

Note that in this format, a given observation has values across multiple rows. This is an especially useful format when dealing with time series data, or aggregated data, because we can make use of ***Multi-Hierarchical Indexing***,

## Multi-Hierarchical Indexing

A common task when working with data is to create pivot tables, or group the data using aggregation functions. In this respect, the Long format provides a very neat, organized way of structuring our data with multiple levels of indexes, allowing us to cleanly and easily represent different combinations of data. Consider the following pivot table below (which you'll create yourself in the next lab):

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-pivot-tables-pandas/master/images/pt1.png)

We can see by looking at the left two columns that this DataFrame has a Multi-Hierarchical Index with 2 levels, consisting of the "State" and Gender. In this way, we have an easy way to aggregate and organize information to allow us to quickly answer questions with our data like "What was the total number of deaths by gender in Alabama?".

Let's take a look at one more example:

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-pivot-tables-pandas/master/images/pt2.png)

In this DataFrame, the index has three hierarchical levels, with the outermost being "State" and the innermost being "Race".

## `.groupby()` and aggregation methods

Pandas DataFrames provide an easy way to group data using the `.groupby()` method. To use this method, we just specify our indices in order (the columns we want to group the data by) and the method will return a new DataFrame containing the data grouped as we asked.

For instance, if we wanted to group the Titanic Dataset by the port of embarkation, we would type:

```python
dataframe.groupby("Embarked")
```

This would give us a long format DataFrame with a flat index structure akin to the example in the top-most diagram.

Perhaps we want to group our data by both the port of embarkation and the ticket class (Labeled as *Pclass* in the Titanic Dataset), we would type:

```python
dataframe.groupby(['Embarked', 'Pclass'])
```

This would return a DataFrame with a multi-hierarchical index, with `'Embarked'` being the outermost level.

Groupby statements are most commonly used with aggregation methods, which allow us to quickly calculate summary statistics such as the mean, median, min, max, mode, count, etc.

Building on our last example, if we wanted to see the mean values for every grouping of `Embarked` and `Pclass` across different variables, we would type:

```python
dataframe.groupby(['Embarked', 'Pclass']).mean()
```

Notice that we can make use of method chaining to quickly and concisely call the aggregation function at the same time as the `.groupby()` method.

## Pivot tables

Pivot tables are a common toolset that you might have used before in spreadsheet software such as Microsoft Excel or Google Sheets.

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-pivot-tables-pandas/master/images/excel_pt.png)

 *An Example Pivot Table created in Microsoft Excel*

Pivot tables allow us to quickly examine our data by "pivoting" on different variables of interest. Pandas allows us to easily create pivot tables with a built-in `.pivot()` method.

In order to create a pivot table, we need to just call the `dataframe.pivot()` method and specify the `index` column, the `columns` to put in our pivot table, and the `value` to put in each cell.

For example, let's look at a pivot table you'll create in the next lab:

```python
some_dataframe.pivot(index='State', columns='Gender', values='Deaths_mean')
```

would return this pivot table:

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-pivot-tables-pandas/master/images/pt3.png)

Don't worry about the data this actually contains, as you don't yet have the context because you haven't been introduced to the dataset. Instead, just pay attention to the structure of the indexes.

## Stacking and unstacking data

One of the quickest ways to manipulate the format of a dataset in python is to use the `.stack()` and `unstack()` methods built into pandas DataFrames.

Take a look at the following diagram and see if you can figure out what the `unstack()` is doing.

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-pivot-tables-pandas/master/images/Image_201_unstack.png)

By telling the `.unstack()` call which index we want to unstack, we can move it from the index section over to the right as a variable column -- `.stack()` would do the exact opposite, moving data to the left and making it a level of the index.

## Summary

We spent some time in this lesson learning about approaches to indexing and structuring our data sets. In the next lesson, we'll get some hands-on practice!

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
- `causes_of_death.tsv` — supporting data/helper file for the exercise.
