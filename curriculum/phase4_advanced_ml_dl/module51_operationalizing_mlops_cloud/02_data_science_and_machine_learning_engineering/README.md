# Data Science and Machine Learning Engineering

> Part of **Topic 43: Operationalizing Code and AWS** · source item type: WikiPage

---
## Introduction

In this lesson, we'll learn about the importance of being able to write production-quality code to make the models you've trained usable, and the leading cloud environments that make this possible!

## Objectives

- Explain why cloud computing and putting models into production is important to data scientists

## Data Science Skills and the Job Market

You're almost done with your studies, and will soon be ready to begin the job hunt. Since this is one of the most important topics a Data Scientist can know, we've elected to leave it until the very end, so that it'll be fresh in your mind going into your capstone project and the start of your career -- ***putting models into production***.

As you start to look at job postings, you probably notice that a "Data Scientist" job can mean many, many different things. In some companies, it means a data analyst or a DBA focused on databases or data pipelines. In others, it means someone with a scientific mindset skilled with running A/B tests. Yet others may be highly specialized machine learning roles in areas like NLP, Computer Vision, or Deep Learning -- and these roles may break down further into specializations focused on either research or implementation. As a Junior Data Scientist entering the workforce, it's most likely that you'll land in a generalist role, spending the first few years of your career working on various tasks that focus on all of these areas at least a little bit. Specialization happens later in your career. Out of the gate, the best thing that you can be is a strong generalist, with the demonstrated ability to contribute to many different sorts of projects that might be expected of a Data Science team.

Over the course of your studies, you've picked up many different skills in many different domain areas that will allow you to contribute to data science projects in a professional environment. However, when it comes to the job market, not all Data Science skills are created equal. While different data scientists or recruiters may rank these skills differently based on their own experiences or needs, one thing most agree on is that the ability to ***productionize a model*** is both very valuable and very rare when it comes to Junior Data Scientists. This presents a massive opportunity for you -- if you can become proficient in productionizing the models you've created (and demonstrate this proficiency in your portfolio of projects!), you become a much more interesting candidate for any role.

## Productionizing Models as a Career Skill

At large companies such as Google and Facebook, Data Scientists typically run experiments and train models until they have found a solution that works. Once they have trained a validated the model, they typically then hand off productionization of the model to ***Machine Learning Engineers***. Whereas the Data Scientist creates the basic prototype, the Machine Learning Engineer's job is to put that model into a production system in a performant and maintainable manner. Whereas Data Scientists at large companies focus on the "big picture" by finding solutions to business problems, Machine Learning Engineers focus on the details, implementing the solutions created by the data scientists in the best way possible. Data Scientists focus more on analytics and statistics, whereas Machine Learning Engineers will have a stronger command of backend engineering, data structures and algorithms, and software engineering overall. The following diagram lays out the relationship between different technical roles well:

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-data-science-and-machine-learning-engineering/master/images/new-venn-diagram.png)

As you can see from the overlap between *Data Scientist* and *Machine Learning Engineer* , there is still significant overlap between the two -- a Data Scientist should be able to productionize a basic machine learning model, just as a Machine Learning Engineer should able to train a model, validate results, and deal with overfitting.

### Being a 'Scrappy' Data Scientist

Many junior data scientists have at least one or two areas where they have significant holes in their knowledge. There are many paths into data science, and many junior data scientists are from backgrounds that have overlap with certain parts of data science. For instance, it's not uncommon for bioinformatics professionals or statisticians to rebrand themselves as a data scientist to take advantage of the higher salary in this field. While their backgrounds may give them a very strong understanding of analytics, scientific experimentation, or understanding how machine learning models work, these professionals often have little exposure to engineering, and thus can create and train models, but aren't able to put them into production so that the company can actually use them. Similarly, many junior data scientists on the job market have nothing more than a bachelor's degree in computer science and a passing understanding of machine learning -- in this case, productionizing a model is easy, but they may lack depth of understanding when it comes to the model itself. This isn't an insurmountable problem -- large companies almost always have some role where a candidate's skills can be useful, and they can invest in training the employee and skilling them up in areas where they're a bit weak.

With small and medium-sized companies, this is a much bigger problem. Data Scientists in smaller organizations are expected to be a bit more independent, and will likely have to "wear more hats". For a data science role at a startup, it's a common expectation for their data scientists to handle every part of a data science project. This means starting by interviewing key stakeholders and identifying the problem to be solved, followed by rapidly prototyping a solution until you've trained/tuned/validated a model that meets your standards, followed by actually putting that model in production! This means that it's very important to be 'scrappy', and be able to handle anything that's thrown at you as a data scientist. Smaller companies often don't have the funds or the infrastructure for a separate Machine Learning Engineering team to handle the details of implementation. In this respect, being able to productionize a machine learning model is the most practical, useful skill you can have in your Data Science toolbox. For all but the largest companies, it doesn't matter how great you are at training models -- until you put that model into production so that the rest of the organization can actually *use* it, it might as well not exist!

The TL;DR here is quite simple:

1. Many data scientists don't know how to put machine learning models into production.

2. Putting a model into production is a mandatory skill for data scientists at most small to medium-sized companies.
3. Being able to productionize models will make you a much more attractive candidate to employers, and give you a competitive advantage!

## Data Science and Cloud Computing

We've established that being able to productionize machine learning models is a valuable skill -- so how do we do it? This answer has changed in recent years thanks to cloud computing platforms such as ***Amazon Web Services***. A decade ago, productionizing a machine learning model would have meant building your own web server with something like [Flask](http://flask.pocoo.org/) or [Django](https://www.djangoproject.com/) and hosting somewhere, just like you would with any web app. However, the creation of cloud computing platforms changed things in a big way, and data science is no exception. Now, we don't even need to worry about things like server code -- instead, we can use preexisting services from AWS that were created specifically to simplify the process of productionizing machine learning solutions!

For the remainder of this section, we're going to dig deep into all the amazing tools AWS provides, and learn how we can use them to make you more effective data scientists!

## Summary

In this lesson, we learned about the similarities and differences between Data Scientists and Machine Learning Engineers. We also learned why the ability to productionize a machine learning model is a crucial skill for data scientists, as well as how this skill can provide a great competitive advantage when applying for jobs!

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
