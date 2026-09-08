# HTML Introduction

> Part of **Topic 10: HTML, CSS and Web Scraping** · source item type: WikiPage

---
## Introduction

HTML, or HyperText Markup Language, is a markup language that describes the structure and semantic meaning of web pages. Web browsers, such as Mozilla Firefox, Internet Explorer, and Google Chrome interpret the HTML code and use it to render output. Unlike Python, JavaScript and other programming languages, markup languages like HTML don't have any logic behind them. Instead, they simply surround the content to convey structure and meaning.

Every web page you've ever visited is structured using HTML code. Being able to read and understand an HTML document is an incredibly useful tool in a data scientist's toolbox.

## Objectives

You will be able to:

- Explain what HTML is and why it's important in the context of web development

- Compare and contrast HTML tags
- Create an HTML document with appropriate tags

## HTML Syntax

HTML makes use of **tags** which are interpreted by web browsers to affect how content is displayed. The `p` tag to define a paragraph is shown below:

```python

Hello World
```

Elements, like the `p` tags above, won't be displayed in the browser. Technologists might say that the tags "affect how the content is rendered by the browser."

You can also alter any number of attributes inside of the opening tags. For example, the `a` element, which is used for links, has an `href` attribute to specify the destination address of the link. If you wanted to link to [www.flatironschool.com](http://www.flatironschool.com), you could do so as follows:

```python
[Flatiron School](http://www.flatironschool.com)
```

This would render as:

[Flatiron School](http://www.flatironschool.com)

You can also nest elements inside of each other. To have a link displayed as a separate paragraph, we could nest an `a` element inside of a `p`.

```python

This [link](http://www.google.com) will be a part of a separate paragraph.
```

## Basic HTML Document Structure

All HTML documents begin with a "doctype declaration" tag, which tells the web browser which version of HTML to use. HTML is a language that is currently evolving — just like English. When you open a novel such as "Romeo and Juliet," your expectation is that the "doctype" is "Elizabethan English." In the same way "Elizabethan English" has changed to a more modern form, HTML 1.0 was *essentially* the same as modern HTML5 but had some tags that are no longer used and was lacking some tags often used today.

Since it's not wrapping any content, the doctype declaration doesn't require a closing tag. To use HTML5, the current up-to-date version, you can simply declare `<!DOCTYPE html>`.

```python

```

Next, you add an opening and closing `html` tag. This tells the web browser to interpret everything inside the tags as HTML code.

```python

```

Every HTML page is made up of two primary sections: a `head` and a `body`. The `head` element contains metadata about the HTML document and other information for the browser, while the `body` element contains the actual content.

```python

```

## Comments

Let's also take a brief moment to recognize how to add comments into an HTML document. These won't get rendered to the browser at all: they're just helpful notes for the author.

```python

Top 5 Pizza Places in NYC
```

## Common HTML Elements

You've already looked at some common HTML elements, such as `a` and `p`. Let's take a look at some more HTML elements.

## Headers

HTML gives us access to different header elements, ranging from `h1` to `h6`, with `h1` being the largest and `h6` being the smallest.

```python

# Dogs!

### Why Dogs are Great

###### Different Breeds
```

In addition to changing how the text is displayed, search engines use headers to help determine what a web page is about. Remember when you provide *semantic* markup, machines can infer the "main points" of a page. A well structured article will generally have its principal arguments bracketed by low-number header tags -- this very document does exactly that!

## Images

You can embed images on our web pages using the `img` element. The `img` element doesn't have a closing tag. The `src` attribute tells the browser where to find the image. The `alt` attribute will be displayed if an image can't be loaded, and also describes the image to search engines.

The `alt` tag presents a moment to talk about an important principle behind [Tim Berners-Lee's vision for the Web](https://webfoundation.org/about/vision/history-of-the-web/): it is *inclusive*. If you're using assistive technologies because you have a sight impairment, it's helpful to know what's being displayed. If you're in a remote community where internet access is expensive, you might choose to disable images and only pay to download those which you *absolutely need*. So while an `img` will inject an image and "work," honoring the Web's vision for openness and inclusivity requires that you provide the `alt` tag as well.

`<img src="https://raw.githubusercontent.com/learn-co-curriculum/dsc-html-introduction/master/URL_TO_IMAGE" alt="Picture of a Dog">`

## Lists

Some other useful HTML elements are lists. You can make bulleted, or unordered lists, using opening and closing `ul` tags. Inside, you can nest a `li`, or "list item" element for each item on our list.

```python

##### My Favorite Things in No Particular Order

- Coffee

- Vinyl Records

- Pickling

```

This would render as:

---

##### My Favorite Things in No Particular Order

- Coffee
- Vinyl Records
- Pickling

---

You can also make a numbered, or ordered list, using an `ol` tag.

```python

##### Top 5 Pizza Places in NYC

1. DiFara Pizza

2. Lucali's

3. Sal and Carmine's

4. Juliana's

5. Joe's

```

Would render as:

---

##### Top 5 Pizza Places in NYC

1. DiFara Pizza
2. Lucali's
3. Sal and Carmine's
4. Juliana's
5. Joe's

---

## Summary

Welcome to the world of the web! In this lesson, you learned about HTML, why it's important in web development, and how web pages are structured. You also compared and contrasted a few common HTML tags as well as saw how tags can be used to construct HTML documents.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
