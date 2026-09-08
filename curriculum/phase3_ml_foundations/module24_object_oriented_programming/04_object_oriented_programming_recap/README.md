# Object-Oriented Programming - Recap

> Part of **Topic 21: Object-Oriented Programming** · source item type: WikiPage

---
## Introduction

In this section, you learned about Object-oriented programming (OOP) as a foundational practice for software development and programming.

## OOP overview

You now know all about OOP and how to define classes. Like functions, using classes in your programming can save you a lot of time by eliminating repetitive tasks. Classes go further than functions by allowing you to persist data. After all, class methods are fairly analogous to functions, while attributes add functionality by acting as data storage containers.

## Class structure

As you saw, the most basic class definition starts off with:

```python
class ClassName:
```

From there, you then saw how you can further define class methods:

```python
class ClassName:
    def method_1(self):
        pass # Ideally a method does something, but you get the point
    def method_2(self):
        print('This is a pretty useless second method.')
```

You also learned about `self`. Specifically, that `self` is the default parameter used to define methods. This is necessary since instance methods implicitly pass in the object itself as an argument during execution.

## Creating instances

Recall that after you define a class, you can then create instances of that class to bring it to life and use it! You're probably wondering what all of this has to do with data science. In turns out you'll use OOP principles when you start working with common data science libraries. For example, you might import the `LinearRegression` class from the scikit-learn library in order to create a regression model!

Remember, creating an instance of a class would look like this:

```python
# Import class definition
from sklearn.linear_model import LinearRegression()

# Create an instance of the class
reg = LinearRegression()
```

Once you create an instance object of the class, you can then use all the methods associated with that class!

## Level up

If you would like to dive deeper into OOP and learn some advanced topics, you can check out the additional OOP lessons and labs in the Appendix.

## Summary

Congrats, you now have a solid foundation in OOP! You first learned how to define a class and methods. Then you learned how to create an instance of a class and define instance attributes. These skills will be useful for collaboration and writing concise, modular code!

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
