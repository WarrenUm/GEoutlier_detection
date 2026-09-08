# Importing Data Using Pandas

> Part of **Topic 4: Data Analysis in Pandas** · source item type: Assignment

---
## Introduction

Pandas is a popular library for efficiently wrangling data. It is particularly optimized to work with two-dimensional tabular data that is organized in rows and columns. In this lesson, you will learn how to import tabular data as a Pandas DataFrame object, how to access and manipulate the data in DataFrame objects, and how to export DataFrames to some common file formats.

For more information on Pandas, refer to [https://pandas.pydata.org/pandas-docs/stable/](https://pandas.pydata.org/pandas-docs/stable/) .

## Objectives

You will be able to:

- Use pandas to import data from a CSV and and an Excel spreadsheet

 - Use pandas to export a DataFrame to a file

## Loading Pandas

When importing Pandas, it is standard to import it under the alias `pd`

```python
import pandas as pd
```

## Importing Data

There are a few main functions for importing data into a Pandas DataFrame including:

- `pd.read_csv()`
- `pd.read_excel()`
- `pd.read_json()`
- `pd.DataFrame.from_dict()`

Most of these functions are fairly straightforward; you use `read_csv()` for csv files, `read_excel()` for excel files (both new and old `.xlx` and `.xlsx` formats), and `read_json()` for json files. That said, there are a few nuances you should know about. The first is that the `read_csv()` format can be used for any plain-text delimited file. This may include (but is not limited to) pipe (|) delimited files (`.psv`) and tab separated files (`.tsv`).

Let's look at an example by investigating a file, `'bp.txt'`, stored in the `Data` folder.

```python
# Import 'bp.txt' file
df = pd.read_csv('Data/bp.txt', delimiter='\t')
```

We've now loaded the data from a file into a DataFrame. To investigate the DataFrame, we can use a method called `.head(n)` or `.tail(n)`, which will respectively return first and last **n** items in the DataFrame.

```python
# Look at the first 3 rows
df.head(3)
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      Pt BP Age Weight BSA Dur Pulse Stress     0 1 105 47 85.4 1.75 5.1 63 33   1 2 115 49 94.2 2.10 3.8 70 14   2 3 116 49 95.3 1.98 8.2 72 10

```python
# Look at the last 4 rows
df.tail(4)
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      Pt BP Age Weight BSA Dur Pulse Stress     16 17 106 46 87.0 1.87 3.6 62 18   17 18 113 46 94.5 1.90 4.3 70 12   18 19 110 48 90.5 1.88 9.0 71 99   19 20 122 56 95.7 2.09 7.0 75 99

This example shows that the data was tab delimited (`\t`), so an appropriate file extension could have also been `.tsv`. Once we've loaded the dataset, we can export it to any format we would like with the related methods:

- `df.to_csv()`
- `df.to_excel()`
- `df.to_json()`
- `df.to_dict()`

There are also several other options available, but these are the most common.

## Skipping and Limiting Rows

Another feature that you may have to employ is skipping rows when there is metadata stored at the top of a file. You can do this using the optional parameter `skiprows`. Similarly, if you want to only load a portion of a large file as an initial preview, you can use the `nrows` parameter.

```python
# Import the first 100 rows of 'ACS_16_5YR_B24011_with_ann.csv' file
df = pd.read_csv('Data/ACS_16_5YR_B24011_with_ann.csv', nrows=100)

# Look at the first five rows
df.head()
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      GEO.id GEO.id2 GEO.display-label HD01_VD01 HD02_VD01 HD01_VD02 HD02_VD02 HD01_VD03 HD02_VD03 HD01_VD04 ... HD01_VD32 HD02_VD32 HD01_VD33 HD02_VD33 HD01_VD34 HD02_VD34 HD01_VD35 HD02_VD35 HD01_VD36 HD02_VD36     0 Id Id2 Geography Estimate; Total: Margin of Error; Total: Estimate; Total: - Management, business, scien... Margin of Error; Total: - Management, business... Estimate; Total: - Management, business, scien... Margin of Error; Total: - Management, business... Estimate; Total: - Management, business, scien... ... Estimate; Total: - Natural resources, construc... Margin of Error; Total: - Natural resources, c... Estimate; Total: - Production, transportation,... Margin of Error; Total: - Production, transpor... Estimate; Total: - Production, transportation,... Margin of Error; Total: - Production, transpor... Estimate; Total: - Production, transportation,... Margin of Error; Total: - Production, transpor... Estimate; Total: - Production, transportation,... Margin of Error; Total: - Production, transpor...   1 0500000US01001 01001 Autauga County, Alabama 33267 2306 48819 1806 55557 4972 63333 ... 31402 5135 35594 3034 36059 3893 47266 13608 19076 4808   2 0500000US01003 01003 Baldwin County, Alabama 31540 683 49524 1811 57150 6980 63422 ... 35603 3882 30549 1606 29604 4554 35504 6260 24182 3580   3 0500000US01005 01005 Barbour County, Alabama 26575 1653 41652 2638 51797 5980 52775 ... 37847 11189 26094 4884 25339 4900 37282 6017 16607 3497   4 0500000US01007 01007 Bibb County, Alabama 30088 2224 40787 2896 50069 12841 67917 ... 45952 5622 28983 3401 31881 2317 26580 2901 23479 4942

5 rows × 75 columns

### Notice the first row is descriptions of the variables

We could manually remove:

```python
# Delete the first row
df = df.drop(0)
df.head(2)
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      GEO.id GEO.id2 GEO.display-label HD01_VD01 HD02_VD01 HD01_VD02 HD02_VD02 HD01_VD03 HD02_VD03 HD01_VD04 ... HD01_VD32 HD02_VD32 HD01_VD33 HD02_VD33 HD01_VD34 HD02_VD34 HD01_VD35 HD02_VD35 HD01_VD36 HD02_VD36     1 0500000US01001 01001 Autauga County, Alabama 33267 2306 48819 1806 55557 4972 63333 ... 31402 5135 35594 3034 36059 3893 47266 13608 19076 4808   2 0500000US01003 01003 Baldwin County, Alabama 31540 683 49524 1811 57150 6980 63422 ... 35603 3882 30549 1606 29604 4554 35504 6260 24182 3580

2 rows × 75 columns

Or if we knew from the start, we could use the skiprows argument:

```python
# Import the first 100 rows of 'ACS_16_5YR_B24011_with_ann.csv' file while skipping the first row
df = pd.read_csv('Data/ACS_16_5YR_B24011_with_ann.csv', skiprows=1, nrows=100)
df.head()
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      Id Id2 Geography Estimate; Total: Margin of Error; Total: Estimate; Total: - Management, business, science, and arts occupations: Margin of Error; Total: - Management, business, science, and arts occupations: Estimate; Total: - Management, business, science, and arts occupations: - Management, business, and financial occupations: Margin of Error; Total: - Management, business, science, and arts occupations: - Management, business, and financial occupations: Estimate; Total: - Management, business, science, and arts occupations: - Management, business, and financial occupations: - Management occupations ... Estimate; Total: - Natural resources, construction, and maintenance occupations: - Installation, maintenance, and repair occupations Margin of Error; Total: - Natural resources, construction, and maintenance occupations: - Installation, maintenance, and repair occupations Estimate; Total: - Production, transportation, and material moving occupations: Margin of Error; Total: - Production, transportation, and material moving occupations: Estimate; Total: - Production, transportation, and material moving occupations: - Production occupations Margin of Error; Total: - Production, transportation, and material moving occupations: - Production occupations Estimate; Total: - Production, transportation, and material moving occupations: - Transportation occupations Margin of Error; Total: - Production, transportation, and material moving occupations: - Transportation occupations Estimate; Total: - Production, transportation, and material moving occupations: - Material moving occupations Margin of Error; Total: - Production, transportation, and material moving occupations: - Material moving occupations     0 0500000US01001 1001 Autauga County, Alabama 33267 2306 48819 1806 55557 4972 63333 ... 31402 5135 35594 3034 36059 3893 47266 13608 19076 4808   1 0500000US01003 1003 Baldwin County, Alabama 31540 683 49524 1811 57150 6980 63422 ... 35603 3882 30549 1606 29604 4554 35504 6260 24182 3580   2 0500000US01005 1005 Barbour County, Alabama 26575 1653 41652 2638 51797 5980 52775 ... 37847 11189 26094 4884 25339 4900 37282 6017 16607 3497   3 0500000US01007 1007 Bibb County, Alabama 30088 2224 40787 2896 50069 12841 67917 ... 45952 5622 28983 3401 31881 2317 26580 2901 23479 4942   4 0500000US01009 1009 Blount County, Alabama 34900 2063 46593 2963 47003 6189 50991 ... 42489 7176 32969 3767 31814 4551 41375 5280 26755 2963

5 rows × 75 columns

## Header

Related to `skiprows` is the `header` parameter. This specifies the row where column names are and starts importing data from that point:

```python
# Look at the error output once you run this cell. What type of error is it?
df = pd.read_csv('Data/ACS_16_5YR_B24011_with_ann.csv', header=1)
df.head()
```

```python
---------------------------------------------------------------------------

UnicodeDecodeError                        Traceback (most recent call last)

pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._convert_tokens()

pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._convert_with_dtype()

pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._string_convert()

pandas/_libs/parsers.pyx in pandas._libs.parsers._string_box_utf8()

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 2: invalid continuation byte

During handling of the above exception, another exception occurred:

UnicodeDecodeError                        Traceback (most recent call last)

 in
      1 # look at the error output once you run this cell. What type of error is it?
----> 2 df = pd.read_csv('Data/ACS_16_5YR_B24011_with_ann.csv', header=1)
      3 df.head()

//anaconda3/lib/python3.7/site-packages/pandas/io/parsers.py in parser_f(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, dialect, tupleize_cols, error_bad_lines, warn_bad_lines, delim_whitespace, low_memory, memory_map, float_precision)
    700                     skip_blank_lines=skip_blank_lines)
    701
