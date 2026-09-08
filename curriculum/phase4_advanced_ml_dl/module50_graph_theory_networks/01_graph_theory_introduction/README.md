# Graph Theory - Introduction

> Part of **Phase 4 Appendix: Graph Theory** · source item type: WikiPage

---
## Introduction

In this section, you'll investigate a new data structure: networks! Networks are a useful data structure to map a range of applications from driving directions to social networks.

## Network Graphs

Networks are another way of representing data that you have yet to fully investigate. In their most simple case, a network contains **nodes** connected by **edges** like this:

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-network-introduction/master/images/graph.png)

Nodes represent some object such as people, languages, countries, or tags, to name a few. The relationships between these objects are the edges between them. For example, later in this section you'll investigate the relationship of various technology tags on the popular website [StackOverflow](stackoverflow.com). One potential network visualization of this data looks like this:

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-network-introduction/master/images/stackoverflow_clusters.png)

## Path Searching

An important concept in network analysis are path searching algorithms. Finding the shortest path between two nodes is a foundational concept for creating a distance metric which can then be used to conduct more advanced analyses. Mapping applications such as Google Maps, Apple Maps, Waze, or Uber are also natural applications for path searching algorithms. In this section, you'll investigate Dijkstra's algorithm for finding the shortest path between two points, coding it from scratch using Python.

## Centrality

Once you've familiar with the concept of path searching, you'll then go on to investigate properties of nodes and edges. Centrality is a key concept in this, helping to determine which nodes are most influential in a network, or hold pivotal positions in connecting the network.

## Cliques and Clustering

Moving from the study of single objects nodes and edges within the network, you'll then start to investigate larger structures. With this, you'll investigate the concept of cliques and clusters in order to subdivide a network into smaller groups. Natural applications of this include sub-setting social networks into groups or categorizing items such as books or languages.

## Recommendation Systems

To round out this section, you'll investigate how networks can be used to fuel recommendation systems, a popular and exciting topic. With this, you'll work on recommending amazon products to customers.

## Summary

Get ready to dive into the exciting realm of networks! In this section, you'll get to play around with a range of datasets from Twitter, Game of Thrones, and the Amazon Marketplace!

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
