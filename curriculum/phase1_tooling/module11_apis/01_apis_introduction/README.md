# APIs - Introduction

> Part of **Topic 9: APIs** · source item type: WikiPage

---
One of the many ways you'll find yourself accessing data as a professional data scientist is via APIs (Application Programming Interfaces). Typically, you'll send a request and get some data back, often in JSON or XML format. In this section, you'll get some hands-on experience retrieving and working with data provided by a range of different APIs.

## Introduction to APIs

In this section, we'll provide a conceptual introduction to various kinds of APIs and some of the reasons that businesses create them.

### The Client Server Model

We then look at the basic model of "clients" and "servers" to provide a framework for thinking about how your "client" retrieves information from an API "server".

### The Request/Response Cycle

Next, we'll look at the fundamental mechanism by which web-based APIs are typically accessed - sending an HTTP request and then processing the response provided by the server. We'll also get a little experience working with HTTP requests using the Python `.get()` method within the `requests` package. We also get some hands-on experience retrieving information from NASA using [Open Notify](http://open-notify.org/).

### APIs and OAuth

Usually, access to a given API is limited to avoid abuse. One of the most common mechanisms for identifying your API requests to make sure they fit within acceptable usage guidelines is OAuth - Open Authorization - a standard for authorizing clients across web requests. In this section, we'll provide an overview of what OAuth is and how it works by looking at how it is implemented by Dropbox.

### Working with the Yelp API

Next, we'll get some practice working with a real API, retrieving information from the Yelp API.

### Creating Interactive Maps with Folium

We wrap up the section by creating interactive maps with Folium. In the cumulative lab, you will obtain data from the Yelp API to display it on an interactive map.

## Summary

Many companies provide access to their data via an API, so being able to connect to and work with data provided via an API is a critical skill as a professional data scientist!

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
