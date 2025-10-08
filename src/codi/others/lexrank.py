"""
Lexicographic rank of a string
Given a string, find its rank among all its permutations sorted lexicographically.
For example, rank of “abc” is 1, rank of “acb” is 2, and rank of “cba” is 6.
Examples:

Input : str[] = "acb"
Output : Rank = 2

Input : str[] = "string"
Output : Rank = 598

Input : str[] = "cba"
Output : Rank = 6

From https://www.geeksforgeeks.org/lexicographic-rank-of-a-string/
Assume
- All unique characters
- Not limited to some charset, otherwise n is limited too and solution would take O(1) time.
- Factorial function is provided and takes O(1) time.
- Binary search function is provided and takes O(lg n) time.

SOLUTION
Count the number of permutations that are less than the given string.
e.g. given "STRING"
Sorted chars are "GINRST" where G has zero chars less than and T has 5 chars less than.
Repeat the same process for T, rank is 4*5! + 4*4! +…
Now fix T and repeat the same process for R, rank is 4*5! + 4*4! + 3*3! +…
Now fix R and repeat the same process for I, rank is 4*5! + 4*4! + 3*3! + 1*2! +…
Now fix I and repeat the same process for N, rank is 4*5! + 4*4! + 3*3! + 1*2! + 1*1! +…
Now fix N and repeat the same process for G, rank is 4*5! + 4*4! + 3*3! + 1*2! + 1*1! + 0*0!
Rank = 4*5! + 4*4! + 3*3! + 1*2! + 1*1! + 0*0! + 1 = 598

Time O(n^2)
Space O(n)
"""

from math import factorial

from codi.sortingandsearching.binary_search import search


def rank(string):
    if len(string) == 0:
        raise ValueError("arr must not be empty")
    sorted_chars = sorted(string)  # O(n lg n)
    res = 1  # add all smaller strings in following loop
    for i, c in enumerate(string):
        n_less = search(sorted_chars, c)  # O(lg n) time, binary search
        res += n_less * factorial(len(string) - i - 1)
        # Update the count of chars to the left, this takes O(n) time!
        del sorted_chars[n_less]
    return res