--> 702         return _read(filepath_or_buffer, kwds)
    703
    704     parser_f.__name__ = name

//anaconda3/lib/python3.7/site-packages/pandas/io/parsers.py in _read(filepath_or_buffer, kwds)
    433
    434     try:
--> 435         data = parser.read(nrows)
    436     finally:
    437         parser.close()

//anaconda3/lib/python3.7/site-packages/pandas/io/parsers.py in read(self, nrows)
   1137     def read(self, nrows=None):
   1138         nrows = _validate_integer('nrows', nrows)
-> 1139         ret = self._engine.read(nrows)
   1140
   1141         # May alter columns / col_dict

//anaconda3/lib/python3.7/site-packages/pandas/io/parsers.py in read(self, nrows)
   1993     def read(self, nrows=None):
   1994         try:
-> 1995             data = self._reader.read(nrows)
   1996         except StopIteration:
   1997             if self._first_chunk:

pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader.read()

pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._read_low_memory()

pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._read_rows()

pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._convert_column_data()

pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._convert_tokens()

pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._convert_with_dtype()

pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._string_convert()

pandas/_libs/parsers.pyx in pandas._libs.parsers._string_box_utf8()

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 2: invalid continuation byte
```

## Encoding

Encoding errors like the one above are always frustrating. This has to do with how the strings within the file itself are formatted. The most common encoding other than `utf-8` that you are likely to come across is `latin-1`.

```python
# Import the 'ACS_16_5YR_B24011_with_ann.csv' file using a proper encoding
df = pd.read_csv('Data/ACS_16_5YR_B24011_with_ann.csv', header=1, encoding='latin-1')
df.head()
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      Id Id2 Geography Estimate; Total: Margin of Error; Total: Estimate; Total: - Management, business, science, and arts occupations: Margin of Error; Total: - Management, business, science, and arts occupations: Estimate; Total: - Management, business, science, and arts occupations: - Management, business, and financial occupations: Margin of Error; Total: - Management, business, science, and arts occupations: - Management, business, and financial occupations: Estimate; Total: - Management, business, science, and arts occupations: - Management, business, and financial occupations: - Management occupations ... Estimate; Total: - Natural resources, construction, and maintenance occupations: - Installation, maintenance, and repair occupations Margin of Error; Total: - Natural resources, construction, and maintenance occupations: - Installation, maintenance, and repair occupations Estimate; Total: - Production, transportation, and material moving occupations: Margin of Error; Total: - Production, transportation, and material moving occupations: Estimate; Total: - Production, transportation, and material moving occupations: - Production occupations Margin of Error; Total: - Production, transportation, and material moving occupations: - Production occupations Estimate; Total: - Production, transportation, and material moving occupations: - Transportation occupations Margin of Error; Total: - Production, transportation, and material moving occupations: - Transportation occupations Estimate; Total: - Production, transportation, and material moving occupations: - Material moving occupations Margin of Error; Total: - Production, transportation, and material moving occupations: - Material moving occupations     0 0500000US01001 1001 Autauga County, Alabama 33267 2306 48819 1806 55557 4972 63333 ... 31402 5135 35594 3034 36059 3893 47266 13608 19076 4808   1 0500000US01003 1003 Baldwin County, Alabama 31540 683 49524 1811 57150 6980 63422 ... 35603 3882 30549 1606 29604 4554 35504 6260 24182 3580   2 0500000US01005 1005 Barbour County, Alabama 26575 1653 41652 2638 51797 5980 52775 ... 37847 11189 26094 4884 25339 4900 37282 6017 16607 3497   3 0500000US01007 1007 Bibb County, Alabama 30088 2224 40787 2896 50069 12841 67917 ... 45952 5622 28983 3401 31881 2317 26580 2901 23479 4942   4 0500000US01009 1009 Blount County, Alabama 34900 2063 46593 2963 47003 6189 50991 ... 42489 7176 32969 3767 31814 4551 41375 5280 26755 2963

