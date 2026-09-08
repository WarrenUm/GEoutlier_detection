# Amazon Web Services - Recap

> Part of **Topic 43: Operationalizing Code and AWS** · source item type: WikiPage

---
## Key Takeaways

The key takeaways from this section include:

- AWS is a ***Cloud-Computing Platform*** which we can use for a variety of use cases in data science.
- In this section, we learned about how to sign up for AWS, and how to make sure that we have the right region selected when working in AWS.
- Amazon has centralized all of the major data science services inside ***Amazon SageMaker***. SageMaker provides numerous services for things such as:
  - Data Labeling
  - Cloud-based Notebooks
  - Training and Model Tuning
  - Inference

- We can set up our own models, or use the preexisting models provided by AWS. Similarly, we can set up our own inference endpoints, or make use of preexisting endpoints created by AWS.
- Creating our own endpoint requires us to use a Docker instance, as we saw in the previous codealong. Much of the work required to create an endpoint for our own model is boilerplate, and we can use it again and again across multiple projects.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
