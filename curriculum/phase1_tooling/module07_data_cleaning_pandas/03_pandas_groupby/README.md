# Pandas Groupby

> Part of **Topic 5: Data Cleaning in Pandas** · source item type: WikiPage

---
## Introduction

In this lab, you'll learn how to use the `.groupby()` method in Pandas to summarize datasets.

## Objectives

You will be able to:

- Use groupby methods to aggregate different groups in a dataframe


## Using `.groupby()`

Consider an example of the titanic DataFrame:

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-pandas-groupby/master/images/titanic_1.png)

During the Exploratory Data Analysis phase, one of the most common tasks you'll want to do is split the dataset into subgroups and compare them to see if you can notice any trends. For instance, you may want to group the passengers together by gender or age. You can do this by using the `.groupby()` method built-in to pandas DataFrames.

To group passengers by gender, you would type:

```python
df.groupby('Sex')

# This line of code is equivalent to the one above
df.groupby(df['Sex'])
```

Note that this alone will not display a result -- although you have split the dataset into groups, you don't have a meaningful way to display information until you chain an ***Aggregation Function*** onto the groupby. This allows you to compute summary statistics!

You can quickly use an aggregation function by chaining the call to the end of the `.groupby()` method.

```python
df.groupby('Sex').sum()
```

The code above returns displays the following DataFrame:

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-pandas-groupby/master/images/titanic_2.png)

You can use aggregation functions to quickly help us compare subsets of our data. For example, the aggregate statistics displayed above allow you to quickly notice that there were more female survivors overall than male survivors.

## Aggregation functions

There are many built-in aggregate methods provided for you in the `pandas` package, and you can even write and apply your own. Some of the most common aggregate methods you may want to use are:

- `.min()`: returns the minimum value for each column by group

- `.max()`: returns the maximum value for each column by group

- `.mean()`: returns the average value for each column by group

- `.median()`: returns the median value for each column by group

- `.count()`: returns the count of each column by group

You can also see a list of all of the built-in aggregation methods by creating a grouped object and then using tab completion to inspect the available methods:

```python
grouped_df = df.groupby('Sex')
grouped_df.
```

This will display the following output:

```python
In [26]: grouped_df.
gb.agg        gb.boxplot    gb.cummin     gb.describe   gb.filter     gb.get_group  gb.height     gb.last       gb.median     gb.ngroups    gb.plot       gb.rank       gb.std        gb.transform
gb.aggregate  gb.count      gb.cumprod    gb.dtype      gb.first      gb.groups     gb.hist       gb.max        gb.min        gb.nth        gb.prod       gb.resample   gb.sum        gb.var
gb.apply      gb.cummax     gb.cumsum     gb.fillna     gb.gender     gb.head       gb.indices    gb.mean       gb.name       gb.ohlc       gb.quantile   gb.size       gb.tail       gb.weight
```

This is a comprehensive list of all built-in methods available to grouped objects. Note that some are aggregation methods, while others, such as `gb.fillna()`, allow us to fill missing values to individual groups independently.

## Multiple groups

You can also split data into multiple different levels of groups by passing in an array containing the name of every column you want to group by -- for instance, by every combination of both `Sex` and `Pclass`.

```python
df.groupby(['Sex', 'Pclass']).mean()
```

The code above would return the following DataFrame:

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-pandas-groupby/master/images/titanic_3.png)

## Selecting information from grouped objects

Since the resulting object returned is a DataFrame, you can also slice a selection of columns you're interested in from the DataFrame returned.

The example below demonstrates the syntax for returning the mean of the `Survived` class for every combination of `Sex` and `Pclass`:

```python
df.groupby(['Sex', 'Pclass'])['Survived'].mean()
```

The code above returns the following DataFrame:

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-pandas-groupby/master/images/titanic_4.png)

The above example slices by column, but you can also slice by index. Take a look:

```python
grouped = df.groupby(['Sex', 'Pclass'])['Survived'].mean()
print(grouped['female'])

# Output:
# Pclass
# 1    0.968085
# 2    0.921053
# 3    0.500000
# Name: Survived, dtype: float64

print(grouped['female'][1])
# Output:
# 0.968085
```

Note that you need to provide only the value `female` as the index, and are returned all the groups where the passenger is female, regardless of the `Pclass` value. The second example shows the results for female passengers with a 1st-class ticket.

## Summary

In this lab, you learned about how to split a DataFrame into subgroups using the `.groupby()` method. You also learned to generate aggregate views of these groups by applying built-in methods to a groupby object.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