5 rows × 75 columns

## Selecting Specific Columns

You can also select specific columns if you only want to load specific features.

```python
# Import the file with specific columns
df = pd.read_csv('Data/ACS_16_5YR_B24011_with_ann.csv',
                 usecols=[0, 1, 2, 5, 6], encoding='latin-1')
df.head(2)
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      GEO.id GEO.id2 GEO.display-label HD01_VD02 HD02_VD02     0 Id Id2 Geography Estimate; Total: - Management, business, scien... Margin of Error; Total: - Management, business...   1 0500000US01001 01001 Autauga County, Alabama 48819 1806

**or**

```python
# Import the file with specific columns
df = pd.read_csv('Data/ACS_16_5YR_B24011_with_ann.csv', usecols=['GEO.id', 'GEO.id2'], encoding='latin-1')
df.head(2)
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      GEO.id GEO.id2     0 Id Id2   1 0500000US01001 01001

## Selecting Specific Sheets

You can also select specific sheets for Excel files! This can be done by index number.

```python
# Import an Excel file
df1 = pd.read_excel('Data/Yelp_Selected_Businesses.xlsx', header=2)
df1.head()
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      business_id cool date funny review_id stars text useful user_id     0 RESDUcs7fIiihp38-d6_6g 0 2015-09-16 0 gkcPdbblTvZDMSwx8nVEKw 5 Got here early on football Sunday 7:30am as I ... 0 SKteB5rgDlkkUa1Zxe1N0Q   1 RESDUcs7fIiihp38-d6_6g 0 2017-09-09 0 mQfl6ci46mu0xaZrkRUhlA 5 This buffet is amazing. Yes, it is expensive,... 0 f638AHA_GoHbyDB7VFMz7A   2 RESDUcs7fIiihp38-d6_6g 0 2013-01-14 0 EJ7DJ8bm7-2PLFB9WKx4LQ 3 I was really looking forward to this but it wa... 0 -wVPuTiIEG85LwTK46Prpw   3 RESDUcs7fIiihp38-d6_6g 0 2017-02-08 0 lMarDJDg4-e_0YoJOKJoWA 2 This place....lol our server was nice. But fo... 0 A21zMqdN76ueLZFpmbue0Q   4 RESDUcs7fIiihp38-d6_6g 0 2012-11-19 0 nq_-8lZPUVGomDEP5OOj1Q 1 After hearing all the buzz about this place, I... 2 Jf1EXieUV7F7s-HGA4EsdA

```python
# Import a specific sheet of an Excel file
df2 = pd.read_excel('Data/Yelp_Selected_Businesses.xlsx', sheet_name=2, header=2)
df2.head()
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      business_id cool date funny review_id stars text useful user_id     0 YJ8ljUhLsz6CtT_2ORNFmg 1 2013-04-25 0 xgUz0Ck4_ciNaeIk-H8GBQ 5 I loved this place. Easily the most hipsters p... 1 6cpo8iqgnW3jnozhmY7eAA   1 YJ8ljUhLsz6CtT_2ORNFmg 0 2014-07-07 0 Au7MG4QlAxqq9meyKSQmaw 5 So my boyfriend and I came here for my birthda... 0 8bFE3u1dMoYXkS7ORqlssw   2 YJ8ljUhLsz6CtT_2ORNFmg 0 2015-12-04 0 8IQnZ54nenXjlK-FGZ82Bg 5 I really enjoyed their food. Went there for th... 1 bJmE1ms0MyZ6KHjmfZDWGw   3 YJ8ljUhLsz6CtT_2ORNFmg 2 2016-07-06 1 XY42LMhKoXzwtLoku4mvLA 5 A complete Vegas experience. We arrived right ... 3 PbccpC-I-8rxzF2bCDh8YA   4 YJ8ljUhLsz6CtT_2ORNFmg 0 2014-04-15 0 1xlYVWhyLedoA0HddOJMOw 4 Very great atmosphere had a wonderful bartende... 0 yvlRColhqo_4TzpUFKyroA

