# Web Scraping in Practice

> Part of **Topic 10: HTML, CSS and Web Scraping** · source item type: Assignment

---
## Introduction

Now that you've gotten a brief introduction to Beautiful Soup and how to select various elements from a web page, it's time to practice scraping a website. You'll start to see that scraping is a dynamic process that involves investigating the web page(s) at hand and developing scripts tailored to those structures.

## Objectives

You will be able to:

- Navigate HTML documents using Beautiful Soup's children and sibling relations

- Select specific elements from HTML using Beautiful Soup
- Use regular expressions to extract items with a certain pattern within Beautiful Soup
- Determine the pagination scheme of a website and scrape multiple pages

```python
from bs4 import BeautifulSoup
import requests
```

## Grabbing an HTML Page

To start, here's how to retrieve an arbitrary web page and load its content into Beautiful Soup for parsing. You first use the requests package to pull the HTML itself and then pass that data to beautiful soup.

```python
html_page = requests.get('http://books.toscrape.com/') # Make a get request to retrieve the page
soup = BeautifulSoup(html_page.content, 'html.parser') # Pass the page contents to beautiful soup for parsing
```

## Previewing the Structure

While it's apt to be too much information to effectively navigate, taking a quick peek into the structure of the HTML page is always a good idea.

```python
soup.prettify
```

