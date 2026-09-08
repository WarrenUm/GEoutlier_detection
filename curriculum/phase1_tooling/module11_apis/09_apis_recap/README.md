# APIs - Recap

> Part of **Topic 9: APIs** · source item type: WikiPage

---
## Introduction

In this section, you learned about the HTTP request/response cycle and using APIs. APIs are critical to software development, and they can be powerful tools for gathering data for data scientists.

## Key Takeaways

APIs can provide access to a wide range of data that you might need as a data scientist.

Key takeaways include:

- While there are many other kinds of APIs, as a data scientist, you'll typically be working with web APIs.
- The `requests` library in Python is a great starting point for making HTTP requests to APIs.
- Most APIs you encounter will return results in JSON format.
- The two most common HTTP methods you'll use when accessing APIs are `GET` (to retrieve information) and `POST` (to send information).
- Typically, you'll need to authenticate in some manner to gain access to most APIs - one common method for doing so is using OAuth.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
