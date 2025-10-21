"""
721. Accounts Merge https://leetcode.com/problems/accounts-merge/description/

Given a list of accounts where each element accounts[i] is a list of strings,
where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
Now, we would like to merge these accounts.
Two accounts definitely belong to the same person if there is some common email to both accounts.
Note that even if two accounts have the same name, they may belong to different people as people could have the same name.
A person can have any number of accounts initially, but all of their accounts definitely have the same name.
After merging the accounts, return the accounts in the following format:
the first element of each account is the name, and the rest of the elements are emails in sorted order.
The accounts themselves can be returned in any order.
Example 1:
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Example 2:
Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
Constraints:
1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j].length <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.

SOLUTION
Union-Find (Disjoint Set Union)
We treat each account as a node.
If two accounts share an email → they are connected (i.e., part of the same set).
So we’ll use Union-Find to merge connected components.
Union-Find Concepts
find(x) → finds the root parent of node x.
union(x, y) → merges the groups of x and y.
This helps us efficiently find all accounts that belong to the same user.

Union-Find operations:	Time O(α(N)) ≈ O(1)	Amortized inverse Ackermann function
Looping over all emails: Time O(E log E)	Sorting all emails in the final output
Overall	Time O(E log E) where E=total number of emails
Space O(E): For storing ownership maps and groups

References
- https://leetcode.com/problems/accounts-merge/solutions/1084738/python-the-clean-union-find-solution-you-are-looking-for/
- https://youtu.be/wU6udHRIkcc?si=Ts-KinfVDaJwm1j9
"""

from typing import Dict, List


class UnionFind:
    def __init__(self, n: int):
        # Each account is its own parent at the start. Each node (account) is in its own disjoint set.
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        # The find(x) function returns the root (representative) of the set that element x belongs to.
        # Every disjoint set (or connected component) is represented by one root node.
        # If two nodes share the same root, they are in the same set.

        # Path compression: make every node point directly to the root
        # Without path compression:
        # find() could take O(N) in the worst case (a long chain).
        # With path compression:
        # find() becomes almost constant time, formally amortized O(α(N)),
        # where α(N) is the inverse Ackermann function — so small it’s < 5 for all realistic N.
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        # Connect the components that x and y belong to
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        email_to_owner: Dict[str, int] = {}

        # Step 1: Union accounts with shared emails
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in email_to_owner:
                    uf.union(i, email_to_owner[email])
                email_to_owner[email] = i

        # Step 2: Group emails by their root account
        merged: Dict[int, List[str]] = {}
        for email, owner in email_to_owner.items():
            root = uf.find(owner)
            merged.setdefault(root, []).append(email)

        # Step 3: Build the final result with sorted emails and account name
        result = []
        for root, emails in merged.items():
            name = accounts[root][0]
            result.append([name] + sorted(emails))

        return result
