# Scraping Images

> Part of **Topic 10: HTML, CSS and Web Scraping** · source item type: Assignment

---
## Introduction

You've definitely started to hone your skills at scraping now! With that, let's look at another data format you're apt to want to pull from the web: images! In this lesson, you'll see how to save images from the web as well as display them in a Pandas DataFrame for easy perusal!

## Objectives

You will be able to:

- Select specific elements from HTML using Beautiful Soup

- Identify and scrape images from a web page

## Grabbing an HTML Page

Start with the same page that you've been working with: books.toscrape.com.

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book-section.png)

```python
from bs4 import BeautifulSoup
import requests
```

```python
html_page = requests.get('http://books.toscrape.com/') # Make a get request to retrieve the page
soup = BeautifulSoup(html_page.content, 'html.parser') # Pass the page contents to beautiful soup for parsing
warning = soup.find('div', class_="alert alert-warning")
book_container = warning.nextSibling.nextSibling
```

## Finding Images

First, simply retrieve a list of images by searching for `img` tags with beautiful soup:

```python
images = book_container.findAll('img')
ex_img = images[0] # Preview an entry
ex_img
```

```python

![A Light in the Attic](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg)

```

```python
# Use tab complete to preview what types of methods are available for the entry
# ex_img.
```

```python
# While there's plenty of other methods to explore, simply select the url for the image for now.
ex_img.attrs['src']
```

```python
'media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg'
```

## Saving Images

Great! Now that you have a URL (well, a URL extension to be more precise) you can download the image locally!

```python
import shutil
```

```python
url_base = "http://books.toscrape.com/"
url_ext = ex_img.attrs['src']
full_url = url_base + url_ext
r = requests.get(full_url, stream=True)
if r.status_code == 200:
    with open("images/book1.jpg", 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
```

## Showing Images in the File Directory

You can also run a simple bash command in a standalone cell to preview that the image is indeed there:

```python
ls images/
```

```python
book-section.png  book14.jpg        book2.jpg         book7.jpg
book1.jpg         book15.jpg        book20.jpg        book8.jpg
book10.jpg        book16.jpg        book3.jpg         book9.jpg
book11.jpg        book17.jpg        book4.jpg
book12.jpg        book18.jpg        book5.jpg
book13.jpg        book19.jpg        book6.jpg
```

## Previewing an Individual Image

```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
```

```python
img = mpimg.imread('images/book1.jpg')
imgplot = plt.imshow(img)
plt.show()
```

![png](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/index_files/index_15_0.png)

## Displaying Images in Pandas DataFrames

You can even display images within a pandas DataFrame by using a little HTML yourself!

```python
import pandas as pd
from IPython.display import Image, HTML
```

```python
row1 = [ex_img.attrs['alt'], '

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book1.jpg)
']
df = pd.DataFrame(row1).transpose()
df.columns = ['title', 'cover']
HTML(df.to_html(escape=False))
```
     title cover     0 A Light in the Attic

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book1.jpg)

## All Together Now

```python
data = []
for n, img in enumerate(images):
    url_base = "http://books.toscrape.com/"
    url_ext = img.attrs['src']
    full_url = url_base + url_ext
    r = requests.get(full_url, stream=True)
    path = "images/book{}.jpg".format(n+1)
    title = img.attrs['alt']
    if r.status_code == 200:
        with open(path, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
        row = [title, '

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/{})
'.format(path)]
        data.append(row)
df = pd.DataFrame(data)
print('Number of rows: ', len(df))
df.columns = ['title', 'cover']
HTML(df.to_html(escape=False))
```

```python
Number of rows:  20
```
     title cover     0 A Light in the Attic

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book1.jpg)
   1 Tipping the Velvet

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book2.jpg)
   2 Soumission

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book3.jpg)
   3 Sharp Objects

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book4.jpg)
   4 Sapiens: A Brief History of Humankind

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book5.jpg)
   5 The Requiem Red

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book6.jpg)
   6 The Dirty Little Secrets of Getting Your Dream Job

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book7.jpg)
   7 The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book8.jpg)
   8 The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book9.jpg)
   9 The Black Maria

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book10.jpg)
   10 Starving Hearts (Triangular Trade Trilogy, #1)

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book11.jpg)
   11 Shakespeare's Sonnets

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book12.jpg)
   12 Set Me Free

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book13.jpg)
   13 Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book14.jpg)
   14 Rip it Up and Start Again

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book15.jpg)
   15 Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book16.jpg)
   16 Olio

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book17.jpg)
   17 Mesaerion: The Best Science Fiction Stories 1800-1849

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book18.jpg)
   18 Libertarianism for Beginners

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book19.jpg)
   19 It's Only the Himalayas

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-scraping-images/master/images/book20.jpg)

## Summary

Voila! You now know how to use your knowledge of HTML and Beautiful Soup to scrape images. You really are turning into a scraping champion! Now, go get scraping!

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
