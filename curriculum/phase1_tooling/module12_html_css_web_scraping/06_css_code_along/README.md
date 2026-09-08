# CSS Code Along

> Part of **Topic 10: HTML, CSS and Web Scraping** · source item type: WikiPage

---
## Introduction

It's time to see some CSS code in action. [Codepen](https://codepen.io/) is a great tool to easily test HTML and CSS code that you'll see in practice here.

## Objectives

You will be able to:

- Use Codepen to preview and modify HTML and CSS files


- Comment and uncomment CSS and HTML

## Code Example HTML Structure

This [Pen](https://codepen.io/curiositypaths/pen/WddzQM?editors=1100) (saved Codepen document) contains an HTML document with the following structure:

- A ``[<body>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/body) element (root of the html content. In Codepen you will not see a body tag, it's implicitly present and wraps all the HTML content)
- An ``[<article>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article) tag to define our content as self-contained unit (e.g. blog post, newspaper article)
- An ``[<h1>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements) tag to wrap the `<article>`'s header text
- ``[<p>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p) tags to wrap the `<article>`'s unstructured text
- ``[<ul>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul) tags to represent unordered lists
- ``[<li>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li) tags to wrap each list item

## Code Example CSS Structure

The [Pen](https://codepen.io/curiositypaths/pen/WddzQM?editors=1100) also includes commented-out CSS Code to:

- Set the background of the `<body>` element (whole document) to `#00b3e6` (light blue)
- Sets the `<article>` element width to `700px`
- Centers the `<article>` element
- Sets the font family of the `<article>` element to `Helvetica Neue`. Alternative fonts are provided in the event `Helvetica Neue` is not available on your computer
- Set the background of the `<article>` element to `white`
- Add 30px of white space to the perimeter of the `<article>`
- Set the `font-size` to `22px` for the element with `id` `main-header`
- Set the `font-style` to `italic` for elements containing the class `perspective-questions`

## Code Along Instructions

Open the [Pen](https://codepen.io/curiositypaths/pen/WddzQM?editors=1100) in a separate browser tab to follow the code along instructions.

All the CSS code you need to successfully modify the page is already included but commented out. All you need to do is uncomment all the `CSS declarations` (`property-name`:`value`) one-by-one.

## Pen Screenshot

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-css-code-along/master/images/codepen.jpeg)

## Unstyled HTML Document Screenshot

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-css-code-along/master/images/unstyled-codepen.jpeg)

## Styled HTML Document Screenshot

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-css-code-along/master/images/styled-codepen.jpeg)

## CSS Declarations Uncommenting Steps

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-css-code-along/master/images/css-code-codepen.jpg)

## Summary

Awesome! In this code along you got to preview and practice a standard web development environment and modify CSS code! Specifically, you used Codepen to modify HTML and CSS files. You also learned how commenting/uncommenting works in CSS and HTML!

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
