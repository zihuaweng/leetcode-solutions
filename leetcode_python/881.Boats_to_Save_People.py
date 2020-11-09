#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/boats-to-save-people/
# two pointers

# Time complexity: O(nlogn)
# Space complexity: O()


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        s = 0
        e = len(people) - 1

        while s <= e:
            if people[s] + people[e] <= limit:
                e -= 1
            s += 1

        return s

