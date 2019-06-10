"""
Factorial Zeros: Write an algorithm which computes the number of trailing zeros in n factorial.
(16.5, p485)
"""


def factorial_zeroes(n):
    """Consider a factorial like 19!:
    19! = 1*2* 3*4* 5*6*7*8*9* 10* 11* 12* 13*14*15* 16* 17*18*19
    A trailing zero is created with multiples of 10
    and multiples of 10 are created with pairs of 5-multiples and 2-multiples.

    Therefore, to count the number of zeros, we only need to count the pairs of multiples of 5 and 2.
    There will always be more multiples of 2 than 5, though,
    so simply counting the number of multiples of 5 is sufficient.
    One "gotcha" here is 15 contributes a multiple of 5 (and therefore one trailing zero),
    while 25 contributes two (because 25 = 5 * 5).
    """
    if n < 0:
        raise ValueError('factorial is undefined for negative numbers')
    count = 0
    i = 5
    while int(n / i) > 0:
        count += int(n / i)
        i *= 5
    return count