```python

<br />    All products | Books to Scrape - Sandbox<br />

[Books to Scrape](index.html) We love being scraped!

-
[Home](index.html)

- All products

-

[Books](catalogue/category/books_1/index.html)

  -

[Travel](catalogue/category/books/travel_2/index.html)

  -

[Mystery](catalogue/category/books/mystery_3/index.html)

  -

[Historical Fiction](catalogue/category/books/historical-fiction_4/index.html)

  -

[Sequential Art](catalogue/category/books/sequential-art_5/index.html)

  -

[Classics](catalogue/category/books/classics_6/index.html)

  -

[Philosophy](catalogue/category/books/philosophy_7/index.html)

  -

[Romance](catalogue/category/books/romance_8/index.html)

  -

[Womens Fiction](catalogue/category/books/womens-fiction_9/index.html)

  -

[Fiction](catalogue/category/books/fiction_10/index.html)

  -

[Childrens](catalogue/category/books/childrens_11/index.html)

  -

[Religion](catalogue/category/books/religion_12/index.html)

  -

[Nonfiction](catalogue/category/books/nonfiction_13/index.html)

  -

[Music](catalogue/category/books/music_14/index.html)

  -

[Default](catalogue/category/books/default_15/index.html)

  -

[Science Fiction](catalogue/category/books/science-fiction_16/index.html)

  -

[Sports and Games](catalogue/category/books/sports-and-games_17/index.html)

  -

[Add a comment](catalogue/category/books/add-a-comment_18/index.html)

  -

[Fantasy](catalogue/category/books/fantasy_19/index.html)

  -

[New Adult](catalogue/category/books/new-adult_20/index.html)

  -

[Young Adult](catalogue/category/books/young-adult_21/index.html)

  -

[Science](catalogue/category/books/science_22/index.html)

  -

[Poetry](catalogue/category/books/poetry_23/index.html)

  -

[Paranormal](catalogue/category/books/paranormal_24/index.html)

  -

[Art](catalogue/category/books/art_25/index.html)

  -

[Psychology](catalogue/category/books/psychology_26/index.html)

  -

[Autobiography](catalogue/category/books/autobiography_27/index.html)

  -

[Parenting](catalogue/category/books/parenting_28/index.html)

  -

[Adult Fiction](catalogue/category/books/adult-fiction_29/index.html)

  -

[Humor](catalogue/category/books/humor_30/index.html)

  -

[Horror](catalogue/category/books/horror_31/index.html)

  -

[History](catalogue/category/books/history_32/index.html)

  -

[Food and Drink](catalogue/category/books/food-and-drink_33/index.html)

  -

[Christian Fiction](catalogue/category/books/christian-fiction_34/index.html)

  -

[Business](catalogue/category/books/business_35/index.html)

  -

[Biography](catalogue/category/books/biography_36/index.html)

  -

[Thriller](catalogue/category/books/thriller_37/index.html)

  -

[Contemporary](catalogue/category/books/contemporary_38/index.html)

  -

[Spirituality](catalogue/category/books/spirituality_39/index.html)

  -

[Academic](catalogue/category/books/academic_40/index.html)

  -

[Self Help](catalogue/category/books/self-help_41/index.html)

  -

[Historical](catalogue/category/books/historical_42/index.html)

  -

[Christian](catalogue/category/books/christian_43/index.html)

  -

[Suspense](catalogue/category/books/suspense_44/index.html)

  -

[Short Stories](catalogue/category/books/short-stories_45/index.html)

  -

[Novels](catalogue/category/books/novels_46/index.html)

  -

[Health](catalogue/category/books/health_47/index.html)

  -

[Politics](catalogue/category/books/politics_48/index.html)

  -

[Cultural](catalogue/category/books/cultural_49/index.html)

  -

[Erotica](catalogue/category/books/erotica_50/index.html)

  -

[Crime](catalogue/category/books/crime_51/index.html)

# All products

**1000** results - showing **1** to **20**.

**Warning!** This is a demo website for web scraping purposes. Prices and ratings here were randomly assigned and have no real meaning.

1.

![A Light in the Attic](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg)

**
**
**
**
**

### [A Light in the ...](catalogue/a-light-in-the-attic_1000/index.html)

£51.77

**

        In stock

Add to basket

2.

![Tipping the Velvet](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/26/0c/260c6ae16bce31c8f8c95daddd9f4a1c.jpg)

**
**
**
**
**

### [Tipping the Velvet](catalogue/tipping-the-velvet_999/index.html)

£53.74

**

        In stock

Add to basket

3.

![Soumission](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/3e/ef/3eef99c9d9adef34639f510662022830.jpg)

**
**
**
**
**

### [Soumission](catalogue/soumission_998/index.html)

£50.10

**

        In stock

Add to basket

4.

![Sharp Objects](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/32/51/3251cf3a3412f53f339e42cac2134093.jpg)

**
**
**
**
**

### [Sharp Objects](catalogue/sharp-objects_997/index.html)

£47.82

**

        In stock

Add to basket

5.

![Sapiens: A Brief History of Humankind](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/be/a5/bea5697f2534a2f86a3ef27b5a8c12a6.jpg)

**
**
**
**
**

### [Sapiens: A Brief History ...](catalogue/sapiens-a-brief-history-of-humankind_996/index.html)

£54.23

**

        In stock

Add to basket

6.

![The Requiem Red](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/68/33/68339b4c9bc034267e1da611ab3b34f8.jpg)

**
**
**
**
**

### [The Requiem Red](catalogue/the-requiem-red_995/index.html)

£22.65

**

        In stock

Add to basket

7.

![The Dirty Little Secrets of Getting Your Dream Job](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/92/27/92274a95b7c251fea59a2b8a78275ab4.jpg)

**
**
**
**
**

### [The Dirty Little Secrets ...](catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html)

£33.34

**

        In stock

Add to basket

8.

![The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/3d/54/3d54940e57e662c4dd1f3ff00c78cc64.jpg)

**
**
**
**
**

### [The Coming Woman: A ...](catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html)

£17.93

**

        In stock

Add to basket

9.

![The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/66/88/66883b91f6804b2323c8369331cb7dd1.jpg)

**
**
**
**
**

### [The Boys in the ...](catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html)

£22.60

**

        In stock

Add to basket

10.

![The Black Maria](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/58/46/5846057e28022268153beff6d352b06c.jpg)

**
**
**
**
**

### [The Black Maria](catalogue/the-black-maria_991/index.html)

£52.15

**

        In stock

Add to basket

11.

![Starving Hearts (Triangular Trade Trilogy, #1)](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/be/f4/bef44da28c98f905a3ebec0b87be8530.jpg)

**
**
**
**
**

### [Starving Hearts (Triangular Trade ...](catalogue/starving-hearts-triangular-trade-trilogy-1_990/index.html)

£13.99

**

        In stock

Add to basket

12.

![Shakespeare's Sonnets](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/10/48/1048f63d3b5061cd2f424d20b3f9b666.jpg)

**
**
**
**
**

### [Shakespeare's Sonnets](catalogue/shakespeares-sonnets_989/index.html)

£20.66

**

        In stock

Add to basket

13.

![Set Me Free](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/5b/88/5b88c52633f53cacf162c15f4f823153.jpg)

**
**
**
**
**

### [Set Me Free](catalogue/set-me-free_988/index.html)

£17.46

**

        In stock

Add to basket

14.

![Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/94/b1/94b1b8b244bce9677c2f29ccc890d4d2.jpg)

**
**
**
**
**

### [Scott Pilgrim's Precious Little ...](catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html)

£52.29

**

        In stock

Add to basket

15.

![Rip it Up and Start Again](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/81/c4/81c4a973364e17d01f217e1188253d5e.jpg)

**
**
**
**
**

### [Rip it Up and ...](catalogue/rip-it-up-and-start-again_986/index.html)

£35.02

**

        In stock

Add to basket

16.

![Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/54/60/54607fe8945897cdcced0044103b10b6.jpg)

**
**
**
**
**

### [Our Band Could Be ...](catalogue/our-band-could-be-your-life-scenes-from-the-american-indie-underground-1981-1991_985/index.html)

£57.25

**

        In stock

Add to basket

17.

![Olio](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/55/33/553310a7162dfbc2c6d19a84da0df9e1.jpg)

**
**
**
**
**

### [Olio](catalogue/olio_984/index.html)

£23.88

**

        In stock

Add to basket

18.

![Mesaerion: The Best Science Fiction Stories 1800-1849](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/09/a3/09a3aef48557576e1a85ba7efea8ecb7.jpg)

**
**
**
**
**

### [Mesaerion: The Best Science ...](catalogue/mesaerion-the-best-science-fiction-stories-1800-1849_983/index.html)

£37.59

**

        In stock

Add to basket

19.

![Libertarianism for Beginners](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/0b/bc/0bbcd0a6f4bcd81ccb1049a52736406e.jpg)

**
**
**
**
**

### [Libertarianism for Beginners](catalogue/libertarianism-for-beginners_982/index.html)

£51.33

**

        In stock

Add to basket

20.

![It's Only the Himalayas](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/27/a5/27a53d0bb95bdd88288eaf66c9230d7e.jpg)

**
**
**
**
**

### [It's Only the Himalayas](catalogue/its-only-the-himalayas_981/index.html)

£45.17

**

        In stock

Add to basket

-

                Page 1 of 50

- [next](catalogue/page-2.html)

>
```

