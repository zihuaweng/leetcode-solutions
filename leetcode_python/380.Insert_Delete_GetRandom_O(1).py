#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(1)
# Space complexity: O(n)


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num = []
        self.idx = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.idx:
            self.num.append(val)
            self.idx[val] = len(self.num) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # 将列表的最后一个和val调换位置，pop可以是O(1)
        if val in self.idx:
            target = self.idx[val]
            self.num[target] = self.num[-1]
            self.idx[self.num[-1]] = target
            self.num.pop()
            del self.idx[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.num[random.randint(0, len(self.num) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()