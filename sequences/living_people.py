"""
Living People: Given a list of people with their birth and death years, implement a method to
compute the year with the most number of people alive. You may assume that all people were born
between 1900 and 2000 (inclusive). If a person was alive during any portion of that year, they should
be included in that year's count. For example, Person (birth = 1908, death = 1909) is included in the
counts for both 1908 and 1909.
(16.10, p493)
"""
from collections import namedtuple, defaultdict


Person = namedtuple('Person', 'yob yod')


def year_with_most_people_alive(people):
    """Use a hash table to tally yearly count of people alive.
    O(P) time and O(Y) space, where P is number of persons and Y is range in years."""
    yearly_counts = defaultdict(int)
    for p in people:  # O(P) time because lifespan can be taken as constant time
        for year in range(p.yob, p.yod + 1):
            yearly_counts[year] += 1
    _max = 0
    res = None
    for year, count in yearly_counts.items():
        if count > _max:
            _max = count
            res = year
    return res