## Using the Inspect Element Feature

As you can see, there's a lot going on in a production level HTML page. Rather than tediously scrolling through all of this, you'll typically have specific information you're looking to pull from a page. For example, the page you've just loaded is a mock online bookstore used for scraping practice. (As noted in the previous lesson, be careful what you attempt to scrape and at what rate/volume; many websites will quickly blacklist you if you attempt to make too many requests.) For this page, you'll see how to programmatically extract the book names, cover images, and price. Once you have a goal in mind, you can ctrl+click (Windows: right click) on the portion of the page that you're interested in and select inspect element. This will bring up the developer's portion of your web browser and allow you to preview the underlying HTML code.

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/images/inspect.png)

This will also reveal underlying `divs`, `headers` and other containers the web designers have used to organize their web pages.

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/images/book-section.png)

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/images/book_img.png)

## Selecting a Container

While you're eventually looking to select each of the individual books, it's often easier to start with an encapsulating container. In this case, the `section` displayed above. Once you select this container, you can then make sub-selections within it to find the relevant information you are searching for. In this case, the warning just above the div for the books is easy to identify. You can start by selecting this element and then navigating to the next div element.

```python
warning = soup.find('div', class_="alert alert-warning")
warning # Previewing is optional but can help you verify you are selecting what you think you are
```

