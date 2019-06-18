"""
Shuffle: Write a method to shuffle a deck of cards. It must be a perfect shuffle-in other words, each
of the 52! permutations of the deck has to be equally likely. Assume that you are given a random
number generator which is perfect.

(17.2, p544)
"""
from random import randint


def shuffle_rec(cards, index):
    """Base case and build approach:
    First shuffle the first n - 1 elements. Then, we would take the nth
    element and randomly swap it with an element in the array.
    O(n) time and O(n) space.
    """
    if index < 0:
        raise ValueError('index must not be negative number')
    if index == 0:
        return cards
    shuffle_rec(cards, index - 1)
    k = randint(0, index)
    tmp = cards[k]
    cards[k] = cards[index]
    cards[index] = tmp
    return cards


def shuffle(cards):
    """The array has two partitions: shuffled (left) and unshuffled (right).
    Initially the shuffled region is empty. Move from left to right.
    """
    res = list(cards)
    for i in range(len(res)):
        k = randint(0, i)
        tmp = res[k]
        res[k] = res[i]
        res[i] = tmp
    return res
