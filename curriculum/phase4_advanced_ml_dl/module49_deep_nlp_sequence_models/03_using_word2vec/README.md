# Using Word2Vec

> Part of **Phase 4 Appendix: Deep NLP** · source item type: WikiPage

---
## Introduction

In this lesson, you'll take a look at how the ***Word2Vec*** model actually works, and then learn how you can make use of Word2Vec using the open-source `gensim` library!

## Objectives

You will be able to:

- Describe the tunable parameters of a Word2Vec model

- Describe the architecture of the Word2Vec model
- Train a Word2Vec model and transform words into vectors

## How Word2Vec Works

By now, you've gained an understanding of what a word embedding space is, and you've learned a little bit about how the words are represented as Dense vectors. However, we haven't touched on how the model actually learns the correct values for all the word vectors in the embedding space. To put it another way, how does the Word2Vec model learn exactly *where* to embed each word vector inside the high dimensional embedding space?

Note that this explanation will stay fairly high-level, since you don't actually need to understand every part of how the Word2Vec model works in order to use it effectively for Data Science tasks. If you'd like to dig deeper in to how the model actually works, we recommend you start by reading this tutorial series from Chris McCormick ([part 1](http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/) and [part 2](http://mccormickml.com/2017/01/11/word2vec-tutorial-part-2-negative-sampling/)), and then moving onto the actual [Word2Vec White Paper by Mikolov et al](https://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf). The graphics used in this lesson are actually from Chris McCormick's excellent blog posts explaining how Word2Vec actually works.

### Window Size and Training Data

At its core, Word2Vec is just another deep neural network. It's not even a particularly complex neural network -- the model contains an input layer, a single hidden layer, and and an output layer that uses the softmax activation function, meaning that the model is meant for multiclass classification. The model examines a ***window*** of words, which is a tunable parameter that you can set when working with the model. Let's take a look at a graphic that explains how this all actually looks on a real example of data:

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-using-word2vec/master/images/training_data.png)

In the example above, the model has a window size of 5, meaning that the model considers a word, and the two words to the left and right of this word.

### The Skip-Gram Architecture

So what exactly is this deep neural network predicting?

The most clever thing about the Word2Vec model is the type of problem it trains the network to solve, which creates the dense vectors for every word as a side effect! A typical task for a neural network is sentence completion. A trained model should be able to take in a sentence like "the cat sat on the" and output the most likely next word in the sentence, which should be something like "mat", or "floor". This is a form of ***Sequence Generation***. Given a certain context (the words that came before), the model should be able to generate the next most plausible word (or words) in the sequence.

Word2Vec takes this idea, and flips it on its head. Instead of predicting the next word given a context, the model trains to predict the context surrounding a given word! This means that given the example word "fox" from above, the model should learn to predict the words "quick", "brown", "jumps", and "over", although crucially, not in any particular order. You're likely asking yourself why a model like this would be useful -- there are a massive amount of correct contexts that can surround a given word, which means that the output trained model itself likely isn't very useful to us. This intuition is correct -- the *output* of the model is pretty useless to us. However, in the case of Word2Vec, it's not the model that we're interested in. It turns out that by training to predict the context window for a given word, the neurons in the hidden layer end up learning the embedding space! This is the reason why the size of the word vectors output by a Word2Vec model are a parameter that you can set ourselves. If you want word vectors of size 300, then you just include 300 neurons in our hidden layer. If you want vectors of size 100, then you include 100 neurons, and so on. Take a look at the following diagram of the Word2Vec model's architecture:

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-using-word2vec/master/images/new_skip_gram_net_arch.png)

### Hidden Layers as a "Lookup Table"

To recap, the Word2Vec model learns to solve a "fake" problem, which you don't actually care about. The input layer of the network contains one neuron for every word in the vocabulary. If there are 10,000 words, then there are 10,000 input neurons, with each one corresponding to a unique word in the vocabulary. Since these input neurons feed into a dense hidden layer, this means that each neuron will have a unique weight for each of the 10,000 words in the vocabulary. If there are 10,000 words and you want vectors of size 300, then this means the hidden layer will be of shape `[10000, 300]`. To put it another way -- each of the 10,000 words will have it's own unique vector of weights, which will be of size 300, since there are 300 neurons.

Once you've trained the model, you don't actually need the output layer anymore -- all that matters is the hidden layer, which will now act as a "Lookup Table" that allows us to quickly get the vector for any given word in the vocabulary.

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-using-word2vec/master/images/new_word2vec_weight_matrix_lookup_table.png)

Here's the beautiful thing about this lookup table -- when you input a given word, it is passed into the model in a one-hot encoded format. This means that in a vocabulary of 10,000 words, you'll have a `1` at the element that corresponds to the word that we're looking up the word vector for, and `0` for every other element in the vector. If you multiply this one-hot encoded vector by the weight matrix that is our hidden layer, then the vector for every word will be zeroed out, except for the vector that corresponds to the word that you are most interested in!

