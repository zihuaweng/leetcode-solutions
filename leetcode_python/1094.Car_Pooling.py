#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# 这一类问题的解答总结
# https://leetcode.com/problems/meeting-rooms-ii/discuss/322622/Simple-Python-solutions


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips:
            return True

        lst = []
        for num, on, off in trips:
            lst.append((on, num))
            lst.append((off, -num))
        lst.sort()

        for _, num in lst:
            capacity -= num
            if capacity < 0:
                return False
        return True
