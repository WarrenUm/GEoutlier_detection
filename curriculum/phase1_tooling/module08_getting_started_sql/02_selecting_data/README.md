# Selecting Data

> Part of **Topic 6: Getting Started with SQL** · source item type: Assignment

---
## Introduction

Now that you've gotten a brief introduction to SQL, its time to get some hands-on practice connecting to a database via Python and executing some queries.

## Objectives

You will be able to:

- Connect to a SQL database using Python
- Retrieve all information from a SQL table
- Retrieve a subset of records from a table using a `WHERE` clause
- Write SQL queries to filter and order results
- Retrieve a subset of columns from a table


## Connecting to a Database Using Python

SQLite databases are stored as files on disk. The one we will be using in this lesson is called `data.sqlite`.

```python
! ls
```

```python
CONTRIBUTING.md README.md       [34mimages[m[m
LICENSE.md      data.sqlite     index.ipynb
```

(Here the file extension is `.sqlite` but you will also see examples ending with `.db`)

If we try to read from this file without using any additional libraries, we will get a bunch of garbled nonsense, since this file is encoded as bytes and not plain text:

```python
with open("data.sqlite", "rb") as f:
    print(f.read(100))
```

```python
b'SQLite format 3\x00\x10\x00\x01\x01\x00@  \x00\x00\x00\x10\x00\x00\x008\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00.\x05B'
```

### Connection

