"""
380. Insert Delete GetRandom O(1) https://leetcode.com/problems/insert-delete-getrandom-o1/description/

Implement the RandomizedSet class:
RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present.
Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present.
Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements
(it's guaranteed that at least one element exists when this method is called).
Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]
Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
Constraints:
-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.

SOLUTION
Swap item to delete to the last index of the array. Array pop() takes O(1) time.
References
- https://leetcode.com/problems/insert-delete-getrandom-o1/solutions/2858286/python3-hashmap-list-got-this-in-google-phone-interview/
"""
import random


class RandomizedSet:
    def __init__(self):
        self.ht = {}
        self.ar = []

    def insert(self, val: int) -> bool:
        if val not in self.ht:
            self.ar.append(val)
            self.ht[val] = len(self.ar) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.ht:
            i = self.ht[val]
            if i != len(self.ar) - 1:
                self.ar[-1], self.ar[i] = self.ar[i], self.ar[-1]
                self.ht[self.ar[i]] = i
            del self.ht[val]
            self.ar.pop()
            return True
        return False

    def getRandom(self) -> int:
        return int(random.choice(self.ar))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