![image](https://raw.githubusercontent.com/learn-co-curriculum/dsc-using-word2vec/master/images/matrix_mult_w_one_hot.png)

### Understanding the Intuition Behind Word2Vec

So how does the model actually learn the correct weights for each word in a way that captures their semantic context and meaning? The intuition behind Word2Vec is actually quite simple, when you think about the idea of the context window that it's learning to predict. Recall the following quote, which you've seen before:

> "You shall know a word by the company it keeps." -- J.R. Firth, Linguist

In the case of the Word2Vec model, the "company" a word keeps are the words surrounding it, and the model is learning to predict these companions! By exploring many different contexts, the model attempts to decipher which words are appropriate in which contexts. For example, consider the sentence "we have two cats as pets". You could easily substitute the word "cats" for "dogs" and the entire sentence would still make perfect sense. While the meaning of the sentence is undoubtedly changed, there is also a lesson regarding the fact that both are nouns and pets. Without even worrying about the embedding space, you can easily understand that words that have similar meanings will likely also be used in many of the same kinds of sentences. The more similar words are, the more sentences in which they are likely to share context windows! This is exactly what the model is learning, and this is why words that are similar end up near each other inside the embedding space. The ways that they are *not* similar also helps the model learn to differentiate between them, since there will be patterns here as well. For instance, consider "ran" and "run", and "walk" and "walked". They differ only in tense. From the perspective of the sentences present in a large text corpus (models are commonly trained on all of Wikipedia, to give you an idea of the sheer size and scale of most datasets), the model will see numerous examples of how "ran" is similar to "walked", as well as examples of how the context windows for "ran" are different from "run" in the same ways that the context windows for "walked" are different from "walk"!

## Training A Word2Vec Model with `gensim`

Now, take look at how you can apply the Word2Vec model using the `gensim` library!

To train a Word2Vec model, you first need to import the model from the `gensim` library and instantiate it. Upon instantiation, you'll need to provide the model with certain parameters including:

- the dataset you'll be training on
- the `size` of the word vectors you want to learn
- the `window` size to use when training the model
- `min_count`, which corresponds to the minimum number of times a word must be used in the corpus in order to be included in the training (for instance, `min_count=5` would only learn word embeddings for words that appear 5 or more times throughout the entire training set)
- `workers`, the number of threads to use for training, which can speed up processing (`4` is typically used, since most processors nowadays have at least 4 cores).

Once you've instantiated the model, you'll still need to call the model's `.train()` method, and pass in the following parameters:

- The same dataset that you passed in at instantiation
- `total_examples`, which is the number of words in the model. You don't need to calculate this manually -- instead, you can just pass in the instantiated model's `.corpus_count` attribute for this parameter.
- The number of `epochs` to train the model for.

The following example demonstrates how to instantiate and train a Word2Vec model:

```python
from gensim.models import Word2Vec

# Normally, you would also perform preprocessing steps such as tokenization before training a Word2Vec model

model = Word2Vec(data, size=100, window=5, min_count=1, workers=4)

model.train(data, total_examples=model.corpus_count)
```

### Exploring the Embedding Space

Once you have trained the model, you can easily explore the embedding space using the built-in methods and functionality provided by gensim's `Word2Vec` class.

The actual Word2Vec model itself is quite large. Normally, you only need the actual vectors and the words that correspond to them, which are stored inside of `model.wv` as a `Word2VecKeyedVectors` object. To save time and space, it's usually easiest to just store the `model.wv` inside it's own variable, and then work directly with that. You can then use this model for various sorts of functionality, which you'll demonstrate below!

```python
wv = model.wv

# Get the most similar words to a given word
wv.most_similar('Cat')

# Get the least similar words to a given word. NOTE: you'll see in
# the next lab that this function doesn't always work the way you
# might intuitively think it will!
wv.most_similar(negative='Cat')

# Get the word vector for a given word
wv['Cat']

# Get all the vectors for all the words!
wv.vectors

# Compute some word vector arithmetic, such as (king - man + woman)
# which should be roughly equal to 'queen'
wv.most_similar(positive=['king', 'woman'], negative=['man'])
```

In the next lab, you'll train a Word2Vec model, and then explore the embedding space it has learned.

## Summary

In this lesson, you learned about how the Word2Vec model actually works, and how you can train and use a Word2Vec model using the `gensim` library!

---

## Your work

Do this lesson's exercises in `work.ipynb` in this folder. Where the concept
applies to market data, load it with the shared `ge_data` helper and interpret
the result in OSRS terms. Add `assert` cells to check yourself — `pytest` in
this folder runs the notebook (and your asserts) end-to-end.
