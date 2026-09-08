# Data Analysis in Base Python - Recap

> Part of **Topic 3: Data Analysis in Base Python** · source item type: WikiPage

---
## Introduction

In this section, you started by learning about how Python code interacts with files, and how to use the `open` built-in function to read data from files on disk into Python objects in memory. Then you learned about the CSV and JSON formats for serializing data, and how to use the built-in `csv` and `json` Python modules to parse and extract data from files using those formats.

## Key Takeaways

### Base Python

While there are many popular third-party libraries used for data analysis with Python, you can create simple, powerful analyses with just the built-in language data types and modules. When working with data in base Python:

- Data is stored in familiar data structures such as lists and dictionaries, which are often nested
- Analysis is performed using familiar control structures such as `for` loops and `if` statements
- Files are opened using the `open` built-in function, and CSV or JSON files are parsed using the built-in `csv` or `json` modules

### Loading Data from Files

As you were initially learning to work with Python, you often used Python variables that were declared in the code of a Jupyter Notebook, manipulated using that code, then never existed again after that notebook was shut down. These are variables "in memory". In many cases data scientists will want to work with larger data files that are saved after the code is finished running. This is data "on disk". Python has built-in functionality to facilitate communication between variables in memory and files on disk.

Key takeaways:

- Variables **in memory** are the current active variables in your code, which go away if you shut down the kernel or shut down your computer
- Files **on disk** are the things you see printed out when you type `ls` in the terminal, which persist when you shut down the kernel or shut down your computer
- There is no concept like "editing" when working with files in Python. You are either reading from the first line to the last line of the file (sometimes all at once), or writing lines one after another
- In Python, the typical way to interact with these files is to use the `open` built-in function
  - The first step is identifying the path to the file, which is a string and represents the relative path from the current code execution context to the location of the file on the computer. It is represented as `path_to_file` in the examples below
  - To open a file for reading, that looks like: `python with open(path_to_file) as f: # Read data from file object f `
  - To open a file for writing, that looks like: `python with open(path_to_file, "w") as f: # Write data to the file object f `
  - The `with...:` syntax means that the file is automatically closed after the `with` block ends. If you use the syntax `f = open(path_to_file)` instead, you also need to call `f.close()` when you are finished working with the file
  - You will find that some third-party libraries handle opening and closing the files for you. In this case, you only need to identify the file path and do not need to call `open` and `.close` yourself
  - The `open` function assumes that you are working with a file encoded as plain text, such as an unstructured `.txt` file, CSV file, or JSON file. If you are working with a file encoded as bytes, such as a JPEG image, you need to specify a mode of `"rb"` to read or `"wb"` to write when you call `open`

### CSV

The CSV format stands for "comma-separated values". It is possibly the most common data serialization format used by data scientists, and we will use it very frequently in this course.

Key takeaways:

- CSV is a file format. The file names typically end with the extension `.csv`
- CSV is a **plain text** format. This means that it is encoded as text that is readable without specialized software, and you can explore the contents using VS Code, Vim, or any other general-purpose editor
- CSV is a **delimited** format. This means that there are characters in the text of the file that are intended to separate the pieces of data from one another
  - As you might assume from the name, the most common delimiter is a comma. A line of comma-delimited CSV content representing four pieces of data might look like: ` 10,2,1.5,"Firstname Lastname" `
  - It is also possible to use some other delimiter. One of the most common is a tab `\t`, to the extent that there is a name "TSV" (tab-separated values) for that specific kind of file. You could also use a pipe `|`, semicolon `;`, or really any other character as long as the markup is consistent and the code knows how to interpret it. Technically all of these files would still be referred to as CSVs, even though the delimiter is not a comma

- In Python, we can use the `csv` module to parse data from CSV files ([documentation here](https://docs.python.org/3/library/csv.html))
  - If the data file does not contain headings, the `csv.reader` function works well. It will return a reader iterable that produces a Python list for each row of the file. There is a matching `csv.writer` option for writing data to files rather than reading data from files
  - If the data file does contain headings, the `csv.DictReader` class works well. It will use a reader iterable that produces a Python dictionary for each row of the file. There is a matching `csv.DictWriter` option

### JSON

The JSON format stands for "JavaScript object notation". It is a widely-adopted format for storing and transferring data between applications, particularly on the web.

Key takeaways:

- JSON is a file format. The file names typically end with the extension `.json`
- JSON is a **plain text** format, like CSV
- The markup of JSON is more complex than CSV. While it typically does contain comma delimiters, it can also contain square brackets (`[` and `]`) and curly braces (`{` and `}`).
  - For example, the same line represented as CSV above might look like this in JSON: ` [10, 2, 1.5, "Firstname Lastname"] `
  - Unlike CSV (which mainly works for "flat" tabular data) it is also possible to store nested data with JSON. For example, this comes from the `json` docs: ` ["foo", {"bar": ["baz", null, 1.0, 2]}] `

- In Python, we can use the `json` module to parse data from JSON files ([documentation here](https://docs.python.org/3/library/json.html))
  - Typically you will want to load the entire file contents at once using `json.load`
  - You can also use `json.dump` to serialize an object in memory and write it to a file on disk

## Conclusion

A major part of data science is loading the data, and you just learned the fundamental building blocks of how to do this with Python! In future sections we will cover additional libraries and data formats, but you already have the knowledge to dig up interesting data sets and use Python to answer questions about the data.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
