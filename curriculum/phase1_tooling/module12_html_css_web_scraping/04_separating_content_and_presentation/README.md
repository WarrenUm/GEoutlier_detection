# Separating Content and Presentation

> Part of **Topic 10: HTML, CSS and Web Scraping** · source item type: WikiPage

---
## Introduction

You now know what HTML is and have explored a properly-formatted HTML document. That said, if you look at the HTML pages thus far, you can't help but notice that they look a little plain. To make them more attractive (and responsive), you can use Cascading Style Sheets or CSS!

## Objectives

You will be able to:

- Identify the separation of content and presentation


- Explain the role of CSS

## Identify the Separation of Content and Presentation

HTML lets you mark-up your content with semantic *structure*. It forms the skeleton of your web page. It would be great to be able to say, "Browser, when you see a `p` tag with `id` of `my-name`, make the first letter be huge!" Or, to get your readers' attention, you might say, "Browser, if you see *any* tag with a `class` of `warning` surround it with a red box!" HTML authors believe that *creating* marked-up documents and *styling* marked-up documents are entirely separate tasks. They see a difference between writing *content* (the data within the HTML document) and specifying *presentation*, the rules for displaying the rendered elements.

## Explain the Role of CSS

CSS, or "Cascading Style Sheets," tells you how to write rules that define how browsers will present HTML. Rules in CSS won't look like HTML and they usually live in a file apart from our HTML file.

CSS handles all of the ways you want to customize your content's look and feel from margins and colors, to column-based layout!

## Additional Resources

- [CSS Guidelines: The Separation of Concerns](https://cssguidelin.es/#the-separation-of-concerns)
- [CSS Zen Garden](http://www.csszengarden.com/)

## Summary

Web developers separate the content of our HTML pages from their presentation, which they style with CSS. By keeping the two separate, you not only utilize the best tools for each job, but you can change code for one without disturbing the code for the other.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
