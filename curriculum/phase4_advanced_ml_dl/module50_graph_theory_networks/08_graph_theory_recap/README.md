# Graph Theory - Recap

> Part of **Phase 4 Appendix: Graph Theory** · source item type: WikiPage

---
## Introduction

In this section you explored a new data structure: networks! While network analysis is a deep topic with many additional topics to explore, you should have a good initial introduction and enough to conduct some preliminary analyses for social networks and building recommendation systems.

## Networks

You've seen that networks can represent a range of different underlying data. From directions, social networks, and customer databases, networks are a wonderful way to represent the relationships between individuals. They also make for some snazzy visuals!

## Paths

The first stop along your journey was paths! Here, you investigated Dijkstra's algorithm to find the shortest path between nodes. This harked back to some of your experience scraping the web when you used recursive functions to perform breadth and depth based search techniques to transverse a json file. While you didn't directly explore this application, networks are also a natural representation for exploring internet traffic and web page structures.

## Centrality

Once you had a metric to calculate the distance between nodes, you then started to investigate other important concepts of networks such as which nodes were most influential or connected within a graph. You saw how alternative metrics can provide different insights on node structure. As a quick recap:

- **Degree-centrality**: The number of edges attached to a node
- **Closeness-centrality**: The reciprocal of the sum of the distances to all other nodes in the network
- **Betweeness-centrality**: The number of shortest paths between all node pairs the node lies on divided by the maximum number of shortests-paths any one node in the network lies on
- **Eigenvalue-centrality**: An iterative algorithm which assigns relative influence to a node based on the number and importance of connected nodes. Can be very computationally expensive to compute for large networks. Google's PageRank algorithm is a variation of eigenvalue-centrality

## Clustering

After discussing centrality, you then focused on larger structures within a network, breaking apart nodes into clusters to examine subgroups. While this is a common and useful application, it is an ill-defined problem mathematically, often making it difficult to definitively determine an optimal clustering schema.

## Recommendations

Finally, you rounded out the section by investigating how networks can be used to provide recommendations to users. To do this, you investigated a preliminary approach known as collaborative filtering, specifically exploring user-based collaborative filtering in which similar users are identified and their preferences are used to generate recommendations to the user in question. There are many alternative approaches to recommendations systems such as using Singular Value Decomposition.

## Summary

A lot was covered in this section! From this, you should have a solid introduction to networks, and some of their applications. Going forward, continue to explore ongoing developments in clustering social networks, and generating recommendations from these fascinating data structures.

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
