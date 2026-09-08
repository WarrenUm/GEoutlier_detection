# P-Values and the Null Hypothesis

> Part of **Topic 14: Hypothesis Testing** · source item type: WikiPage

---
## Introduction

In this lesson, you'll dig deeper into the relationship between p-values and the null hypothesis, and their role in designing an experiment.

## Objectives

You will be able to:

- Describe what it means to "reject the null hypothesis" and how it is related to p-value

- Identify examples of null and alternative hypotheses, including one-tail and two-tail tests

## Understanding the Null Hypothesis

As stated previously, scientific experiments actually have 2 hypotheses:

***Null Hypothesis***: There is no relationship between A and B
 Example: "There is no relationship between this flu medication and a *reduced* recovery time from the flu."

The *null hypothesis* is usually denoted as

![image](https://render.githubusercontent.com/render/math?math=H_{0})

***Alternative Hypothesis***: The hypothesis traditionally thought of when creating a hypothesis for an experiment
 Example: "This flu medication reduces recovery time for the flu."

The *alternative hypothesis* is usually denoted as

![image](https://render.githubusercontent.com/render/math?math=H_{1})
 or

![image](https://render.githubusercontent.com/render/math?math=H_{a})

An easy way to differentiate between the null hypothesis and the alternative hypothesis is that the null hypothesis is the more conservative choice. It always assumes that there is no difference between some variables of interest, and therefore when it is represented mathematically, it should always contain an equals sign (

![image](https://render.githubusercontent.com/render/math?math==)
 ,

![image](https://render.githubusercontent.com/render/math?math=\geq)
 , or

![image](https://render.githubusercontent.com/render/math?math=\leq)
 ).

The alternative hypothesis is whatever claim you are trying to prove with an experiment. It posits that there is some difference between some variables of interest, and therefore when it is represented mathematically it should never contain an equals sign, but rather some symbol representing inequality (

![image](https://render.githubusercontent.com/render/math?math=\neq)
 ,

![image](https://render.githubusercontent.com/render/math?math=<)
 , or

![image](https://render.githubusercontent.com/render/math?math=>%22>%20).</p>%20%20<p>Whenever%20you%20are%20performing%20a%20statistical%20test,%20you%20are%20determining%20whether%20you%20have%20enough%20evidence%20to%20reject%20the%20null%20hypothesis.%20If%20you%20do%20not%20have%20enough%20evidence,%20you%20fail%20to%20reject%20the%20null%20hypothesis.</p>%20%20<h2>p-Values%20and%20Alpha%20Values</h2>%20%20<p>No%20matter%20what%20you're%20experimenting%20on,%20statistical%20tests%20come%20down%20to%20one%20question:%20Is%20your%20p-value%20less%20than%20your%20alpha%20value?%20Let's%20dive%20into%20what%20each%20of%20these%20values%20represents,%20and%20why%20they're%20so%20important%20to%20experimental%20design.%20</p>%20%20<p><strong><em>p-value</em></strong>:%20The%20probability%20of%20observing%20a%20test%20statistic%20at%20least%20as%20large%20as%20the%20one%20observed,%20by%20random%20chance,%20assuming%20that%20the%20null%20hypothesis%20is%20true.</p>%20%20<p>If%20you%20calculate%20a%20p-value%20and%20it%20comes%20out%20to%200.03,%20you%20can%20interpret%20this%20as%20saying%20%22There%20is%20a%203%%20chance%20of%20obtaining%20the%20results%20I'm%20seeing%20when%20the%20null%20hypothesis%20is%20true.%22</p>%20%20<p>A%20low%20p-value%20means%20that%20either%20<em>the%20null%20hypothesis%20is%20false</em>%20or%20<em>the%20null%20hypothesis%20is%20true%20and%20a%20highly%20improbable%20event%20has%20occurred</em>.%20It%20is%20impossible%20to%20know%20which%20of%20these%20is%20what%20actually%20happened!%20So%20the%20best%20practice%20is%20to%20set%20an%20%20<img%20src=)
 prior to conducting the experiment, to establish what level of this particular kind of incorrectness you are willing to tolerate.

![image](https://render.githubusercontent.com/render/math?math=\alpha)
 ***(alpha value)***: The marginal threshold at which you're okay with agreeing that the null hypothesis is implausible enough to be rejected.

If you set an alpha value of

![image](https://render.githubusercontent.com/render/math?math=\alpha%20=%200.05)
 , you're essentially saying "I'm okay with accepting my alternative hypothesis as true when we expect that the null hypothesis would randomly cause the results I'm seeing less than 5% of the time."

When you conduct an experiment, your goal is to calculate a p-value and compare it to the alpha value. If

![image](https://render.githubusercontent.com/render/math?math=p%20<%20\alpha)
 , then you ***reject the null hypothesis*** because the idea that there is "no relationship" between the variables of interest has become too implausible. Note that any good scientist will admit that this doesn't prove that there is a *direct causal relationship* between some chosen "independent" and "dependent" variables, just that they now have enough evidence to the contrary to show that they no longer believe that there is no relationship between them.

In simple terms:

![image](https://render.githubusercontent.com/render/math?math=p%20<%20\alpha)
 : Reject the *null hypothesis* and in favor of the *alternative hypothesis*

![image](https://render.githubusercontent.com/render/math?math=p%20>=%20\alpha%22>%20:%20Fail%20to%20reject%20the%20<em>null%20hypothesis</em>.</p>%20%20<p>So%20for%20example,%20if%20you%20set%20an%20alpha%20of%200.05%20and%20your%20statistical%20test%20produces%20a%20p-value%20of%200.02,%20you%20reject%20the%20null%20hypothesis.%20(You%20would%20say%20<em>we%20reject%20the%20null%20hypothesis%20at%20a%20significance%20level%20of%200.05</em>.)%20If%20you%20set%20an%20alpha%20of%200.05%20and%20your%20statistical%20test%20produces%20a%20p-value%20of%200.06,%20you%20fail%20to%20reject%20the%20null%20hypothesis.%20(You%20would%20say%20<em>we%20fail%20to%20reject%20the%20null%20hypothesis%20at%20a%20significance%20level%20of%200.05</em>.)</p>%20%20<p><strong><em>Whether%20something%20is%20statistically%20significant%20depends%20on%20the%20specified%20alpha%20value.</em></strong>%20Statistical%20significance%20is%20not%20a%20purely%20objective%20measure;%20it%20is%20dependent%20on%20the%20design%20choices%20you%20make%20as%20you%20set%20up%20your%20experiment.</p>%20%20<h3>Choosing%20an%20Alpha%20Value</h3>%20%20<p>An%20alpha%20value%20can%20be%20any%20value%20set%20between%200%20and%201.%20However,%20the%20most%20common%20alpha%20value%20in%20science%20is%200.05%20(although%20this%20is%20somewhat%20of%20a%20controversial%20topic%20in%20the%20scientific%20community,%20currently).</p>%20%20<p>Choosing%20an%20alpha%20value%20is%20also%20known%20as%20choosing%20a%20<strong>significance%20level</strong>.%20Much%20like%20choosing%20the%20confidence%20level%20for%20a%20confidence%20interval,%20you%20are%20attempting%20to%20balance%20between%20two%20undesirable%20outcomes.</p>%20%20<ul>%20<li>Confidence%20level%20trade-offs%20(review)%20%20<ul>%20<li>If%20a%20confidence%20level%20is%20too%20high,%20there%20is%20a%20higher%20risk%20of%20creating%20a%20range%20of%20values%20that%20is%20too%20wide%20to%20be%20useful.%20In%20other%20words,%20failing%20to%20produce%20any%20%22interesting%22%20confidence%20interval.</li>%20<li>If%20a%20confidence%20level%20is%20too%20low,%20there%20is%20a%20higher%20risk%20of%20the%20true%20value%20being%20outside%20of%20the%20interval.%20In%20other%20words,%20producing%20an%20%22interesting%22%20confidence%20level%20that%20doesn't%20actually%20capture%20the%20true%20value.</li>%20</ul></li>%20<li>Significance%20level%20trade-offs%20(new%20concept)%20%20<ul>%20<li>If%20an%20alpha%20is%20too%20low,%20there%20is%20a%20higher%20risk%20of%20failing%20to%20reject%20the%20null%20hypothesis%20even%20though%20it%20is%20false.%20In%20other%20words,%20accidentally%20missing%20an%20%22interesting%22%20finding%20about%20the%20differences%20between%20variables.</li>%20<li>If%20an%20alpha%20is%20too%20high,%20there%20is%20a%20higher%20risk%20of%20rejecting%20the%20null%20hypothesis%20even%20though%20it%20is%20true.%20In%20other%20words,%20accidentally%20claiming%20that%20you%20have%20an%20%22interesting%22%20finding%20about%20the%20differences%20between%20variables,%20even%20though%20that%20finding%20isn't%20true.</li>%20</ul></li>%20</ul>%20%20<p>(For%20a%20longer%20aside%20about%20what%20scientists%20mean%20by%20%22interesting%22,%20check%20out%20the%20classic,%20irreverent%20paper%20<em>That's%20Interesting!</em>%20by%20sociologist%20Murray%20S.%20Davis%20(<a%20href=)
DOI link, [Google Scholar search](https://scholar.google.com/scholar?cluster=4050715004907820129&hl=en&as_sdt=0,33)))

In general, we tend to think that setting an alpha too high is more worrisome than setting it too low. For example, if we set a significance level of

![image](https://render.githubusercontent.com/render/math?math=\alpha%20=%200.5)
 , that means that if the null hypothesis is true, we would still get a statistically significant result (indicating to reject the null hypothesis) 50% of the time! Intuitively, that is not a good idea, because it means claiming lots of relationships between variables that don't actually exist. So generally we err on the side of setting the alpha lower and possibly missing some interesting relationships, in order to minimize all of these false positives.

At the same time, setting an alpha *too* low means we will miss a lot of interesting findings. So you will rarely see an alpha set lower than 0.01, and 0.05 is fairly standard.

In future lessons we will dig deeper into defining terms like "false positive" more precisely, and also consider the "multiple comparisons problem" that comes into play when performing multiple experiments with the same alpha.

## Null and Alternative Hypothesis Examples

There are many different ways that you can structure a hypothesis statement, but they always come down to some statement of equality (null hypothesis) and some statement of inequality (alternative hypothesis).

It is important that these two hypotheses are mutually exclusive (cannot both occur at the same time, so the intersection of

![image](https://render.githubusercontent.com/render/math?math=H_{0})
 and

![image](https://render.githubusercontent.com/render/math?math=H_{a})
 is the empty set) and exhaustive (all possible scenarios are represented by the union of

![image](https://render.githubusercontent.com/render/math?math=H_{0})
 and

![image](https://render.githubusercontent.com/render/math?math=H_{a})
 ). (You will see some contexts where they are not defined in an exhaustive way, but for our statistical tests they will need to be.)

In all of the following examples, we will focus on **statistical tests that compare means (

![image](https://render.githubusercontent.com/render/math?math=\mu)
 values) of normally distributed data**. This is only one kind of statistical test! There are numerous other statistical tests for comparing categorical data, comparing variances of data, comparing an observed distribution to a theoretical distribution, comparing a sample to a population, etc. that we are not digging into just yet.

### One-Tail and Two-Tail Tests

In normally distributed data, you calculate p-values from t-statistics (or

![image](https://render.githubusercontent.com/render/math?math=z)
 -scores if the population parameters are known). One of the main considerations is whether to perform a ***one-tail*** or a ***two-tail*** test.

***Example One-Tail Hypotheses***

A ***one-tail test*** is when you want to know if a parameter from the treatment group is greater than (or less than) a corresponding parameter from the control group.

![image](https://render.githubusercontent.com/render/math?math=H_{1}%20:%20\mu_1%20<%20\mu_2)
 The treatment group given this weight loss drug will lose more weight on average than the control group that was given a competitor's weight loss drug

![image](https://render.githubusercontent.com/render/math?math=H_{0}%20:%20\mu_1%20\geq%20\mu_2)
 The treatment group given this weight loss drug will not lose more weight on average than the control group that was given a competitor's weight loss drug".

In general,

![image](https://render.githubusercontent.com/render/math?math=<)
 or

![image](https://render.githubusercontent.com/render/math?math=>%22>%20in%20the%20alternative%20hypothesis%20and%20%20<img%20src=)
 or

![image](https://render.githubusercontent.com/render/math?math=\leq)
 in the null hypothesis indicates that this is a one-tail test.

***Example Two-Tail Hypotheses***

A ***two-tail test*** is for when you want to test if a parameter falls between (or outside of) a range of two given values.

![image](https://render.githubusercontent.com/render/math?math=H_{1}%20:%20\mu_1%20\neq%20\mu_2)
 "People in the experimental group that are administered this drug will not lose the same amount of weight as the people in the control group. They will be heavier or lighter".

![image](https://render.githubusercontent.com/render/math?math=H_{0}%20:%20\mu_1%20=%20\mu_2)
 "People in the experimental group that are administered this drug will lose the same amount of weight as the people in the control group."

In general,

![image](https://render.githubusercontent.com/render/math?math=\neq)
 in the alternative hypothesis and

![image](https://render.githubusercontent.com/render/math?math==)
 in the null hypothesis indicates that this is a two-tail test.

### What Does an Experiment Really Prove?

You may be wondering ***why you need a null hypothesis*** at all. This is a good question. It has to do with being honest about what an experiment actually proves.

Scientists use the null hypothesis so that they can be very specific in their findings. This is because a successful experiment doesn't actually *prove a relationship* between a dependent and independent variable. Instead, it just argues that there is enough evidence to convince us that the null hypothesis regarding this relationship is implausible.

Even if you have a statistically significant result, either of these could be true:

1. The null hypothesis about this relationship is actually true, and you experienced an unlikely sampling event
2. There is a lurking confounding variable that is actually responsible for the perceived relationship

However, we can call an experiment where

![image](https://render.githubusercontent.com/render/math?math=p%20<%20\alpha)
 a "successful experiment" because we are confident that it's statistically unlikely for the first of those to occur. Handling confounding variables is much more challenging, although we will consider this in more depth when we learn about statistical models, especially multiple linear regression.

## The Null Hypothesis Loves You and Wants You To Be Happy

You've covered a lot about the null hypothesis and how it's used in experiments in this lesson, but there's a lot more to learn about it!

Read the following article, [The Null Hypothesis Loves You and Wants You To Be Happy](https://byrslf.co/the-null-hypothesis-loves-you-and-wants-you-to-be-happy-3189413d8cd0). This does an excellent job of explaining why the concept of the *Null Hypothesis* is crucial to good science.

## Summary

In this lesson, you learned about the relationship between p-values and the null hypothesis. You'll use this knowledge in all of the upcoming lessons about hypothesis testing, as well as later lessons about interpreting linear regression models!

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