Or the name of the sheet itself

```python
# Import a specific sheet of an Excel file
df = pd.read_excel('Data/Yelp_Selected_Businesses.xlsx', sheet_name='Biz_id_RESDU', header=2)
df.head()
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      business_id cool date funny review_id stars text useful user_id     0 RESDUcs7fIiihp38-d6_6g 0 2015-09-16 0 gkcPdbblTvZDMSwx8nVEKw 5 Got here early on football Sunday 7:30am as I ... 0 SKteB5rgDlkkUa1Zxe1N0Q   1 RESDUcs7fIiihp38-d6_6g 0 2017-09-09 0 mQfl6ci46mu0xaZrkRUhlA 5 This buffet is amazing. Yes, it is expensive,... 0 f638AHA_GoHbyDB7VFMz7A   2 RESDUcs7fIiihp38-d6_6g 0 2013-01-14 0 EJ7DJ8bm7-2PLFB9WKx4LQ 3 I was really looking forward to this but it wa... 0 -wVPuTiIEG85LwTK46Prpw   3 RESDUcs7fIiihp38-d6_6g 0 2017-02-08 0 lMarDJDg4-e_0YoJOKJoWA 2 This place....lol our server was nice. But fo... 0 A21zMqdN76ueLZFpmbue0Q   4 RESDUcs7fIiihp38-d6_6g 0 2012-11-19 0 nq_-8lZPUVGomDEP5OOj1Q 1 After hearing all the buzz about this place, I... 2 Jf1EXieUV7F7s-HGA4EsdA

## Loading a Full Workbook and Previewing Sheet Names

You can also load an entire excel workbook (which is a collection of spreadsheets) with the `pd.ExcelFile()` function.

```python
# Import the names of Excel sheets in a workbook
workbook = pd.ExcelFile('Data/Yelp_Selected_Businesses.xlsx')
workbook.sheet_names
```

```python
['Biz_id_RESDU',
 'Biz_id_4JNXU',
 'Biz_id_YJ8lj',
 'Biz_id_ujHia',
 'Biz_id_na4Th']