```python
**Warning!** This is a demo website for web scraping purposes. Prices and ratings here were randomly assigned and have no real meaning.
```

## Traversing the Soup

Now, you can navigate to the section using the next sibling method. (In actuality you need to use nextSibling twice in this case.)

```python
# This code is a bit brittle but works for now; in general, ask, are you confident that this will work for all pages?
book_container = warning.nextSibling.nextSibling
book_container
```

```python

1.

![A Light in the Attic](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg)

**
**
**
**
**

### [A Light in the ...](catalogue/a-light-in-the-attic_1000/index.html)

£51.77

**

        In stock

Add to basket

2.

![Tipping the Velvet](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/26/0c/260c6ae16bce31c8f8c95daddd9f4a1c.jpg)

**
**
**
**
**

### [Tipping the Velvet](catalogue/tipping-the-velvet_999/index.html)

£53.74

**

        In stock

Add to basket

3.

![Soumission](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/3e/ef/3eef99c9d9adef34639f510662022830.jpg)

**
**
**
**
**

### [Soumission](catalogue/soumission_998/index.html)

£50.10

**

        In stock

Add to basket

4.

![Sharp Objects](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/32/51/3251cf3a3412f53f339e42cac2134093.jpg)

**
**
**
**
**

### [Sharp Objects](catalogue/sharp-objects_997/index.html)

£47.82

**

        In stock

Add to basket

5.

![Sapiens: A Brief History of Humankind](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/be/a5/bea5697f2534a2f86a3ef27b5a8c12a6.jpg)

**
**
**
**
**

### [Sapiens: A Brief History ...](catalogue/sapiens-a-brief-history-of-humankind_996/index.html)

£54.23

**

        In stock

Add to basket

6.

![The Requiem Red](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/68/33/68339b4c9bc034267e1da611ab3b34f8.jpg)

**
**
**
**
**

### [The Requiem Red](catalogue/the-requiem-red_995/index.html)

£22.65

**

        In stock

Add to basket

7.

![The Dirty Little Secrets of Getting Your Dream Job](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/92/27/92274a95b7c251fea59a2b8a78275ab4.jpg)

**
**
**
**
**

### [The Dirty Little Secrets ...](catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html)

£33.34

**

        In stock

Add to basket

8.

![The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/3d/54/3d54940e57e662c4dd1f3ff00c78cc64.jpg)

**
**
**
**
**

### [The Coming Woman: A ...](catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html)

£17.93

**

        In stock

Add to basket

9.

![The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/66/88/66883b91f6804b2323c8369331cb7dd1.jpg)

**
**
**
**
**

### [The Boys in the ...](catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html)

£22.60

**

        In stock

Add to basket

10.

![The Black Maria](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/58/46/5846057e28022268153beff6d352b06c.jpg)

**
**
**
**
**

### [The Black Maria](catalogue/the-black-maria_991/index.html)

£52.15

**

        In stock

Add to basket

11.

![Starving Hearts (Triangular Trade Trilogy, #1)](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/be/f4/bef44da28c98f905a3ebec0b87be8530.jpg)

**
**
**
**
**

### [Starving Hearts (Triangular Trade ...](catalogue/starving-hearts-triangular-trade-trilogy-1_990/index.html)

£13.99

**

        In stock

Add to basket

12.

![Shakespeare's Sonnets](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/10/48/1048f63d3b5061cd2f424d20b3f9b666.jpg)

**
**
**
**
**

### [Shakespeare's Sonnets](catalogue/shakespeares-sonnets_989/index.html)

£20.66

**

        In stock

Add to basket

13.

![Set Me Free](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/5b/88/5b88c52633f53cacf162c15f4f823153.jpg)

**
**
**
**
**

### [Set Me Free](catalogue/set-me-free_988/index.html)

£17.46

**

        In stock

Add to basket

14.

![Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/94/b1/94b1b8b244bce9677c2f29ccc890d4d2.jpg)

**
**
**
**
**

### [Scott Pilgrim's Precious Little ...](catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html)

£52.29

**

        In stock

Add to basket

15.

![Rip it Up and Start Again](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/81/c4/81c4a973364e17d01f217e1188253d5e.jpg)

**
**
**
**
**

### [Rip it Up and ...](catalogue/rip-it-up-and-start-again_986/index.html)

£35.02

**

        In stock

Add to basket

16.

![Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/54/60/54607fe8945897cdcced0044103b10b6.jpg)

**
**
**
**
**

### [Our Band Could Be ...](catalogue/our-band-could-be-your-life-scenes-from-the-american-indie-underground-1981-1991_985/index.html)

£57.25

**

        In stock

Add to basket

17.

![Olio](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/55/33/553310a7162dfbc2c6d19a84da0df9e1.jpg)

**
**
**
**
**

### [Olio](catalogue/olio_984/index.html)

£23.88

**

        In stock

Add to basket

18.

![Mesaerion: The Best Science Fiction Stories 1800-1849](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/09/a3/09a3aef48557576e1a85ba7efea8ecb7.jpg)

**
**
**
**
**

### [Mesaerion: The Best Science ...](catalogue/mesaerion-the-best-science-fiction-stories-1800-1849_983/index.html)

£37.59

**

        In stock

Add to basket

19.

![Libertarianism for Beginners](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/0b/bc/0bbcd0a6f4bcd81ccb1049a52736406e.jpg)

**
**
**
**
**

### [Libertarianism for Beginners](catalogue/libertarianism-for-beginners_982/index.html)

£51.33

**

        In stock

Add to basket

20.

![It's Only the Himalayas](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/media/cache/27/a5/27a53d0bb95bdd88288eaf66c9230d7e.jpg)

**
**
**
**
**

### [It's Only the Himalayas](catalogue/its-only-the-himalayas_981/index.html)

£45.17

**

        In stock

Add to basket

-

                Page 1 of 50

- [next](catalogue/page-2.html)

```

