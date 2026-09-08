# Getting Started with SQL - Recap

> Part of **Topic 6: Getting Started with SQL** · source item type: WikiPage

---
## Introduction

In this section, you were introduced to SQL databases and learned the basics of writing `SELECT` queries as well as some introductory database administration queries.

## Key Takeaways

### SQL Format

While you may end up primarily using tools such as pandas to do a lot of your exploratory analysis and data manipulation, databases provide a much more powerful data storage option than flat files like CSVs or spreadsheets.

SQL is short for "structured query language". SQL *databases* are containers that can contain multiple *tables*. Each table has a *schema* that describes its columns (and their data types), and an *entity relationship diagram* (or ERD) is a visual representation of all tables and their relationships.

Interacting with SQL databases requires that you write queries using SQL syntax. Then you can execute the queries using tools such as a command-line interface or a Python library.

Most database software is actually a type of server, but we mainly use SQLite in this course because it is lightweight and portable. SQLite databases are files located on the computer's file system, similar to CSV or JSON files. We used the `sqlite3` Python library to open connections to these databases.

### `SELECT` Queries

As a data scientist, typically you are interacting with a database because you want to extract some data for analysis. To do this, you write SQL queries that start with `SELECT`. This allows you to read specific columns by name, or read all columns using `SELECT *`.

If you want to **filter** your selection so it only contains rows that meet certain criteria, you can use the `WHERE` clause.

If you want to **order** your selection, you can use the `ORDER BY` clause. Remember that the default behavior is to return results in ascending order (smallest to largest). You can verbosely specify this with the `ASC` keyword, or, more commonly, modify the behavior to sort in descending order (largest to smallest) with the `DESC` keyword.

If you want to **limit** the number of results, you can use the `LIMIT` clause. This is frequently used with `ORDER BY` to select the largest or smallest N results.

### Grouping

The unit of analysis of a SQL table is whatever is represented by a row. Sometimes you want to use a different unit of analysis that is less granular than the original. Maybe a row represents a city, but you want analysis that is by country. This is a good use case for **grouping** data using the `GROUP BY` clause.

Often you also want to use an **aggregate function** when grouping, so that you can summarize the grouped data in some meaningful way. Examples of these aggregate functions include `COUNT()`, `MAX()`, `MIN()`, and `AVG()`. You can also use those aggregate functions without grouping, and they will return a single record for the table overall (or all rows selected based on your filters).

If you want to **filter based on the result of an aggregate function**, you need to use `HAVING` rather than `WHERE`. `WHERE` applies to the original rows of the table, whereas `HAVING` applies to the rows created by `GROUP BY`. Both can be used in the same query if needed, applied to different features.

### Database Administration

As a data scientist, your responsibilities will typically be limited to writing `SELECT` queries. However it is useful to be familiar with the other queries used for managing data using databases, including commands for creating tables (specifying the data types in their schemas) and inserting, updating, and deleting data. Understanding the basics will help you collaborate with the team members who are responsible for these tasks, as well as occasional ad hoc work needed for your data analysis tasks.

## Summary

In this section, you were introduced to some foundational concepts in SQL. Next you'll expand your skills to more complex queries that integrate information from multiple tables!

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
