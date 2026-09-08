# Introduction to Probability

> Part of **Topic 11: Combinatorics and Probability** · source item type: WikiPage

---
## Introduction

Now that you understand the basics of sets, you'll learn how this knowledge can be used to calculate your first probabilities! In this section, you'll learn how to use sets to create probabilities and you'll learn about the foundations of probability through the three probability axioms.

## Objectives

You will be able to:

- Compare experiments, outcomes, and the event space

- Calculate probabilities by using relative frequency of outcomes to event space
- Describe the three axioms of probability
- Describe the addition law of probability

## Probability Terminology

For the following examples, we will consider what happens when throwing a single 6-sided die ("die" is the singular of ["dice"](https://en.wikipedia.org/wiki/Dice)).

### Experiments and Outcomes

When you throw a die once, you can consider this a ***random experiment***. The result of this "experiment" is the ***outcome***. So, for example, the outcome could be a 2.

### Events

An ***event*** is the outcome of a particular random experiment. So, for example, "rolling the die and getting a 5" is an event.

### Sample Spaces

The ***sample space*** represents the universe of all possible outcomes. With our die rolling example, that space includes the values of 1, 2, 3, 4, 5, and 6.

### Event Spaces

The ***event space*** is a subset of the sample space. You can think of it as the collection of events we "care about" out of all possible events. For example, our event space could be "rolling a number higher than a 4", which would include the values of 5 and 6.

## Sets and Probability

As you may have noticed, we used the term "subset" to describe event spaces. Sets are a very useful way to represent the probability concepts described above. Let's expand on that now.

### Sample Spaces as Sets

Let's define the sample space for rolling a single die as the set

![image](https://render.githubusercontent.com/render/math?math=S)
 .

![image](https://render.githubusercontent.com/render/math?math=S)
 looks like this:

![image](https://render.githubusercontent.com/render/math?math=S=%20\{1,2,3,4,5,6\})

You can then say that:

-

![image](https://render.githubusercontent.com/render/math?math=S)
 defines all the possible outcomes when throwing the die once
-

![image](https://render.githubusercontent.com/render/math?math=S)
 is our universal set

![image](https://render.githubusercontent.com/render/math?math=\Omega)
 , as seen before

Other examples of sample spaces:

#### The number of text messages you send each day:

- In this case,

![image](https://render.githubusercontent.com/render/math?math=S)
 is equal to some number x, with x being a **non-negative integer**
- Mathematically, x being an integer looks like

![image](https://render.githubusercontent.com/render/math?math=x%20\in%20\mathbb{Z})
 .

![image](https://render.githubusercontent.com/render/math?math=\mathbb{Z})
 is a "special" set, containing all integers.
- x being non-negative looks like

![image](https://render.githubusercontent.com/render/math?math=x%20\geq%200)

- To represent the set of x values that meet both requirements, we'll use an additional way of defining a set, called the "set builder" notation. In set builder notation, the vertical bar

![image](https://render.githubusercontent.com/render/math?math=\mid)
 means "such that", and the conditions are separated by commas
- Our overall definition of

![image](https://render.githubusercontent.com/render/math?math=S)
 is

![image](https://render.githubusercontent.com/render/math?math=S%20=%20\{x%20\mid%20x%20\in%20\mathbb{Z},%20x%20\geq%200\})
 . In other words,

![image](https://render.githubusercontent.com/render/math?math=S)
 contains all instances of x such that x is an integer and x is greater than or equal to zero.

#### The number of hours someone watches TV each day:

- In this case, let's say that x is a **real number between 0 and 24**
- Mathematically, x being a real number (roughly equivalent to a floating point value, although there are subtle differences) looks like

![image](https://render.githubusercontent.com/render/math?math=x%20\in%20\mathbb{R})
 .

![image](https://render.githubusercontent.com/render/math?math=\mathbb{R})
 is another special set, the set of all real numbers.
- x being between 0 and 24 looks like

![image](https://render.githubusercontent.com/render/math?math=0%20\leq%20x%20\leq%2024)

- Putting that all together, we get

![image](https://render.githubusercontent.com/render/math?math=S%20=%20\{x%20\mid%20x%20\in%20\mathbb{R},%200%20\leq%20x%20\leq%2024%20\})
 . In other words,

![image](https://render.githubusercontent.com/render/math?math=S)
 contains all instances of x such that x is a real number and x is between 0 and 24.

### Event Spaces as Sets

Let's define the event space as

![image](https://render.githubusercontent.com/render/math?math=E)
 . As noted previously,

![image](https://render.githubusercontent.com/render/math?math=E%20%20\subseteq%20S)
 , i.e.

![image](https://render.githubusercontent.com/render/math?math=E)
 is a subset of

![image](https://render.githubusercontent.com/render/math?math=S)
 .

An example of

![image](https://render.githubusercontent.com/render/math?math=E)
 could be "rolling a number higher than 4". This would be written

![image](https://render.githubusercontent.com/render/math?math=E=\{5,%206\})
 .

Or if

![image](https://render.githubusercontent.com/render/math?math=E)
 were "rolling an odd number", that would be written

![image](https://render.githubusercontent.com/render/math?math=E=%20\{1,3,5\})
 .

Once

![image](https://render.githubusercontent.com/render/math?math=E)
 is defined, we can say that event

![image](https://render.githubusercontent.com/render/math?math=E)
 happened if the actual outcome after rolling the die belongs to the predefined event space

![image](https://render.githubusercontent.com/render/math?math=E)
 .

Other examples of event spaces based on previously defined sample spaces:

#### Low daily number of text messages sent:

- We can define this as 20 or fewer text messages
- The event space still includes only non-negative integers, but this time there is an upper bound of 20 also
-

![image](https://render.githubusercontent.com/render/math?math=E%20=%20\{x%20\mid%20x%20\in%20\mathbb{Z},%200%20\leq%20x%20\leq%2020%20\})
 . In other words,

![image](https://render.githubusercontent.com/render/math?math=S)
 contains all instances of x such that x is an integer between 0 and 20.

#### Binge-watch day:

- We can define this as 6 or more hours watched
- The event space still includes only real numbers below 24, but now the lower bound is 6 rather than 0
-

![image](https://render.githubusercontent.com/render/math?math=E%20=%20\{x%20\mid%20x%20\in%20\mathbb{R},%206%20\leq%20x%20\leq%2024%20\})
 . In other words,

![image](https://render.githubusercontent.com/render/math?math=S)
 contains all instances of x such that x is a real number between 6 and 24.

## Introduction to Probability

Once you understand sample spaces and event spaces, you understand the foundational concepts of probability.

### The Law of Relative Frequency

While conducting an endless stream of experiments, the relative frequency by which an event will happen becomes a fixed number.

Let's denote an event by

![image](https://render.githubusercontent.com/render/math?math=E)
 , and the *probability* of the event

![image](https://render.githubusercontent.com/render/math?math=E)
 occurring by

![image](https://render.githubusercontent.com/render/math?math=P(E))
 . Next, let

![image](https://render.githubusercontent.com/render/math?math=n)
 be the number of conducted experiments, and

![image](https://render.githubusercontent.com/render/math?math=S(n))
 the count of "successful" experiments (i.e. the times that event

![image](https://render.githubusercontent.com/render/math?math=E)
 happened). The formal definition of probability as a relative frequency is given by:

![image](https://render.githubusercontent.com/render/math?math=P(E)%20=%20\lim_{n\rightarrow\infty}%20\dfrac{S{(n)}}{n})

In other words, the probability of the event (

![image](https://render.githubusercontent.com/render/math?math=P(E))
 ) equals the limit as the number of experiments

![image](https://render.githubusercontent.com/render/math?math=n)
 goes to infinity of the count of successful experiments

![image](https://render.githubusercontent.com/render/math?math=S(n))
 divided by the number of experiments

![image](https://render.githubusercontent.com/render/math?math=n)
 .

This is the basis of a frequentist statistical interpretation: an event's probability is the ratio of the positive trials to the total number of trials as we repeat the process infinitely.

### Probability Axioms

In the early 20th century, Kolmogorov and Von Mises came up with three axioms that further expand on the idea of probability. The three axioms are:

#### 1. Positivity

A probability is always bigger than or equal to 0, or

![image](https://render.githubusercontent.com/render/math?math=0%20\leq%20P(E)%20\leq%201)

#### 2. Probability of a Certain Event

If the event of interest is the sample space (

![image](https://render.githubusercontent.com/render/math?math=S%20=%20E)
 ), we say that the outcome is a certain event, or

![image](https://render.githubusercontent.com/render/math?math=P(S)%20=%201)

#### 3. Additivity

The probability of the union of two exclusive events is equal to the sum of the probabilities of the individual events happening.

Remember the inclusion-exclusion principle states that:

![image](https://render.githubusercontent.com/render/math?math=\mid%20S%20%20\cup%20T\mid%20=%20\mid%20S%20\mid%20%2b%20\mid%20T%20\mid%20-%20\mid%20S%20%20\cap%20T%20\mid)

If we know that

![image](https://render.githubusercontent.com/render/math?math=S%20%20\cap%20T%20=%20\emptyset)
 (that there is no intersection between

![image](https://render.githubusercontent.com/render/math?math=S)
 and

![image](https://render.githubusercontent.com/render/math?math=T)
 , so the set formed by their intersection is the empty set

![image](https://render.githubusercontent.com/render/math?math=\emptyset)
 ), then we can skip that part of the formula, so the cardinality of

![image](https://render.githubusercontent.com/render/math?math=S%20%20\cup%20T)
 is simply:

![image](https://render.githubusercontent.com/render/math?math=\mid%20S%20\mid%20%2b%20\mid%20T%20\mid)

The same logic works for the probability of events in two event space sets. If the events are exclusive — they never happen at the same time, so the intersection between them is empty — you can simply add the two probabilities together.

If

![image](https://render.githubusercontent.com/render/math?math=A%20%20\cap%20B%20=%20\emptyset)
 , then

![image](https://render.githubusercontent.com/render/math?math=P(A%20\cup%20B)%20=%20P(A)%20%2b%20P(B))

### Addition Law of Probability

The additivity axiom is great, but most of the time events are not exclusive. Then we need to bring in the rest of the inclusion-exclusion principle (subtracting the intersection), which is now referred to as the **addition law of probability** or the **sum rule** when we are talking about probabilities.

![image](https://render.githubusercontent.com/render/math?math=P(A%20\cup%20B)%20=%20P(A)%20%2b%20P(B)%20-%20P(A%20%20\cap%20B))

Put in words, the probability that

![image](https://render.githubusercontent.com/render/math?math=A)
 or

![image](https://render.githubusercontent.com/render/math?math=B)
 will happen is the sum of the probabilities that

![image](https://render.githubusercontent.com/render/math?math=A)
 will happen and that

![image](https://render.githubusercontent.com/render/math?math=B)
 will happen, minus the probability that *both*

![image](https://render.githubusercontent.com/render/math?math=A)
 and

![image](https://render.githubusercontent.com/render/math?math=B)
 will happen.

## Examples

Let's reconsider the dice example to explain what was explained before:

### Additivity of Exclusive Events

Let's consider two events: event

![image](https://render.githubusercontent.com/render/math?math=M)
 means throwing a 6, event

![image](https://render.githubusercontent.com/render/math?math=N)
 means that you throw an odd number (

![image](https://render.githubusercontent.com/render/math?math=N={1,3,5})
 ). These events are exclusive, so you can use the additivity rule if you want to know the answer to the question:

*"what is the probability that your outcome will be a 6, or an odd number?"*

![image](https://render.githubusercontent.com/render/math?math=P(M%20\cup%20N)%20=%20P(M)%20%2b%20P(N)%20=%20\dfrac{1}{6}%2b\dfrac{3}{6}=\dfrac{4}{6}=\dfrac{2}{3})

There is a 2/3 probability that the outcome will be a 6 or an odd number.

### Addition Law of Probability

Now, let's consider the same event

![image](https://render.githubusercontent.com/render/math?math=N={1,3,5})
 and another event

![image](https://render.githubusercontent.com/render/math?math=Q={4,5,6})
 . These events are *not* mutually exclusive, so if you want to know the probability that

![image](https://render.githubusercontent.com/render/math?math=N)
 or

![image](https://render.githubusercontent.com/render/math?math=Q)
 will happen, you need to use the addition law of probability.

Note that

![image](https://render.githubusercontent.com/render/math?math=(N%20%20\cap%20Q))
 is equal to getting an outcome of 5, as that is the "common" element in the respective event spaces of

![image](https://render.githubusercontent.com/render/math?math=N)
 and

![image](https://render.githubusercontent.com/render/math?math=Q)
 . This means that

![image](https://render.githubusercontent.com/render/math?math=P(N%20%20\cap%20Q)%20=%20\dfrac{1}{6})

![image](https://render.githubusercontent.com/render/math?math=P(N%20\cup%20Q)%20=%20P(N)%20%2b%20P(Q)%20-%20P(N%20%20\cap%20Q)%20=%20\dfrac{3}{6}%20%2b%20\dfrac{3}{6}%20-%20\dfrac{1}{6}%20=%20\dfrac{5}{6})

There is a 5/6 probablity that the outcome will be in

![image](https://render.githubusercontent.com/render/math?math=N)
 or

![image](https://render.githubusercontent.com/render/math?math=Q)
 .

## Final Note

In the previous examples, you noticed that for our dice example, it is easy to use these fairly straightforward probability formulas to calculate probabilities of certain outcomes.

However, if you think about our text message example, things are less straightforward, e.g.:

*"What is the probability of sending less than 20 text messages in a day?"*

This is where the probability concepts introduced here fall short. The probability of throwing any number between 1 and 6 with a die is always exactly

![image](https://render.githubusercontent.com/render/math?math=\dfrac{1}{6})
 , but we can't simply count our messages event space. In words, the probability of sending 20 messages is likely different than the probability of sending, say, 5 messages, and will be different for any number of messages sent. You'll learn about tools to solve problems like these later on.

## Summary

Well done! In this section, you learned how to use sets to get to probabilities. You learned about experiments, event spaces, and outcomes. Next, you learned about the law of relative frequency and how it can be used to calculate probabilities, along with the three probability axioms.

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