Now that you have the master container with all of the books of interest, you can then search within this smaller block to extract the relevant information. If you take a look at the preview above, you should see that each of the books is referenced twice: first as a simple link via an `a` tag and then again nested within an `h3` tag. You could, therefore, select all of the `a` tags and simply extract every other block of code, although this could be brittle and prone to error. A more reliable method would be to select only the `img` tags or only the `h3` tags. As you are starting to see, web scraping is a back and forth process of investigating a page and generalizing its structure.

Generally, this is best done with a little trial and error: make a selection, preview it, and continue slicing down until you have what you're after.

```python
titles = book_container.findAll('h3') # Make a selection
titles[0] # Preview the first entry it
```

```python

### [A Light in the ...](catalogue/a-light-in-the-attic_1000/index.html)
```

Looks like you need to further slice into these `h3` tags:

```python
titles[0].find('a')
```

```python
[A Light in the ...](catalogue/a-light-in-the-attic_1000/index.html)
```

Closer. Once you make it down to a single tag that's not nested, you can use the `.attrs` attribute to pull up a dictionary of the tag's attributes. In this case, you're looking for the title:

```python
titles[0].find('a').attrs['title']
```

```python
'A Light in the Attic'
```

Great! Now that you've done some exploration to find what you were after, you can formalize the process and put it all together.

```python
final_titles = [h3.find('a').attrs['title'] for h3 in book_container.findAll('h3')]
print(len(final_titles), final_titles[:5])
```

```python
20 ['A Light in the Attic', 'Tipping the Velvet', 'Soumission', 'Sharp Objects', 'Sapiens: A Brief History of Humankind']
```

## Passing Regular Expressions