Instead, we will use the `sqlite3` module ([documentation here](https://docs.python.org/3/library/sqlite3.html)). The way that this module works is that we start by opening a *connection* to the database with `sqlite3.connect`:

```python
import sqlite3
conn = sqlite3.connect('data.sqlite')
```

We will use this connection throughout the lesson, then close it at the end.

Let's look at some more attributes of the connection:

```python
print("Data type:", type(conn))
print("Uncommitted changes:", conn.in_transaction)
print("Total changes:", conn.total_changes)
```

```python
Data type:
Uncommitted changes: False
Total changes: 0
```

As you can see, since we have only opened the connection and not performed any queries, there are no uncommitted changes and 0 total changes so far. Let's continue on and create a *cursor*.

### Cursor

A cursor object is what can actually execute SQL commands. You create it by calling `.cursor()` on the connection.

```python
cur = conn.cursor()
```

```python
type(cur)
```

```python
sqlite3.Cursor
```

### Exploring the Schema

Let's use the cursor to find out what tables are contained in this database. This requires two steps:

1. Executing the query (`.execute()`)
2. Fetching the results (`.fetchone()`, `.fetchmany()`, or `.fetchall()`)

This is because some SQL commands (e.g. deleting data) do not require results to be fetched, just commands to be executed. So the interface only fetches the results if you ask for them.

```python
# Execute the query
cur.execute("""SELECT name FROM sqlite_master WHERE type = 'table';""")
# Fetch the result and store it in table_names
table_names = cur.fetchall()
table_names
```

```python
[('orderdetails',),
 ('payments',),
 ('offices',),
 ('customers',),
 ('orders',),
 ('productlines',),
 ('products',),
 ('employees',)]
```

So now we know the names of the tables. What if we want to know the schema of the `employees` table?

```python
cur.execute("""SELECT sql FROM sqlite_master WHERE type = 'table' AND name = 'employees';""")
employee_columns = cur.fetchone()
employee_columns
```

```python
('CREATE TABLE `employees` (`employeeNumber`, `lastName`, `firstName`, `extension`, `email`, `officeCode`, `reportsTo`, `jobTitle`)',)
```

Ok, now we know the names of the columns!

## ERD Overview

The database that you've just connected to is the same database you have seen previously, containing data about orders, employeers, etc. Here's an overview of the database:

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-selecting-data/master/images/Database-Schema.png)

If we want to get all information about the first 5 employee records, we might do something like this (`*` means all columns):

```python
cur.execute("""SELECT * FROM employees LIMIT 5;""")
cur.fetchall()
```

```python
[('1002',
  'Murphy',
  'Diane',
  'x5800',
  'dmurphy@classicmodelcars.com',
  '1',
  '',
  'President'),
 ('1056',
  'Patterson',
  'Mary',
  'x4611',
  'mpatterso@classicmodelcars.com',
  '1',
  '1002',
  'VP Sales'),
 ('1076',
  'Firrelli',
  'Jeff',
  'x9273',
  'jfirrelli@classicmodelcars.com',
  '1',
  '1002',
  'VP Marketing'),
 ('1088',
  'Patterson',
  'William',
  'x4871',
  'wpatterson@classicmodelcars.com',
  '6',
  '1056',
  'Sales Manager (APAC)'),
 ('1102',
  'Bondur',
  'Gerard',
  'x5408',
  'gbondur@classicmodelcars.com',
  '4',
  '1056',
  'Sale Manager (EMEA)')]
```

Because `.execute()` returns the cursor object, it also possible to combine the previous two lines into one line, like so:

```python
cur.execute("""SELECT * FROM employees LIMIT 5;""").fetchall()
```

```python
[('1002',
  'Murphy',
  'Diane',
  'x5800',
  'dmurphy@classicmodelcars.com',
  '1',
  '',
  'President'),
 ('1056',
  'Patterson',
  'Mary',
  'x4611',
  'mpatterso@classicmodelcars.com',
  '1',
  '1002',
  'VP Sales'),
 ('1076',
  'Firrelli',
  'Jeff',
  'x9273',
  'jfirrelli@classicmodelcars.com',
  '1',
  '1002',
  'VP Marketing'),
 ('1088',
  'Patterson',
  'William',
  'x4871',
  'wpatterson@classicmodelcars.com',
  '6',
  '1056',
  'Sales Manager (APAC)'),
 ('1102',
  'Bondur',
  'Gerard',
  'x5408',
  'gbondur@classicmodelcars.com',
  '4',
  '1056',
  'Sale Manager (EMEA)')]
```

### Quick Note on String Syntax

When working with strings, you may have previously seen a `'string'`, a `"string"`, a `'''string'''`, or a `"""string"""`. While all of these are strings, the triple quotes have the added functionality of being able to use multiple lines within the same string as well as to use single quotes within the string. Sometimes, SQL queries can be much longer than others, in which case it's helpful to use new lines for readability. Here's the same example, this time with the string spread out onto multiple lines:

```python
first_five_employees_query = """
SELECT *
FROM employees
LIMIT 5
;
"""

cur.execute(first_five_employees_query).fetchall()
```

```python
[('1002',
  'Murphy',
  'Diane',
  'x5800',
  'dmurphy@classicmodelcars.com',
  '1',
  '',
  'President'),
 ('1056',
  'Patterson',
  'Mary',
  'x4611',
  'mpatterso@classicmodelcars.com',
  '1',
  '1002',
  'VP Sales'),
 ('1076',
  'Firrelli',
  'Jeff',
  'x9273',
  'jfirrelli@classicmodelcars.com',
  '1',
  '1002',
  'VP Marketing'),
 ('1088',
  'Patterson',
  'William',
  'x4871',
  'wpatterson@classicmodelcars.com',
  '6',
  '1056',
  'Sales Manager (APAC)'),
 ('1102',
  'Bondur',
  'Gerard',
  'x5408',
  'gbondur@classicmodelcars.com',
  '4',
  '1056',
  'Sale Manager (EMEA)')]
```

## Wrapping Results into Pandas DataFrames

Often, a more convenient output will be to turn these results into pandas DataFrames. One way to do this would be to wrap the `c.fetchall()` output with a pandas DataFrame constructor:

```python
import pandas as pd
```

```python
df = pd.DataFrame(cur.execute(first_five_employees_query).fetchall())
df
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      0 1 2 3 4 5 6 7     0 1002 Murphy Diane x5800 dmurphy@classicmodelcars.com 1  President   1 1056 Patterson Mary x4611 mpatterso@classicmodelcars.com 1 1002 VP Sales   2 1076 Firrelli Jeff x9273 jfirrelli@classicmodelcars.com 1 1002 VP Marketing   3 1088 Patterson William x4871 wpatterson@classicmodelcars.com 6 1056 Sales Manager (APAC)   4 1102 Bondur Gerard x5408 gbondur@classicmodelcars.com 4 1056 Sale Manager (EMEA)

Sadly as you can see this is slightly clunky as we do not have the column names. Pandas just automatically assigns the numbers 0 through 7.

We can access the column names by calling `cur.description`, like so:

```python
cur.description
```

```python
(('employeeNumber', None, None, None, None, None, None),
 ('lastName', None, None, None, None, None, None),
 ('firstName', None, None, None, None, None, None),
 ('extension', None, None, None, None, None, None),
 ('email', None, None, None, None, None, None),
 ('officeCode', None, None, None, None, None, None),
 ('reportsTo', None, None, None, None, None, None),
 ('jobTitle', None, None, None, None, None, None))
```

Then using a list comprehension, assign the column names after we instantiate the dataframe:

```python
df.columns = [x[0] for x in cur.description]
df
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      employeeNumber lastName firstName extension email officeCode reportsTo jobTitle     0 1002 Murphy Diane x5800 dmurphy@classicmodelcars.com 1  President   1 1056 Patterson Mary x4611 mpatterso@classicmodelcars.com 1 1002 VP Sales   2 1076 Firrelli Jeff x9273 jfirrelli@classicmodelcars.com 1 1002 VP Marketing   3 1088 Patterson William x4871 wpatterson@classicmodelcars.com 6 1056 Sales Manager (APAC)   4 1102 Bondur Gerard x5408 gbondur@classicmodelcars.com 4 1056 Sale Manager (EMEA)

Even better, there is a pandas method directly designed for reading from SQL databases ([documentation here](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html)). Instead of using the cursor, all you need is the connection variable:

```python
pd.read_sql(first_five_employees_query, conn)
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      employeeNumber lastName firstName extension email officeCode reportsTo jobTitle     0 1002 Murphy Diane x5800 dmurphy@classicmodelcars.com 1  President   1 1056 Patterson Mary x4611 mpatterso@classicmodelcars.com 1 1002 VP Sales   2 1076 Firrelli Jeff x9273 jfirrelli@classicmodelcars.com 1 1002 VP Marketing   3 1088 Patterson William x4871 wpatterson@classicmodelcars.com 6 1056 Sales Manager (APAC)   4 1102 Bondur Gerard x5408 gbondur@classicmodelcars.com 4 1056 Sale Manager (EMEA)

It is still useful to be aware of the cursor construct in case you ever need to develop Python code that fetches one result at a time, or is a command other than `SELECT`. But in general if you know that the end result is creating a pandas dataframe to display the result, you don't really need to interface with the cursor directly.

Note that we can also use `SELECT` to select only certain columns, and those will be reflected in the dataframe column names:

```python
pd.read_sql("""SELECT lastname, firstName FROM employees;""", conn)
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      lastName firstName     0 Murphy Diane   1 Patterson Mary   2 Firrelli Jeff   3 Patterson William   4 Bondur Gerard   5 Bow Anthony   6 Jennings Leslie   7 Thompson Leslie   8 Firrelli Julie   9 Patterson Steve   10 Tseng Foon Yue   11 Vanauf George   12 Bondur Loui   13 Hernandez Gerard   14 Castillo Pamela   15 Bott Larry   16 Jones Barry   17 Fixter Andy   18 Marsh Peter   19 King Tom   20 Nishi Mami   21 Kato Yoshimi   22 Gerard Martin

## The `WHERE` Clause

Now that we have the general syntax down, let's try for some more complex queries!

In general, the `WHERE` clause filters `SELECT` query results by some condition.

### Selecting Customers from a Specific City

Note that because the query is surrounded by triple quotes (`"""`) we can use single quotes (`'`) around the string literals within the query, e.g. `'Boston'`. You need to put quotes around strings in SQL just like you do in Python, so that it is interpreted as a string and not a variable name.

```python
pd.read_sql("""SELECT * FROM customers WHERE city = 'Boston';""", conn)
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      customerNumber customerName contactLastName contactFirstName phone addressLine1 addressLine2 city state postalCode country salesRepEmployeeNumber creditLimit     0 362 Gifts4AllAges.com Yoshido Juri 6175559555 8616 Spinnaker Dr.  Boston MA 51003 USA 1216 41900.00   1 495 Diecast Collectables Franco Valarie 6175552555 6251 Ingle Ln.  Boston MA 51003 USA 1188 85100.00

### Selecting Multiple Cities

As you are starting to see, you can also combine multiple conditions.

```python
pd.read_sql("""SELECT * FROM customers WHERE city = 'Boston' OR city = 'Madrid';""", conn)
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      customerNumber customerName contactLastName contactFirstName phone addressLine1 addressLine2 city state postalCode country salesRepEmployeeNumber creditLimit     0 141 Euro+ Shopping Channel Freyre Diego (91) 555 94 44 C/ Moralzarzal, 86  Madrid  28034 Spain 1370 227600.00   1 237 ANG Resellers Camino Alejandra (91) 745 6555 Gran Vía, 1  Madrid  28001 Spain  0.00   2 344 CAF Imports Fernandez Jesus +34 913 728 555 Merchants House 27-30 Merchant's Quay Madrid  28023 Spain 1702 59600.00   3 362 Gifts4AllAges.com Yoshido Juri 6175559555 8616 Spinnaker Dr.  Boston MA 51003 USA 1216 41900.00   4 458 Corrida Auto Replicas, Ltd Sommer Martín (91) 555 22 82 C/ Araquil, 67  Madrid  28023 Spain 1702 104600.00   5 465 Anton Designs, Ltd. Anton Carmen +34 913 728555 c/ Gobelas, 19-1 Urb. La Florida  Madrid  28023 Spain  0.00   6 495 Diecast Collectables Franco Valarie 6175552555 6251 Ingle Ln.  Boston MA 51003 USA 1188 85100.00

## The `ORDER BY` and `LIMIT` Clauses

Two additional keywords that you can use to refine your searches are the `ORDER BY` and `LIMIT` clauses.

The `ORDER BY` clause allows you to sort the results by a particular feature. For example, you could sort by the `customerName` column if you wished to get results in alphabetical order.

By default, `ORDER BY` is ascending. So, to continue the previous example, if you want the customers in reverse alphabetical order, use the additional parameter `DESC` immediately after whatever you are ordering by.

Finally, the limit clause is typically the last argument in a SQL query and simply limits the output to a set number of results, as seen with the employee data above. This is especially useful when you are performing initial data exploration and do not need to see thousands or millions of results.

### Selecting Specific Columns with Complex Criteria

This query demonstrates essentially all of the SQL features we have covered so far. It is asking for the number, name, city, and credit limit for all customers located in Boston or Madrid whose credit limit is above 50,000.00. Then it sorts by the credit limit and limits to the top 15 results.

```python
complex_query = """
SELECT customerNumber, customerName, city, creditLimit
FROM customers
WHERE (city = 'Boston' OR city = 'Madrid') AND (creditLimit >= 50000.00)
ORDER BY creditLimit DESC
LIMIT 15
;"""
df = pd.read_sql(complex_query, conn)
df
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      customerNumber customerName city creditLimit     0 495 Diecast Collectables Boston 85100.00   1 344 CAF Imports Madrid 59600.00   2 362 Gifts4AllAges.com Boston 41900.00   3 141 Euro+ Shopping Channel Madrid 227600.00   4 458 Corrida Auto Replicas, Ltd Madrid 104600.00   5 237 ANG Resellers Madrid 0.00   6 465 Anton Designs, Ltd. Madrid 0.00

You might notice that the output of this query doesn't seem to respect our credit limit criterion. There are results here where the credit limit is *not* over 50,000.00.

A little investigation shows that this is because the number is actually stored as a string!

```python
df["creditLimit"].iloc[0]
```

```python
'85100.00'
```

```python
print(df["creditLimit"].dtype)
```

```python
object
```

Let's do some additional investigation to figure out what happened.

One additional technique we can use to understand the schema of a SQLITE table is the `PRAGMA` `table_info` command. You can read more about it in the [SQLite docs](https://www.sqlite.org/pragma.html#pragma_table_info). Essentially it shows you the full schema of a given table:

```python
pd.read_sql("""PRAGMA table_info(customers)""", conn, index_col="cid")
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      name type notnull dflt_value pk   cid          0 customerNumber  0 None 0   1 customerName  0 None 0   2 contactLastName  0 None 0   3 contactFirstName  0 None 0   4 phone  0 None 0   5 addressLine1  0 None 0   6 addressLine2  0 None 0   7 city  0 None 0   8 state  0 None 0   9 postalCode  0 None 0   10 country  0 None 0   11 salesRepEmployeeNumber  0 None 0   12 creditLimit  0 None 0

According to this, none of the columns actually have a data type specified (the `type` column is empty) and none of the columns is marked as the primary key (`pk` column). SQLite is defaulting to treating them like strings — even `creditLimit`, which we clearly want to treat as a number — because the schema doesn't specify their types.

This is an annoying problem to encounter and also underlines the importance of setting up a database in an appropriate manner at the get-go. Sometimes you will encounter an issue like this and you won't be able to do all of the desired filtering in SQL, and instead will need to use pandas or some other technique for your final analysis.

### Bonus: Database Administration

In this case, you have full control over the database since it's just a file on disk, on a computer you control. You can do some database administration and make a correctly-typed copy of `creditLimit` called `creditLimitNumeric`, so that the above complex query works.

***Important note:*** it is okay if you don't understand this part. Much of the time, data scientists are only given read access (so they can write `SELECT` queries) and are not responsible for database administration. This is just to give an example of what it takes to fix a database that is not set up correctly.

First, note that because all of our queries so far have been `SELECT` queries, we still have not made any changes. It's a good idea to keep track of these attributes of `conn` as you attempt to perform any database administration.

```python
print("Uncommitted changes:", conn.in_transaction)
print("Total changes:", conn.total_changes)
```

```python
Uncommitted changes: False
Total changes: 0
```

Now we can write a query that will alter the database structure (adding a new column `creditLimitNumeric`):

```python
add_column = """
ALTER TABLE customers
ADD COLUMN creditLimitNumeric REAL;
"""
cur.execute(add_column)
```

```python

```

Then copy all of the `creditLimit` values to the new `creditLimitNumeric` column:

```python
fill_values = """
UPDATE customers
SET creditLimitNumeric = creditLimit
;
"""
cur.execute(fill_values)
```

```python

```

Now if we check the attributes of `conn`, we do have some uncommitted changes:

```python
print("Uncommitted changes:", conn.in_transaction)
print("Total changes:", conn.total_changes)
```

```python
Uncommitted changes: True
Total changes: 122
```

So we need to commit them:

```python
conn.commit()
```

```python
print("Uncommitted changes:", conn.in_transaction)
print("Total changes:", conn.total_changes)
```

```python
Uncommitted changes: False
Total changes: 122
```

Now we can look at our table info again:

```python
pd.read_sql("""PRAGMA table_info(customers)""", conn, index_col="cid")
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      name type notnull dflt_value pk   cid          0 customerNumber  0 None 0   1 customerName  0 None 0   2 contactLastName  0 None 0   3 contactFirstName  0 None 0   4 phone  0 None 0   5 addressLine1  0 None 0   6 addressLine2  0 None 0   7 city  0 None 0   8 state  0 None 0   9 postalCode  0 None 0   10 country  0 None 0   11 salesRepEmployeeNumber  0 None 0   12 creditLimit  0 None 0   13 creditLimitNumeric REAL 0 None 0

Ok, all the way at the bottom we see there is a column `creditLimitNumeric` with `type` of `REAL` (the SQLite name for floating point values). Let's try our complex query again:

```python
# query edited to refer to creditLimitNumeric
complex_query = """
SELECT customerNumber, customerName, city, creditLimitNumeric
FROM customers
WHERE (city = 'Boston' OR city = 'Madrid') AND (creditLimitNumeric >= 50000.00)
ORDER BY creditLimitNumeric DESC
LIMIT 15
;"""
df = pd.read_sql(complex_query, conn)
df
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      customerNumber customerName city creditLimitNumeric     0 141 Euro+ Shopping Channel Madrid 227600.0   1 458 Corrida Auto Replicas, Ltd Madrid 104600.0   2 495 Diecast Collectables Boston 85100.0   3 344 CAF Imports Madrid 59600.0

```python
print(df['creditLimitNumeric'].dtype)
```

```python
float64
```

It worked!

Note that this was a fairly conservative, cautious approach to editing the database. We could have dumped the entire contents into a temp database, then read them back in with the appropriate schema, if we wanted to keep the name `creditLimit` while also setting the appropriate data type. But that kind of operation carries more risk compared to making a copy like this. Most of the time as a data scientist (not a database administrator), these are the kinds of changes you want to make: not true administrative overhauls, but just enough modification so that your query will work how you need it to.

Now we can go ahead and close our database connection. Similar to working with CSV or JSON files, it is mainly important to close the connection if you are writing data to the file/database, but it's a best practice to close it regardless.

```python
conn.close()
```

## Summary

In this lesson, you saw how to connect to a SQL database via Python and how to subsequently execute queries against that database. Going forward, you'll continue to learn additional keywords for specifying your query parameters!

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
- `data.sqlite` — supporting data/helper file for the exercise.
