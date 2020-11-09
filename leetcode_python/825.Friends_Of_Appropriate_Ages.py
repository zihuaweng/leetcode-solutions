#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n^2)
# Space complexity: O(n)

# https://leetcode.com/problems/friends-of-appropriate-ages/


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        res = 0
        if len(ages) < 2:
            return res

        counter = collections.Counter(ages)
        for age_1, count_1 in counter.items():
            for age_2, count_2 in counter.items():
                if self.compare(age_1, age_2):
                    res += count_1 * (count_2 - (age_1 == age_2))

        return res

    def compare(self, i, j):
        if i <= 0.5 * j + 7:
            return False
        if i > j:
            return False
        if i > 100 and j < 100:
            return False
        return True