Another useful feature is passing a regular expression (regex) into a Find statement. A regex is a sequence of characters that is used to search and match specific patterns of text. Think about the find feature of a web browser or text editor. Regex syntax is a bit complicated and you will learn all about it later. For now, try to follow along with the example below keeping in mind that the regex is matching a specific pattern of text.

Going back to our book example, you may have noticed that the star ratings for each of the books are encapsulated within a `p` tag whose class reads "star-rating ...". Let's take a look at how you could extract these features.

```python
import re
```

```python
regex = re.compile("star-rating (.*)")
book_container.findAll('p', {"class" : regex}) # Initial Trial in developing the script
```

```python
[

 **
 **
 **
 **
 **
 ,

 **
 **
 **
 **
 **
 ,

 **
 **
 **
 **
 **
 ,

 **
 **
 **
 **
 **
 ,

 **
 **
 **
 **
 **
 ,

 **
 **
 **
 **
 **
 ,

 **
 **
 **
 **
 **
 ,

 **
 **
 **
 **
 **
 ,

 **
 **
 **
 **
 **
 ,

 **
 **
 **
 **
 **
 ,

 **
 **
 **
 **
 **
 ,

 **
 **
 **
 **
 **
 ,

 **
 **
 **
 **
 **
 ,

 **
 **
 **
 **
 **
 ,

 **
 **
 **
 **
 **
 ,

 **
 **
 **
 **
 **
 ,

 **
 **
 **
 **
 **
 ,

 **
 **
 **
 **
 **
 ,

 **
 **
 **
 **
 **
 ,

 **
 **
 **
 **
 **
 ]
```

As you can see, as before, you need to navigate a little further in order to remove the extraneous information.

```python
star_ratings = []
for p in book_container.findAll('p', {"class" : regex}):
    star_ratings.append(p.attrs['class'][-1])
star_ratings
```

```python
['Three',
 'One',
 'One',
 'Four',
 'Five',
 'One',
 'Four',
 'Three',
 'Four',
 'One',
 'Two',
 'Four',
 'Five',
 'Five',
 'Five',
 'Three',
 'One',
 'One',
 'Two',
 'Two']
```

As you can see, even here we have strings whereas integers would probably be a more useful representation so you may still have to do some further data transformations.

```python
star_dict = {'One': 1, 'Two': 2, 'Three':3, 'Four': 4, 'Five':5} # Manually create a dictionary to translate to numeric
star_ratings = [star_dict[s] for s in star_ratings]
star_ratings
```

```python
[3, 1, 1, 4, 5, 1, 4, 3, 4, 1, 2, 4, 5, 5, 5, 3, 1, 1, 2, 2]
```

## Further Practice

You're definitely making some progress here! Let's take a look at extracting two more pieces of information: the price and availability.

```python
book_container.findAll('p', class_="price_color") # First preview
```

```python
[

£51.77,

£53.74,

£50.10,

£47.82,

£54.23,

£22.65,

£33.34,

£17.93,

£22.60,

£52.15,

£13.99,

£20.66,

£17.46,

£52.29,

£35.02,

£57.25,

£23.88,

£37.59,

£51.33,

£45.17]
```

```python
prices = [p.text for p in book_container.findAll('p', class_="price_color")] # Keep cleaning it up
print(len(prices), prices[:5])
```

```python
20 ['£51.77', '£53.74', '£50.10', '£47.82', '£54.23']
```

```python
prices = [float(p[1:]) for p in prices] # Removing the pound sign and converting to float
print(len(prices), prices[:5])
```

```python
20 [51.77, 53.74, 50.1, 47.82, 54.23]
```

Hopefully, the process is starting to feel a bit smoother.

```python
avails = book_container.findAll('p', class_="instock availability")
avails[:5] # Preview our selection
```

```python
[

 **

         In stock

 ,

 **

         In stock

 ,

 **

         In stock

 ,

 **

         In stock

 ,

 **

         In stock

 ]
```

```python
avails[0].text # Dig a little deeper into the structure
```

```python
'\n\n    \n        In stock\n    \n'
```