```

```python
# Import a specific sheet
df = workbook.parse(sheet_name=1, header=2)
df.head()
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      business_id cool date funny review_id stars text useful user_id     0 4JNXUYY8wbaaDmk3BPzlWw 0 2012-06-10 0 wl8BO_I-is-JaMwMW5c_gQ 4 I booked a table here for brunch and it did no... 0 fo4mpUqgXL2mJqALc9AvbA   1 4JNXUYY8wbaaDmk3BPzlWw 0 2012-01-20 0 cf9RrqHY9eQ9M53OPyXLtg 4 Came here for lunch after a long night of part... 0 TVvTtXwPXsvrg2KJGoOUTg   2 4JNXUYY8wbaaDmk3BPzlWw 0 2017-05-10 0 BvmhSQ6WFm2Jxu01G8OpdQ 5 Loved the fried goat cheese in tomato sauce al... 0 etbAVunw-4kwr6VTRweZpA   3 4JNXUYY8wbaaDmk3BPzlWw 0 2014-05-03 0 IoKp9n1489XohTV_-EJ0IQ 5 Love the outdoor atmosphere. Price was right, ... 0 vKXux2Xx3xcicTgYZoR0pg   4 4JNXUYY8wbaaDmk3BPzlWw 0 2014-06-04 0 7YNmSq7Lb1zi4SUKXaSjfg 5 Best steak in Vegas. Best mashed potatoes in V... 3 e3s1x4LLqfSkRTWDy_-Urg

## Saving Data

Once we have data loaded that we may want to export back out, we use the **`.to_csv()`** or **`.to_excel()`** methods of any DataFrame object.

```python
# Write data to a CSV file
# Notice how we have to pass index=False if we do not want it included in our output
df.to_csv('NewSavedView.csv', index=False)
```

```python
# Write data to an Excel file
df.to_excel('NewSavedView.xlsx')
```

## Summary

We've spent some time looking into how data importing with Pandas works and some of the methods you can use to manage the import and access of data. In the next lesson, you'll get some hands on practice!

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
