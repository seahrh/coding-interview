"""
There are n applicants and m free apartments.
Your task is to distribute the apartments so that as many applicants as possible will get an apartment.
Each applicant has a desired apartment size,
and they will accept any apartment whose size is close enough to the desired size.

Input
The first input line has three integers n, m, and k:
the number of applicants, the number of apartments, and the maximum allowed difference.
The next line contains n integers a1,a2,…,an:
the desired apartment size of each applicant.
If the desired size of an applicant is x, he or she will accept any apartment whose size is between x−k and x+k.
The last line contains m integers b1,b2,…,bm: the size of each apartment.

Output
Print one integer: the number of applicants who will get an apartment.

Constraints
1 <= n,m <= 2⋅10^5
0 <= k <= 10^9
1 <= ai,bi <= 10^9

Example
Input:
4 3 5
60 45 80 60
30 60 75
Output:
2

See https://cses.fi/problemset/task/1084
SOLUTION
Time O(N lg N + M lg M)
Space O(1)
"""

from typing import List


def allocate(apartments: List[int], applicants: List[int], tolerance: int) -> int:
    if tolerance < 0:
        raise ValueError("tolerance must not be less than zero")
    apartments.sort()
    applicants.sort()
    i, j, res = 0, 0, 0
    while i < len(apartments) and j < len(applicants):
        if applicants[j] - tolerance <= apartments[i] <= applicants[j] + tolerance:
            i += 1
            j += 1
            res += 1
            continue
        if apartments[i] < applicants[j]:
            i += 1
            continue
        # this apartment and the rest of the apartments are larger than applicant's requirement
        # so move on to the next applicant
        j += 1
    return res