```python
avails = [a.text.strip() for a in book_container.findAll('p', class_="instock availability")] # Finalize the selection
print(len(avails), avails[:5])
```

```python
20 ['In stock', 'In stock', 'In stock', 'In stock', 'In stock']
```

## Putting it All Together

Now that you have the relevant information, it's time to put it all together into a dataset!

```python
import pandas as pd
```

```python
df = pd.DataFrame([final_titles, star_ratings, prices, avails]).transpose()
df.columns = ['Title', 'Star_Rating', 'Price_(pounds)', 'Availability']
df
```
   .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; }      Title Star_Rating Price_(pounds) Availability     0 A Light in the Attic 3 51.77 In stock   1 Tipping the Velvet 1 53.74 In stock   2 Soumission 1 50.1 In stock   3 Sharp Objects 4 47.82 In stock   4 Sapiens: A Brief History of Humankind 5 54.23 In stock   5 The Requiem Red 1 22.65 In stock   6 The Dirty Little Secrets of Getting Your Dream... 4 33.34 In stock   7 The Coming Woman: A Novel Based on the Life of... 3 17.93 In stock   8 The Boys in the Boat: Nine Americans and Their... 4 22.6 In stock   9 The Black Maria 1 52.15 In stock   10 Starving Hearts (Triangular Trade Trilogy, #1) 2 13.99 In stock   11 Shakespeare's Sonnets 4 20.66 In stock   12 Set Me Free 5 17.46 In stock   13 Scott Pilgrim's Precious Little Life (Scott Pi... 5 52.29 In stock   14 Rip it Up and Start Again 5 35.02 In stock   15 Our Band Could Be Your Life: Scenes from the A... 3 57.25 In stock   16 Olio 1 23.88 In stock   17 Mesaerion: The Best Science Fiction Stories 18... 1 37.59 In stock   18 Libertarianism for Beginners 2 51.33 In stock   19 It's Only the Himalayas 2 45.17 In stock

## Pagination and URL Hacking

Now that you have successfully scraped one page of books, the next logical step is to extrapolate this to successive pages. In general, the two most common approaches are to search for a button that will take you to the next page or to investigate the structure of the page URLs. For example, at the bottom of the page you should see a button like this:

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-web-scraping-in-practice/master/images/pager.png)

As you can see, this portion contains a link to the next page of the book listings. What's more, is that you can also see that the next pages are easy to anticipate the URL for. They're simply:

- [http://books.toscrape.com/catalogue/page-2.html](http://books.toscrape.com/catalogue/page-2.html)
- [http://books.toscrape.com/catalogue/page-3.html](http://books.toscrape.com/catalogue/page-3.html)
- [http://books.toscrape.com/catalogue/page-4.html](http://books.toscrape.com/catalogue/page-4.html)
- etc.

In more complex examples, you would simply have to use selections such as those for the title, price, star rating and availability to retrieve the URL of the next page. However, in simple cases like this, it is possible to simply hardwire the page URLs in a `for` loop. In the upcoming lab, you'll formalize this knowledge by writing a script to scrape all 50 pages from the site. The pseudo-code will look something like this:

```python
df = pd.DataFrame()
for i in range(2,51):
    url = "http://books.toscrape.com/catalogue/page-{}.html".format(i)
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.content, 'html.parser')
    warning = soup.find('div', class_="alert alert-warning")
    book_container = warning.nextSibling.nextSibling
    new_titles = retrieve_titles(book_container)
    new_star_ratings = retrieve_ratings(book_container)
    new_prices = retrieve_prices(book_container)
    new_avails = retrieve_avails(book_container)
    ...
```

## Summary

Well done! In this lesson, you took a look at some methods for traversing and dissecting a web page with Beautiful Soup! You also got some practice selecting specific elements from HTML and scraping multiple pages. In the upcoming lab, you'll continue to formalize this, turning the current script into modularized functions which you can then use to scrape all of the information from all 50 pages of the book listings.

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
